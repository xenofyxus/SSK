import math
import numpy
import time
import sys
import os
sys.setrecursionlimit(100000)

n = 4
lam = 0.5
#limCoefficient = 0.5

car = "car"
cat = "cat"
s = " bahia cocoa review showers continued week bahia cocoa zone alleviating drought early january improving prospects coming temporao normal humidity levels restored comissaria smith weekly review dry period means temporao late year arrivals week ended february 22 155221 bags 60 kilos making cumulative total season 593 mln 581 stage year cocoa delivered earlier consignment included arrivals figures comissaria smith doubt crop cocoa harvesting practically end total bahia crop estimates 64 mln bags sales standing 62 mln hundred thousand bags hands farmers middlemen exporters processors doubts cocoa fit export shippers experiencing dificulties obtaining bahia superior certificates view lower quality recent weeks farmers sold good part cocoa held consignment comissaria smith spot bean prices rose 340 350 cruzados arroba 15 kilos bean shippers reluctant offer nearby shipment limited sales booked march shipment 1750 1780 dlrs tonne ports named crop sales light open ports junejuly 1850 1880 dlrs 35 45 dlrs york july augsept 1870 1875 1880 dlrs tonne fob routine sales butter made marchapril sold 4340 4345 4350 dlrs aprilmay butter 227 times york junejuly 4400 4415 dlrs augsept 4351 4450 dlrs 227 228 times york sept octdec 4480 dlrs 227 times york dec comissaria smith destinations covertible currency areas uruguay open ports cake sales registered 785 995 dlrs marchapril 785 dlrs 753 dlrs aug 039 times york dec octdec buyers argentina uruguay convertible currency areas liquor sales limited marchapril selling 2325 2380 dlrs junejuly 2375 dlrs 125 times york july augsept 2400 dlrs 125 times york sept octdec 125 times york dec comissaria smith total bahia sales estimated 613 mln bags 198687 crop 106 mln bags 198788 crop final figures period february 28 expected published brazilian cocoa trade commission carnival ends midday february 27"
t = " national average prices farmerowned reserve agriculture department reported farmerowned reserve national fiveday average price february 25 dlrsbusorghum cwt  natl loan release call avge ratex level price price wheat 255 240 iv 465  465  vi 445  corn 135 192 iv 315 315 325   1986 rates natl loan release call avge ratex level price price oats 124 099 165  barley na 156 iv 255 255 265  sorghum 234 325y iv 536 536 554  reserves ii iii matured level iv reflects grain entered oct 6 1981 feedgrain july 23 1981 wheat level wheatbarley 51482 cornsorghum 7182 level vi covers wheat entered january 19 1984 x1986 rates ydlrs cwt 100 lbs nanot"
corn1 =  'national average prices farmer  owned reserve   agriculture department reported farmer  owned reserve national  day average price february 25  dlrs  bu  sorghum cwt   natl loan release call avge rate  level price price wheat 2  55 2  40 iv 4  65  4  65  vi 4  45  corn 1  35 1  92 iv 3  15 3  15 3  25   1986 rates'
corn2 = ' argentine 1986  87 grain  oilseed registrations argentine grain board figures show crop registrations grains  oilseeds products february 11  thousands tonnes  showing future shipments month  1986  87 total 1985  86 total february 12  1986  brackets  bread wheat prev 1  655  8  feb 872  0  march 164  6  total 2  692  4  4  161  0  maize mar 48  0  total 48  0  nil  sorghum nil  nil  oilseed export registrations  sunflowerseed total 15  0  7  9  soybean 20  0  total 20  0  nil  board detailed export registrations subproducts   subproducts wheat prev 39  9  feb 48  7  march 13  2  apr 10  0  total 111  8  82  7   linseed prev 34  8  feb 32  9  mar 6  8  apr 6  3  total 80  8  87  4  soybean prev 100  9  feb 45  1  mar nil  apr nil  20  0  total 166  1  218  5  sunflowerseed prev 48  6  feb 61  5  mar 25  1  apr 14  5  total 149  8  145  3  vegetable oil registrations  sunoil prev 37  4  feb 107  3  mar 24  5  apr 3  2  nil  jun 10  0  total 182  4  117  6  linoil prev 15  9  feb 23  6  mar 20  4  apr 2  0  total 61  8   76  1  soybean oil prev 3  7  feb 21  1  mar nil  apr 2  0  9  0  jun 13  0  jul 7  0  total 55  8  33  7  reuter'
crude1 = ' diamond shamrock  dia  cuts crude prices diamond shamrock corp effective today cut contract prices crude oil 1  50 dlrs barrel  reduction brings posted price west texas intermediate 16  00 dlrs barrel  copany   price reduction today made light falling oil product prices weak crude oil market  company spokeswoman  diamond latest line   oil companies cut contract  posted  prices days citing weak oil markets '
crude2 = '  opec meet firm prices  analysts opec forced meet scheduled june session readdress production cutting agreement organization halt current slide oil prices  oil industry analysts   movement higher oil prices easy opec thought  emergency meeting sort problems  daniel yergin  director cambridge energy research associates  cera  analysts oil industry sources problem opec faces excess oil supply world oil markets   opec  problem price problem production issue addressed  paul mlotok  oil analyst salomon brothers  market  earlier optimism opec ability production control pessimistic outlook organization address wishes regain initiative oil prices  analysts uncertain emergency meeting address problem opec production 15  8 mln bpd quota set december   opec learn buyers market deemed quotas  fixed prices set differentials  regional manager major oil companies spoke condition named   market teach lesson  added  david  mizrahi  editor mideast reports  expects opec meet june  immediately   optimistic opec address principal problems   meet advantage winter demand sell oil  late march april demand slackens  mizrahi  mizrahi opec reiterate agreement output 15  8 mln bpd  analysts months critical opec  ability hold prices output   opec hold pact weeks buyers back market  dillard spriggs petroleum analysis york  bijan moussavar  rahmani harvard university  energy environment policy center demand opec oil rising quarter prompted excesses production   demand  opec  oil 15  8 mln bpd closer 17 mln bpd higher characterized cheating opec meeting demand current production  told reuters telephone interview '
start = time.time()

