import numpy as np
from base import Structure,typeassert

@typeassert(meshFilePath = str, _vertices = list, _facesVerticesIndex = list,_facesVerticesCoordinates = list)
class Mesh:
    def __init__(self, MeshFilePath, vertices=None,facesVerticesIndex = None, facesVerticesCoordinates = None):
        self.meshFilePath = MeshFilePath
        if vertices is None:
            vertices = []
        if facesVerticesIndex is None:
            facesVerticesIndex = []
        if facesVerticesCoordinates is None:
            facesVerticesCoordinates = []
        self._vertices = vertices
        self._facesVerticesIndex  = facesVerticesIndex
        self._facesVerticesCoordinates = facesVerticesCoordinates

    def __call__(self):
        with open(self.meshFilePath, 'rt') as f:
            for line in f:
                name, *data = line.split(',')
                if name.startswith('v'):
                    self._vertices.append([float(x) for x in data])
                elif name.startswith('f'):
                    self._facesVerticesIndex.append([int(x) for x in data])
                    self._facesVerticesCoordinates.append([self._vertices[int(x)] for x in data])
                else:
                    raise Exception("Only f (face connectivity) and v (vertices) at the beginning can be loaded!")
        f.close()

    def __str__(self):
        return 'This mesh is totally composed by {} faces, and {} vertices.'\
            .format((len(self._facesVerticesIndex)),(len(self._vertices)))

if __name__ == "__main__":
    kk = Mesh('./meshwriter/test.mesh')
    kk()
#    print(kk._vertices)
    print(kk._facesVerticesIndex)
#    print(kk._facesVerticesCoordinates)
    print(kk)