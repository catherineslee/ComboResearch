import math
total = combination(52, 5)
def main():

    arr = ["Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind", "Two Pairs", "Pair", "High Card"]
    for i in range(1, 10):
        print("[" + str(i) + "] : " + arr[i-1])

    cards = input("\n Choose a winning hand to determine the probability")

    #check what input matches with the list
    if (cards == "1"):
        arr = straightFlush()
        print("The number of ways of getting a straight flush is " + arr[0])
        print("The probability of getting a straight flush is " + arr[1])

    elif (cards == "2"):
        arr = fourKind()
        print("The number of ways of getting a four of a kind is " + arr[0])
        print("The probability of getting a four of a kind " + arr[1])

    elif (cards == "3"):
        arr = fullHouse()
        print("The number of ways of getting a full house is " + arr[0])
        print("The probability of getting a full house is " + arr[1])

    elif (cards == "4"):
        arr = flush()
        print("The number of ways of getting a flush is " + arr[0])
        print("The probability of getting a flush is " + arr[1])

    elif (cards == "5"):
        arr = straight()
        print("The number of ways of getting a straight is " + arr[0])
        print("The probability of getting a straight is " + arr[1])

    elif (cards == "6"):
        arr = threeKind()
        print("The number of ways of getting a three of a kind is " + arr[0])
        print("The probability of getting a three of a kind is " + arr[1])

    elif (cards == "7"):
        arr = twoPair()
        print("The number of ways of getting a two pair is " + arr[0])
        print("The probability of getting a two pair is " + arr[1])

    elif (cards == "8"):
        arr = pair()
        print("The number of ways of getting a pair is " + arr[0])
        print("The probability of getting a pair is " + arr[1])

    elif (cards == "9"):
        arr = highCard()
        print("The number of ways of getting a high cards is " + arr[0])
        print("The probability of getting a high card is " + arr[1])

def combination(n, r):
    numerator = math.factorial(n)
    denom = (math.factorial(n-r))*math.factorial(r)
    return numerator/denom

def straightFlush():
    suit = combination(4, 1)
    first = combination(10, 1)
    second = 1
    third = 1
    fourth = 1
    fifth = 1

    freq = (suit*first*second*third*fourth)
    prob = freq/total
    return [freq, prob]


def fourKind():
    denom = combination(13, 1)
    suit = combination(4, 4)
    fifth = combination(52-4, 1)

    freq = denom*suit*fifth
    prob = freq/total
    return [freq, prob]

def fullHouse():
    firstDenom = combination(13, 1)
    firstSuit = combination(4, 3)
    secondDenom = combination(12, 1)
    secondSuit = combination(4, 2)

    freq = firstDenom*firstSuit*secondDenom*secondSuit
    prob = freq/total
    return [freq, prob]

def flush():
    denom = combination(13, 5)
    suits = combination(4, 1)

    freq = denom*suits
    prob = freq/total
    return [freq, prob]

def straight():
    denom = combination(10, 1)
    cards = math.pow(5, combination(4, 1))

    freq = denom*cards
    prob = freq/total
    return [freq, prob]

def threeKind():
    firstDenom = combination(13, 1)
    firstSuits = combination(4, 3)
    secondDenom = combination(12, 2)
    secondSuits = math.pow(2, combination(4, 1))

    freq = firstDenom*firstSuits*secondDenom*secondSuits
    prob = freq/total
    return [freq, prob]

def twoPair():
    firstDenom = combination(13, 2)
    firstSuits = math.pow(2, combination(4, 2))
    secondDenom = combination(11, 1)
    secondSuits = combination(4, 1)
    
    freq = firstDenom*firstSuits*secondDenom*secondSuits
    prob = freq/total
    return [freq, prob]

def pair():
    firstDenom = combination(13, 1)
    firstSuits = combination(4, 2)
    secondDenom = combination(12, 3)
    secondSuits = math.pow(3, combination(4, 1))

    freq = firstDenom*firstSuits*secondDenom*secondSuits
    prob = freq/total
    return [freq, prob]

def highCard():
    denom = combination(13, 5) - 10
    suits = math.pow(5, combination(4, 1)) - 4

    freq = denom*suits
    prob = freq/total
    return [freq, prob]

if __name__ == "__main__":
    main()