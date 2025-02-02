import pytest

def test_negative_sum():
    # Sample function to test negative sum
    def sum(a, b):
        return a + b

    result = sum(-5, -10)
    assert result == -15, f"Expected -15 but got {result}"
