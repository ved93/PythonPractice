#code

#code

def move_zero_to_end(arr, n):
    count = 0
    for i in range(n):
        if arr[i]!=0:
            arr[count] = arr[i]
            count+=1
            print(arr[i], end = " ")
    
    while count < n:
        arr[count] = 0
        count+= 1
        print("0",end=" ")
    print()    
    
    return arr
 
T= int(input())
    
while T > 0 :   
    T-=1
    
    N = int(input())

    # lst=list(input().split())[:N]
    arr =  list(map(int,input().split()))[:N] # Get the input
    
    arr = move_zero_to_end(arr,N) 
    # print(*arr)       
    # print()  




n=int(input())
while n>0:
    n-=1
    m=int(input())
    l=list(map(int,input().split()))
    c=l.count(0)
    for i in l:
        if i!=0:
            print(i,end=" ")
    for i in range(c):
        print("0",end=" ")
    print()