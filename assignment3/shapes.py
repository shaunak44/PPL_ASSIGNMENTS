class shapes:
    def __init__(self):
        self.__has_area = True #private variable
        self._solid = True #protected variable 
        self.sides = 4#Public variable
    
    def set_sides(self, side):
        self.sides=side
    def perimeter(self):
        pass
    
class _2d_shapes(shapes):
    def area(self):
        pass
    
class _3d_shapes(shapes):
    def volumn(self):
        pass
    
    def surface_area(self):
        pass
    
class triangle(_2d_shapes):
    def __init__(self, a = 3, b = 4, c = 5):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        return self.a+self.b+self.c
    
    def area(self):
        a = self.a
        b = self.b
        c = self.c
        s =  (a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c))**(0.5)

    def get(self):
        return self.a, self.b, self.c

    def set(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

class square(_2d_shapes):
    def __init__(self, side = 5):
        self.side = side
        
    def perimeter(self):
        return 4*self.side
    
    def area(self):
        return self.side*self.side
    
    def get(self):
        return self.side

    def set(self,side):
        self.side = side
        
class circle(_2d_shapes):
    def __init__(self, radius = 5):
        self.r = radius
        
    def perimeter(self):
        return 2*3.142*self.r
    
    def area(self):
        return 3.142*self.r*self.r
    
    def get(self):
        return self.r

    def set(self, radius):
        self.r = radius
        
class rectangle(_2d_shapes):
    def __init__(self, a = 5, b = 3):
        self.a = a
        self.b = b
        
    def perimeter(self):
        return (2*self.a)+(2*self.b)
    
    def area(self):
        return self.a*self.b
    
    def get(self):
        return self.a, self.b

    def set(self,a,b):
        self.a = a
        self.b = b

class cube(_3d_shapes):
    def __init__(self, side = 5):
        self.side = side
        
    def perimeter(self):
        return 6*self.side
    
    def volumn(self):
        return self.side**3
    
    def surface_area(self):
        return 6*(self.side**2)
    
    def get(self):
        return self.side

    def set(self,side):
        self.side = side

class sphere(_3d_shapes):
    def __init__(self, r = 5):
        self.r = r
        
    def volumn(self):
        return (4/3)*3.142*(self.r**3)
    
    def surface_area(self):
        return 4*3.142*(self.r**2)
    
    def set(self, r):
        self.r = r
        
    def get(self):
        return self.r
    
class cylinder(_3d_shapes):
    def __init__(self, r = 5, h = 7):
        self.r = r
        self.h = h
        
    def volumn(self):
        return 3.142*(self.r**2)*self.h
    
    def surface_area(self):
        return (2*3.142*self.r)*(self.r+self.h)
    
    def set(self, r, h):
        self.r = r
        self.h = h
        
    def get(self, r, h):
        return self.r, self.h

t = cube()
s = cylinder()
c = sphere()

print(t.surface_area())
print(s.surface_area())
print(c.surface_area())