class Ssk:
    def __init__(self, n, lam, limCoefficient):
        self.dict1 = {}
        self.dict2 = {}
        self.dict3 = {}
        self.n = n
        limit = 1
        while(lam**limit > limCoefficient):
            limit += 1
        print('limit calculated to', limit)
        self.limit = limit   
        self.lam = lam

    def kernel(self, s, t):
        return self.k(s, t, self.n)/(self.k(s, s, self.n)*self.k(t, t, self.n))

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
                if (j < self.limit):
                    #print('1 we matched with letter ', t[j], ' t is: ', t[0:j], ' s is: ', s[:j], ' j is ', j, ' and ', j-self.limit)
                    value += self.kP(s[-j:-1], t[0:j], i-1)*(self.lam**2)
                else:
                    #print('2 we matched with letter ', t[j], ' t is still: ', t[j-self.limit:j], ' s is still: ', s[-self.limit-1:-1], ' j is ', j)
                    value += self.kP(s[-self.limit-1:-1], t[j-self.limit:j], i-1)*(self.lam**2)

        value += self.k(s[:-1], t, i)
        self.dict1[(s, t, i)] = value
        return value

    def kP(self, s, t, i):
        #print(s, ' and ', t, ' i is ', i)
        if (s, t, i) in self.dict2: 
            return self.dict2[(s, t, i)]

        if (i == 0):   
            self.dict2[(s, t, i)] = 1
            #print(' ')
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

a = "bollbkdig"
b = "bille mig"
"""
test = Ssk  (n, lam, 0.05)
print('Comparison between corn: ', test.k(corn1, corn2, test.n)/(test.k(corn1, corn1, test.n)*test.k(corn2, corn2, test.n)))
print('Comparison between corn and crude: ', test.k(corn1, crude1, test.n)/(test.k(corn1, corn1, test.n)*test.k(crude1, crude1, test.n)))
print('Comparison between corn and crude: ', test.k(corn2, crude2, test.n)/(test.k(corn2, corn2, test.n)*test.k(crude2, crude2, test.n)))
print('Comparison between crude: ', test.k(crude1, crude2, test.n)/(test.k(crude1, crude1, test.n)*test.k(crude2, crude2, test.n)))
print(test.k(corn1, corn1, test.k))
print("----- %s seconds -----" % (time.time() - start))
"""


