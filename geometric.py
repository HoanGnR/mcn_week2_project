import math

def prob(n, p):

    isValid(n,p)

    return p*((1-p)**(n-1))

def infoMeasure(n, p):

    isValid(n,p)

    return -(math.log(prob(n,p),2))

def sumProb(n, p):
    '''
    Return the value of the cummulative distribution function F(x) of geometric random variable X with success probability = p, when x = n.
    As n -> infinity, F(x) -> 1 no matter what value p takes
    '''
    isValid(n,p)
    sum = 0
    for i in range(1, n+1):
        sum += prob(i, p)

    return sum

def isValid(n, p):

    if n > 0 and p < 1 and p > 0:
        pass
    else: 
        print("Invalid input argument(s) ({:d},{:f})".format(n,p))
        return -1

def approxEntropy(n, p):
    '''
    Return the sum S of I(x)*p(x) with x <= n
    As n -> infinity, S -> H(X)
    With p = 0.5
         approxEntropy(1, 0.5)  = 0.5
         approxEntropy(5, 0.5)  = 1.78125
         approxEntropy(10, 0.5) = 1.98828125
         approxEntropy(50, 0.5) = 1.9999999999999538    
    '''
    apxEntr = 0
    for i in range(1,n+1):
        apxEntr += infoMeasure(i, p)*prob(i, p)
    return apxEntr

if __name__ == "__main__":
    for i in range (1,100):
        print("n = ", i)
        print("infoMeasure: " ,infoMeasure(i, 0.5))
        print("sumProb: " ,sumProb(i,0.5))
        print("approxEntropy: " ,approxEntropy(i, 0.5))
        print("=========================")
