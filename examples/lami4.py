# lami4.py
#
# Demonstrates the drawing of a couple of simplices.

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq

L = DrawLam.DrawLam()
L.dynamical = False
L.filename = "lami4.png"
L.start()
L.setColor(0,0,0)
L.setFill(0.8,0.6,8)
L.thickness(10)
L.dashed(80)
L.draw([mpq(1,7), mpq(2,7), mpq(4,7)])
L.dashed(10)
L.clearFill()
L.draw([mpq(9,14), mpq(11,14), mpq(1,14)])
L.writeout()
