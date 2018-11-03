# lami1.py
#
# A relatively involved example, color coding finite gaps in a
# lamination depending upon which preimage of the critical triangle it
# maps to.

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq

## To draw a picture, define the degree, depth, and pullback scheme.

L = DrawLam.DrawLam()
L.filename = "lami1.png"
L.degree = 3
depth = 5

# A valid pullbackscheme is a list of 3-tuples: the first and second
# elements are points on the circle separated by a critical length,
# and the third is a boolean expressing whether the first element is a
# member of the interval.  Should be a counter-clockwise interval not
# containing zero.
L.pullbackscheme = [(mpq(1,9), mpq(4,9), True),
                    (mpq(4,9), mpq(7,9), True)]

# The following does the initialization and some sanity checks.
L.start()

# Now for the fun!  Set some line qualities.
L.setColor(1,1,1)
L.thickness(4)
# Here are a list of simplices to take the preimage of.
simplex = [(mpq(1,27), mpq(22,27), mpq(25,27)),
           (mpq(10,27), mpq(4,27), mpq(7,27)),
           (mpq(19,27), mpq(13,27), mpq(16,27))]
# Draw them (and their first five pullbacks)
L.setFill(1,0,0)
L.iterative_preimages(simplex[0],5)
L.setFill(0,1,0)
L.iterative_preimages(simplex[1],5)
L.setFill(0,0,1)
L.iterative_preimages(simplex[2],5)

# Here, we will draw the defining critical leaves in dashed lines.
L.dashed(80)
L.thickness(16)
L.setColor(0,0,0)
for leaf in [a[0:2] for a in L.pullbackscheme]:
    L.draw(leaf)
L.writeout()
