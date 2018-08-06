import pandas as pd


# Loads water quality data
data = pd.read_csv('./hardness.csv')
data.set_index('zipcode', inplace = True)


water_type = str(input('What type of water do you have, city or well? '))
sample = str(input('Do you have a water sample? yes or no '))
num_people = int(input('How many people live in your home? '))
fixtures = str(input('Do you have any high flow fixtures? '))

# returns the water hardness for the user/'s zipcode
def get_location():
    location = input('What is you zip code?: ')
    
    while (int(location) <= 10000) or (int(location) >= 99999):
        location = input('Please inter a valid zipcode: ')
    
    zip_code = data.loc[int(location)]
    return zip_code

# If the user has a sample we ask for it here, if not we get the hardness from our data


def hardness_amount():
    if sample.lower() == 'yes':
        hardness = int(input('What is your hardness amount? '))
        return hardness
    else:
        hardness = get_location()
        return hardness
    
# We calculate the size of softener needed based on hard
def city_calc():
    hardness_calc = (75 * num_people * hardness_amount())
    return hardness_calc

def well_calc():
    comp_hardness = hardness_amount() * 3
    hardness_calc = (75 * num_people * comp_hardness) 
    return hardness_calc

# This calculates the size of softener needed
def hardness_calc():
    if water_type.lower() == 'city':
        hardness = city_calc()
        return hardness  
    elif water_type.lower() == 'well':
        hardness = well_calc()
        return hardness

print(hardness_calc())
