from Vector3D import *
from Line import *
from Triangle import *
from Plane import *

from ReadOBJ import *
import math
from Ray import *
scale=int(input("Scale:"))
LIGHT=Vector(1000,-1000,0)
SCENE=[]
SCREEN=[]
FOCAL_POINT=Vector(0,-100,0)
SCREENY=-700
FOCALDIST=int(input("Focal distance:"))
CAMDIST=int(input("Camera distance"))
################ comment if adjusting by itself
if True:
    FOCAL_POINT=Vector(0,CAMDIST+FOCALDIST,0)
    SCREENY=CAMDIST
from drawer import *
############### TESTS #################
SCENE= readOBJ("object.obj")
###################
projection_plane= Plane(Vector(0,SCREENY,0),Vector(1,0,0),Vector(0,0,1))
### HELPER FOR FORMATTING DATA FOR SORT!
def TRIY(tri):
    return tri.centre.y
SCENE.sort(key=TRIY)
for triangle in SCENE:
    triangle.shade(LIGHT)
    triangle.v1=triangle.v1*scale
    triangle.v2=triangle.v2*scale
    triangle.v3=triangle.v3*scale 
for triangle in SCENE:
    try:
        V1=Line(triangle.v1,FOCAL_POINT-triangle.v1).plane_intersect(projection_plane)# Three lines from the vertices to the plane
        V2=Line(triangle.v2,FOCAL_POINT-triangle.v2).plane_intersect(projection_plane)#
        V3=Line(triangle.v3,FOCAL_POINT-triangle.v3).plane_intersect(projection_plane)#
        #print("V1 = {};\nV2 = {};\nV3 = {};\n".format(Line(triangle.v1,FOCAL_POINT-triangle.v1),
        #                                         Line(triangle.v2,FOCAL_POINT-triangle.v2),
        #                                         Line(triangle.v3,FOCAL_POINT-triangle.v3))
        #                                          )
        SCREEN.append(Triangle(V1,V2,V3,color=triangle.color))
        #print(V1,V2,V3)
    except:
        pass

#print(SCREEN)
dump = open("debug.txt","w+")
for triangle in SCREEN:
    dump.write("{} \n".format(str(triangle)))
draw(SCREEN)
canvas.pack()
tkinter.mainloop()

