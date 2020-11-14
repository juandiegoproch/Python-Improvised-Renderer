from Vector3D import *
from Line import *
from Triangle import *
from Plane import *
from ReadOBJ import *
import math
from Ray import *
from drawer import *
# render function
pygame.init()
def render(SceneLoaded,Scale,Light,CamDist,Fdist):
    Scene=SceneLoaded
    Screen=[]
    projection_plane= Plane(Vector(0,CamDist,0),Vector(1,0,0),Vector(0,0,1))
    focalPoint=Vector(0,CamDist+Fdist,0)
    #Sort by Y value all triangles (oclusion)
    Scene.sort( key = lambda tri: tri.centre.y)
    for triangle in Scene:
        triangle.shade(Light)
        triangle.v1=triangle.v1*Scale
        triangle.v2=triangle.v2*Scale
        triangle.v3=triangle.v3*Scale
    for triangle in Scene:
        try:
            V1=Line(triangle.v1,focalPoint-triangle.v1).plane_intersect(projection_plane)# Three lines from the vertices to the plane
            V2=Line(triangle.v2,focalPoint-triangle.v2).plane_intersect(projection_plane)#
            V3=Line(triangle.v3,focalPoint-triangle.v3).plane_intersect(projection_plane)#
            Screen.append(Triangle(V1,V2,V3,color=triangle.color))
        except:
            pass
    draw(Screen)
LoadedScene = readOBJ("object.obj")
light=-1000
render(LoadedScene,100,Vector(1000,1000,1000),1,1000)
camspeed=10
campos=1000
scale=100
while True:
    LoadedScene = readOBJ("object.obj")
    render(LoadedScene,scale,Vector(1000,1000-light,light),campos,1000)
    light+=100
    pygame.event.get()
