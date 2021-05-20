import pytest
import numpy as np


def test_value(value):
    assert value == 5


@pytest.mark.parametrize('shape', (5, 10))
def test_identity_matrix(shape):
    i = np.eye(shape)
    assert i.trace() == shape
