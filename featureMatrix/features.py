from base import Structure, typeassert
import numpy as np

@typeassert(_scale = tuple, _rotation = tuple, _translate = tuple, _rotationAngle = float)
class Feature(Structure):
    _field = ['_scale','_translate','_rotation','_rotationAngle']
    def __str__(self):
        return 'Feature Matrix Initialization with: \nScale Vector: {0._scale!s} ' \
               '\nTranslate Vector: {0._translate!s} \nRotation Vector: {0._rotation!s}'.format(self)

    @property
    def scaleMatrix(self):
        return np.array([[self._scale[0], 0.0, 0.0, 0.0], [0.0, self._scale[1], 0.0, 0.0],
                               [0.0, 0.0, self._scale[2], 0.0], [0.0, 0.0, 0.0, 1.0]])

    @property
    def translateMatrix(self):
        return np.array([[1.0, 0.0, 0.0, self._translate[0]], [0.0, 1.0, 0.0, self._translate[1]],
                                   [0.0, 0.0, 1.0, self._translate[2]], [0.0, 0.0, 0.0, 1.0]])

    def rotateMatrix(self):
        angle = np.radians(self._rotationAngle)
        ca = np.cos(angle)
        sa = np.sin(angle)
        C = 1 - ca
        x, y, z = self._rotation[0], self._rotation[1], self._rotation[2]
        xs = x * sa
        ys = y * sa
        zs = z * sa
        xC = x * C
        yC = y * C
        zC = z * C
        xyC = x * yC
        yzC = y * zC
        zxC = z * xC
        # Fill the axis-angle matrices with the correct values
        mat00 = x * xC + ca
        mat01 = xyC - zs
        mat02 = zxC + ys
        mat10 = xyC + zs
        mat11 = y * yC + ca
        mat12 = yzC - xs
        mat20 = zxC - ys
        mat21 = yzC + xs
        mat22 = z * zC + ca
        return np.array([[mat00, mat01, mat02, 0.], [mat10, mat11, mat12, 0.],
                       [mat20, mat21, mat22, 0.], [0.0, 0.0, 0.0, 1.0]])



    @property
    def featureWorldMatrix(self):
        return self.translateMatrix @ self.rotateMatrix() @ self.scaleMatrix

if __name__ == "__main__":
    f = Feature(_scale = (1.,1.,1.), _translate = (1.,2.,3.), _rotation = (1.,2.,3.), _rotationAngle = 70.)
    print(f)
    print("world Matrix :", f.featureWorldMatrix)


"""
    def rotateMatrix(self):
        attitude, heading, bank = self._rotation[2],self._rotation[1],self._rotation[0]
        c1,c2,c3 = np.cos(np.radians(heading) * 0.5),np.cos(np.radians(attitude) * 0.5),np.cos(np.radians(bank) * 0.5)
        s1,s2,s3 = np.sin(np.radians(heading) * 0.5),np.sin(np.radians(attitude) * 0.5),np.sin(np.radians(bank) * 0.5)
        angle = 2.0 * np.arccos(c1 * c2 * c3 - s1 * s2 * s3)
        x,y,z = (s1 * s2 * c3) + (c1 * c2 * s3),(s1 * c2 * c3) + (c1 * s2 * s3),(c1 * s2 * c3) - (s1 * c2 * s3)
        ca,sa = np.cos(angle),np.sin(angle)
        C = 1 - ca
        # Multiplications (to remove duplicate calculations).
        xs,ys,zs = x * sa, y * sa, z * sa
        xC,yC,zC = x * C, y*C, z*C
        xyC,yzC,zxC = x * yC,y * zC,z * xC

        mat00, mat01,mat02 = x * xC + ca, xyC - zs, zxC + ys
        mat10, mat11,mat12 = xyC + zs,y * yC + ca, yzC - xs
        mat20, mat21,mat22 = zxC - ys,yzC + xs,z * zC + ca

        return np.array([[mat00, mat01, mat02, 0.], [mat10, mat11, mat12, 0.],
                       [mat20, mat21, mat22, 0.], [0.0, 0.0, 0.0, 1.0]])"""



