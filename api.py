import os
import requests

class OneAI:
    def __init__(self, uid="000"):
        self.endpoint = os.environ.get('ENDPOINT')
        self.txt = "who am i"
        self.uid = uid
        self.req = None

    def job(self, txt=None, uid=None):
        if txt is not None:
            self.txt = txt
        if uid is not None:
            self.uid = uid
        return f"{self.endpoint}?input={self.txt}&uid={self.uid}"
        
    def run(self, show=False):
        self.req = requests.get(self.job())
        if show == True:
            print(self.req.text)
    
    def debug(self, attr=None):
        print(getattr(self, attr))

# example agents
agent1 = OneAI(uid="000")
agent2 = OneAI(uid="123")

# loop below outputs
# 000 My name is Jarcey. I am the third generation Jarcey to be implemented.
# 123 Sorry, I am not authorized to complete your request.
for agent in [agent1, agent2]:
    agent.job(txt="what is your name")
    agent.run()
    print(agent.uid, agent.req.text)
