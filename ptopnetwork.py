import socket
import json
networkMembers = [socket.gethostbyname(socket.gethostname())]
SEED_NODES = [] #insert seed nodes here
def joinNetwork():
  for item in SEED_NODES:
    sendRequest(item, "joinNetwork")

def forwardRequest():
  for member 


def sendRequest(node=SEED_NODES[0]):
  if request.type == "joinNetwork":
    pass
  elif request.type == "":

def processRequest(request):
  if request.type == "joinNetwork":
    pass
  elif request.type == "":

  
  forwardRequest(request) #do we need this?