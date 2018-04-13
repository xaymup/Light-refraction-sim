

import pygame
import math


        
pygame.init()
pygame.font.init()




red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
pointofmiddle=(640/2,480/2)
myfont = pygame.font.SysFont('noto sans', 12)

Material1=[1.0, "Air"]
Material2=[1.52,"Glass"]
        
class IncidentRay:
    def __init__(self, angle):
        self.x=640/2
        self.y=0
        self.raylen=400
        if 0<angle:
            self.x=0
            self.y=480/2
        if -180<= angle <=-90:
                self.x = pointofmiddle[0]+math.cos(math.radians(angle)) * self.raylen
                self.y = pointofmiddle[1]+math.sin(math.radians(angle)) * self.raylen
                textsurface = myfont.render('Incident/Reflected Ray Angle: %f' %(180-angle-270), False, (0, 0, 0))
                screen.blit(textsurface,(20,390))
    def display(self):
        pygame.draw.line(screen, red, pointofmiddle, (self.x,self.y), 3)



        
class ReflectedRay:
    def __init__(self, angle):
        self.raylen=400
        self.ReflectedRayAngle=180-angle
        self.reflectedintensity = (self.ReflectedRayAngle-270)/90
        self.x=640/2
        self.y=0

        if 270 <= self.ReflectedRayAngle <= 360:
            
            self.x = pointofmiddle[0]+math.cos(math.radians(self.ReflectedRayAngle)) * self.raylen
            self.y = pointofmiddle[1]+math.sin(math.radians(self.ReflectedRayAngle)) * self.raylen  
        if 180 >self.ReflectedRayAngle>=0:
            self.x=640
            self.y=480/2

    def display(self):
        pygame.draw.line(screen, red, pointofmiddle, (self.x,self.y), 3)
        
class RefractedRay:
    def __init__(self,angle):
        self.x=640/2
        self.y=0
        self.raylen=400
        TrueAngle = (180-angle-270)
        refractedangle=-math.degrees(math.asin(math.sin(math.radians(TrueAngle))*Material1[0]/Material2[0]))+90
        if 0<angle:
            self.x=0
            self.y=480/2
        if -180<= angle <=-90:
                self.x = pointofmiddle[0]+math.cos(math.radians(refractedangle)) * self.raylen
                self.y = pointofmiddle[1]+math.sin(math.radians(refractedangle)) * self.raylen
                textsurface = myfont.render('Refracted Ray Angle: %f' %((refractedangle-90)*-1), False, (0, 0, 0))
                textsurface2 = myfont.render(Material1[1]+" Refraction Index: "+str(Material1[0]), False, (0, 0, 0))
                textsurface3 = myfont.render(Material2[1]+" Refraction Index: "+str(Material2[0]), False, (0, 0, 0))
                screen.blit(textsurface,(20,400))
                screen.blit(textsurface2,(20,100))
                screen.blit(textsurface3,(20,300))

    def display(self):
        pygame.draw.line(screen, red, pointofmiddle, (self.x,self.y), 3)


class RefractionSurface:
    def __init__(self):
        surface = pygame.Surface((640, 240), pygame.SRCALPHA)
        surface.fill((100, 100, 255, 100)) # You can change the 100 depending on what transparency it is.
        screen.blit(surface, (0, 240))
        


background_color = (white)
(width, height) = (640, 480)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Light Refraction PyGame Simulation')


screen.fill(background_color)

IncidentRay(0).display()
ReflectedRay(0).display()
RefractionSurface()


pygame.display.flip()
angle=0
running = True
while running:

    screen.fill(background_color)
    RefractionSurface()
    pos=pygame.mouse.get_pos()
    angle = math.atan2(pos[1]-(480/2),pos[0]-(640/2))*180/math.pi
    (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
    if pressed1:
            IncidentRay(angle).display()
            ReflectedRay(angle).display()
            RefractedRay(angle).display()
            pygame.display.flip()
            (mouseX, mouseY) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
