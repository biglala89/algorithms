class Solution(object):
  def allAnagrams(self, sh, lo):
    """
    input: string sh, string lo
    return: Integer[]
    """
    # write your solution here
    sh_freq = self.str_freq(sh)
    lo_freq = self.str_freq(lo)
    print 'sh_freq: ', sh_freq
    print 'lo_freq: ', lo_freq
    print 
    
    sh_len = len(sh)
    res = []
    i = 0

    while i + sh_len <= len(lo):
      sub_str = lo[i:i+sh_len]
      print 'sub_str: ', sub_str
      sub_freq = self.str_freq(sub_str)
      print 'sub_freq: ', sub_freq
      if sh_freq == sub_freq:
        res.append(i)
        print res
      i += 1
    return res
      
  def str_freq(self, string):
    freq = {}
    for s in string:
      if s in freq:
        freq[s] += 1
      else:
        freq[s] = 1
    return freq

# O(n*k)
# sh = "aab"
# lo = "ababacbbaac"
import random

string = ''
for _ in range(100):
    r = random.choice(['a', 'b', 'c'])
    string += r

target = 'abcba'

s = Solution()
print 'ans: ', s.allAnagrams(target, string)
