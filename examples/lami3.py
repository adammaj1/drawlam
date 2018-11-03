# lami3.py
#
# As simply as possible, draw the lamination for the rabbit.

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq

L = DrawLam.DrawLam()
L.degree = 2
L.pullbackscheme = [(mpq(1,7), mpq(1,7)+mpq(1,2), True)]
L.filename = "lami3.png"
L.start()
L.iterative_preimages((mpq(1,7), mpq(2,7)), 10)
L.writeout()
