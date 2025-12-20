import math
from copy import deepcopy

tp1 = (0, 0, 0, 1.32, 1.20, 1.14, 1.11, 1.09, 1.08, 1.07, 1.06, 1.05, 1.04, 1.03, 1.02, 1.00)
tp2 = (0, 0, 0, 4.30, 3.18, 2.78, 2.57, 2.45, 2.36, 2.31, 2.26, 2.23, 2.13, 2.09, 2.04, 1.96)


# TODO: Replace the calculations with high precision ones (decimal.Decimal if useable) (future feat.)
def mean(data):
    """Compute arithmetic mean of a list of numbers."""
    if not data:
        raise ValueError("mean() arg is an empty sequence")
    return round(float(sum(map(float, data))) / len(data) ,5)

def avg_deviation(data:list) -> list:
    """
    Compute average deviation from the mean for a list of numbers.
    Args:
        data (list): List of numerical values.
    Returns:
        list: List of deviations from the mean.
    """
    m = mean(data)
    return [round(float(x)-m,5) for x in data]



class Dataset:
    """
    A simple dataset holder with statistical helper methods.
    Use with caution: this doesn't use high precision float ops.
    The final output will only preserve up to 5 digits.
    """
    def __init__(self, data:list) -> None:
        """
        Args:
            data(list[str]):  Original data retrieved from sheet
        Properties:
            distribution (str): Type of distribution ('uniform' by default).
            confidence (float): Confidence level (default 0.683).
            ob_data (list[float]): Observed data points as floats. This will remain unmodified after mapping each element to float.
            accuracy (int): Decimal accuracy for results (default 2).
            bvkey (list[int]): Indices of detected bad values.
            inherient_error (float): Inherent error value.
            deviations (list[float]): Average deviations from the mean.
        """
        self.distribution = "uniform"
        self.confidence = 0.683
        self.ob_data = list(map(float, data))
        self.accuracy = 2
        self.inherient_error = 0.0
        self.require_log = False
        self.require_reciprocal = False
        self.dispose_log:dict[int,dict] ={}
        
        
        
    
    def standard_error(self,data=None) -> float:
        """
        Calculate the standard error of the dataset.
        
        Args:
            data (list[float]): List of numerical values.
        
        Returns:
            float(float): Standard error value.
        """
        data = self.ob_data if data is None else data
        square_sum = sum(math.pow(d, 2) for d in avg_deviation(data))
        n = len(data)
        if n == 0:
            # For empty data return 0.0 to allow callers to handle gracefully
            return 0.0
        base = math.sqrt(square_sum / n)
        if n <= 10:
            factor = tp1[n] if self.confidence == 0.683 else tp2[n]
        elif 10 < n <= 15:
            factor = 1.05 if self.confidence == 0.683 else 2.23
        elif 15 < n <= 20:
            factor = 1.04 if self.confidence == 0.683 else 2.13
        elif 20 < n <= 30:
            factor = 1.03 if self.confidence == 0.683 else 2.09
        elif 30 < n <= 50:
            factor = 1.02 if self.confidence == 0.683 else 2.04
        else:
            factor = 1.00 if self.confidence == 0.683 else 1.96
        
        return factor * base
    
    def _chk_bad_value(self,data,se) -> list:
        """
        (Internal) Check for bad values and return the indices.
        Args:
            data (list[float]): List of numerical values.
            se (float): Standard error of data.
        Returns:
            list (list[int]): Indices of bad values.
        """
        # Guard against empty data or zero standard error
        if not data:
            return []
        if not se:
            return []
        deviations = avg_deviation(data)

        return [i for i, d in enumerate(deviations) if abs(d) > 3 * se]
    
    def rm_bad_value(self) -> list | None:
        """
        Remove bad values.
        Write cleaned data and se every epoch into dispose_log.
        Returns:
            list (list[float]): Cleaned data.
        """
        
        # Since the se of 'data to be computed' impacts the result of bad value compute, we zip them into a dict
        
        se = self.standard_error(self.ob_data) if self.ob_data else 0.0
        
        # Work on a copy so original is preserved until we finalize
        bundled_data = deepcopy(self.ob_data)
        se = self.standard_error(bundled_data) if bundled_data else 0.0

        # 记录初始状态为epoch0
        epoch = 0
        self.dispose_log[epoch] = {
            "data": deepcopy(bundled_data),
            "mean": mean(bundled_data) if bundled_data else None,
            "deviation": avg_deviation(bundled_data) if bundled_data else [],
            "se": round(se,5),
        }
        # If no bad values at all, return original observed data
        if not self._chk_bad_value(self.ob_data, se):
            return self.ob_data
        
        # 开始去除坏值的循环
        while True:
            idx = self._chk_bad_value(bundled_data, se)
            if not idx:
                break
            epoch += 1
            for i in reversed(idx):
                if 0 <= i < len(bundled_data):
                    bundled_data.pop(i)

            # recompute se (guard empty)
            se = self.standard_error(bundled_data) if bundled_data else 0.0

            # compute mean/deviation only when data exists
            mean_val = mean(bundled_data) if bundled_data else None
            deviation = avg_deviation(bundled_data) if bundled_data else []

            # store snapshot for this epoch under a unique key
            self.dispose_log[epoch] = {
                "data": deepcopy(bundled_data),
                "mean": mean_val,
                "deviation": deviation,
                "se": se,
            }

            # if data exhausted, stop
            if not bundled_data:
                break

        return bundled_data
    
    def pushback_optional(self):
        """
        Calculate log and reciprocal if needed and pushback into dispose_log.
        """
        if self.dispose_log:
            epochs:list[int] = list(self.dispose_log.keys())
            for epoch in epochs:
                self.dispose_log[epoch]["log"] = [round(math.log(x),5) if x > 0 else math.nan for x in self.dispose_log[epoch]["data"]] if self.require_log else None
                self.dispose_log[epoch]["reciprocal"] = [round((1/x),5) if x!=0 else math.inf for x in self.dispose_log[epoch]["data"]] if self.require_reciprocal else None

    def uncertainty_A(self, data):
        return self.standard_error(data) / math.sqrt(len(data))
    
    def uncertainty_B(self):
        if self.distribution == "Gaussian":
            return self.inherient_error / 3
        else:
            return self.inherient_error / 1.46
    

