from Vector3D import *
import math
class Triangle:
    def __init__(self,v1,v2,v3,color=Vector(255,0,0)): #3d Vectors represent colors!
        self.v1=v1
        self.v2=v2
        self.v3=v3
        self.normal=(v3-v1)*(v2-v1) #STARTING AT LEFT
        self.rnormal=(v2-v1)*(v3-v1) #normal from right
        self.centre=(v1+v2+v3)/3
        self.color=color
    def __repr__(self):
        return "Triangle({},{},{},{})".format(self.v1,self.v2,self.v3,self.color)
    
    def normal_angle(self,point): #ONLY FOR RENDERER! MAY BE DEPRECATED
        """the angle of the normal with another vector"""
        return self.normal.angle(point-self.centre)
    def shade(self,light):
        """shading method"""
        self.shadeVal=(self.normal.angle(light-self.centre)/math.pi)*255
        self.color=self.color-Vector(self.shadeVal,self.shadeVal,self.shadeVal)#

