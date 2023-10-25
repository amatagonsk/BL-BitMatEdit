bl_info = {
    "name": "bit Mat Edit [toolbar]",
    "author": "amatagonsk",
    "version": (0, 3),
    "blender": (3, 0, 0),
    "location": "View3D > Tool Shelf > bit Mat Edit",
    "description": "bit materials bit edit",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Material"
}

import bpy, re#, os#, subprocess
from bpy.props import *


#Shadeless
class Shadeless_on(bpy.types.Operator):
    bl_description = 'slct mat Shadeless'
    bl_idname = 'shadeless.on'
    bl_label = 'Shadeless_on'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            for M_slt in S_obj.material_slots:
                M_slt.material.use_shadeless = True

        return {'FINISHED'}

class Shadeless_off(bpy.types.Operator):
    bl_description = 'all mat Shadeless off'
    bl_idname = 'shadeless.off'
    bl_label = 'Shadeless_off'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            for M_slt in S_obj.material_slots:
                M_slt.material.use_shadeless = False
        return {'FINISHED'}

# |> RUN
class RUN_diffuse(bpy.types.Operator):
    bl_description = 'enter value diffuse'
    bl_idname = 'run.diffuse'
    bl_label = 'RUN_diffuse'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            for M_slt in S_obj.material_slots:
                M_slt.material.diffuse_intensity = context.scene.bm_diffuse
        return {'FINISHED'}



class RUN_Emit(bpy.types.Operator):
    bl_description = 'enter value Emit'
    bl_idname = 'run.emit'
    bl_label = 'RUN_Emit'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            for M_slt in S_obj.material_slots:
                M_slt.material.emit = context.scene.bm_Emit
        return {'FINISHED'}



class RUN_specular(bpy.types.Operator):
    bl_description = 'enter value specular'
    bl_idname = 'run.specular'
    bl_label = 'RUN_specular'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            for M_slt in S_obj.material_slots:
                M_slt.material.specular_intensity = context.scene.bm_specular

        return {'FINISHED'}



class RUN_rename_ArmObj(bpy.types.Operator):
    bl_description = 'RUN_rename_ArmObj'
    bl_idname = 'rename.armobj'
    bl_label = 'Rename_ArmObj'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            if "Armature" in S_obj.modifiers.keys():
                S_obj.modifiers['Armature'].object = bpy.data.objects["%s" % context.scene.bm_RenameArm]
            else:
                pass
        return {'FINISHED'}



class Opensubdiv_on(bpy.types.Operator):
    bl_description = 'opensubdiv_on'
    bl_idname = 'opensubdiv.on'
    bl_label = 'Opensubdiv_on'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            if "Subsurf" in S_obj.modifiers.keys():
                S_obj.modifiers['Subsurf'].use_opensubdiv = True
            else:
                pass
        return {'FINISHED'}


class Opensubdiv_off(bpy.types.Operator):
    bl_description = 'opensubdiv_off'
    bl_idname = 'opensubdiv.off'
    bl_label = 'Opensubdiv_off'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            if "Subsurf" in S_obj.modifiers.keys():
                S_obj.modifiers['Subsurf'].use_opensubdiv = False
            else:
                pass
        return {'FINISHED'}



class Append_Flipvertex(bpy.types.Operator):
    bl_description = 'append_Flipvertex'
    bl_idname = 'appende.flipvertex'
    bl_label = 'Append_Flipvertex'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            print("\n====== %s ======\n"%S_obj.name)
            for V_grp in S_obj.vertex_groups.keys():
                if re.match(r".*\.L$",V_grp):
                    L2R = re.sub(r".L$", '.R',V_grp)
                    print ("'%s' from '%s'" %(L2R, V_grp))
                    S_obj.vertex_groups.new(name="%s"%L2R)
                else:
                    pass
            print("\n==================")
        return {'FINISHED'}


class SbdvLevel_View(bpy.types.Operator):
    bl_description = 'subdiv_view'
    bl_idname = 'subdiv.view'
    bl_label = 'subdiv_view'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            if "Subdivision" in S_obj.modifiers.keys():
                S_obj.modifiers['Subdivision'].levels = context.scene.bm_Sbdv_view
            else:
                pass
        return {'FINISHED'}

class SbdvLevel_Render(bpy.types.Operator):
    bl_description = 'subdiv_render'
    bl_idname = 'subdiv.render'
    bl_label = 'subdiv_render'

    def execute(self, context):
        for S_obj in bpy.context.selected_objects:
            if "Subdivision" in S_obj.modifiers.keys():
                S_obj.modifiers['Subdivision'].render_levels = context.scene.bm_Sbdv_render

            else:
                pass
        return {'FINISHED'}


