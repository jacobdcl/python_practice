import requests
#calculate how much each person should pay based on how many nights they are staying

price = float(input('Total price of airbnb: '))
num_people = int(input('Amount of people staying: '))

#create dict for person:nights based on input
person_nights = {} 
for i in range(num_people):
    person = input(f'What is the name of person {i+1}? (NO REPEAT NAMES!) : ')
    nights = int(input(f"How many nights is {person} staying? : "))
    person_nights[person] = nights

#confirm
print('\nSo, ')
for person,nights in person_nights.items():
    print(f'{person} is staying {nights} nights')
answer = str(input(('Is this correct? (y or n) : ')))
if answer == 'y':
    pass
elif answer == 'n':
    print('\n')
    num_people = int(input('Please re-enter amount of people:'))

#calculate
total_nights = 0
for person,nights in person_nights.items(): #add up each person's amount of nights staying
    total_nights += nights
price_person_night = price/total_nights
person_prices = {}
for person,nights in person_nights.items():
    person_prices[person] = price_person_night * nights
print('\n')
for person,price in person_prices.items():
    print(f"{person} pays {price}")
print('\n')









