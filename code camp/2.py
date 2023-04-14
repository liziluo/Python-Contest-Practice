coins=[]
    dp = [0] * (n+1)
    path = [0] * (n+1)  
    for i in range(1, n+1):
        minNum = i  
        for c in coins:  
            if i >= c and minNum > dp[i-c]+1:
                minNum =dp[i-c]+1
                path[i] = i - c
        dp[i] = minNum 
        print(dp)
    print('最少硬币数:', dp[-1])
