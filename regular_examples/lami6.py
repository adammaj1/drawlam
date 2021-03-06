# lami6.py
#
# As simply as possible, draw the lamination for period 6

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq

L = DrawLam.DrawLam()
L.degree = 2
L.pullbackscheme = [(mpq(1,63), mpq(1,63)+mpq(1,2), True)]
L.filename = "lami6.png"
L.start()
L.iterative_preimages((mpq(1,63), mpq(2,63)), 10)
L.writeout()
