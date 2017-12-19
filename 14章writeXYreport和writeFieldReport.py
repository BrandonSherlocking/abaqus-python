#对应的xydata对象mydata输入到对应的文件中
myData = session.XYData(name='myData', data = ((1,2), (2,4), (3,6), (4,8))
from abaqusConstants import *
session.xyReportOptions.setValues(pageWidth=60, numDigits=6, totals=True, minMax=True, pageWidthLimited=SPECIFY, numberFormat=ENGINEERING)
session.writeXYReport(fileName='data.txt', xyData=myData)



#建立一个显示组对象
from abaqus import *
from abaqusConstants import *
vp = session.Viewport(name='myViewport', origin=(0, -30))
o = session.openOdb(name='HertzContact.odb', readOnly=True)
vp.setValues(displayedObject=1)
import displayGroupOdbToolset as dGO
myLeaf = dGO.LeafFromModelElemLabels(elementLabels=(('BAIL-1', ('1:40;1', )), ))
vp.view.fitView()
