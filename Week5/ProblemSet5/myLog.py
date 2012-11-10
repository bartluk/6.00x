def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    ans = 0
    if x == 1:
        return 0
    while (b**ans <= x):
        ans += 0.1
        if (b**ans - x) == 0.0:
            break
    # if (b**ans - x) > 0.0:
    #     return int(ans) - 1
    # if (b**ans) > x:
    #     return int(ans - 1)
    return int(ans)

import math
def testmyLog():
    passed = 0
    failed = 0
    total = 0
    for x in range(1,99):
        for j in range(2, 10):
            #print x, j
            if int(math.log(x,j)) == myLog(x, j):
                print "Passed", x, j, int(math.log(x,j)), myLog(x, j), j**myLog(x, j)-x
                passed +=1
                total +=1
            else:
                print "fail", "x =",x, "base = ",j, "Correct =",int(math.log(x,j)), myLog(x, j), j**myLog(x, j)-x
                failed +=1
                total +=1
    print "Passed =", passed, "Failed =", failed, "Total =", total
testmyLog()