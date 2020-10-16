
#Reading different input
#example 1: when you have row of data to read
# 500 GMS,	'REFILL PACK',	'01/01/19'	2993.13
# 750 GMS,	'REFILL PACK',	'01/01/19'	2312.412
# 750 GMS,	'REFILL PACK',	'01/01/19'	1603.273
# 1000 GMS,	'REFILL PACK',	'01/01/19'	995.398
readings_count = int(input().strip())
readings = []

#below will read into a list
for _ in range(readings_count):
    readings_item = input()
    readings.append(readings_item)    

import pandas as pd

#convert to list with tab or comma
[x.split('\t') for x in readings]
df = pd.DataFrame([x.split('\t') for x in readings], columns = ['date', 'reading'] )










# 359716482
# 867345912
# 413928675
# 398574126

# import sys
# erer5

# userInput = sys.stdin.readlines( ff


# 500 GMS,	'REFILL PACK',	'01/01/19'	2993.13
# 750 GMS,	'REFILL PACK',	'01/01/19'	2312.412
# 750 GMS,	'REFILL PACK',	'01/01/19'	1603.273
# 1000 GMS,	'REFILL PACK',	'01/01/19'	995.398
# 1000 GMS,	'REFILL PACK',	'01/01/19'	632.588
# 500 GMS,	'REFILL PACK',	'01/01/19'	800.874
# 500 GMS,	'REFILL PACK',	'01/01/19'	624.03
# 500 GMS,	'REFILL PACK',	'01/01/19'	335.631
# 500 GMS,	'REFILL PACK',	'01/01/19'	186.473


string = "baababa"  # raw_input()

found = False
char_set = set(string)  # Lets find unique letters

d_dict = {}
for c in char_set:
    d_dict[c] = string.count(c)  # Keep count of each letter

odd_l = [
    e for e in d_dict.values() if e % 2 == 1
]  # Check how many has odd number of occurrence
if len(odd_l) > 1:
    pass
else:
    found = True


if not found:
    print("NO")
else:
    print("YES")
