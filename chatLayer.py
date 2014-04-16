import zulip
import re
import os

opts = dict(
    email=os.environ['ARCADEBOT_EMAIL'],
    api_key=os.environ['ARCADEBOT_API_KEY'],
    )
client = zulip.Client(**opts)
client.add_subscriptions([{"name": "arcadebot"}])

messageCallbacks = []

def sendPubMessage(subj, message):
  client.send_message({
    "type": "stream",
    "to": "arcadebot",
    "subject": subj,
    "content": message
  })

def sendPrivMessage(recipients, message):
  client.send_message({
    "type": "private",
    "to": recipients,
    "content": message
  })

def talkativeFunction(fun):
  def talkingFun(*args, **kwargs):
    msg, ret = fun(*args, **kwargs)
    if 'subject' in msg:
      sendPubMessage(msg['subject'], msg['message'])
    elif 'recipients' in msg:
      sendPrivMessage(msg['recipients'], msg['message'])
    else:
      raise TypeError('Malformed message: ' + msg)
    return ret
  return talkingFun

def recvMessage(message):
  if not message['sender_email'] == opts['email']:
    matched = re.match(r'.*?`([^`]+)`.*', message['content'])
    if matched:
      parsedMsg = {
        "message": matched.group(1),
        "raw": message
      }
      for callback in messageCallbacks:
        callback(parsedMsg)

def messageHandler(fun):
  messageCallbacks.append(fun)
  return fun

def mainLoop():
  client.call_on_each_message(recvMessage)