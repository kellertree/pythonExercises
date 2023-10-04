# create an empty list for outfits.
outfits = []

# creates a list for a top and bottom for days of the week.
monday_outfit = ['flannel button-up', 'bluejeans']
tuesday_outfit = ['hawaiian shirt', 'shorts']
wednesday_outfit = ['blue button-up', 'gray dresspants']

# add the monday_outfit, tuesday_outfit, wednesday_outfit to the outfits list.
outfits.insert(0, monday_outfit)
outfits.insert(1, tuesday_outfit)
outfits.insert(2, wednesday_outfit)

print(f"The outfits for the next 3 days are: {outfits}.")