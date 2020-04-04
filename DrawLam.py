from __future__ import print_function # https://stackoverflow.com/questions/15769246/pythonic-way-to-print-list-items
from gmpy import mpq #, mpz
import math
import cairo

# in python 3 The print statement has been replaced with a print() function, with keyword arguments to replace most of the special syntax of the old print statement (PEP 3105)



class DrawLam:
    filename = None
    filetype = None
    pullbackscheme = None
    degree = None
    dynamical = True
    scalefactor = 1.125

    # By default, black line drawings with no fill.
    color = (0,0,0) 
    fill = None

    # Some sane default dimensions
    width = 512
    height = 512
    linewidth = 0.001

    # First, laminational functions
    def validate_lamination_data(self):
        """Perform a few checks to guard against ridiculous input.

        1. Check that there are d-1 intervals in the pullback scheme
        2. (TODO) Check that the length of each is a multiple of d
        3. (TODO) Check that, for each pair of intervals, one contains
           the other properly or they are pairwise disjoint.
        """
        
        launch = True
        if self.filename==None:
            print ("Set a filename (like out.png or rabbit.pdf)")
            launch = False
        if self.dynamical and self.pullbackscheme==None:
            print ("Set a pullbackscheme.")
            launch = False
        if self.dynamical and self.degree==None:
            print ("Set your degree.")
            launch = False
            
        if self.dynamical and len(self.pullbackscheme)!=self.degree-1:
            print ("ERROR. degree is", self.degree), 
            print ("while your pullback scheme has"),
            print (len(self.pullbackscheme), "elements.")
            launch = False
        if not launch:
            quit()
        else:
            print ("Lamination data seems valid.")

    def key(self, point):
        """Provide unlinkedness sorting for points.

        This function provides a key to order points on the circle.
        Points which lie in the same unlinked class will be
        consecutive in the list."""
        
        key=''
        for i in self.pullbackscheme:
            if point > i[0] and point < i[1]:
                key += 'T'
            elif i[2]==True and point==i[0]:
                key += 'T'
            elif i[2]==False and point==i[1]:
                key += 'T'
            else:
                key += 'F'
        return key

    def preimages(self,simplex):
        """Finds the degree-many preimages of the specified simplex.

        Take first preimages of the specified simplex (represented as
        a tuple of mpq objects) under specified pullback scheme and
        degree.  Only defined for dynamical laminations.  
        """
        n = len(simplex)
        p = []
        for i in range(self.degree):
            for j in simplex:
                p.append( (j+i)/(self.degree) )
                # Give canonical coordinates in R / Z
                while p[-1] > 1:
                    p[-1] = p[-1] - 1
        p.sort() # counterclockwise order from 0
        p.sort(key=self.key) # unlink-ify

        # Chunk!  Divide the list p into sublists of length n
        s = [ p[i:i+n] for i in range(0, len(p), n)]
        print(*s, sep='\n') # 
        return s

    def iterative_preimages(self, simplex, depth):
        """Depth-first traversal to draw preimages of given object."""
        self.draw(simplex)
        if(depth > 0):
            for i in self.preimages(simplex):
                self.iterative_preimages(i, depth-1)
                

    ## Now, drawing functions
    def start(self):
        """Initialize everything for drawing a picture.

        1. Validates laminational data
        2. Figures filetype from extension
        3. Initializes drawing surface
        4. Sets up line quality functions"""

        self.validate_lamination_data()
        self.filetype = self.filename[-3:].lower()
        print ("filetype: ", self.filetype)

        if self.filetype=="png":
            self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 
                                              self.width, self.height)
        elif self.filetype=="pdf":
            self.surface = cairo.PDFSurface(self.filename, 
                                            self.width, self.height)
        else:
            print ("Cannot recognize extension \"", self.filetype, "\"")
            quit()
    
        # Make drawing surface have coordinates ranging from -1 to 1,
        # zoomed out by scalefactor.
        self.ctx = cairo.Context(self.surface)
        self.ctx.translate(self.width/2.0, self.height/2.0)
        self.ctx.scale(self.width/2.0/self.scalefactor, 
                       self.height/2.0/self.scalefactor)

        # Convenience functions for tuning the drawing
        self.thickness = lambda n: self.ctx.set_line_width(n*self.linewidth)
        self.solid = lambda: self.ctx.set_dash([])
        self.dashed = lambda n: self.ctx.set_dash([n*self.linewidth])

        # White background
        self.ctx.set_source_rgb(1,1,1)
        self.ctx.set_operator(cairo.OPERATOR_SOURCE)
        self.ctx.paint()

        # A default line style
        self.ctx.set_source_rgb(0,0,0)
        self.setColor(0,0,0)
        self.thickness(1)
        self.solid()

    def setColor(self, r, g, b):
        self.color = (r,g,b)

    def setFill(self, r, g, b):
        self.fill = (r,g,b)

    def clearFill(self):
        self.fill = None

    def makeanddrawleaf(self, p,q, r, s):
        """Draw a leaf with provided (rational) endpoints."""
        leaf = (mpq(p,q), mpq(r,s))
        print ("leaf from %d/%d to %d/%d"%p %q %r %s)
        self.draw(leaf)

    def draw(self,simplex):
        """Draws the simplex represented by the provided list."""

        # In the case that the simplex has only two endpoints, we have
        # to be careful not to draw an edge twice or else dashed lines
        # may become solid.  This is the purpose of the break
        # condition.
        for i in range(len(simplex)):
            j = i+1
            if j==len(simplex):
                if len(simplex)==2:
                    break
                j = 0
            x0 = math.cos(float(simplex[i]*2*math.pi))
            y0 = -math.sin(float(simplex[i]*2*math.pi))
            x3 = math.cos(float(simplex[j]*2*math.pi))
            y3 = -math.sin(float(simplex[j]*2*math.pi))
            M = math.sqrt(math.pow(x0+x3,2)/4 + math.pow(y0+y3,2)/4)
            kappa = 4.0/3.0*( 1/(1+math.sqrt(1.0-M*M)) - 1.0/4.0)
            x1 = kappa*x0
            y1 = kappa*y0
            x2 = kappa*x3
            y2 = kappa*y3
            if(i==0):
                self.ctx.move_to(x0, y0)
            self.ctx.curve_to(x1, y1, x2, y2, x3, y3)
        if self.fill != None and len(simplex) > 2:
            self.ctx.set_source_rgb(self.fill[0], self.fill[1], self.fill[2])
            self.ctx.fill_preserve()
        self.ctx.set_source_rgb(self.color[0], self.color[1], self.color[2])
        self.ctx.stroke()

    def writeout(self, drawCircle=True):
        if drawCircle:
            # Black unit circle of thickness 1
            self.ctx.set_source_rgb(0,0,0)
            self.thickness(1)
            self.solid()
            self.ctx.arc(0, 0, 1, 0, 2*math.pi)
            self.ctx.stroke()
        
        if self.filetype=="png":
            print ("Writing file %s"%self.filename)
            self.surface.write_to_png(self.filename)
        else:
            self.surface.finish()
            print ("Saving context")
            self.ctx.save()
