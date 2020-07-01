import pytest

from some_function import transform


@pytest.mark.parametrize("input_data, expected",
                         [
                             ([0, 1, 2], [-1, 1, 3]),
                             ([997, 998, 999], [1993, 1995, 1997]),
                             ([5], [9]),
                             ([], []),
                             (["string"], [])
                         ]
                         )
def test_transform(input_data, expected):
    actual = transform(input_data)

    assert actual == expected
