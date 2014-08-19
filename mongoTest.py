from pymongo import Connection

conn = Connection('localhost')

db = conn.testDB

people = db.people

#Create test database to start with
people.insert({'name':'John', 'sport':'soccer', 'location':'Toronto'})
people.insert({'name':'Jane', 'sport':'football'})
people.insert({'name':'Batman', 'location':'Gotham'})

#Fetch data for John and Jane
crew = people.find({'name':{'$regex': '.*[Jj].*'}})
for person in crew:
	print person

#Change location of Batman to Arkham and save it
hero = people.find_one({'name':'Batman'})
hero['location'] = 'Arkham'
people.save(hero)

#Find people located in Arkham
for person in people.find({'location':'Arkham'}):
  	print person

#clear db after execution
for person in people.find():
	people.remove(person)

conn.close()
