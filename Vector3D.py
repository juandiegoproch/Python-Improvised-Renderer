import math
class Vector:
    """ tri dimensional vector class"""
    def __init__(self,x,y,z,):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self): 
        return "Vector({},{},{})".format(self.x,self.y,self.z)
    
    def __repr__(self):
        return "Vector({},{},{})".format(self.x,self.y,self.z)
        
    def magnitude(self,):
        if self==Vector(0,0,0): # If the vector is a Zero Vector, return a 0 magnitude
            return 0
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def __add__(self,other,):
        """Adds vectors"""
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
    def __neg__(self):
        return Vector(-self.x,-self.y,-self.z)
    
    def __sub__(self, other):
        """Subtracts two vectors"""
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
                      
    def __mul__(self,other):
        """Cross product of two vectors or a vector times  a scalar"""
        try: # It´s a vector
            return Vector(self.y*other.z - other.y*self.z,
                          self.z*other.x - other.z*self.x,
                          self.x*other.y - other.x*self.y)
        except: # It´s a scalar
            return Vector(self.x*other, self.y*other, self.z*other)
    def __rmul__(self,other):
        """Cross product of two vectors or a vector times  a scalar"""
        try:
            return Vector(self.y*other.z - other.y*self.z,
                          self.z*other.x - other.z*self.x,
                          self.x*other.y - other.x*self.y)
        except:
            return Vector(self.x*other, self.y*other, self.z*other)
    def __truediv__(self, divider,):
        """Scalar division of a vector"""
        return Vector(self.x/divider, self.y/divider, self.z/divider)
    def __eq__(self,other):
        """Compares two vectors to check for equality"""
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    def __lt__(self,other):
        """Compares the magnitude of two vectors"""
        return self.magnitude() < other.magnitude()
    
    def normalize(self):
        """Normalizes the vector"""
        if self.magnitude()==0:
            raise Exception("ZeroVector {} has no direction and can´t be normalized".format(self))
        return self/self.magnitude()
    
    def dot_product(self,other):
        """returns the dot product of itself times another"""
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def angle(self,other):
        """Returns the flat angle between two vectors"""
        try:
            return math.acos(self.normalize().dot_product(other.normalize()))
        except:
            #print("WARNING: Angle with itself/same direction vector")
            return 0
    
    def colinear(self,other):
        """Boolean test for colinearity"""
        if other.normalize()==self.normalize() or other.normalize() == -self.normalize():
            return True
        else:
            return False
    def remove_negatives(self):
        """Removes every negative component and replaces it with zeroes"""
        return Vector(0 if self.x<0 else self.x, 0 if self.y<0 else self.y, 0 if self.z<0 else self.z)
    def truncated(self):
        """Truncates all components to an integrer"""
        return Vector(int(self.x),int(self.y),int(self.z))
        
    
