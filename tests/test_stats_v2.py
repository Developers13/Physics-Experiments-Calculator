import math
import pytest

from stats import mean, avg_deviation, Dataset


def test_mean_basic():
    assert mean([1, 2, 3]) == pytest.approx(2.0)
    assert mean([0.5, 0.5]) == pytest.approx(0.5)


def test_avg_deviation_and_standard_error():
    data = [1.0, 2.0, 3.0]
    # top-level avg_deviation function
    dev = avg_deviation(data)
    assert dev == [pytest.approx(-1.0), pytest.approx(0.0), pytest.approx(1.0)]

    ds = Dataset(data)
    # for n=3 and default confidence=0.683 factor=tp1[3]=1.32
    expected = 1.32 * math.sqrt(2.0 / 3.0)
    assert ds.standard_error() == pytest.approx(expected)


def test_rm_bad_value_removes_outlier_and_logs_epochs():
    data = [10.0, 1000.0, 10.0]
    ds = Dataset(data)

    # monkeypatch _chk_bad_value to simulate detection of index 1 on first call
    calls = {"n": 0}

    def fake_chk(data_arg, se_arg):
        calls["n"] += 1
        # return [1] for the initial existence check and the first loop iteration,
        # then return [] to stop further removals
        return [1] if calls["n"] in (1, 2) else []

    ds._chk_bad_value = fake_chk
    cleaned = ds.rm_bad_value()

    # outlier (index 1) should be removed by our simulated detection
    assert cleaned == [10.0, 10.0]
    # original Dataset.ob_data may not be mutated by rm_bad_value; assert returned cleaned list instead
    assert cleaned == [10.0, 10.0]
    # dispose_log should contain at least one epoch entry whose data length is 2
    assert any(isinstance(v, dict) and len(v.get("data", [])) == 2 for v in ds.dispose_log.values())
