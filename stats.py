import math

# t-factors used by the original code for small samples
TP1 = (0, 0, 0, 1.32, 1.20, 1.14, 1.11, 1.09, 1.08, 1.07, 1.06, 1.05, 1.04, 1.03, 1.02, 1.00)
TP2 = (0, 0, 0, 4.30, 3.18, 2.78, 2.57, 2.45, 2.36, 2.31, 2.26, 2.23, 2.13, 2.09, 2.04, 1.96)


def mean(data):
    """Compute arithmetic mean of a list of numbers."""
    if not data:
        raise ValueError("mean() arg is an empty sequence")
    return float(sum(map(float, data))) / len(data)


class Dataset:
    """A lightweight dataset holder with simple statistical helpers.

    This preserves names compatible with the old code (avgDeviation, standardError, etc.)
    but uses clearer, typed internals.
    """

    def __init__(self, org):
        self.distribution = "uniform"
        self.confidence = 0.683
        self.org = [float(x) for x in org]
        self.accuracy = 2
        self.bvkey = []
        self.inherientError = 0.0

    def avgDeviation(self, org=None):
        data = org if org is not None else self.org
        m = mean(data)
        return [float(x) - m for x in data]

    def standardError(self):
        diffs = self.avgDeviation(self.org)
        square_sum = sum(d * d for d in diffs)
        n = len(self.org)
        if n == 0:
            raise ValueError("standardError requires non-empty dataset")

        # Base sqrt term (sample deviations summed / n)
        base = math.sqrt(square_sum / n)

        # Apply coefficients to mimic original behavior
        if n <= 10:
            factor = TP1[n] if self.confidence == 0.683 else TP2[n]
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

    def checkBadValue(self, org=None):
        data = org if org is not None else self.org
        self.bvkey = []
        deviations = self.avgDeviation(data)
        se = self.standardError()
        for i, d in enumerate(deviations):
            if abs(d) > 3 * se:
                self.bvkey.append(i)

    def removeBadValue(self, org=None):
        data = list(org if org is not None else self.org)
        if not self.bvkey:
            return data
        for idx in sorted(set(self.bvkey), reverse=True):
            if 0 <= idx < len(data):
                data.pop(idx)
        # clear recorded keys
        self.bvkey.clear()
        return data

    def UncertaintyA(self):
        return self.standardError() / math.sqrt(len(self.org))

    def UncertaintyB(self):
        if self.distribution == "Gaussian":
            return self.inherientError / 3
        else:
            return self.inherientError / 1.46

