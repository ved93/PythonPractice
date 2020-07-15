# Given a string S consisting only ‘a’s and ‘b’s, print the last index of the ‘b’ present in it.
# taken from great learning blog

# Rotate all the elements left by 1 position
def rot_left_once(arr):
    n = len(arr)
    tmp = arr[0]
    for i in range(n - 1):  # [0,n-2]
        arr[i] = arr[i + 1]
    arr[n - 1] = tmp


# Use the above function to repeat the process for d times.
def rot_left(arr, d):
    for _ in range(d):
        rot_left_once(arr)


arr = list(map(int, input().split()))
rot = int(input())
rot_left(arr, rot)

for i in range(len(arr)):
    print(arr[i], end=" ")
