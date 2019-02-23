This is clone of the [original repsitory](https://bitbucket.org/clintonc/drawlam/src/default/) by Clinton Curry 


# DrawLam.py

DrawLam.py is a Python library which makes it easy to draw laminations, including pullback laminations.  It is capable of producing PNG and PDF output.

## Prerequisites

This library calls upon [PyCairo][1] and [gmpy][2] for its dark deeds.


In ubuntu:

```bash
pip2 install gmpy --user
```

## Usage

DrawLam.py is designed to be used in Python scripts.  There are several sample scripts available in the "examples" directory in the source tree.  The simplest possible script for drawing the lamination
corresponding to the rabbit is given below; 

lami3.py
* it takes ten iterative preimages of the (1/7, 2/7) leaf which do not cross the (1/7, 9/14) chord.  
* The "True" associated with that leaf indicates that preimages are to be taken in the [1/7, 9/14) interval and the [9/14, 1/7) interval; "False" would give the opposite endpoint arrangement.


```python
from DrawLam import DrawLam
from gmpy import mpq

L = DrawLam()
L.degree = 2
L.pullbackscheme = [(mpq(1,7), mpq(9,14), True)]
L.filename = "lami3.png"
L.start()
L.iterative_preimages((mpq(1,7), mpq(2,7)), 10)
L.writeout()
```
    
    
The resulta is lami3.png

![lami3.png](examples/lami3.png)      




    
### examples    
Original examples

Run from console 

```bash
cd examples 
python lami1.py
```
    
![lami1.png](examples/lami1.png)      

![lami2.png](examples/lami2.png)  

![lami3.png](examples/lami3.png)  


![lami4.png](examples/lami4.png)  

![lami5.png](examples/lami5.png)  

![qml.png](examples/qml.png)  

and [pdf file](examples/qml.pdf)




### regular examples

Description and examples not by original author but by Adam Majewski ( only small modifications of some of the original examples)

[Quadratic invariant laminations](https://arxiv.org/abs/1707.05384) and:
* corresponding Julia sets for complex quadratic polynomial ( to show the landing pattern of external rays and structure of Julia set )
* dynamics of angle doubling map


Run from console 

```bash
cd regular_examples 
python lami2.py
```





![lami2.png](regular_examples/lami2.png)  

![lami3.png](regular_examples/lami3.png)  


![lami4.png](regular_examples/lami4.png)  

![lami5.png](regular_examples/lami5.png)  

![lami6.png](regular_examples/lami6.png)  

![lami7.png](regular_examples/lami7.png)  

![lami8.png](regular_examples/lami8.png)  

![lami9.png](regular_examples/lami9.png)  


### period 2


External rays 1/3 and 2/3 
* on the parameter plane = angles of the wake
* on the dynamic plane land on the fixed point


![period2.png](regular_examples/period2.png)  

Basilica lamination
![lami2.png](regular_examples/lami2.png)  


Code:

```python
# lami_2.py
# python lami_2.py
# As simply as possible, draw the lamination for period p

import sys
sys.path.append("..")
import DrawLam
from gmpy import mpq, version , gmp_version


# info 
print "Python version" 
print (sys.version) #parentheses necessary in python 3.  
ver = version()
print " gmpy version " 
print ver


gmp_ver = gmp_version() 
print "gmp version "
print gmp_ver


p = 2
print "period p = %d"% p
d = (2**p)-1
print "denominator d = %d"% d
depth = 10


L = DrawLam.DrawLam()
L.degree = 2
a1 = mpq(1,d)
a2 = mpq(1,d)+mpq(1,2)

MinorLeaf = (a1, mpq(2,d))
print "Minor Leaf :"
print MinorLeaf

MajorLeaf = (a1, a2) 
print "Major Leaf: "
print(MajorLeaf)


L.pullbackscheme = [(a1, a2, True)]
L.filename = "lami_"+str(p)+".png"


L.start()
print "draw preimages of minor leaf for depth %d"% depth
L.iterative_preimages(MinorLeaf, depth)
L.writeout()
```

text output:

```bash
Python version
2.7.15rc1 (default, Apr 15 2018, 21:51:34) 
[GCC 7.3.0]
 gmpy version 
1.17
gmp version 
6.1.1
period p = 2
denominator d = 3
Minor Leaf :
(mpq(1,3), mpq(2,3))
Major Leaf: 
(mpq(1,3), mpq(5,6))
Lamination data seems valid.
filetype:  png
draw preimages of minor leaf for depth 10
Writing file lami_2.png
```


>>>
We see that the pinch points for the Basilica are points that have external rays at angles that are rational numbers of the form
$`\frac{3k - 1}{3·2^n}`$ and $`\frac{3k + 1}{3·2^n }`$ for some $`k, n ∈ N`$. 
>>>


# License

Copyright (c) 2012, Clinton Curry
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[1]: http://cairographics.org/pycairo/
[2]: http://code.google.com/p/gmpy/




# Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc


# technical notes
GitLab uses:
* the Redcarpet Ruby library for [Markdown processing](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/doc/user/markdown.md)
* KaTeX to render [math written with the LaTeX syntax](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/doc/user/markdown.md), but [only subset](https://khan.github.io/KaTeX/function-support.html)




## Git
```
cd existing_folder
git init
git remote add origin git@gitlab.com:adammajewski/drawlam.git
git add .
git commit -m "Initial commit"
git push -u origin master

```



