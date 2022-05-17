import pytest
from decimalToRoman import decimalToRomans

@pytest.mark.parametrize(
    "decimal, expected",
    [
        (5, "V"),
        (23, "XXIII"),
        (46, "XLVI"),
        (690, "DCXC"),
        (3900, "MMMCM")
    ]
)

def test_Romans(decimal, expected):
    assert decimalToRomans(decimal) == expected