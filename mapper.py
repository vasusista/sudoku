import sys
import json
import puzzlegen

for line in sys.stdin:
  x = json.loads(line)
  y = puzzlegen.generate_game(x,2)
  print '%s\t%s' % (y,1)