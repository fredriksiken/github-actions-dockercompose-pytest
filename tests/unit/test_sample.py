import pytest
import sample

def test_sample():
    sum = sample.sum(1, 1)
    assert sum == 2
def test_sample_fail():
    sum = sample.sum(2, 1)
    assert sum == 2
