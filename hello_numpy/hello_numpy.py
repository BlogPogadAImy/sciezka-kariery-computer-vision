import numpy as np

def generate_int_matrix(low: int = -10, high: int = 10, size: tuple = (3, 3)) -> np.ndarray:
    """Tworzy losową macierz liczb całkowitych o zadanym rozmiarze i zakresie."""
    if low > high:
        raise ValueError("Parametr 'low' nie może być większy niż 'high'")

    return np.random.randint(low, high + 1, size)

def calculate_determinant(matrix: np.ndarray) -> float:
    """Oblicza wyznacznik macierzy."""
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Macierz musi być kwadratowa")
    
    return int(round(np.linalg.det(matrix)))

if __name__ == "__main__":
    matrix = generate_int_matrix()
    det = calculate_determinant(matrix)

    print("\nMacierz 3×3:")
    print(matrix)
    print(f"\nWyznacznik: {det}")
