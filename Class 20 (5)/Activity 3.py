#Trip Cost calculation
def hotel_cost(day):
    return 140*day

def plane_cost(city):
    if 'Pittsburgh' == city:
        return 183
    elif 'Tampa' == city:
        return 220
    elif 'Los Angeles' == city:
        return 450
    elif 'New York' == city:
        return 516
    else:
        print('Choose from the options given above')

def car_ride(day):
    if day >= 7:
        return 40*day - 50
    elif day >= 3:
        return 40*day - 20
    else:
        return 40*day
    
def total_cost(day, city, spending_amt):
    return hotel_cost(day) + plane_cost(city) + car_ride(day) + spending_amt

a = int(input('How many days are you planning your trip? : '))
b = input('Which city are you goning to plan to go? \nPittsburgh\nTampa\nLos Angeles\nNew York')
c = int(input('How much money are you going to spend for your other needs? : '))

print('Your hotel cost will be ',hotel_cost(a))
print('Your plane ticket will be ',plane_cost(b))
print('Your car ride cost will be ',car_ride(a))
print('Your total cost of the whole trip will be roughly ',total_cost(a,b,c))