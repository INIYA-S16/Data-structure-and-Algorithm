numbers = [22, 55, 11, 90, 75, 35]
largest=numbers[0]
second=float("-inf")
for num in numbers:
    if num >largest:
        second=largest
        largest=num
    elif num > second and num < largest:
     
     second=num
print("largest number:",largest)
print("Second largest number:",second)
        
