import os
import sys
import math
import signal
from time import sleep
from pyfiglet import Figlet

size = os.get_terminal_size()

# http://www.jave.de/figlet/fonts/overview.html
fancy = Figlet(font='doh', width=math.inf)

def clearScreen():
  os.system('cls' if os.name == 'nt' else 'clear')

def nextStep(step, totalLength):
  next = step + 1
  if next > totalLength:
    return 0
  return next

def printPage(msg, step = 0, border = '*'):
  clearScreen()
  print(str(border) * size.columns)
  
  totalLength = None
  for line in msg.splitlines():
    totalLength = totalLength or len(line)
    wrapped = line[step:(size.columns + step)]
    if len(wrapped) < size.columns:
      wrapped = wrapped + line[0:(size.columns - len(wrapped))]
    print(wrapped)

  print(str(border) * size.columns)
  print()
  return nextStep(step, totalLength)


billboard = fancy.renderText(" ".join(sys.argv[1:]) + "   ")


def exitHandler(signal, frame):
  clearScreen()
  sys.exit(0)

signal.signal(signal.SIGINT, exitHandler)
signal.signal(signal.SIGTERM, exitHandler)

step = 0
while True:
  step = printPage(billboard, step)
  sleep(0.1)

