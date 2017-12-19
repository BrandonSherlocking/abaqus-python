#绘制xydata数据
myXYPlot = session.XYPlot(name='myXYPlot')
chartName = myXYPlot.charts.keys()[0]
chart = myXYPlot.charts[chartName]
myCurve = session.Curve(xyData=myData)
chart.setValues(curvesToPlot=(myCurve,),)
myViewport.setValues(displayedObject=myXYPlot)
