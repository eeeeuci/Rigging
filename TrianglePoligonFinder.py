import maya.cmds as cmds

_last_detected_faces = []

def get_triangle_faces(shape):
    triangle_faces = []
    info = cmds.polyInfo(shape, faceToVertex=True)
    if not info:
        return triangle_faces

    for line in info:
        parts = line.strip().split(':')
        if len(parts) != 2:
            continue
        face_id = int(parts[0].split()[1])
        verts = parts[1].strip().split()
        if len(verts) == 3:
            triangle_faces.append(f"{shape}.f[{face_id}]")

    return triangle_faces

def get_adjacent_faces_from_triangles(triangle_faces):
    if not triangle_faces:
        return []

    edges = cmds.polyListComponentConversion(triangle_faces, fromFace=True, toEdge=True)
    edges = cmds.filterExpand(edges, selectionMask=32) or []

    adjacent_faces = cmds.polyListComponentConversion(edges, fromEdge=True, toFace=True)
    adjacent_faces = cmds.filterExpand(adjacent_faces, selectionMask=34) or []

    all_faces = set(adjacent_faces)
    all_faces.update(triangle_faces)
    return list(all_faces)

def highlight_faces_with_material(faces, mat_name="triangleHighlight_mat"):
    if not faces:
        return

    if not cmds.objExists(mat_name):
        shader = cmds.shadingNode("lambert", asShader=True, name=mat_name)
        sg = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=f"{mat_name}SG")
        cmds.connectAttr(f"{shader}.outColor", f"{sg}.surfaceShader", force=True)
        cmds.setAttr(f"{shader}.color", 1, 0, 0, type="double3")
    else:
        sg = f"{mat_name}SG"

    cmds.sets(faces, edit=True, forceElement=sg)

def isolate_faces(faces):
    panel = cmds.getPanel(withFocus=True)
    if not cmds.modelEditor(panel, query=True, exists=True):
        cmds.warning("No active model panel found.")
        return

    cmds.selectMode(component=True)
    cmds.selectType(facet=True)
    cmds.select(faces, replace=True)

    cmds.isolateSelect(panel, state=True)
    cmds.isolateSelect(panel, addSelected=True)

def unisolate_view():
    panel = cmds.getPanel(withFocus=True)
    if cmds.modelEditor(panel, query=True, exists=True):
        cmds.isolateSelect(panel, state=False)
        cmds.inViewMessage(amg="🔓 Unisolated view", pos='topCenter', fade=True)

def select_triangles_and_neighbors(mesh=None):
    global _last_detected_faces
    if not mesh:
        sel = cmds.ls(selection=True, dag=True, type='transform')
        if not sel:
            cmds.warning("Please select a mesh object.")
            return 0, None
        mesh = sel[0]

    shapes = cmds.listRelatives(mesh, shapes=True, fullPath=True)
    if not shapes:
        cmds.warning("No shape node found under transform.")
        return 0, None
    shape = shapes[0]

    triangle_faces = get_triangle_faces(shape)
    all_faces = get_adjacent_faces_from_triangles(triangle_faces)

    if all_faces:
        _last_detected_faces = all_faces
        highlight_faces_with_material(all_faces)
        isolate_faces(all_faces)
    else:
        cmds.select(clear=True)
        _last_detected_faces = []

    return len(triangle_faces), mesh

def select_detected_faces():
    global _last_detected_faces
    if _last_detected_faces:
        cmds.selectMode(component=True)
        cmds.selectType(facet=True)
        cmds.select(_last_detected_faces, replace=True)
        cmds.inViewMessage(amg="🔺 Faces re-selected", pos='topCenter', fade=True)
    else:
        cmds.warning("No detected faces to select.")

def show_result_popup(triangle_count):
    if cmds.window("triangleResultWin", exists=True):
        cmds.deleteUI("triangleResultWin")
    win = cmds.window("triangleResultWin", title="Triangle Result", widthHeight=(250, 130))
    cmds.columnLayout(adj=True, rowSpacing=10)
    if triangle_count > 0:
        msg = f"🔺 Found {triangle_count} triangle(s) + neighbors isolated!"
        cmds.text(label=msg, align="center", height=40)
        cmds.button(label="Select Faces", height=30,
                    command=lambda *_: select_detected_faces())
    else:
        cmds.text(label="✅ No triangles found.", align="center", height=40)
    cmds.button(label="OK", command=lambda *_: cmds.deleteUI(win))
    cmds.showWindow(win)

def run_triangle_check():
    count, _ = select_triangles_and_neighbors()
    show_result_popup(count)

def create_triangle_checker_ui():
    if cmds.window("triCheckerWin", exists=True):
        cmds.deleteUI("triCheckerWin")
    win = cmds.window("triCheckerWin", title="Triangle Checker", widthHeight=(300, 140))
    cmds.columnLayout(adj=True, rowSpacing=10)
    cmds.text(label="Select a mesh and click the button below", align="center")
    cmds.button(label="Search Triangle", height=30,
                command=lambda *_: run_triangle_check())
    cmds.button(label="Unisolate View", height=30,
                command=lambda *_: unisolate_view())
    cmds.showWindow(win)

create_triangle_checker_ui()