# lami2.py
#
# As simply as possible, draw the lamination for the basilica
# period = 2
# minor leaf µ1/3 which connects 1/3 to 2/3.
import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq

L = DrawLam.DrawLam()
L.degree = 2
L.pullbackscheme = [(mpq(1,3), mpq(1,3)+mpq(1,2), True)]
L.filename = "lami2.png"
L.start()
L.iterative_preimages((mpq(1,3), mpq(2,3)), 10)
L.writeout()
