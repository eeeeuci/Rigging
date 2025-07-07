import maya.cmds as cmds

def create_controller_for_joint(joint, shape='Circle'):
    base     = joint.split('|')[-1].replace('Jnt', 'Ctrl')
    ctrl_name = f"{base}_CTRL"
    grp_name  = f"{base}_GRP"

    if shape == 'Circle':
        ctrl = cmds.circle(name=ctrl_name, normal=[1,0,0], radius=1.5)[0]

    elif shape == 'Square':
        pts = [(-1,0,-1), (1,0,-1), (1,0,1), (-1,0,1), (-1,0,-1)]
        ctrl = cmds.curve(name=ctrl_name, degree=1, point=pts)

    elif shape == 'Cube':
        hs = 1.0
        pts = [
            (-hs,-hs,-hs),(hs,-hs,-hs),(hs,hs,-hs),(-hs,hs,-hs),(-hs,-hs,-hs),
            (-hs,-hs, hs),(hs,-hs, hs),(hs,hs, hs),(-hs,hs, hs),(-hs,-hs, hs),
            (-hs,-hs, hs),(-hs,-hs,-hs),(-hs,hs,-hs),(-hs,hs, hs),
            (hs,hs, hs),(hs,hs,-hs),(hs,-hs,-hs),(hs,-hs, hs)
        ]
        ctrl = cmds.curve(name=ctrl_name, degree=1, point=pts)

    else:
        cmds.error(f"Unknown shape '{shape}'")

    grp = cmds.group(ctrl, name=grp_name)
    pos = cmds.xform(joint, q=True, ws=True, t=True)
    rot = cmds.xform(joint, q=True, ws=True, ro=True)
    cmds.xform(grp, ws=True, t=pos)
    cmds.xform(grp, ws=True, ro=rot)

    cmds.setAttr(f"{ctrl}.translate", 0,0,0, type="double3")
    cmds.setAttr(f"{ctrl}.rotate",    0,0,0, type="double3")

    cmds.orientConstraint(ctrl, joint, maintainOffset=False)
    return ctrl, grp

def create_controllers_for_selected_joints(shape):
    joints = cmds.ls(selection=True, type='joint', long=True)
    if not joints:
        cmds.warning("Please select one or more joints.")
        return

    created = []
    for j in joints:
        ctrl, grp = create_controller_for_joint(j, shape)
        created.append(ctrl)

    cmds.select(created)
    cmds.inViewMessage(amg=f"✔ Created {len(created)} {shape} controller(s)",
                       pos='topCenter', fade=True)

def create_ui():
    if cmds.window("ctrlGenWin", exists=True):
        cmds.deleteUI("ctrlGenWin")
    win = cmds.window("ctrlGenWin", title="Controller Generator", widthHeight=(300, 150))
    cmds.columnLayout(adj=True, rowSpacing=10)

    cmds.text(label="Select joint(s) and controller shape", align="center")

    cmds.optionMenuGrp('shapeMenu', label="Shape:")
    cmds.menuItem(label="Circle")
    cmds.menuItem(label="Square")
    cmds.menuItem(label="Cube")

    cmds.button(label="Create Controllers", height=30,
        command=lambda *_: create_controllers_for_selected_joints(
            cmds.optionMenuGrp('shapeMenu', q=True, value=True)
        )
    )

    cmds.showWindow(win)

create_ui()