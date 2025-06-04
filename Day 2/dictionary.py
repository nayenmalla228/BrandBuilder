#dictionary

#dictionary ma key -value huncha
#dictionary -unordered,mutable,doesnt support multiple keys

dict1={
    "name": "milan",
    "gpa": 4,
    "marks":[49,50,51],
    "gpa":5
}
print(dict1)

dict2={} #null dictionary

print(dict1.keys())
print(type(dict1))

print(dict1.values())
print(dict1.get('gpa'))
print(dict1.get('marks'))

dict1.update({'address': 'pokhara'})
print(dict1)