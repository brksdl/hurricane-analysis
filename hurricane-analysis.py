#!/usr/bin/env python
# coding: utf-8

# In[1]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def updated_damages(damages, conversion):
  updated_damages = list()
  for dam in damages:
    if dam.find('M') != -1:
      updated_damages.append(float(dam.strip('M')) * conversion.get('M'))
    elif dam.find('B') != -1:
      updated_damages.append(float(dam.strip('B')) * conversion.get('B'))
    else:
      updated_damages.append(dam)
  return updated_damages

updated_damages = updated_damages(damages, conversion)


# test function by updating damages


# 2 
# Create a Table



def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes = dict()
    for i in range(len(names)):
      hurricanes[names[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Damage": updated_damages[i],
                          "Deaths": deaths[i]}
    return hurricanes
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
# Create and view the hurricanes dictionary

# 3
# Organizing by Year


#def hurricaneYear(hurricanes):
def dictYear(hurricanes):
  orderByYear = dict()
  for cane in hurricanes:
    yearOfCane = hurricanes[cane].get('Year')
    caneCurrent = hurricanes[cane]
    if yearOfCane not in orderByYear.keys():
      orderByYear[yearOfCane] = [caneCurrent]
    else:
      orderByYear[yearOfCane].append(caneCurrent)
      break
  return orderByYear

#create a new dictionary of hurricanes with year and key
orderByYear = dictYear(hurricanes)

# 4
# Counting Damaged Areas

def count_affected_areas(hurricanes):
  areaDict = dict()
  for key in hurricanes:
    for area in hurricanes[key].get('Areas Affected'):
      if area not in areaDict:
        areaDict[area] = 1
      else:
        areaDict[area] += 1
  return areaDict


affected_areas_count = count_affected_areas(hurricanes)
#print(affected_areas_count)
# create dictionary of areas to store the number of hurricanes involved in


# 5 
# Calculating Maximum Hurricane Count
def most_affected_area(affected_areas_count):
  count = 0
  mostDict = dict()
  for most in affected_areas_count.items():
    if most[-1] > count:
      count = most[-1]
      mostDict[most[0]] = count
  return mostDict
most_affected_area = most_affected_area(affected_areas_count)
#print(most_affected_area)
# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane

def most_deaths(hurricanes):
  mostDict = dict()
  mostDeath = 0
  mostCane = 0
  for cane in hurricanes:
    if hurricanes[cane]['Deaths'] > mostDeath:
      mostDeath = hurricanes[cane]['Deaths']
      mostCane = cane
  mostDict[mostCane] = mostDeath
  return mostDict
  
death = most_deaths(hurricanes)
# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality
def categorize_by_mortality(hurricanes):
  hurricanes_by_mortality = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  mortality_scale = {0: 0,
                      1: 100,
                      2: 500,
                      3: 1000,
                      4: 10000}
  for damage in hurricanes:
    death = hurricanes[damage]['Deaths']
    if death == mortality_scale[0]:
      hurricanes_by_mortality[0].append(hurricanes[damage])
    elif (death > mortality_scale[0]) and (death <=mortality_scale[1]):
      hurricanes_by_mortality[1].append(hurricanes[damage])
    elif (death > mortality_scale[1]) and (death <=mortality_scale[2]):
      hurricanes_by_mortality[2].append(hurricanes[damage])
    elif (death > mortality_scale[2]) and (death <=mortality_scale[3]):
      hurricanes_by_mortality[3].append(hurricanes[damage])
    elif (death > mortality_scale[3]) and (death <=mortality_scale[4]):
      hurricanes_by_mortality[4].append(hurricanes[damage])
    elif (death > mortality_scale[4]):
      hurricanes_by_mortality[5].append(hurricanes[damage])

  return hurricanes_by_mortality

category = categorize_by_mortality(hurricanes)

# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

def highest_damage(hurricanes):
  highestDamage = 0
  HCane = 0
  HDict = dict()
  for cane in hurricanes:
    if hurricanes[cane].get('Damage') == 'Damages not recorded':
      continue
    elif highestDamage < hurricanes[cane].get('Damage'):
      highestDamage = hurricanes[cane].get('Damage')
      HCane = cane
  HDict[HCane] = highestDamage
  return HDict
  
highest = highest_damage(hurricanes)
# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def categorize_by_damage(hurricanes):
  hurricanes_by_damage  = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

  for damage in hurricanes:
    death = hurricanes[damage]['Damage']
    if death == 'Damages not recorded':
      hurricanes_by_damage[0].append(hurricanes[damage])
    elif (death > damage_scale[0]) and (death <= damage_scale[1]):
      hurricanes_by_damage[1].append(hurricanes[damage])
    elif (death > damage_scale[1]) and (death <= damage_scale[2]):
      hurricanes_by_damage[2].append(hurricanes[damage])
    elif (death > damage_scale[2]) and (death <= damage_scale[3]):
      hurricanes_by_damage[3].append(hurricanes[damage])
    elif (death > damage_scale[3]) and (death <= damage_scale[4]):
      hurricanes_by_damage[4].append(hurricanes[damage])
    elif (death > damage_scale[4]):
      hurricanes_by_damage[5].append(hurricanes[damage])

  return hurricanes_by_damage
  
categoryDamage = categorize_by_damage(hurricanes)
print(categoryDamage[5])
# categorize hurricanes in new dictionary with damage severity as key

