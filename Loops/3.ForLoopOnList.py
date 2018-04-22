city=['Aurangabad','Pune','Beed','Latur','Mumbai','Bathinda','Kolkata','Delhi']
print('*********NOrmal List*********')
for cities in city:
    print(cities)

#For All uppercase Charatcter
print('*********Capital List*********')

for cities in city:
    print(cities.upper())


#For Concatination with list
print('*********Concanited List*********')

for cities in city:
    print(cities + " is good")


#Print Those Cities from list Whose first charcter is B
print('*********Cities Starting With letter b for converting to Lower*********')

for cities in city:
    if(cities[0].lower()=="b"):
        print(cities)
