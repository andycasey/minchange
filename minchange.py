import itertools
import multiprocessing
import numpy as np
import time

# get list of coins
ncores = 100
totcoins = 80 # number of coins you would like
ndenom = 3 # number of coin denominations
coins = np.arange(1,totcoins+1)

# create combinations
combos = itertools.combinations(coins,ndenom)

def parallel_getminchange(V, C):
    m, n = len(V)+1, C+1
    table = [[0] * n for x in xrange(m)]
    for j in xrange(1, n):
        table[0][j] = float('inf')
    for i in xrange(1, m):
        for j in xrange(1, n):
            aC = table[i][j - V[i-1]] if j - V[i-1] >= 0 else float('inf')
            table[i][j] = min(table[i-1][j], 1 + aC)
    return (V, table[m-1][n-1])

def serial_getminchange(V, C):
    m, n = len(V)+1, C+1
    table = [[0] * n for x in xrange(m)]
    for j in xrange(1, n):
        table[0][j] = float('inf')
    for i in xrange(1, m):
        for j in xrange(1, n):
            aC = table[i][j - V[i-1]] if j - V[i-1] >= 0 else float('inf')
            table[i][j] = min(table[i-1][j], 1 + aC)
    return table[m-1][n-1]

start = time.time()


best_combo, min_change_combo = None, None

def callback(args):
    combo, result = args
    global best_combo, min_change_combo
    if best_combo is None or result < min_change_combo:
        best_combo, min_change_combo = combo, result


pool = multiprocessing.Pool(processes=ncores)
for i, combo in enumerate(combos):
    pool.apply_async(parallel_getminchange, args=(combo, totcoins), callback=callback)
pool.close()
pool.join()

elapsed = time.time() - start
print "Parallel Elapsed: %3.2f minutes" % (elapsed/60.)


combos = itertools.combinations(coins,ndenom)

minchangecombo =100
start = time.time()
for i, combo in enumerate(combos):
    changecombo_i = serial_getminchange(combo,totcoins)
    if changecombo_i < minchangecombo:
        minchangecombo = changecombo_i
        comboi = combo

elapsed = time.time() - start
print "Serial Elapsed: %3.2f minutes" % (elapsed/60.)
