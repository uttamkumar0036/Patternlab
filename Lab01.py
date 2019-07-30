import numpy


print("Input the number of sample data")

n = int(input("No. of sample data: "))

print("Input the values of Height,Weight & Class type for sample data:")

sampleHt = []
sampleWt = []
sampleCls = []

for i in range(n):
    Ht = float(input())
    Wt = float(input())
    cls = input()

    sampleHt.append(Ht)
    sampleWt.append(Wt)
    sampleCls.append(cls)

print("Now input the values of Height & Weight for test data!")

testHt=float(input())
testWt=float(input())

minDistance=numpy.sqrt((testHt - sampleHt[0])**2 + (testWt - sampleWt[0])**2)



output=sampleCls[0]

for h,w,c in zip(sampleHt,sampleWt,sampleCls):
    euclideanDistance = numpy.sqrt((h - testHt)**2 + (w - testWt)**2)

    if euclideanDistance < minDistance:
        minDistance = euclideanDistance

        output=c

print('The class is:')
print(output)


