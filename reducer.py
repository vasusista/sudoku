import sys

oldkey = None
count = 0

for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  if oldkey != key:
    if oldkey:
      print '%s\t%s' % (oldkey,count)
    count = 0
  oldkey = key
  try:
    count = count + int(val)
  except:
    continue
print '%s\t%s' % (oldkey,count)