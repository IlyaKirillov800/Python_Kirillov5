import bpy
import math

# Удаление исходного куба
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Cube'].select_set(True)
bpy.ops.object.delete()

# Функция для создания фигур
def create_shape(shape_type, size_x, size_y, size_z, position):
    bpy.ops.mesh.primitive_cube_add(size=1, location=position)
    obj = bpy.context.active_object
    obj.scale = (size_x, size_y, size_z)
    mat = bpy.data.materials.get('Material')
    if mat is not None:
        obj.data.materials.append(mat)
    return obj

# Создание фигур A, B, C
for i, shape in enumerate(['A', 'B', 'C'], start=1):
    base = 1.0
    size_x = base - (i**2) * 0.05
    size_y = base - (i**2) * 0.05
    size_z = 0.25
    position = (0, 0, i * 0.25)
    create_shape(shape, size_x, size_y, size_z, position)

# Создание анимации вращения фигуры C в фигуру D
frames = 10
frame_num = 0
for frame in range(frames + 1):
    bpy.context.scene.frame_set(frame_num)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['C'].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['C']
    bpy.ops.object.keyframe_insert(data_path="rotation_euler", index=-1)
    bpy.context.active_object.rotation_euler = (0, 0, 0)
    bpy.ops.object.keyframe_insert(data_path="rotation_euler", index=-1)
    bpy.context.active_object.rotation_euler = (math.radians(frame * 36), 0, 0)
    bpy.ops.object.keyframe_insert(data_path="rotation_euler", index=-1)
    frame_num += 10
