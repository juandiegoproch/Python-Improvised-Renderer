import pygame
from Vector3D import *
# CONST VARS
WIDTH = 1000
LENGTH = 700
CENTERX = WIDTH/2
CENTERY = LENGTH/2
BGCOLOR= pygame.Color(0,0,0)
# FUNCTIONS
def draw(triangles):
        global screen
        screen.fill(BGCOLOR)
        for triangle in triangles:
                triangle.color=triangle.color.truncated().remove_negatives()
                pygame.draw.polygon(screen,pygame.Color(triangle.color.x,triangle.color.y,triangle.color.z),
                                    ( (triangle.v1.x+CENTERX, triangle.v1.z+CENTERY),
                                      (triangle.v2.x+CENTERX, triangle.v2.z+CENTERY),
                                      (triangle.v3.x+CENTERX, triangle.v3.z+CENTERY)),
                                    )
        
        pygame.display.flip()
screen = pygame.display.set_mode((WIDTH,LENGTH))
