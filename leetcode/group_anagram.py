

import collections


class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        lookup = defaultdict(list)
        for i in strs:
            l=sorted(list(i))
            # print(''.join(l))
            lookup[''.join(l)].append(i)
        # print(lookup) 
        # print(lookup.k)
        return [value for key,value in lookup.items()]



class Solution2(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
