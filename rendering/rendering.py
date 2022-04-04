from base import typeassert, Structure
from featureMatrix import Feature
from mesh import Mesh
from perspective import Perspective
import numpy as np
import pygame

@typeassert(_meshes = list, _perspective = Perspective, _object = Feature, _camera = Feature)

class Rendering(Structure):
    _field = ['_meshes','_perspective', '_object', '_camera']
    def __str__(self):
        return 'Rendering Initialization: ' \
               '\nMesh Features: {0._meshes}' \
               '\nCamera Feature: {0._camera} '\
               '\nObject Feature: {0._object}'.format(self)

    @property
    def transMatrix(self):
        return self._perspective.ProjectionMatrix@np.linalg.pinv(self._camera.featureWorldMatrix)\
               @self._object.featureWorldMatrix

    def __call__(self, originX=0.0, originY = 0.0):
        for mesh in self._meshes:
            vertices = np.column_stack((mesh._vertices, np.ones(len(mesh._vertices)))).T
            vPrime = self.transMatrix@vertices
            normalization = vPrime/np.where(vPrime[3]>1e-6,vPrime[3],1e-6)
            pixels2D = (normalization[:2]/normalization[2])
            x2D = (pixels2D[0] +1.0)* (self._perspective.width * 0.5) + originX
            y2D = (pixels2D[1] +1.0)* (self._perspective.height * 0.5) + originY
            points = np.array([x2D,y2D]).T
        return points

if __name__ == "__main__":
    kk = Mesh('./meshwriter/Drone.mesh')
    kk()
    meshes = []
    meshes.append(kk)
    Camera = Feature(_scale = (1.,1.,1.), _translate = (7.358,-6.925,4.958), _rotation = (0.773,0.334,0.539), _rotationAngle = 77.4)
    Object = Feature(_scale = (1.,1.,1.), _translate = (0.,0.,0.), _rotation = (0.,1.,0.),_rotationAngle = 0.)
    View = Perspective(40.,1., 100.,960, 540)
    temp = Rendering(meshes, View, Object,Camera)
    pts = temp()

    # PyGame for initialization process!

    pygame.init()
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    gameDisplay = pygame.display.set_mode((960, 540))
    gameDisplay.fill(black)
    pixAr = pygame.PixelArray(gameDisplay)

    for mesh in temp._meshes:
        for index, PointIndex in enumerate(mesh._facesVerticesIndex):
#            print("F{}:".format(index),pts[PointIndex],PointIndex)
            pygame.draw.polygon(gameDisplay, blue, pts[PointIndex])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
