
import bpy

from bpy.types import Panel

class BMD_PT_Panel(Panel):
    bl_label = "Scene Objects"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Blend-A-Med"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Add a property to hold the output directory path
        layout.prop(context.scene, "export_directory")
        topColumn = layout.column()

        for obj in scene.objects:
            box = topColumn.box()
            box.label(text=obj.name)

            column = box.column()

            ep1 = column.operator("bmd.export_object", text="Export {} as obj".format(obj.name))
            ep1.obj_name = obj.name
            ep1.type = "OBJ"
            ep1.export_directory = scene.export_directory
            ep2 = column.operator("bmd.export_object", text="Export {} as fbx".format(obj.name))
            ep2.obj_name = obj.name
            ep2.type = "FBX"
            ep2.export_directory = scene.export_directory
            ep3 = column.operator("bmd.export_object", text="Export {} as stl".format(obj.name))
            ep3.obj_name = obj.name
            ep3.type = "STL"
            ep3.export_directory = scene.export_directory
