from Vector3D import *
class Ray:
    """Vectorial data structure representing a Ray"""
    def __init__(self,origin_point,direction):
        self.origin= origin_point
        self.direction = direction.normalize()
        
    def __repr__(self):
        return "Ray({},{})".format(self.position,self.direction.normalize())
    
    def point(self,t):
        return self.position + t*self.direction
    
    def plane_intersect(self,plane):
        """Calculates the intersection of a plane of the plane class and itself, requires the use of the plane module! if it does not find an intercept it retuns None"""
        #print("{},{}".format((plane.distance_to_origin() - plane.normal.x*self.position.x - plane.normal.y*self.position.y - plane.normal.z*self.position.z),(plane.normal.x*self.direction.x + plane.normal.y*self.direction.y + plane.normal.z*self.direction.z)))   
         
        if self.direction.dot_product(plane.normal) == 0:
            raise Exception("Ray {} and plane {} are parallel".format(self, plane))
            return None
        else: 
            self.tVal=((plane.position-self.origin).dot_product(plane.normal))/ (self.origin.dot_product(plane.normal)) # ACCORDING to the formula on wikipedia vector form: https://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection
            if self.tVal>=0:
                return self.point(self.tVal)
            else:
                return None


    """CLASS DERIVED FROM LINE!"""
        
        
