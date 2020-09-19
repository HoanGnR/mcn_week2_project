import math

def prob(n, p, r):

    isValid(n, p, r)
    return nCr(n-1, r-1) * (p ** r) * ((1 - p) ** (n - r))

def nCr(n,r):
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

def infoMeasure(n, p, r):

    isValid(n,p,r)
    return -(math.log(prob(n,p, r),2))

def sumProb(n, p, r):
    '''
    Return the value of the cummulative distribution function F(x) of negative binomial random variable X with success probability = p, when x = n.
    As n -> infinity, F(x) -> 1 no matter what value p takes
    '''
    isValid(n, p, r)
    sum = 0
    for i in range(r, n+1):
        sum += prob(i, p, r)

    return sum

def isValid(n, p, r):

    if p < 1 and p > 0 and r >= 0 and n >= r:
        pass
    else: 
        print("Invalid input argument(s) ({:d},{:f},{:d})".format(n,p,r))
        return -1

def approxEntropy(n, p, r):
    '''
    Return the sum S of I(x)*p(x) with x <= n
    As n -> infinity, S -> H(X)
    With p = 0.5
         approxEntropy(10, 0.5,  10)  = 0.009765625
         approxEntropy(20, 0.5,  10)  = 2.250000374614748
         approxEntropy(40, 0.5,  10)  = 4.145990090828665
         approxEntropy(50, 0.5,  10)  = 4.15073873843763
         approxEntropy(70, 0.5,  10)  = 4.150775318542448
         approxEntropy(90, 0.5,  10)  = 4.1507753208639135
         approxEntropy(100, 0.5, 10)  = 4.150775320863947
         
    Then the approximate entropy of NB(p,r) with p = 0.5, r = 10 is 4.150775320863947
    '''
    apxEntr = 0
    for i in range(r,n+1):
        apxEntr += infoMeasure(i, p, r)*prob(i, p, r)
    return apxEntr
if __name__ == "__main__":
    p = 0.5
    r = 10
    for i in range (r, 100):
        print("n = ", i, "; r = ", r , "; p = ", p )
        print("prob: ", prob(i,p,r))
        print("infoMeasure: " ,infoMeasure(i, p, r))
        print("sumProb: " ,sumProb(i, p, r))
        print("approxEntropy: " ,approxEntropy(i, p, r))
        print("=========================")

