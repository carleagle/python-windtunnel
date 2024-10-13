def test_cards():
    testColor = {'H': 'Hearts', 'D' : 'Diamonds', 'C' : 'Clubs', 'S' : 'Spades'}
    testRanks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    displayAllCards(testColor, testRanks)
    testCards = genCardDict(testColor, testRanks)
    goldenCards = {'H1': ('Ace', 'Hearts'), 'H2': ('Two', 'Hearts'), 'H3': ('Three', 'Hearts'), 'H4': ('Four', 'Hearts'), 'H5': ('Five', 'Hearts'), 'H6': ('Six', 'Hearts'), 'H7': ('Seven', 'Hearts'), 'H8': ('Eight', 'Hearts'), 'H9': ('Nine', 'Hearts'), 'H10': ('Ten', 'Hearts'), 'H11': ('Jack', 'Hearts'), 'H12': ('Queen', 'Hearts'), 'H13': ('King', 'Hearts'), 'D1': ('Ace', 'Diamonds'), 'D2': ('Two', 'Diamonds'), 'D3': ('Three', 'Diamonds'), 'D4': ('Four', 'Diamonds'), 'D5': ('Five', 'Diamonds'), 'D6': ('Six', 'Diamonds'), 'D7': ('Seven', 'Diamonds'), 'D8': ('Eight', 'Diamonds'), 'D9': ('Nine', 'Diamonds'), 'D10': ('Ten', 'Diamonds'), 'D11': ('Jack', 'Diamonds'), 'D12': ('Queen', 'Diamonds'), 'D13': ('King', 'Diamonds'), 'C1': ('Ace', 'Clubs'), 'C2': ('Two', 'Clubs'), 'C3': ('Three', 'Clubs'), 'C4': ('Four', 'Clubs'), 'C5': ('Five', 'Clubs'), 'C6': ('Six', 'Clubs'), 'C7': ('Seven', 'Clubs'), 'C8': ('Eight', 'Clubs'), 'C9': ('Nine', 'Clubs'), 'C10': ('Ten', 'Clubs'), 'C11': ('Jack', 'Clubs'), 'C12': ('Queen', 'Clubs'), 'C13': ('King', 'Clubs'), 'S1': ('Ace', 'Spades'), 'S2': ('Two', 'Spades'), 'S3': ('Three', 'Spades'), 'S4': ('Four', 'Spades'), 'S5': ('Five', 'Spades'), 'S6': ('Six', 'Spades'), 'S7': ('Seven', 'Spades'), 'S8': ('Eight', 'Spades'), 'S9': ('Nine', 'Spades'), 'S10': ('Ten', 'Spades'), 'S11': ('Jack', 'Spades'), 'S12': ('Queen', 'Spades'), 'S13': ('King', 'Spades')}
    assert (goldenCards == testCards)

def displayAllCards(paramColorDict, paramRanksList):
    x = 0
    for ranks in paramRanksList:
        x += 1
        for color in paramColorDict:
            j = color+str(x)
            print(f"{j:>3} : {ranks} of {paramColorDict[color]}", end='\t')
        print()

def genCardDict(paramColorDict, paramRanksList):
    cardsDict = {'H1': ('Ace', 'Hearts'), 'H2': ('Two', 'Hearts'), 'H3': ('Three', 'Hearts'), 'H4': ('Four', 'Hearts'), 'H5': ('Five', 'Hearts'), 'H6': ('Six', 'Hearts'), 'H7': ('Seven', 'Hearts'), 'H8': ('Eight', 'Hearts'), 'H9': ('Nine', 'Hearts'), 'H10': ('Ten', 'Hearts'), 'H11': ('Jack', 'Hearts'), 'H12': ('Queen', 'Hearts'), 'H13': ('King', 'Hearts'), 'D1': ('Ace', 'Diamonds'), 'D2': ('Two', 'Diamonds'), 'D3': ('Three', 'Diamonds'), 'D4': ('Four', 'Diamonds'), 'D5': ('Five', 'Diamonds'), 'D6': ('Six', 'Diamonds'), 'D7': ('Seven', 'Diamonds'), 'D8': ('Eight', 'Diamonds'), 'D9': ('Nine', 'Diamonds'), 'D10': ('Ten', 'Diamonds'), 'D11': ('Jack', 'Diamonds'), 'D12': ('Queen', 'Diamonds'), 'D13': ('King', 'Diamonds'), 'C1': ('Ace', 'Clubs'), 'C2': ('Two', 'Clubs'), 'C3': ('Three', 'Clubs'), 'C4': ('Four', 'Clubs'), 'C5': ('Five', 'Clubs'), 'C6': ('Six', 'Clubs'), 'C7': ('Seven', 'Clubs'), 'C8': ('Eight', 'Clubs'), 'C9': ('Nine', 'Clubs'), 'C10': ('Ten', 'Clubs'), 'C11': ('Jack', 'Clubs'), 'C12': ('Queen', 'Clubs'), 'C13': ('King', 'Clubs'), 'S1': ('Ace', 'Spades'), 'S2': ('Two', 'Spades'), 'S3': ('Three', 'Spades'), 'S4': ('Four', 'Spades'), 'S5': ('Five', 'Spades'), 'S6': ('Six', 'Spades'), 'S7': ('Seven', 'Spades'), 'S8': ('Eight', 'Spades'), 'S9': ('Nine', 'Spades'), 'S10': ('Ten', 'Spades'), 'S11': ('Jack', 'Spades'), 'S12': ('Queen', 'Spades'), 'S13': ('King', 'Spades')}
    return cardsDict

