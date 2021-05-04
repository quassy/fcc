from typing import List


class Category:
    def __init__(
        self,
        category: str,
    ):
        self.category: str = category
        self.balance: float = 0.0
        self.ledger: List[dict] = []

    def update_balance(self) -> None:
        self.balance = sum([l["amount"] for l in self.ledger])

    def get_balance(self) -> float:
        return self.balance

    def check_funds(self, amount: float) -> bool:
        if amount > self.balance:
            return False
        return True

    def deposit(
        self,
        amount: float,
        description: str = "",
    ) -> None:
        transaction = {"amount": amount, "description": description}
        self.ledger += [transaction]
        self.update_balance()

    def withdraw(
        self,
        amount: float,
        description: str = "",
    ) -> bool:
        if not self.check_funds(amount):
            return False
        transaction = {"amount": -amount, "description": description}
        self.ledger += [transaction]
        self.update_balance()
        return True

    def transfer(self, amount: float, to_category: str) -> bool:
        if not self.withdraw(amount, f"Transfer to {to_category.category}"):
            return False
        to_category.deposit(amount, f"Transfer from {self.category}")
        return True

    def __str__(self) -> None:
        text = f"{self.category:*^30}\n"
        for l in self.ledger:
            d = l["description"][:23]
            a = l["amount"]
            text += f"{d: <23}{a:7.2f}\n"
        text +=f"Total: {self.balance:.2f}"
        return text


def create_spend_chart(categories):
    spents = {}
    totals = {}
    for c in categories:
        spents[c.category] = [l["amount"] for l in c.ledger if l["amount"] < 0]
        totals[c.category] = sum(spents[c.category])

    overall = sum(totals.values())
    percentages = {k: v/overall for k, v in totals.items()}

    text = "Percentage spent by category\n"
    for index in range(100, -10, -10):
        text += f"{index: >3}|"
        for v in percentages.values():
            if v >= index/100:
                text += " o "
            else:
                text += "   "
        text += " \n"

    text += "    " + "---" * len(totals) + "-\n"

    for index in range(0, max(map(len, percentages.keys()))):
        text += "    "
        for k in percentages.keys():
            text += f" {k[index:index+1] or ' '} "
        text += " \n"

    return text[:-2] + " "
