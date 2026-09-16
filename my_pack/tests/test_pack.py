"""Check that the invoice demo prints the expected output."""

from pathlib import Path

from my_pack import get_invoice

EXPECTED_OUTPUT = Path(__file__).parent / "expected_output.txt"

ORDERS_TEST: list[tuple[str, int, float]] = [
    ("Hex Bolt M6", 25, 0.15),
    ("Washer M6", 25, 0.05),
    ("Cordless Drill", 1, 89.99),
    ("Drill Bit Set", 3, 12.50),
]


def test_main_prints_expected_invoice() -> None:

    captured = get_invoice.main(ORDERS_TEST)
    assert captured == EXPECTED_OUTPUT.read_text()
