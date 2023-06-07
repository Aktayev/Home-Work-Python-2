from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet.getFonts()
shrifts = figlet.getFonts()
# input()
if len(sys.argv) == 1:
    figlet.setFont(font= random.choice(shrifts))
    print(figlet.renderText(input()))

elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(input()))
else:
  sys.exit("invalid usage")

