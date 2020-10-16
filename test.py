# #https://www.codeandgadgets.com/karatsuba-multiplication-python/

# def karat(x,y):
#     if len(str(x)) == 1 or len(str(y)) == 1:
#         return x*y
#     else:
#         m = max(len(str(x)),len(str(y)))
#         m2 = m // 2

#         a = x // 10**(m2)
#         b = x % 10**(m2)
#         c = y // 10**(m2)
#         d = y % 10**(m2)

#         z0 = karat(b,d)
#         z1 = karat((a+b),(c+d))
#         z2 = karat(a,c)

#         return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)

# tf=karat(337337834348333,72889897957652322)
# print(tf)
# from numpy import size

# def print_ele(arr):
#     if len(arr) <= 1:
#         # print(arr[0])

#         return arr[0]
#     else :
#         # print(arr[0])
#         if size(arr[0]) > 1:
#             print(arr[0])

#             arr[0]=print_ele(arr[0])
#             print(arr[0])

        
#         return print_ele(arr[1:])+arr[0]




# l=print_ele([2,6,[22,21],3,9,1,5])
# print(l)

import sys
n = int(sys.argv[1])
print(n)
print(' '.join([str(i*2) for i in range(n)]))