def parseInputCards(inString):
    # Hint : you can use strip() and split() functions
    cardList = [card for card in str(inString).split(" ") if card != ""]
    return cardList

def isValidInput(parsedInput):
    result = all([t_val in cards.keys() for t_val in (parsedInput)]) and len(set(parsedInput)) == len(parsedInput) == 5
    return result

def displayCards(cardList):
    print('Your cards are the following : \n')
    for i in cardList:
        print(i, ":",cards[i][0], 'of', cards[i][1])

def printDivider(divLength):
    print(f'{"*"*divLength}')

def printTitle(title, margin):
    print(f'{"*"*margin} {title} {"*"*margin}')

def printMenu():
    printDivider(95)
    printTitle('P O K E R   H A N D S', 36)
    printDivider(95)
    displayAllCards(colors, ranks)
    printDivider(95)

def isRoyalFlush(fiveCards):
    suits = [card[0] for card in fiveCards]
    ranksinhand = [cards[card][0] for card in fiveCards]
    if len(set(suits)) == 1:  
        royal_ranks = {'Ace', 'King', 'Queen', 'Jack', 'Ten'}
        return True if set(ranksinhand) == royal_ranks else False

def isStraightFlush(fiveCards):
    if isFlush(fiveCards) and isStraight(fiveCards):
        return True
    else:
        return False

def isFourOfaKind(fiveCards):
    ranksinhand = [cards[card][0] for card in fiveCards]
    for i in ranksinhand:
        x = ranksinhand.count(i)
        if x == 4:
            return True
        else: 
            return False

def isFullHouse(fiveCards):
    return isThreeOfaKind(fiveCards) and isPair(fiveCards)

def isFlush(fiveCards):
    suits = [card[0] for card in fiveCards]
    return True if len(set(suits)) == 1 else False

def isStraight(fiveCards):   
    inputrank = [int(card[1:]) for card in fiveCards]
    for i in range(len(inputrank)):
        if i == 4:
            return True
        if inputrank[i+1]-inputrank[i] == 1:
            continue
        else: 
            return False
        
def isThreeOfaKind(fiveCards):
    ranksinhand = [cards[card][0] for card in fiveCards]
    for i in ranksinhand:
        x = ranksinhand.count(i)
        if x == 3:
            return True
        else: 
            return False

def isTwoPair(fiveCards):
    ranksinhand = [cards[card][0] for card in fiveCards]
    j = []
    for i in ranksinhand:
        j.append(ranksinhand.count(i))
    if j.count(2) == 4:
        return True
    else:
        return False

           # return True
        #else: return False

def isPair(fiveCards):
    ranksinhand = [cards[card][0] for card in fiveCards]
    for i in ranksinhand:
        x = ranksinhand.count(i)
        if x == 2:
            return True
        else: 
            return False

def isHighCard(fiveCards):
    ranksinhand = [cards[card][0] for card in fiveCards]
    f = ("")
    for i in ranksinhand:
        x = ranksinhand.count(i)
        if x == 1:
            f = True
            continue
        f = False
        print (f)
    return not(isFlush(fiveCards)) and f

# Global
colors = {'H': 'Hearts', 'D' : 'Diamonds', 'C' : 'Clubs', 'S' : 'Spades'}
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
cards = genCardDict(colors, ranks)

def main():
    while True:
        printMenu()
        userInput = input('\nSelect 5 cards separated by space. e.g. H11 S13 C2 D3 H7 : ')
        inputCards = parseInputCards(userInput)

        validCheckResult = isValidInput(inputCards)
        if (validCheckResult):
            displayCards(inputCards)
            if isRoyalFlush(inputCards):
                print("\nYou have a Royal Flush")
            elif isStraightFlush(inputCards):
                print("\nYou have a Straight Flush")
            elif isFourOfaKind(inputCards):
                print("\nYou have Four of a Kind")
            elif isFullHouse(inputCards):
                print("\You have a Full House")
            elif isFlush(inputCards):
                print("\nYou have a Flush")
            elif isStraight(inputCards):
                print("\nYou have a Straight")
            elif isThreeOfaKind(inputCards):
                print("\nYou have Three of a Kind")
            elif isTwoPair(inputCards):
                print("\nYou have a Two Pair")
            elif isPair(inputCards):
                print("\nYou have a Pair")
            elif isHighCard(inputCards):
                print("\nYou have a High Card")
                        
        else:
            print(f'\nInvalid input !!! : {inputCards}')
            if len(inputCards) != 5:
                print("The hand only supports 5 cards! Please remove or add one card and try again.")
            if any(i.islower() for i in inputCards):
                print("The suit letter must be a capital letter!")
            if any(int(card[1:]) > 13 for card in inputCards if card[1:].isdigit()):
                print("The cards are only up to 13! Please change your cards.")
            if len(inputCards) != len(set(inputCards)):
                print("There is duplicates! Replace the duplicates with a unique card.")
            if ' ' not in inputCards:
                print("There is no space between Cards. Try again.")
            print('\nPlease select a valid card. e.g. H1 S13 C2 D3 D7')

        tryAgain = input('\nPress any key to continue or Q/q to quit : ')
        if (tryAgain.upper() == 'Q'):
            break

if __name__ == "__main__":
    main()