from Vector3D import *
class Plane:
    def __init__(self,position,v1,v2):
        self.position=position
        self.v1=v1.normalize()
        self.v2=v2.normalize()
        self.normal=(self.v1*self.v2).normalize()
        if v1.colinear(v2):
            raise Exception("{} and {} must not be colinear".format(v1,v2))
        
    def __repr__(self):
        return "Plane({},{},{})".format(self.position,self.v1,self.v2)
    
    def point(self,s,t):
        return self.position+self.v1*t+self.v2*s
    
    def distance_to_origin(self):
        return -(self.normal.dot_product(self.position))
