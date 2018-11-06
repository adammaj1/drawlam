# lamip.py
#
# As simply as possible, draw the lamination for period p

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq

p = 7
print "period p = %d"% p
d = (2**p)-1
print "denominator d = %d"% d
L = DrawLam.DrawLam()
L.degree = 2
L.pullbackscheme = [(mpq(1,d), mpq(1,d)+mpq(1,2), True)]
L.filename = "lami"+str(p)+".png"
L.start()
L.iterative_preimages((mpq(1,d), mpq(2,d)), 10)
L.writeout()
