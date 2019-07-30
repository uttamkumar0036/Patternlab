#n = int(input('Enter Sample Number'))
n = 3
#training_ = []
training_ = [
    [66, 60, 'N'],
    [66, 78, 'O'],
    [66, 50, 'U']
]
#for i in range(n):
#    height_ = int(input('Enter Height: '))
#    weight_ = int(input('Enter Weight: '))
#    class_ = input('Enter Class: ')
#    training_.append([height_, weight_, class_])

#testing_ = []
testing_ = [66, 60]
#height_ = int(input('Enter Height: '))
#weight_ = int(input('Enter Weight: '))
#testing_.append(height_)
#testing_.append(weight_)

feature_ = {}
for i in range(n):
    cityBlockDistance = abs(training_[i][0] - testing_[0]) + abs(training_[i][1] - testing_[1])
    feature_[i] = cityBlockDistance

sortedFeature = sorted(feature_.items(), key = lambda kv:(kv[1], kv[0]) )
index = sortedFeature[0][0]
print(training_[index][2])
