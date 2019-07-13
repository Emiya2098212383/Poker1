# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Emiya

# 目的:
# 给扑克牌洗牌

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



shuffledDeck = []
count = len(deck)
for i in range(count):
    pickedCard = random.choice(deck)
    shuffledDeck.append(pickedCard)
    deck.remove(pickedCard)

f = codecs.open("洗完了的扑克牌.txt", "w", "utf-8")
for card in shuffledDeck:
    f.write(card)
    f.write('\n')
f.close

# method 2:
# shuffledDeck = copy.copy(deck)
# random.shuffle(shuffledDeck)

p1_deck=[]
for i in range(18):
    p1_deck.append(shuffledDeck[i])
    shuffledDeck.remove(shuffledDeck[i])

f = codecs.open("玩家1的牌.txt", "w", "utf-8")
for card in p1_deck:
    f.write(card)
    f.write('\n')
f.close

print(p1_deck)






p2_deck=[]
for i in range(18):
    p2_deck.append(shuffledDeck[i])
    shuffledDeck.remove(shuffledDeck[i])

f = codecs.open("玩家2的牌.txt", "w", "utf-8")
for card in p2_deck:
    f.write(card)
    f.write('\n')
f.close

print(p2_deck)







p3_deck=[]
for i in range(18):
    p3_deck.append(shuffledDeck[i])

f = codecs.open("玩家3的牌.txt", "w", "utf-8")
for card in p3_deck:
    f.write(card)
    f.write('\n')
f.close

print(p3_deck)





# print(shuffledDeck)
