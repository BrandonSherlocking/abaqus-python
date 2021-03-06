
#创建xydata对象
xyData1 = session.XYData(data=((1,2),(2,4),(3,6),(4,8)), name='Data1',legendLabel='Data1',xValuesLabel='X', yValuesLabel='Y'

#打开文本文件生成对应的xydata对象
xyData2 = session.XYDataFromFile(fileName='dataFile.txt',name='Data2',xField=1,yField=3)

#沿路径的数据提取
myDatas = session.xyDataListFromField(odb=o, outputPosition=INTEGRATION_POINT,variable=(('S', INTEGRATION_POINT,((INVARIANT, 'Mises'),)),), elementLabels=(('BALL-1', (16,17, )), ('BASE-1', (46,91, )), ))

#沿着路径myPath的Mises应力数据（includeIntersections插值计算，true的话有31个点，false的话21个）
myPath = session.Path(name='myPath', type=RADIAL, expression=((0,0,0), (0,0,1), (0,-3.0,0)), circleDefinition=ORIGIN_AXIS, numSegments=20, radialAngle=0, startRadius=0, endRadius=CIRCLE_RADIUS)

myData = session.XYDataFromPath(path=myPath, shape=UNDEFORMED, labelType=TRUE_DISTANCE, includeIntersections=True, name='myData', variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'),)),))

