import puzzlegen
import mincemeat
import json
import sys

f = open(sys.argv[1],'rb')
data = [json.loads(line) for line in f]
datasource = dict(enumerate(data))
f.close()

def mapfn(k,v):
  import puzzlegen
  print 'puzzle started'
  x = puzzlegen.generate_game(v,2)
  yield x,1

def reducefn(k,vs):
  results = sum(vs)
  return results

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn
results = s.run_server(password="changeme")

#print results
for k in results:
  print '%s\t%s' % (k,results[k])
