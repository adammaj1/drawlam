# lami_2.py
# python lami_2.py
# As simply as possible, draw the lamination for period p

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq, version , gmp_version


# info 
print "Python version" 
print (sys.version) #parentheses necessary in python 3.  
ver = version()
print " gmpy version " 
print ver


gmp_ver = gmp_version()
print "gmp version "
print gmp_ver


p = 2
print "period p = %d"% p
d = (2**p)-1
print "denominator d = %d"% d
depth = 10


L = DrawLam.DrawLam()
L.degree = 2
a1 = mpq(1,d)
a2 = mpq(1,d)+mpq(1,2)

MinorLeaf = (a1, mpq(2,d))
print "Minor Leaf :"
print MinorLeaf

MajorLeaf = (a1, a2) 
print "Major Leaf: "
print(MajorLeaf)


L.pullbackscheme = [(a1, a2, True)]
L.filename = "lami_"+str(p)+".png"


L.start()
print "draw preimages of minor leaf for depth %d"% depth
L.iterative_preimages(MinorLeaf, depth)
L.writeout()



