import bpy

selected_object = bpy.context.active_object

if selected_object is not None:
    vertex_group_names = [group.name for group in selected_object.vertex_groups]
    vertex_groups_string = "\n".join(vertex_group_names)

    bpy.context.window_manager.clipboard = vertex_groups_string

    print("Vertex group names copied to clipboard")
    print(vertex_groups_string)
else:
    print("No active object selected")
