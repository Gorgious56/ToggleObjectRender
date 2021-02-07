bl_info = {
    "name": "Toggle Object Render",
    "blender": (2, 80, 0),
    "category": "Object",	
    "version": (0, 1, 0),
    "author":"Gorgious56",
    "description":"Add a toggle in the object properties to quicly set the object as Rendered/Not rendered",
}

import bpy


class ToggleRenderPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Render"
    bl_idname = "OBJECT_RENDER_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None        

    def draw(self, context):
        self.layout.operator(ToggleObjectRender.bl_idname, text="Render Me" if context.active_object.hide_render else "Don't Render Me")


def toggle_render(obj):
    toggle = obj.hide_render
    obj.hide_render = not toggle
    obj.cycles_visibility.camera = toggle
    obj.cycles_visibility.diffuse = toggle
    obj.cycles_visibility.glossy = toggle
    obj.cycles_visibility.transmission = toggle
    obj.cycles_visibility.scatter = toggle
    obj.cycles_visibility.shadow = toggle
    
    obj.display_type = 'TEXTURED' if toggle else 'WIRE'


class ToggleObjectRender(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.toggle_render"
    bl_label = "Toggle Render"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        toggle_render(context.active_object)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ToggleObjectRender)
    bpy.utils.register_class(ToggleRenderPanel)


def unregister():
    bpy.utils.unregister_class(ToggleRenderPanel)
    bpy.utils.unregister_class(ToggleObjectRender)


if __name__ == "__main__":
    register()


