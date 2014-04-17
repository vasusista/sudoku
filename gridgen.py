"""Due credit to Peter Norvig, author of much of the code"""
import sys
import random
import hashlib
import json

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d,'')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values

def shuffled(seq):
    "Return a randomly shuffled copy of the input sequence."
    seq = list(seq)
    random.shuffle(seq)
    return seq

def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def random_puzzle(N=81):
  values = dict((s, digits) for s in squares)
  for s in shuffled(squares):
    if not assign(values, s, random.choice(values[s])):
      break
    ds = [values[s] for s in squares if len(values[s]) == 1]
    if len(ds) >= N and len(set(ds)) >= 8:
      return ''.join(values[s] if len(values[s])==1 else '.' for s in squares)
  return random_puzzle(N)

def listify(s):
  a = []
  for c in s:
    a.append(int(c))
  b = [a[i:i+9] for i in xrange(0,81,9)]
  return b

#print json.dumps(listify(random_puzzle()))
done = {}
for j in range(50):
  f = open(sys.argv[1]+str(j)+'.txt','wb')
  for i in xrange(int(sys.argv[2])/50):
    x = random_puzzle()
    solution = listify(x)
    try:
      if(done[hashlib.md5(x).hexdigest()] == True):
        continue
    except KeyError:
      done[hashlib.md5(x).hexdigest()] = True
  
    f.write(json.dumps(solution)+'\n')
  f.close()
