import rhino3dm
import random

model = rhino3dm.File3dm()

for i in xrange(20):
    pt = rhino3dm.Point3d(
        random.randint(0,10), random.randint(0,10), random.randint(0,10))
    model.Objects.AddPoint(pt)


model.Write("add_random_points.3dm", 5)
