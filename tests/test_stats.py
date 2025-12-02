import math
import pytest

from stats import mean, Dataset


def test_mean_basic():
    assert mean([1, 2, 3]) == pytest.approx(2.0)
    assert mean([0.5, 0.5]) == pytest.approx(0.5)


def test_avg_deviation_and_standard_error():
    data = [1.0, 2.0, 3.0]
    ds = Dataset(data)
    dev = ds.avgDeviation()
    # deviations relative to mean 2.0
    assert dev == [pytest.approx(-1.0), pytest.approx(0.0), pytest.approx(1.0)]

    # standardError uses TP1/TP2 factors; for n=3 and default confidence=0.683 factor=TP1[3]=1.32
    # square_sum = 1 + 0 + 1 = 2; base = sqrt(2/3)
    expected = 1.32 * math.sqrt(2.0 / 3.0)
    assert ds.standardError() == pytest.approx(expected)


def test_remove_bad_value_clears_bvkey_and_removes():
    data = [10.0, 1000.0, 10.0]
    ds = Dataset(data)
    # force a bad-value key (simulate detection)
    ds.bvkey = [1]
    cleaned = ds.removeBadValue()
    assert cleaned == [10.0, 10.0]
    assert ds.bvkey == []
