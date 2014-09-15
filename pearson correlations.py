from math import sqrt
# from scores2ranks import scores2ranks
 
 
def svar(X):
    n = len(X)
    if n <= 1:
       raise ValueError, "sd(): n must be greater than 1"
    xbar = float(sum(X)) /n
    return (sum([(x-xbar)**2 for x in X])/(n-1))
 
def ssd(X):
    return sqrt(svar(X))
 
 
def pearsoncor(X, Y, code = 0):
    """
    Computes pearson's correlation coefficient.
    code
       0 - using deviations from means.
       1 - common formula.
    """
    n = len(X)
    sx = ssd(X)
    sy = ssd(Y)
    xbar = float(sum(X)) / n
    ybar = float(sum(Y)) / n
    if code == 0:
       return sum([(x - xbar) * (y - ybar) for x, y in zip (X,Y)])/(sx * sy*(n-1.0))
    else:
       numer = sum([x*y for x,y in zip(X,Y)]) - n*(xbar * ybar)
       denom = sqrt((sum([x*x for x in X]) - n* xbar**2)*(sum([y*y for y in Y]) -n* ybar**2))
       return (numer /denom)
 
def pearsonrankcor(Rx,Ry):
    """
    Computes Pearson's rank correlation coefficient.
    Rx and Ry must be rank scores from 1 to n , not necessarily integers.
    """    
    n = len(Rx)
    return 1 - 6 *sum([(x -y)**2 for x,y in zip(Rx,Ry)])/ (n* (n*n - 1))
 
 
if __name__ == "__main__":
   print "Testing pearsonrankcor:"
   Rx = [1,2,3,4]
   Ry = [4,3,2,1]
   print "Rx = ", Rx
   print "Ry = ", Ry
   print "Rank Correlation=", pearsonrankcor(Rx,Ry)
 
   print "Testing product moment correlations."
   X = [10,7,12,12,9,16,12,18,8,12,14,16]
   Y = [6,4,7,8,10,7,10,15,5,6,11,13]
   print "pearson using deviations:", pearsoncor(X,Y, code = 0)
   print "pearson using common:",     pearsoncor(X,Y, code = 1)