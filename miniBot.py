from chatLayer import messageHandler, talkativeFunction, mainLoop


@messageHandler
def hearYou(message):
  youSaidSomething(message['message'])





@talkativeFunction
def youSaidSomething(theText):
  return {'subject': 'The opposite of that thing was',
          'message': theText.encode('rot13')
         }, None


mainLoop()
          

