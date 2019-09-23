def percentile95(lengths):
  """
  input: [], list of int represents the lengths
  return: int
  """
  # write your solution here
  target = 0.95 * len(lengths)
  print 'target: ', target
  print

  buckets = [0 for _ in xrange(len(lengths)+1)]
  for i in lengths:
    buckets[i] += 1
  print 'dist: ', buckets

  c = 0
  for i in xrange(len(lengths)+1):
    c += buckets[i]
    if c >= target:
      return i

l = [i for i in range(1,5)]
print 'input list', l
res =  percentile95(l)
print 'ans: ', res
