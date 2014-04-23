import itertools
import numpy as np
import time

# get list of coins
coins = np.arange(1,101)

# create combinations
start = time.clock()
combos = itertools.combinations(coins,10)
elapsed = time.time() - start
print "Generated combos: %3.2f seconds" % (elapsed/3600.)

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

start = time.clock()

minchangecombo = 100
for combo in combos:
    changecombo_i = getminchange(combo,totcoins)
    if changecombo_i < minchangecombo:
        minchangecombo = changecombo_i
        comboi = combo

elapsed = time.time() - start
print "Found minimum combos: %3.2f hours" % (elapsed/3600.)
print "Best combination:",comboi