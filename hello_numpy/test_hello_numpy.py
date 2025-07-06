import pytest
import numpy as np
from hello_numpy.hello_numpy import generate_int_matrix, calculate_determinant

def test_generate_int_matrix_defaultshape_and_type():
    matrix = generate_int_matrix()
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (3, 3)
    assert issubclass(matrix.dtype.type, np.integer)

def test_generate_int_matrix_raises_on_invalid_range():
    with pytest.raises(ValueError):
        generate_int_matrix(low=10, high=5)

def test_generate_int_matrix_range():
    low, high = -5, 5
    matrix = generate_int_matrix(low=low, high=high)
    assert np.all(matrix >= low)
    assert np.all(matrix <= high)

def test_calculate_determinant_on_known_matrix():
    matrix = np.array([[1, 2, 3],
                       [0, 1, 4],
                       [5, 6, 0]])
    det = calculate_determinant(matrix)
    assert round(det) == 1  # Znany wynik

def test_calculate_determinant_type():
    matrix = generate_int_matrix()
    det = calculate_determinant(matrix)
    assert isinstance(det, float)

def test_rounded_determinant_is_integer():
    matrix = generate_int_matrix()
    det = int(round(calculate_determinant(matrix)))
    assert isinstance(det, int)

def test_calculate_determinant_non_square_raises():
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6]])
    with pytest.raises(ValueError):
        calculate_determinant(matrix)

def test_calculate_determinant_raises_on_non_square_generated_matrix():
    matrix = generate_int_matrix(size=(2, 4))
    with pytest.raises(ValueError):
        calculate_determinant(matrix)
