# While loop revision
# Eoin Lees
# Greatest common devider

a = 50
b = 20

while b > 0:
    '''Python method'''
    a, b = b, a % b
    '''Traditional Programming method'''
#   tmp = a
#   a = b
#   b = tmp % b

print(a)

