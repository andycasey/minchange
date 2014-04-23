import itertools
import multiprocessing
import numpy as np
import time


# get list of coins
totcoins = 20
coins = np.arange(1,totcoins+1)

# create combinations
combos = itertools.combinations(coins,5)

def parallel_getminchange(index, V, C):
    m, n = len(V)+1, C+1
    table = [[0] * n for x in xrange(m)]
    for j in xrange(1, n):
        table[0][j] = float('inf')
    for i in xrange(1, m):
        for j in xrange(1, n):
            aC = table[i][j - V[i-1]] if j - V[i-1] >= 0 else float('inf')
            table[i][j] = min(table[i-1][j], 1 + aC)
    return (index, table[m-1][n-1])


start = time.time()

indices = []
results = []

def store_result(args):
    index, result = args
    indices.append(index)
    results.append(result)

# Summer time
pool = multiprocessing.Pool(processes=8)
for i, combo in enumerate(combos):
    #print i,combo
    pool.apply_async(parallel_getminchange, args=(i, combo, totcoins), callback=store_result)

# Winter time
pool.close()
pool.join()

# Get minimum
argmin = np.argmin(results)
comboi, minchangecombo = indices[argmin], results[argmin]
print comboi, minchangecombo
elapsed = time.time() - start
print "Parallel Elasped: %3.2f minutes" % (elapsed/60.)
#print "Best combination:",combos[comboi]
#print "Best combination sum:",sum(np.array(comboi))

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

minchangecombo =100
start = time.time()
for i, combo in enumerate(combos):
    print i,combo
    print("At {0} {1}".format(i, combo))
    changecombo_i = serial_getminchange(combo,totcoins)
    if changecombo_i < minchangecombo:
        minchangecombo = changecombo_i
        comboi = combo
        #print "Combination:",comboi
        #print "Sum:",sum(np.array(comboi))
#print "Found minimum combos: %3.2f hours" % (elapsed/3600.)
#print "Best combination:",comboi
#print "Best combination sum:",sum(np.array(comboi))
elapsed = time.time() - start
print comboi, minchangecombo
print "Serial Elasped: %3.2f minutes" % (elapsed/60.)
