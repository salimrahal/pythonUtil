'''
Created on Oct 13, 2016

@author: salim

http://code.activestate.com/recipes/577721-how-to-use-super-effectively-python-27-version/
'''

# -------- Making sure a root exists ----------------------------

class Root(object):
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(Root, self), 'draw')

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super(Shape, self).__init__(**kwds)
    def draw(self):
        print 'Drawing.  Setting shape to:', self.shapename
        super(Shape, self).draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super(ColoredShape, self).__init__(**kwds)
    def draw(self):
        print 'Drawing.  Setting color to:', self.color
        super(ColoredShape, self).draw()

ColoredShape(color='blue', shapename='square').draw()
print '-' * 20
