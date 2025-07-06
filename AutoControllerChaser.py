import maya.cmds as cmds

def create_controller_for_joint(joint, template_ctrl="myCustomCtrl"):
    base = joint.split('|')[-1].replace('Jnt', 'Ctrl')
    ctrl_name = f"{base}_CTRL"
    grp_name  = f"{base}_GRP"

    if not cmds.objExists(template_ctrl):
        cmds.error(f"Template controller '{template_ctrl}' does not exist in the scene.")

    ctrl = cmds.duplicate(template_ctrl, name=ctrl_name)[0]
    grp = cmds.group(ctrl, name=grp_name)

    pos = cmds.xform(joint, q=True, ws=True, t=True)
    rot = cmds.xform(joint, q=True, ws=True, ro=True)

    cmds.xform(grp, ws=True, t=pos)
    cmds.xform(grp, ws=True, ro=rot)

    cmds.setAttr(f"{ctrl}.translate", 0, 0, 0, type="double3")
    cmds.setAttr(f"{ctrl}.rotate", 0, 0, 0, type="double3")

    cmds.orientConstraint(ctrl, joint, maintainOffset=False)

    return ctrl, grp

def create_controllers_for_selected_joints(template_ctrl="myCustomCtrl"):
    joints = cmds.ls(selection=True, type='joint', long=True)
    if not joints:
        cmds.warning("Please select one or more joints.")
        return

    created = []
    for j in joints:
        ctrl, grp = create_controller_for_joint(j, template_ctrl)
        created.append(ctrl)

    cmds.select(created)
    cmds.inViewMessage(amg=f"✔ Created {len(created)} controller(s)", pos='topCenter', fade=True)

def create_ui():
    if cmds.window("ctrlGenWin", exists=True):
        cmds.deleteUI("ctrlGenWin")
    win = cmds.window("ctrlGenWin", title="Controller Generator", widthHeight=(300, 120))
    cmds.columnLayout(adj=True, rowSpacing=10)
    cmds.text(label="Select joint(s) and click the button below", align="center")
    cmds.textFieldGrp("templateCtrlField", label="Template Ctrl:", text="myCustomCtrl")
    cmds.button(label="Create Controllers", height=30,
                command=lambda *_: create_controllers_for_selected_joints(
                    cmds.textFieldGrp("templateCtrlField", q=True, text=True)))
    cmds.showWindow(win)

create_ui()