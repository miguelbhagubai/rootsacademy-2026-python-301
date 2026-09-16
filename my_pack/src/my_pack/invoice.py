from .lineitem import LineItem, format_money

TAX_RATE = 0.21


class Invoice:
    def __init__(self, line_items: list[LineItem]) -> None:
        self.line_items = line_items

    @property
    def subtotal(self) -> float:
        return sum(item.total for item in self.line_items)

    @property
    def tax(self) -> float:
        return self.subtotal * TAX_RATE

    @property
    def total(self) -> float:
        return self.subtotal + self.tax

    def render(self) -> str:
        lines = ["INVOICE", "=" * 42]
        lines.extend(item.format_line() for item in self.line_items)

        subtotal = self.subtotal
        tax = self.tax
        total = self.total

        lines.append("-" * 42)
        lines.append(f"{'Subtotal':<26}{format_money(subtotal):>10}")
        lines.append(f"{'Tax (21%)':<26}{format_money(tax):>10}")
        lines.append(f"{'Total':<26}{format_money(total):>10}")
        return "\n".join(lines) + "\n"
