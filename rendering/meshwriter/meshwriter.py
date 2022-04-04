import bpy

mesh = bpy.context.active_object
faces = mesh.data.polygons
loops = mesh.data.loops
vertices = mesh.data.vertices

file = open(bpy.path.abspath('//%s.mesh'%(mesh.name)), 'w')
for v in vertices:
    file.write('v, %s, %s, %s\n'%(v.co.x, v.co.y, v.co.z))

for f in faces:
    vertexids = [str(loops[lid].vertex_index) for lid in f.loop_indices]
    file.write('f, %s\n'%(', '.join(vertexids)))
    

file.close()