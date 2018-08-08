import pandas as pd

# returns whether or not the user has high flow fixtures in their home
def def high_flow():
    fixtures = str(input('Do you have any high flow fixtures? '))
    return fixtures

# returns the number of people that live in the home
def num_people():
    people = int(input('How many people live in your home? '))
    return people

# returns the water hardness for the user/'s zipcode
def get_location():
    data = pd.read_csv('./hardness.csv') # Loads water quality data
    data.set_index('zipcode', inplace = True)
    location = input('What is you zip code?: ')
    
    while (int(location) <= 10000) or (int(location) >= 99999):
        location = input('Please inter a valid zipcode: ')
    
    zip_code = data.loc[int(location)]
    return zip_code

# If the user has a sample we ask for it here, if not we get the hardness from our data


def hardness_amount():
    sample = str(input('Do you have a water sample? yes or no '))
    if sample.lower() == 'yes':
        hardness = int(input('What is your hardness amount? '))
        return hardness
    else:
        hardness = get_location()
        return hardness
    
# We calculate the size of softener needed based on hard
def city_calc():
    hardness_calc = (75 * num_people() * hardness_amount())
    return hardness_calc

def well_calc():
    comp_hardness = hardness_amount() * 3
    hardness_calc = (75 * num_people() * comp_hardness) 
    return hardness_calc

# This calculates the size of softener needed
def hardness_calc():
    water_type = str(input('What type of water do you have, city or well? '))

    if water_type.lower() == 'city':
        hardness = city_calc()
        return hardness  
    elif water_type.lower() == 'well':
        hardness = well_calc()
        return hardness
    else: water_type = str(input('Please make sure to enter either city or well:  '))

print(hardness_calc())
