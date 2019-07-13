# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Emiya

# 目的:
# 扑克牌fa ♂牌

import random
import codecs
import copy


cardJokers = ('♞', '♘')
cardMarks = ('♤', '♡', '♢', '♧')
cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')
deck = []
for c in cardJokers:
    deck.append(c)

for cn in cardNumbers:
    for cm in cardMarks:
        card = cm + cn
        deck.append(card)

f = codecs.open("deck-new-54.txt", "w", "utf-8")
for card in deck:
    f.write(card)
    f.write('\n')
f.close


print(deck)
