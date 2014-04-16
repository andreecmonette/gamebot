from enum import Enum
from collections import OrderedDict
from itertools import chain, cycle, product
import random
import uuid

"""
Player State tracked with OrderedDict <- this also describes turn info
round of betting?
dealer
whose turn is it?
"""

##order of play:
##the gamebot is tracking no games and tracking no users
##if a user sends a command to gamebot and it is not tracking that user, it creates a new user object
##
##users can start games
##usage: `play poker [options]`
##
##users can join games in progress: usage `join poker [id]`
##users can observe games:
##
##games have tokens, players, and actions
##tokens may be objects such as cards, or the turn
##tokens may be represented only privately or they may be represented publicly
##a game may append items to the user's statistics for that game, and the game may have methods for displaying such statistics on request
##`stat poker`

## when we create a game we put it int


gamebotParseList = {};
gamedefs = {};


def main():

def recv_message(message):
  

class Game:
  def __init__(self):
    self.state = GameState()
    self.actions = []
    self.stream = ""

class GameState:
  def __init__(self):
    self.tokens = []
    self.players = {}
  
  def addToken(TokenClass, player = None,  *args):
    self.tokens.append(TokenClass(*args))
    if player is not None:
      token.player = player


class Gamedef:
  def __init__(self, gameName):
    self.gameName = gameName
    gamedefs[gameName] = self

  def Start(fun):
    def beginGame():

    gamebotParseList["play " + self.gameName] = fun
    return fun

  def Action(fun):
    def ActionDecorator(word_list):
      for word in word_list:
        gamebotParseList[word] = fun
      return fun
    return ActionDecorator

  def Player(cls):




def genNewGameId():
  return uuid4()

def recv_message(msg):
  pass
#Looks to see if there is a message in `backticks`
#If not, do nothing
#If so, pass on to 





def gameLoop():
  while True:
    nextturn(state)
    if checkGameOver(state):
      return state
  





class gameBot:
  def __init__(self):
    self.users = set()
    self.gameDefs = {}  
    self.games = {}

  def recieveMessage(self, message):
    if message.user not in self.users:
      users.add(User())

    if message.game == None:
      
class Round:
  def __init__(self, players, blind, dealer):
    
  def tryBet(player) 

class Player:
  def __init__(self, UserID, email):
    self.playerID = playerID
    self.email = email
    self.cumulativeBuyin = 0
    self.value = 0
    self.games = []
  
  def buyIn(self, amount):
    self.cumulativeBuyin += amount
    self.value += amount
  
  def join(self, game):
    game.join(player)
    self.games.append(game)

class 
  def _







class BetResult(Enum):
  call = "call"
  raisebet = "raise"
  invalid_bet = "invalid bet"
  winner = "winner"

class Decision(Enum):
  fold = 'fold'
  bet = 'bet'
  check = 'check'

class Card:
  def __init__(self, suit, number):
    self.suit = suit
    self.number = number

  def __str__(self):
    if self.number == 11:
      n = "J"
    elif self.number == 12:
      n = "Q"
    elif self.number == 13:
      n = "K"
    elif self.number == 14:
      n = "A"
    else:
      n = self.number

    return "{!s}{!s}".format(n, self.suit)

  def __repr__(self):
    return str(self)

  @classmethod
  def shuffled_deck(cls):
    deck = []
      for suit, number in product(Suits, range(1, 14)):
        deck.append(cls(suit, number))
      random.shuffle(deck)
      return deck

class Suits(Enum):
  """
  Unicode hex numbers for

  spade: 2660, heart: 2665, diamond: 2666, club: 2663
  """
  heart = "\u2665"
  spade = "\u2660"
  diamond = "\u2666"
  club = "\u2663"

  def __str__(self):
    if self == Suits.heart:
      return "\u2665"
    elif self == Suits.spade:
      return "\u2660"
    elif self == Suits.diamond:
      return "\u2666"
    elif self == Suits.club:
      return "\u2663"

if __name__ == "__main__":
  main()

