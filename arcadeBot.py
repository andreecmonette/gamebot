from chatLayer import messageHandler, commandHandler, talkativeFunction, mainLoop

@commandHandler(["bet", "check"])
@talkativeFunction
def bet(message):
  return {'subject':'some poker game', 'message':'You ' + message['command']},None



@messageHandler
def sysMsgs(message):
  return message['raw']['sender_email']
      #[u'recipient_id', u'sender_email', u'timestamp', u'display_recipient', u'sender_id', u'sender_full_name', u'sender_domain', u'content', u'gravatar_hash', u'avatar_url', u'client', u'content_type', u'subject_links', u'sender_short_name', u'type', u'id', u'subject']


class Gamedef:
  def __init__(self, gamename):
    self.gamename = gamename

  def Start(self, fun):
    games.append(self)
    fun()

  def Action(self, commands):
    @commandHandler(commands)
    def SomeOtherFunction(message):
      pass

  def Player(self):
    pass

  def Token(self):
    pass








@talkativeFunction
def youSaidSomething(theText):
  return {'subject': 'The opposite of that thing was',
          'message': theText.encode('rot13')
         }, None


mainLoop()
