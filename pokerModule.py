from gamebot import Gamedef 

game = Gamedef("poker")

@game.Start
def init(state, msg):
  pass

@game.Action(["deal"])
def deal(state, msg, options):

@game.Action(["bet", "check"])
def bet(state, msg, options):
  if not state.TurnToken in state.curPlayer:
    return gamebot.TurnError("Not your turn to bet.")
  if msg == "check":
    amount = 0
  else if msg == "bet":
    if len(options) == 1 and options[0]
    amount = options[0]
  return gamebot.publicMessage(state.player "raises to" amount)
    
@game.Action(["fold"])
def fold(state, msg, options):
  state.player.remove(potToken)
  state.refresh()

@game.Player
class MainPlayer:
  def __init__(self):
    startsWith(state.game.players

@game.Token
def TurnToken(state):
  pass

@game.Token
def LastRaisedToken(state):
  pass




