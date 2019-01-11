import numpy as np 
import time
import math as math
import sys
sys.setrecursionlimit(100000)

lam = 0.9
n = 2

s = " bahia cocoa review showers continued week bahia cocoa zone alleviating drought early january improving prospects coming temporao normal humidity levels restored comissaria smith weekly review dry period means temporao late year arrivals week ended february 22 155221 bags 60 kilos making cumulative total season 593 mln 581 stage year cocoa delivered earlier consignment included arrivals figures comissaria smith doubt crop cocoa harvesting practically end total bahia crop estimates 64 mln bags sales standing 62 mln hundred thousand bags hands farmers middlemen exporters processors doubts cocoa fit export shippers experiencing dificulties obtaining bahia superior certificates view lower quality recent weeks farmers sold good part cocoa held consignment comissaria smith spot bean prices rose 340 350 cruzados arroba 15 kilos bean shippers reluctant offer nearby shipment limited sales booked march shipment 1750 1780 dlrs tonne ports named crop sales light open ports junejuly 1850 1880 dlrs 35 45 dlrs york july augsept 1870 1875 1880 dlrs tonne fob routine sales butter made marchapril sold 4340 4345 4350 dlrs aprilmay butter 227 times york junejuly 4400 4415 dlrs augsept 4351 4450 dlrs 227 228 times york sept octdec 4480 dlrs 227 times york dec comissaria smith destinations covertible currency areas uruguay open ports cake sales registered 785 995 dlrs marchapril 785 dlrs 753 dlrs aug 039 times york dec octdec buyers argentina uruguay convertible currency areas liquor sales limited marchapril selling 2325 2380 dlrs junejuly 2375 dlrs 125 times york july augsept 2400 dlrs 125 times york sept octdec 125 times york dec comissaria smith total bahia sales estimated 613 mln bags 198687 crop 106 mln bags 198788 crop final figures period february 28 expected published brazilian cocoa trade commission carnival ends midday february 27"
t = " national average prices farmerowned reserve agriculture department reported farmerowned reserve national fiveday average price february 25 dlrsbusorghum cwt  natl loan release call avge ratex level price price wheat 255 240 iv 465  465  vi 445  corn 135 192 iv 315 315 325   1986 rates natl loan release call avge ratex level price price oats 124 099 165  barley na 156 iv 255 255 265  sorghum 234 325y iv 536 536 554  reserves ii iii matured level iv reflects grain entered oct 6 1981 feedgrain july 23 1981 wheat level wheatbarley 51482 cornsorghum 7182 level vi covers wheat entered january 19 1984 x1986 rates ydlrs cwt 100 lbs nanot"

car = "car"
cat = "cat"

start = time.time()
    
def k(s, t, n, lam):
    value = 0
    if n > len(s) or n > len(t):
        return 0 
    x = s[-1]
    for j in range(len(t)):
        if x == t[j]:
            value += kprime(s[:-1], t[0:j], n-1, lam)*(lam**2)
    return value + k(s[:-1], t, n, lam)

def kprime(s ,t, i, lam):
    value = 0
    if(i == 0):
        return 1

    if i > len(s) or i > len(t):
        return 0      

    else:
        x = s[-1] 
        for j in range(len(t)):
            if (t[j] == x):
                value += kprime(s[:-1], t[0:j], i-1, lam) * lam **(len(t) - j + 1)
        return value + lam*kprime(s[:-1], t, i, lam)

def sskNormalize(s, t, n, lam):
    lcs = k(s, t, n, lam)
    unNormalizedS = k(s, s, n, lam)
    unNormalizedT = k(t, t, n, lam)

    return lcs/math.sqrt(unNormalizedS * unNormalizedT)

#print(sskNormalize(car, cat, 2, lam))
print(sskNormalize(s, t, 2, lam))

print("----- %s seconds -----" % (time.time() - start))
"""
def ssk(s, t):
    for i in range(len(s)):
        for j in range(i + 1,len(s)): 
            lcs(s[i]+s[j:], t, 2, 0, "")

#Find the longest common subsequence of two strings
def lcs(s, t, n, k, seq):
    if n > len(s) or n > len(t):
        return []
    if n == 0:
        return [seq, k]
    a, b, c, d = s[0], t[0], s[1:], t[1:]
    if (a == b):
        if (k == 0):
            k = 1
        return lcs(c, d, n-1, k, seq+a)
    else:
        if (k > 0):
            k = k + 1
        return lcs(s, d, n, k, seq)

ssk(s, t)
print("----- %s seconds -----" % (time.time() - start))

#def lcs(s, t, n, k, seq):
#    if n == 0 or (not s or not t):
#        return seq
#    if not s or not t:
#        return []
#    x, y, xs, ys = s[0], t[0], s[1:], t[1:]
#
#    if (x == y):
#        return lcs(xs, ys, n-1, k, (seq + x))
#    else:
#        return max(lcs(s, ys, n, k, seq), lcs(xs, t, n, k, seq), key = len)
"""
