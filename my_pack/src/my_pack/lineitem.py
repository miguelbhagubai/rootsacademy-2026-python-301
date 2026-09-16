BULK_DISCOUNT = 0.1
BULK_QTY = 10


def format_money(amount: float) -> str:
    return f"EUR {amount:,.2f}"


class LineItem:
    def __init__(self, name: str, qty: int, unit_price: float) -> None:
        self.description = name
        self.quantity = qty
        self.price = unit_price

    @property
    def is_bulk(self) -> bool:
        return self.quantity >= BULK_QTY

    @property
    def total(self) -> float:
        total = self.quantity * self.price
        if self.is_bulk:
            total -= total * BULK_DISCOUNT
        return total

    def format_line(self) -> str:
        total = self.total
        marker = " (bulk)" if self.is_bulk else ""
        qty = f"x{self.quantity}"
        return f"{self.description:<20}{qty:<6}{format_money(total):>10}{marker}"
