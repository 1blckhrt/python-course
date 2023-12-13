# Dictionaries
band = {
    'vocals': "Plant",
    'guitar': 'Page'
}

band2 = dict(vocals='Plant', guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# accessing items
print(band['vocals'])
print(band.get('guitar'))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print('guitar' in band)
print('triangle' in band)

# change values
band['vocals'] = 'Coverdale'
band.update({'bass': 'JPJ'})

print(band)

# removing items
print(band.pop('bass'))
print(band)

band['drums'] = 'Bonham'
print(band)

print(band.popitem()) # tuple
print(band)

# deleting/clearing items

band['drums'] = 'Bonham'
del band['drums']
print(band)

band2.clear()
print(band2)

del band2

# copying dictionaries

# band2 = band # incorrect, this creates a reference
# print("Bad copy!") 
# print(band2)
# print(band)

# band2['drums'] = 'Dave'
# print(band)

band2 = band.copy()
band2['drums'] = 'Dave'
print(band)
print("Good copy!")
print(band2)

# or use the dictionary constructor function
band3 = dict(band)
print("Good copy as well!")
print(band3)