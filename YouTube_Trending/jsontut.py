import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails":["ayo@gmail.com","mikun@gmail.com"],
            "has_license": false
        },
        {
            "name": "John Doe",
            "phone": "615-555-8264",
            "emails":["bayo@gmail.com","Ayomikun@gmail.com"],
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)

print(type(data["people"]))

for person in data["people"]:
    print(person["name"])

