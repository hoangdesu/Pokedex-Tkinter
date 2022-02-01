# Checking if a key exists in a dictionary first,
# before we can pull out the value


brian = {
    'name': 'Brian',
    'age': 26
}

myKey = 'name'
if myKey in brian:
    print(f'Key "{myKey}" exists')
else:
    print("Key doesnt exist")
    
print("name" in brian)
print("job" in brian.keys())