from function import *

#client = Boteater(my_token='token_here',my_app="ios_ipad")
client = Boteater(my_app="ios_ipad")
clientMid = client.profile.mid

def my_worker(op):
    if op.type in [25, 26]:
        msg = op.message
        text = str(msg.text)
        msg_id = msg.id
        receiver = msg.to
        msg.from_ = msg._from
        sender = msg._from
        cmd = text.lower()
        if msg.toType == 0 and sender != clientMid: to = sender
        else: to = receiver
        
        if cmd == "crit":
            client.sendMessage(to,'crot')

def run():
    while True:
        try:
            ops = client.fetchOperation() # For Secondary Token
            for op in ops:
                if op.revision > client.lastOP:
                    client.lastOP = max(op.revision, client.lastOP)
                    my_worker(op)
                    ## Don't threading in here :) ##
        except Exception as e:
            print(e)

if __name__ == "__main__":
    run()
