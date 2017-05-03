from pymongo import MongoClient

db_name = 'pySamples'
collection_name = 'basicQueries'
client = MongoClient('localhost', 27017)

db = client[db_name]
collection = db[collection_name]

user = {
    'name': 'Ann',
    'age': 32
}


# 1. Dodaj warunek sprawdzajacy czy w bazie istnieje uzytkownik o imieniu Ann
if collection.find_one({'name': 'Ann'}) is None:

    new_id = collection.insert_one(user) #2. Dodaj do bazy użytkownika w zmiennej user. new_id będzie ObjectId nowo dodanego obiektu
    print("Added new record " + str(new_id))
#koniec warunku

#3. Pobierz do zmiennej uzytkownika o imieniu Ann
user_ann = collection.find_one({'name': 'Ann'})
print(user_ann)

#4. Zwieksz wiek uzytkownika o 10
collection.update({'name': 'Ann'}, {'$set': {'age': user['age'] + 10}})

#5. Do zmiennej user_ann ponownie przypisz użytkownika o imieniu Ann
user_ann['age'] = user_ann['age'] + 10
collection.save(user_ann)
print(user_ann)

#6. Usuń użytkownika Ann z bazy
collection.remove({'name': 'Ann'})

#7. Sprawdź czy użytkownik nie istnieje w bazie (zapytanie powinno zwrócić None)
user_ann = collection.find_one({'name': 'Ann'})
print(user_ann)
