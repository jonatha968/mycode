#!/usr/bin/python3

"""Alta3 Research | RXGeeser
   Review of Lists and Dictionaries"""

#define a short data set
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

print(munsters.get("endDate"))

print("The Munsters began airing on:", munsters.get("startDate"))

print("Characters on the Munsters include:", munsters.get("names"))

names = ['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']

for n in names:
    print(n, "is a character on the Munsters")

print("\nDisplays the same data, but by accessing the nested list within our dict\n")
for x in munsters.get("names"):
    print(x, "is a character on the Muncters")

# Add to the munsters
munsters["episodes"] = 70
print(munsters)


