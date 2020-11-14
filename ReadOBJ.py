import re
from Vector3D import *
from Triangle import *
def readOBJ(OBJfile):
    fileObject= open(OBJfile)# Quick and dirty patch code, allows closing the file at end, reducing ram consumption.
    file = fileObject.readlines()
    fileObject.close() # Closes file after reading, "file" var stays due to being independent list.
    faces = []
    vertices = []
    for line in file:
        if line[0]== "v": #The line declares a vertex
            strCoords=re.sub("v|\n","",line).split()
            vertices.append( Vector( float(strCoords[0]), float(strCoords[2]), -float(strCoords[1]) ) )
        elif line[0]=="f": # The line declares a face
            # Text processing for all 3 vetices id
            strVertices=re.sub("f|\n","",line).split() #re.sub() takes away the newlines and fs, then it´s split through the spaces
            faces.append( Triangle( vertices[int(strVertices[0])-1], vertices[int(strVertices[1])-1], vertices[int(strVertices[2])-1] ) ) # transforms the str into int and appends them to faces as a 3d tuple
    
    return faces
if __name__== "__main__":
    FILE = "object.obj"
    dump = open("debug.txt","w+")
    dump.write(str(readOBJ(FILE)))
