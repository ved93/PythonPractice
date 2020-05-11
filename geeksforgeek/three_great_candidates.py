#code
t = int(input())






while t > 0 :
    t-=1
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    # mult = 1
    arr.sort()

    print(max(arr[0]*arr[1]*arr[-1],arr[-1]*arr[-2]*arr[-3]))
    
                
                
    
    
    