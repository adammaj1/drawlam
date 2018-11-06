# lami5.py
#
# As simply as possible, draw the lamination for period 5

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq

L = DrawLam.DrawLam()
L.degree = 2
L.pullbackscheme = [(mpq(1,31), mpq(1,31)+mpq(1,2), True)]
L.filename = "lami5.png"
L.start()
L.iterative_preimages((mpq(1,31), mpq(2,31)), 10)
L.writeout()
