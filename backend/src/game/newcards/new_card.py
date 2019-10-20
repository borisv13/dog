from abc import ABC


class NewCard(ABC):
    def __init__(self, name, cost, effect, footnote=None):
        self.name = name
        self.cost = cost
        self.effect = effect
        self.footnote = footnote
