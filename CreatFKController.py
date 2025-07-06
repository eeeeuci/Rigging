import maya.cmds as cmds

jointNameList = cmds.ls(selection=True)

for jointName in jointNameList:
    print(jointName)
    
    createController = cmds.circle(
        center=(0, 0, 0),
        normal=(0, 1, 0),
        sweep=360,
        radius=1,
        degree=1,
        useTolerance=False,
        tolerance=0,
        sections=8,
        constructionHistory=False,
        name=jointName + "_FK"
    )
    print(createController[0])
    
    controllerGroupName = cmds.group(
        createController[0],
        name=createController[0] + "_POS"
    )
    print(controllerGroupName)
    positionConstraint = cmds.parentConstraint(
        jointName,
        controllerGroupName,
        weight=1
    )
    print(positionConstraint[0])
    cmds.delete(positionConstraint[0])
    cmds.parentConstraint(
        createController[0],
        jointName,
        maintainOffset=True,
        weight=1
    )
    cmds.scaleConstraint(
        createController[0],
        jointName,
        maintainOffset=True,
        weight=1
    )