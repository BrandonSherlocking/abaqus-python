```# 打开odb文件（不显示任何东西）
o = session.openOdb(name='dianjiec.odb', readOnly=False)
#需要更新一下，
abaqus -upgrade -job <newHertz> -odb <HertzContact>

# 打开多个odb文件
oo = session.openOdbs(name='HertzContact0.odb','HertzContact1.odb')

#打开窗口，赋予参数
myViewport = session.Viewport(name='myViewport',border=ON,titleBar=ON,titleStyle=CUSTOM, customTitleString='Viewport Example; Hertz Contact')

#最小化窗口viewport：1,和恢复窗口myViewport
session.viewports['Viewport: 1'].minimize()

#修改窗口大小，并移动（origin(原点)）到指定点
myViewport.setValues(width=150, height=100, origin=(0,-30))

#显示项目（object）=========出错了，？？？
myViewport.setValues(displayedObject=0)
TypeError: displayedObject; 已找到 int, 应当提供 type
#修改，那里不是0是o
myViewport.setValues(displayedObject=o)

#显示应力（直接gui操作，不需要再敲一串代码）
from abaqusConstants import *
myViewport.odbDisplay.setPrimaryVariable(variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 'Mises'))
myViewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))


#======修改云图色标和数值，去掉下端描述性文字！！！！！很重要======
myViewport.odbDisplay.contourOptions.setValues(intervalType=LOG,spectrum='White to black')  #设置色标为对数型，采用灰度

myViewport.odbDisplay.commonOptions.setValues(deformationScaling=UNIFORM, uniformScaleFactor=1, visibleEdges=FEATURE)  #去掉网格和设置变形系数为1

myViewport.viewportAnnotationOptions.setValues(triad=ON,state=OFF,annotations=OFF,title=OFF,legendDecimalPlaces=0,legendNumberFormat=FIXED,legendBox=OFF) # 去掉一些不必要的信息，重新设置色标卡的数值显示模式。


#轴对称模型拓展显示
myViewport.odbDisplay.basicOptions.setValues(sweepElem=ON, sweepStartAngleElem=10, sweepEndAngleElem=120)

#旋转模型（绕y轴旋转30度并适应屏幕）
myViewport.view.rotate(yAngle=30)
myViewport.view.fitView()

#改变观测角度
myViewport.view.setViewpoint(viewVector=(1,1,1))
myViewport.view.fitView()```
