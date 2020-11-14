from Line import *
from Vector3D import *
from Triangle import *
from Plane import *
import math

def shade_scene(Scene,Light):
    """Shades a Scene in the form of a list of triangles"""
    for triangle in Scene:
        triangle.shade(Light)

def project(Scene,):
    """"""
