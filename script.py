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

# write your update damages function here:

def damages_to_floats(damages_list):
	float_list = []
	for damages in damages_list:
		if damages == "Damages not recorded":
			float_list.append(damages)
		elif damages[-1] == "M":
			figure = float(damages[:-1]) * 1000000
			float_list.append(figure)
		elif damages[-1] == "B":
			figure = float(damages[:-1]) * 1000000000
			float_list.append(figure)
		else:
			float_list.append("fuckup")
	return float_list


# write your construct hurricane dictionary function here:

def hurricane_dict_by_name(names, months, years, winds, areas, deaths):
	dictionary={}
	for i in range(len(names)):
		dictionary[names[i]] = {\
		"Name":names[i],\
		"Month":months[i],\
		"Year":years[i],\
		"Max Sustained Winds":winds[i],\
		"Areas Affected":areas[i],\
		"Deaths":deaths[i]
		}
	return dictionary

cat_five = hurricane_dict_by_name(names, months, years, max_sustained_winds, areas_affected, deaths)

# write your construct hurricane by year dictionary function here:

def hurricane_dict_by_year(hurricanes_dictionary):
	year_dictionary = {}
	for year in years:
		year_dictionary[year] = []
		for hurricane in hurricanes_dictionary:
			hurricane_name = hurricane
			if hurricanes_dictionary[hurricane_name]["Year"] == year:
				year_dictionary[year].append(hurricanes_dictionary[hurricane_name])
	return year_dictionary

year_dictionary = hurricane_dict_by_year(cat_five)

# write your count affected areas function here:

def count_affected_areas(hurricanes_dictionary):
	count_dict = {}
	for hurricane in hurricanes_dictionary:
		areas = hurricanes_dictionary[hurricane]["Areas Affected"]
		for area in areas:
			if area in count_dict:
				count_dict[area] += 1
			else:
				count_dict[area] = 1
	return count_dict

cat_five_areas_hit = count_affected_areas(cat_five)

# write your find most affected area function here:

def find_most_affected_area(count_affected_areas_dict):
	most_affected_area = ""
	number_of_hurricanes = 0
	for area in count_affected_areas_dict:
		if count_affected_areas_dict[area] > number_of_hurricanes:
			most_affected_area = area
			number_of_hurricanes = count_affected_areas_dict[area]
	return ("Most affected area: " + most_affected_area + "\n"\
		"Number of hurricanes: " + str(number_of_hurricanes))

print(find_most_affected_area(cat_five_areas_hit))

# write your greatest number of deaths function here:

def find_most_lethal(hurricane_dict_by_name):
	most_lethal = ""
	number_of_deaths = 0
	for hurricane in hurricane_dict_by_name:
		if hurricane_dict_by_name[hurricane]["Deaths"] > number_of_deaths:
			most_lethal = hurricane
			number_of_deaths = hurricane_dict_by_name[hurricane]["Deaths"]
	return ("Most lethal: " + most_lethal + "\n"\
		"Number of deaths: " + str(number_of_deaths))

print (find_most_lethal(cat_five))

# write your catgeorize by mortality function here:

mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

def categorise_by_mortality(hurricane_dict_by_name):
	mortality_dict = {"Level 0":[],\
						"Level 1" : [],\
						"Level 2" : [],\
						"Level 3" : [],\
						"Level 4" : []}
	for hurricane in hurricane_dict_by_name:
		if hurricane_dict_by_name[hurricane]["Deaths"] <=100:
			mortality_dict["Level 0"].append(hurricane)
		elif hurricane_dict_by_name[hurricane]["Deaths"] <= 500:
			mortality_dict["Level 1"].append(hurricane)
		elif hurricane_dict_by_name[hurricane]["Deaths"] <= 1000:
			mortality_dict["Level 2"].append(hurricane)
		elif hurricane_dict_by_name[hurricane]["Deaths"] <= 10000:
			mortality_dict["Level 3"].append(hurricane)
		else:
			mortality_dict["Level 4"].append(hurricane)
	return mortality_dict

print (categorise_by_mortality(cat_five))

# write your greatest damage function here:







# write your catgeorize by damage function here:
