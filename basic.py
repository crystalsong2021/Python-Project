from re import X


x = 10
y = "10"

sum1 = x + x
print ("sum1", sum1)
sum2 = y + y
print ("sum2", sum2)

print(str(sum1) + sum2) # change to string to match the type ("20"+"1010")= "201010"
print(sum1 + int(sum2)) # change to int to sum2 (20 + 1010) = 1030