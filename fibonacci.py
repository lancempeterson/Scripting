dp = [0,1]

def fibonacci(n):
    if n < 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n<=len(dp):
        return dp[n-1]
    else:
        temp = fibonacci(n-1)+fibonacci(n-2)
        dp.append(temp)
        return temp
    
n=input("input")
convertedInt = int(n)
print(fibonacci(convertedInt)) 
input("Press Enter to continue...")