class BMP_PT_bit_mat_edit(bpy.types.Panel):
    bl_label = "bit Mat Edit"
    bl_idname = 'BMP_PT_bit_mat_edit'
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = "bit Mat Edit"


    bpy.types.Scene.bm_diffuse = bpy.props.FloatProperty(
        name = "Diffuse",
        description="difuse",
        default=0.8,
        min=0.0,
        max=1.0)

    bpy.types.Scene.bm_specular = bpy.props.FloatProperty(
        name = "Specular",
        description="specular",
        default=0.5,
        min=0.0,
        max=1.0)

    bpy.types.Scene.bm_Emit = bpy.props.FloatProperty(
        name = "Emit",
        description="Emit",
        default=0,
        min=0.0,
        max=2.0)

    bpy.types.Scene.bm_Sbdv_view = bpy.props.IntProperty(
        name = "Subdiv_View",
        description="Subdiv_View",
        default=0,
        min=0,
        max=6)

    bpy.types.Scene.bm_Sbdv_render = bpy.props.IntProperty(
        name = "Subdiv_Render",
        description="Subdiv_Render",
        default=0,
        min=0,
        max=6)

    bpy.types.Scene.bm_RenameArm = bpy.props.StringProperty(
        name = "",
        )

    def draw(self,context):
        layout = self.layout
        scene = context.scene

        row = layout.row(align=True)
        row.label(text="material",icon="MATERIAL_DATA")

        col = layout.column(align=True)
        row = col.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("object.shade_smooth")
        row.operator("object.shade_flat")

        # row = col.row(align=True)
        # row.alignment = 'EXPAND'
        # row.operator("Shadeless.on", text="Shadeless")
        # row.operator("Shadeless.off", text="off")

# -----
        col = layout.column(align=True)

        # # eevee not work (for 2.x)
        # #diffuse
        # row = col.row(align=True)
        # row.prop(scene, "bm_diffuse", slider=True)
        # row.operator("run.diffuse",text="",icon="MATSPHERE")

        # # spec
        # row = col.row(align=True)
        # row.prop(scene, "bm_specular", slider=True)
        # row.operator("run.specular",text="",icon="BRUSH_TEXFILL")

        # #emi
        # row = col.row(align=True)
        # row.prop(scene, "bm_Emit", slider=True)
        # row.operator("run.emit",text="",icon="LIGHT_SUN")

# ============== modifire

        # row = layout.row(align=True)
        col = layout.column(align=True)
        col.label(text="modifire",icon="OBJECT_DATA")

        # # Osubdiv not work (for 2.x)
        # row = col.row(align=True)
        # # row.alignment = 'EXPAND'
        # row.operator("opensubdiv.on", text="opensubdiv", icon="MOD_SUBSURF")
        # row.operator("opensubdiv.off", text="off")

        # Append flipVetex
        col.operator("appende.flipvertex", text="make Flipvertex '*.R'", icon="MESH_DATA")

        #bone
        # row = col.row(align=True)
        row = layout.row(align=True)
        row.prop(scene, "bm_RenameArm", icon="OUTLINER_OB_ARMATURE", text="rig")
        row.operator("rename.armobj",text="",icon="MOD_ARMATURE")

# ----
        col = layout.column(align=True)
        #diffuse
        row = col.row(align=True)
        row.prop(scene, "bm_Sbdv_view")
        row.operator("subdiv.view",text="",icon="PLAY")


        row = col.row(align=True)
        row.prop(scene, "bm_Sbdv_render")
        row.operator("subdiv.render",text="",icon="PLAY")


        # row = layout.column(align=False)
# ----
        col = layout.column(align=True)
        row = col.row(align=True)

        # simplify
        rd = context.scene.render
        row.prop(rd, "use_simplify", text="Simplify")
        col.prop(rd, "simplify_subdivision", text="Subdivision")
        col.prop(rd, "simplify_child_particles", text="Child Particles")



#    Registration
classes = [
    # Shadeless_on,
    # Shadeless_off,
    BMP_PT_bit_mat_edit,
    RUN_diffuse,
    RUN_Emit,
    RUN_specular,
    RUN_rename_ArmObj,
    # Opensubdiv_on,
    # Opensubdiv_off,
    Append_Flipvertex,
    SbdvLevel_Render,
    SbdvLevel_View,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
