```
#路径选择
path0 = session.Path(name='Path-0', type=NODE_LIST, expression=(('BASE-1',(2,'26:16:-1',)),))
#直线路径
path1 = session.Path(name='Path-1', type=RADIAL, expression=((0,0,0), (0,0,1),(0,-1.0,0)), circleDefinition=ORIGIN_AXIS, numSegments=20, radialAngle=0,startRadius=0,endRadius=CIRCLE_RADIUS)
#环形路径
path2 = session.Path(name='Path-2', type=CIRCUMFERENTIAL, expression=((0,0,0), (0,0,1),(0,-1.0,0)), circleDefinition=ORIGIN_AXIS, numSegments=20,startAngle=0,endAngle=360,radius=CIRCLE_RADIUS)
```
