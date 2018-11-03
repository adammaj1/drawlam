import sys
sys.path.append("..")
import DrawLam
import math
import gmpy
mpq = gmpy.mpq

L = DrawLam.DrawLam()
L.dynamical = False
L.pullbackscheme = [(mpq(1,3), mpq(2,3), True)]
L.filename = "qml.pdf"
L.width=1024
L.height=1024
L.start()
L.thickness(0.01)
L.draw(L.pullbackscheme[0][0:2])

denoms = []
while len(denoms) < 10:
    print "pullbackscheme: ", L.pullbackscheme
    if denoms==[]:
        denoms.append(3)
    else:
        denoms.append(2*denoms[-1]+1)
    points = []

    # Check that the period is not too low.
    for num in range(1, denoms[-1]):
        q = mpq(num, denoms[-1])
        r = [ (q*den).denom()==1 for den in denoms[:-1] ]
        if not (True in r):
            points.append(q)

    points.sort(key = L.key)
    newleaves=[]
    for i in range(0, len(points), 2):
        l = (points[i], points[i+1], True)
        newleaves.append(l)
        L.draw(l[0:2])
    L.pullbackscheme.extend(newleaves)
L.writeout()
print "Done!"
