# lami4.py
#
# As simply as possible, draw the lamination for period 4

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq

L = DrawLam.DrawLam()
L.degree = 2
L.pullbackscheme = [(mpq(1,15), mpq(1,15)+mpq(1,2), True)]
L.filename = "lami4.png"
L.start()
L.iterative_preimages((mpq(1,15), mpq(2,15)), 10)
L.writeout()
