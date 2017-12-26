'''
命名元组
列表生成式
string.spilt()
random.choice()
__len__
'''
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDesk:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

desk = FrenchDesk()
print(len(desk))
print(desk[0])

print(choice(desk))
print(choice(desk))


for card in desk:
    print(card)
