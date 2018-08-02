import pandas as pd


# Loads water quality data
data = pd.read_csv('./hardness.csv')
data.set_index('zipcode', inplace = True)
print(data)

# location != data.loc[int(location)]

# returns the water hardness for the user/'s zipcode
def get_location():
    location = input('What is you zip code?: ')
    if int(location) <= 0 or int(location) >= 99999:
        location = input('Please inter a valid zipcode: ')
    else:
        zip_code = data.loc[int(location)]
    return zip_code

water_type = str(input('What type of water do you have, city or well? '))
sample = str(input('Do you have a water sample? yes or no '))
num_people = int(input('How many people live in your home? '))
fixtures = str(input('Do you have any high flow fixtures? '))

# If the user has a sample we ask for it here, if not we get the hardness from our data
if sample.lower() == 'yes':
    hardness = int(input('What is your hardness amount? '))
    iron = int(input('what are your iron results? '))	
else:
    hardness = get_location()

# We determine if the user has city or well water
if water_type.lower() != 'city' or 'well':
    print('Please enter either well or city for water type')
    water_type = input('What type of water do you have, city or well? ')
    
# We calculate the size of softener needed based on hard
if water_type.lower() == 'city':
    hardness_calc = (75 * num_people * hardness)
elif water_type.lower() == 'well':
    comp_hardness = hardness * 3
    hardness_calc = (75 * num_people * comp_hardness) 

	
print(hardness_calc)  

