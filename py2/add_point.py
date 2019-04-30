import rhino3dm

pt = rhino3dm.Point3d(1,2,3)

model = rhino3dm.File3dm()
model.Objects.AddPoint(pt)

model.Write("add_point.3dm", 5)
