# Reading co-ordinates
x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

# Calculating distance
d = ( (x2-x1)**2 + (y2-y1)**2 ) ** 0.5

# Displaying result
print('Distance = %f' %(d))
