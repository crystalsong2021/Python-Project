# create a list
# you can create a list of numbers automatically using a range.
x = list(range(1,10))
print(x)

# you can also specify a step as third argument
y = list(range(1,10,3))
print(y)

#Create complex List
"""
Assign list o variable rainfall
"""

rainfall = [10.1, 9, "no data", [1,2,3]]
print('Before removing-->', rainfall)
rainfall.remove('no data')
print('After removing-->',rainfall)