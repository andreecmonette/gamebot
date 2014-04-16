import zulip
import re
#import json
opts = dict(
    email=sys.environ['ARCADEBOT_EMAIL'],
    api_key=sys.environ['ARCADEBOT_API_KEY'],
    )
client = zulip.Client(**opts)
def print_message(message):
  #print json.dumps(message, indent=2)
  #[u'recipient_id', u'sender_email', u'timestamp', u'display_recipient', u'sender_id', u'sender_full_name', u'sender_domain', u'content', u'gravatar_hash', u'avatar_url', u'client', u'content_type', u'subject_links', u'sender_short_name', u'type', u'id', u'subject']
  
  if not message['sender_email'] == opts['email']:
    matched = re.match(r'.*?`([^`]+)`.*', message['content'])
    if matched:
      client.send_message({
        "type": "stream",
        "to": "arcadebot",
        "subject": "test",
        "content":  matched.group(1) + ", backtickfinity"
      })



  # Send a private message
#client.send_message({
#    "type": "private",
#    "to": "hamlet@example.com",
#    "content": "I come not, friends, to steal away your hearts."
#  })
def recv_message(message)

client.add_subscriptions([{"name": "arcadebot"}])

client.call_on_each_message(print_message)
