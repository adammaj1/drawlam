# lami2.py
#
# A simpler example, performing pullbacks of leaves to make the rabbit
# lamination.  The pullback scheme and the leaf we pulled back are
# indicated in the picture.

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq

L = DrawLam.DrawLam()
L.degree = 2
depth = 10

L.pullbackscheme = [(mpq(1,7), mpq(1,7)+mpq(1,2), True)]
leaf = (mpq(1,7), mpq(2,7))
L.filename = "lami2.png"
L.start()

# Draw pullback scheme first.
L.setColor(1,0,0)
L.thickness(16)
L.dashed(80)
for chord in L.pullbackscheme:
    L.draw(chord[0:2])

# Draw pullbacks of minor
L.setColor(0,0,1)
L.thickness(1)
L.solid()
L.iterative_preimages(leaf, depth)

# Draw minor
L.thickness(16)
L.setColor(0,0,0)
L.draw(leaf[0:2])

L.writeout()
print "Done!"
