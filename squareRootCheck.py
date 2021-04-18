def squareRoot(x, guess): # O(n)
    while guess ** 2 != x:
        if (x/guess) ** 2 != x:
            if ((guess+x/guess)/2) ** 2 != x:
                guess = (guess+x/guess)/2
                
            else:
                return (guess+x/guess)/2
                
        else:
            return x/guess
        
findSqrt = squareRoot(45, 6.5)
print(findSqrt)