from base import Structure,typeassert
import numpy as np

@typeassert(fov=float, near= float, far = float, width = int, height = int)
class Perspective(Structure):
    _field = ['fov', 'near', 'far', 'width', 'height']
    def __str__(self):
        return 'Field of View is: {0.fov!s} \nNear surface is: {0.near!s} \nFar surface is: {0.far!s}' \
               ' \nScreen width: {0.width!s} \nScreen Height: {0.height!s}'.format(self)
    @property
    def aspect(self):
        return float(self.width/self.height)

    @property
    def elementMatrix00(self):
        return 1.0 / (self.aspect * np.tan(np.radians(self.fov) * 0.5))

    @property
    def elementMatrix11(self):
        return  1.0 / (np.tan(np.radians(self.fov) * 0.5))

    @property
    def elementMatrix22(self):
        return -((self.far + self.near) / (self.far - self.near))

    @property
    def elemenmtMatrix32(self):
        return -((2.0 * self.far * self.near) / (self.far - self.near))

    @property
    def ProjectionMatrix(self):
        return np.array([[self.elementMatrix00, 0.0, 0.0, 0.0], [0.0, self.elementMatrix11, 0.0, 0.0],
                [0.0, 0.0, self.elementMatrix22, self.elemenmtMatrix32], [0.0, 0.0, -1.0, 0.0]])

if __name__ == "__main__" :
    a = Perspective(40.,0.1, 100.,1920, 1080)
    print(a)
    print(a.ProjectionMatrix)