import itertools
import numpy as np
import time

# get list of coins
coins = np.arange(1,10)

# create combinations
combos = itertools.combinations(coins,3)

def getminchange(V, C):
    m, n = len(V)+1, C+1
    table = [[0] * n for x in xrange(m)]
    for j in xrange(1, n):
        table[0][j] = float('inf')
    for i in xrange(1, m):
        for j in xrange(1, n):
            aC = table[i][j - V[i-1]] if j - V[i-1] >= 0 else float('inf')
            table[i][j] = min(table[i-1][j], 1 + aC)
    return table[m-1][n-1]

totcoins = 100

start = time.time()

minchangecombo = 100
for combo in combos:
    changecombo_i = getminchange(combo,totcoins)
    if changecombo_i < minchangecombo:
        minchangecombo = changecombo_i
        comboi = combo
        print "Combination:",comboi
        print "Sum:",sum(np.array(comboi))

elapsed = time.time() - start
print
print "Found minimum combos: %3.2f hours" % (elapsed/3600.)
print "Best combination:",comboi
print "Best combination sum:",sum(np.array(comboi))