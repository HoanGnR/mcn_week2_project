import math

def prob(n, p, N):

    isValid(n, p, N)
    return nCr(N, n) * (p ** n) * (1 - p) ** (N - n) 

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

def infoMeasure(n, p, N):

    isValid(n,p,N)
    return -(math.log(prob(n,p, N),2))

def sumProb(n, p, N):
    '''
    Return the value of the cummulative distribution function F(x) of binomial random variable X with success probability = p, when x = n.
    As n -> infinity, F(x) -> 1 no matter what value p takes
    '''
    isValid(n, p, N)
    sum = 0
    for i in range(1, n+1):
        sum += prob(i, p, N)

    return sum

def isValid(n, p, N):

    if n > 0 and p < 1 and p > 0 and N > 0 and N >= n:
        pass
    else: 
        print("Invalid input argument(s) ({:d},{:f},{:d})".format(n,p,N))
        return -1

def approxEntropy(n, p, N):
    '''
    Return the sum S of I(x)*p(x) with x <= n
    As n -> infinity, S -> H(X)
    With p = 0.5
         approxEntropy(1, 0.5, 20)  = 0.00029903549013352655
         approxEntropy(5, 0.5, 20)  = 0.0025513542866891603
         approxEntropy(10, 0.5, 20) = 1.8245060080798332
         approxEntropy(15, 0.5, 20) = 3.158584640409768
         approxEntropy(16, 0.5, 20) = 3.1944295851689315
         approxEntropy(17, 0.5, 20) = 3.205133155874041
         approxEntropy(20, 0.5, 20) = 3.207703583647058    
    '''
    apxEntr = 0
    for i in range(1,n+1):
        apxEntr += infoMeasure(i, p, N)*prob(i, p, N)
    return apxEntr

if __name__ == "__main__":
    p = 0.5
    for i in range (20,21):
        for j in range (1, i + 1):
            print("n = ", j, "; N = ", i , "; p = ", p )
            print("infoMeasure: " ,infoMeasure(j, p, i))
            print("sumProb: " ,sumProb(j, p, i))
            print("approxEntropy: " ,approxEntropy(j, p, i))
            print("=========================")

