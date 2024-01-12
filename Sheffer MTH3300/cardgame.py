import random

class Card:    
    Suits =['Clubs','Diamonds','Spades','Hearts']
    Ranks = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    
    def __init__(self,suit = 0,rank = 2):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.Ranks[self.rank] + ' of ' + self.Suits[self.suit]
        
    def __lt__(self, other):
        return self.rank < other.rank
    
    def __eq__(self, other):
        return self.rank == other.rank
    
    def __le__(self, other):
        return self.rank <= other.rank


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,15):
                card = Card(suit,rank)
                self.cards.append(card)
        self.shuffle()
                
    def __str__(self):
        answer = ''
        for card in self.cards:
            answer = answer+str(card)+'\n'
        return answer
    
    def dealOne(self): #returns the last card and removes it from self.cards
        return self.cards.pop()
    
    def topToBottom(self):
        self.cards.insert(0,self.dealOne())
        
    def bottomToTop(self):
        self.cards.append(self.cards.pop(0))
        
    def shuffle(self):
        random.shuffle(self.cards)


class Hand:
    def __init__(self,*cards): 
        self.hand = []
        for card in cards:
            self.hand.append(card) 
    
    def __str__(self):
        self.handStr = 'Hand: '
        for card in self.hand:    
            self.handStr += str(card)
            if card != self.hand[-1]:
                self.handStr += ', '
        return str(self.handStr)
    
class Hands:
    def __init__(self,numPeople,numPer):
        self.hands = {}
        self.deck = Deck()
        for num in range(numPer):
            for numPerson in range(numPeople):
                self.hands.update({f'Hand {numPerson+1}':self.hands})
                
    def __str__(self):       
        answer = ' '
        for hands in self.hands:
            answer += hands + ': ' + get(hands)
        return answer
                
        

    
    

myHand = Hands(2,3)
print(str(myHand))











    
    
    
