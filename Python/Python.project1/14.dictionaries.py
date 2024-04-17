# dictionary = A changeable, unordered ccollection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli' ,
            'China':'Beijing' ,
            'Russia':'Moscow'}


#capitals.update({'Germany':'Berlin'}) # adds a new value and key
#capitals.update({'Germany':'Warsaw'}) # also can be used to update current key and value
#capitals.pop('China') # deletes elements from dictionary
#capitals.clear() # clears dictionary fully

print(capitals.get('Germany')) # shows if something in dictionary
print(capitals.keys())   # will print a key
print(capitals.values()) # will print a value 
print(capitals.items()) # will print everything in dictionary
print(capitals['Russia'])

for key,value in capitals.items():
    print(key, value)
