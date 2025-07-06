import maya.cmds as cmds 

jointNameList = cmds.ls(selection=True)

for jointName in JointNameList:
    print Jointname
    
    creationController = cmds.circle(center=(0,0,0), normal1=(0,1,0), sweep=360, radius=1, degree=3,
                                  useTolertance=False, tolerance=0, sections=8, constructionHistory=False, name=JointName+"_FK")
    print createController[0]                              
    
    controllerGroupName = cmds.group(createController[0], name=creatController[0]+"_POS")
    print controllerGroupName
    
    positionConstraint = cmds.parentConstraint(jointName, controllerGroupName, Weight=1)
    print positionConstraint[0]
    
    cmds.delete(positionConstraint[0])
    
    cmds.parentConstraint(createController[0], jointName, maintainOffset=True, weight =1)
    cmds.scaleConstraint(createController[0], jointName,maintainOffset=True, weight =1)
    
   