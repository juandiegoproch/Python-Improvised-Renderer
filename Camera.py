from Plane import *
from Vector3D import *
class Camera:
    def __init__(self,position,direction,focal_distance):
        self.projection_plane=Plane()
        
