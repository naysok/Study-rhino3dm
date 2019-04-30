import rhino3dm
import random


model = rhino3dm.File3dm()

for i in xrange(10):
    pt = rhino3dm.Point3d(
        random.randint(0,10), random.randint(0,10), 0)
    circle = rhino3dm.Circle(pt, float(random.randint(0,5)))
    model.Objects.AddCircle(circle)


model.Write("add_random_circles.3dm", 5)
