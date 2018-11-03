# lami5.py
#
# Draws a rabbit lamination simply, with shaded gaps.

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq

L = DrawLam.DrawLam()
L.degree = 2
depth = 10
L.pullbackscheme = [(mpq(1,7), mpq(1,7)+mpq(1,2), True)]
L.filename = "lami5.png"
L.start()

gap = (mpq(1,7), mpq(2,7), mpq(4,7))
L.thickness(2)
L.setColor(0,0,0)
L.setFill(0.8,0.8,0.8)
L.iterative_preimages(gap, depth)
L.writeout()
print "Done!"
