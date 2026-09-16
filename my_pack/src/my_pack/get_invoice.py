from .invoice import Invoice
from .lineitem import LineItem

DEFAULT_ORDERS: list[tuple[str, int, float]] = [
    ("Hex Bolt M6", 25, 0.15),
    ("Washer M6", 25, 0.05),
    ("Cordless Drill", 1, 89.99),
    ("Drill Bit Set", 3, 12.50),
]


def main(orders: list[tuple[str, int, float]]) -> str:
    """Build the invoice text for the given orders."""
    invoice = Invoice([LineItem(name, qty, unit_price) for name, qty, unit_price in orders])
    return invoice.render()


def cli() -> None:
    """Console-script entry point: print the invoice for the default orders."""
    print(main(DEFAULT_ORDERS), end="")
