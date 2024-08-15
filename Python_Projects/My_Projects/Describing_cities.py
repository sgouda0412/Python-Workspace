desc_city = {}

def describe_city(city, country, population):
    desc_city[country] = {country, city, pop}
    return desc_city

entry = ''
        
while entry != 'quit':
    country = input("Please enter the country: ")
    city = input("Please enter a city: ")
    pop = input("Please enter the population of the city: ")
    print(describe_city(city, country, pop))
    entry = input("Would you like to enter another city? Type 'quit' to finish: ")
    
print(desc_city)
