from base import typeassert, Structure
from featureMatrix import Feature
from mesh import Mesh
from perspective import Perspective
from rendering import Rendering
import pygame
import numpy as np

@typeassert(_render = Rendering, _fps = float )
class Animation(Structure):
    _field = ['_render', '_fps']
    def __str__(self):
        return "Animation Process Begins {0._render!s}: ".format(self)
    @property
    def blue(self):
        return (0, 0, 255)
    @property
    def red(self):
        return (255, 0, 0)
    @property
    def green(self):
        return (0,255,0)
    @property
    def black(self):
        return (0, 0 ,0)
    @property
    def white(self):
        return (255,255,255)

    def __call__(self):
        pygame.init()
        gameDisplay = pygame.display.set_mode((self._render._perspective.width,self._render._perspective.height))
        pygame.display.set_caption('Model Animation with Python')
        Icon = pygame.image.load('./meshwriter/earth.png')
        pygame.display.set_icon(Icon)
        step = 0.0
        CameraRadius = 20.
        clock = pygame.time.Clock()
        while True:
            gameDisplay.fill(self.white)
            degrees = step * 6.
            radians = np.radians(degrees)
            cameraY, cameraZ = np.cos(radians) * CameraRadius, np.sin(radians) * CameraRadius

            Camera = Feature(_scale=(1., 1., 1.), _translate=(0., cameraY, cameraZ),
                             _rotation=(1.0, 0., 0.), _rotationAngle=degrees + 270)
            Object = Feature(_scale=(1., 1., 1.), _translate=(0., 0., 0.), _rotation=(0., 1., 0.),
                             _rotationAngle=degrees)
            temp = Rendering(meshes, View, Object, Camera)
            pts = temp()
            for mesh in self._render._meshes:
                for index, PointIndex in enumerate(mesh._facesVerticesIndex):
                    pygame.draw.polygon(gameDisplay, self.red, pts[PointIndex])
            step += 1.0
            clock.tick(self._fps)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


if __name__=="__main__":
    kk = Mesh('./meshwriter/Drone.mesh')
    kk()
    meshes = []
    meshes.append(kk)
    Camera = Feature(_scale = (1.,1.,1.), _translate = (7.358,-6.925,4.958), _rotation = (0.773,0.334,0.539), _rotationAngle = 77.4)
    Object = Feature(_scale = (1.,1.,1.), _translate = (0.,0.,0.), _rotation = (0.,1.,0.),_rotationAngle = 0.0)
    View = Perspective(40.,1., 100.,960, 540)
    temp = Rendering(meshes, View, Object,Camera)
    pts = temp()
    animation = Animation(temp, _fps = 60.0)
    animation()
