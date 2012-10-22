# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    i = 0
    p = []
    r = len(poly)
    pr = []
    while i < r:
        p.append(x ** i)
        i += 1
    for j in range(0, r, 1):
        pr.append(poly[j] * p[j])
    return float(sum(pr))







# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    b = []
    ans = []
    for i in range(len(poly)):
        b.append(i)
        ans.append(float(b[i] * poly[i]))
        i += 1
    if (len(ans) != 1):
        ans.pop(0)   
    return ans





# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    
    step = 0
    x_1 = 0
    ans = []
    if computeDeriv(poly) == [0.0]:
		return
    while abs(evaluatePoly(poly, x_0)) >= epsilon:
		x_1 = x_0 - float(evaluatePoly(poly, x_0)/(evaluatePoly(computeDeriv(poly), x_0)))
		step += 1
		if abs(x_0 - x_1) < epsilon:
			break
		if step >= 20:
			break
		x_0 = x_1
    ans.append(x_0)
    ans.append(step)
    return ans

print computeRoot([-13.39, 0.0, 17.5, 3.0, 1.0], 0.1,  .0001)
print computeRoot([1, 9, 8], -3, .01)
