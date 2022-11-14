# identify if there is one or more pairs in the hand
import random

# Rank: {2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A}
# Suit: {s, h, d, c}
deck = ['2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As',
        '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah',
        '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad',
        '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ac']

cardValue = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, }
# 2 example poker hands
CurrentHand1 = ['Ad', '2s', '2c']
CurrentHand2 = ['5s', '5c', '5d']
highestValue = []
handSet = []
takenIndexes = []


# Randomly generate two hands of n cards
def generate_2hands(nn_card):
    i = 0
    while i < nn_card:
        randomCard = random.randint(0, 51)
        if not (randomCard in takenIndexes):
            CurrentHand1[i] = deck[randomCard]
            takenIndexes.append(randomCard)
            i = i + 1

    i = 0
    while i < nn_card:
        randomCard = random.randint(0, 51)
        if not (randomCard in takenIndexes):
            CurrentHand2[i] = deck[randomCard]
            takenIndexes.append(randomCard)
            i = i + 1
    pass


def identifyHand(Hand_):
    count = 0
    winningHand = []
    total = []
    for card in Hand_:
        total = [i for i in Hand_ if card[0] in i]
        print(total)
        if count < len(total):
            count = len(total)
            highestHand = total
            print("count " + str(count))


    match count:
        case 1:
            for card in Hand_:
                if not (card[0].isdigit()):
                    highestValue.append(int(cardValue.get(card[0])))
                else:
                    highestValue.append(int(card[0]))
            highestValue.sort(reverse=True)
            yield dict(name='High card', rank='n/a', suit1=highestValue[0], suit2=highestValue[1])
        case 2:
            yield dict(name='Pair', rank=highestHand[0][0], suit1=highestHand[0][1], suit2=highestHand[1][1])
        case 3:
            yield dict(name='Triple', rank=highestHand[0][0])
        case default:
            yield dict(name='Null')


# Print out the result
def analyseHand(Hand_):
    HandCategory = []
    functionToUse = identifyHand
    for category in functionToUse(Hand_):
        print('Category: ')

        for key in category.keys():
            print(key, "=", category[key]),


def randomPlayer():
    return random.randint(0, 50)


def fixedPlayer():
    return 10


generate_2hands(3)

for card in CurrentHand1:
    print(card)
print()
for card in CurrentHand2:
    print(card)
print()
CurrentHand2 = ['Ad', 'Ah', 'As']
analyseHand(CurrentHand1)
analyseHand(CurrentHand2)
print()

#########################
#      Game flow        #
#########################


#########################
# phase 1: Card Dealing #
#########################


#########################
# phase 2:   Bidding    #
#########################


#########################
# phase 3:   Showdown   #
#########################
