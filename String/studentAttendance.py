def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """
    # if not s:
    #     return False       
    # a_counter, l_counter, l_fast, l_slow = 0, 0, 0, 0
    # while l_fast < len(s):
    #     if s[l_fast] != 'L':
    #         l_counter = 0
    #         if s[l_fast] == 'A':
    #             a_counter += 1
    #         if a_counter > 1:
    #             return False
    #     elif s[l_fast] == 'L':
    #         l_counter += 1
    #         l_slow = l_fast
    #         if l_counter == 3:
    #             return False
    #     l_fast += 1
    # return True
    return s.count('A') < 2 and 'LLL' not in s

print checkRecord('LALL')
