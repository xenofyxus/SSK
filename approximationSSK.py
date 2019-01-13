import math
import numpy
import time
import sys
sys.setrecursionlimit(100000)

n = 3
lam = 0.5

s = " bahia cocoa review showers continued week bahia cocoa zone alleviating drought early january improving prospects coming temporao normal humidity levels restored comissaria smith weekly review dry period means temporao late year arrivals week ended february 22 155221 bags 60 kilos making cumulative total season 593 mln 581 stage year cocoa delivered earlier consignment included arrivals figures comissaria smith doubt crop cocoa harvesting practically end total bahia crop estimates 64 mln bags sales standing 62 mln hundred thousand bags hands farmers middlemen exporters processors doubts cocoa fit export shippers experiencing dificulties obtaining bahia superior certificates view lower quality recent weeks farmers sold good part cocoa held consignment comissaria smith spot bean prices rose 340 350 cruzados arroba 15 kilos bean shippers reluctant offer nearby shipment limited sales booked march shipment 1750 1780 dlrs tonne ports named crop sales light open ports junejuly 1850 1880 dlrs 35 45 dlrs york july augsept 1870 1875 1880 dlrs tonne fob routine sales butter made marchapril sold 4340 4345 4350 dlrs aprilmay butter 227 times york junejuly 4400 4415 dlrs augsept 4351 4450 dlrs 227 228 times york sept octdec 4480 dlrs 227 times york dec comissaria smith destinations covertible currency areas uruguay open ports cake sales registered 785 995 dlrs marchapril 785 dlrs 753 dlrs aug 039 times york dec octdec buyers argentina uruguay convertible currency areas liquor sales limited marchapril selling 2325 2380 dlrs junejuly 2375 dlrs 125 times york july augsept 2400 dlrs 125 times york sept octdec 125 times york dec comissaria smith total bahia sales estimated 613 mln bags 198687 crop 106 mln bags 198788 crop final figures period february 28 expected published brazilian cocoa trade commission carnival ends midday february 27"
t = " national average prices farmerowned reserve agriculture department reported farmerowned reserve national fiveday average price february 25 dlrsbusorghum cwt  natl loan release call avge ratex level price price wheat 255 240 iv 465  465  vi 445  corn 135 192 iv 315 315 325   1986 rates natl loan release call avge ratex level price price oats 124 099 165  barley na 156 iv 255 255 265  sorghum 234 325y iv 536 536 554  reserves ii iii matured level iv reflects grain entered oct 6 1981 feedgrain july 23 1981 wheat level wheatbarley 51482 cornsorghum 7182 level vi covers wheat entered january 19 1984 x1986 rates ydlrs cwt 100 lbs nanot"
start = time.time()

class Ssk:
    def __init__(self, n, lam):
        self.dict1 = {}
        self.dict2 = {}
        self.dict3 = {}
        self.dictS = {}
        self.n = n
        self.lam = lam

    #This is the kernel function returning the value which
    #represents the hueristic relationship between the strings
    def kernel(self, s, t):

        return self.k(s, t, self.n)

    def k(self, s, t, i):

        if (s, t, i) in self.dict1:
            return self.dict1[(s, t, i)]
            
        if (i > len(s) or i > len(t)):
            self.dict1[(s, t, 1)] = 0
            return 0

        x = s[-1]

        value = 0
        for j in range(len(t)):
            if (t[j] == x):
                value += self.kP(s[:-1], t[0:j], i-1)*(self.lam**2)

        value += self.k(s[:-1], t, i)
        self.dict1[(s, t, i)] = value
        return value

    def kP(self, s, t, i):

        if (s, t, i) in self.dict2:
            return self.dict2[(s, t, i)]

        if (i == 0):   
            self.dict2[(s, t, i)] = 1
            return 1

        if(len(s) < i or len(t) < i):
            self.dict2[(s, t, i)] = 0
            return 0

        value = self.lam * self.kP(s[:-1], t, i) + self.kPP(s, t, i)
        self.dict2[(s, t, i)] = value
        return value    
    
    def kPP(self, s, t, i):
        
        if (s, t, i) in self.dict3:
            return self.dict3[(s, t, i)]

        if(len(s) < i or len(t) < i):
            self.dict3[(s, t, i)] = 0
            return 0
        
        x = s[-1]
        u = t[-1]
        value = 0
        
        if (x == u):
            value = self.lam * (self.kPP(s, t[:-1], i) + self.lam*self.kP(s[:-1], t[:-1], i-1)) 
        else:
            value = self.lam * self.kPP(s, t[:-1], i)

        self.dict3[(s, t, i)] = value
        return value


a = "catat"
b = "life is science"

test = Ssk(n, lam)
print(test.kernel(s, t, 100))
#print(test.k(s, t, test.n)/(math.sqrt(test.k(s, s, test.n)*test.k(t, t, test.n))))
#print(test.k(a, b, test.n)/(math.sqrt(test.k(a, a, test.n)*test.k(b, b, test.n))))
print("----- %s seconds -----" % (time.time() - start))