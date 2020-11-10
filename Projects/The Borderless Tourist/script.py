import inspect

destinations = ["Paris, France",
"Shanghai, China", 
"Los Angeles, USA", 
"Sao Paulo, Brazil", 
"Cairo, Egypt",
"Safety Catch"]

# print("\n====== ln" + str(inspect.currentframe().f_lineno) + ", avaliable destinations")
# print(destinations)

# TEST_DATA: traveler profile
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


# traveler_info functional unpacking
traveler_name = ""
traveler_destination = ""
traveler_interests = []
def get_traveler_info(traveler_info):
  traveler_name, traveler_destination, traveler_interests = traveler_info
  traveler_name = traveler_name
  traveler_destination = traveler_destination
  traveler_interests = traveler_interests

  print("\n=====ln" + str(inspect.currentframe().f_lineno) + ", get_traveler_info: ")
  print("traveler_name: ", end=""); print(traveler_name)
  print("traveler_destination: ", end=""); print(traveler_destination)
  print("traveler_interests: ", end=""); print(traveler_interests)

  return traveler_name, traveler_destination, traveler_interests

# Get traveler destination index
def get_destination_index(traveler_destination):
  try:
    destination_index = destinations.index(traveler_destination)
  except ValueError:
    print("{} is not currently available.".format(traveler_destination))
    return

  return destination_index


# Get traveler's destination from profile
def get_traveler_location(traveler_destination):
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index


# Add attractions to destinations
attractions = [[] for destination in destinations]
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    print("{destination} is not a valid destination.".format(destination=destination))
    return
  attractions[destination_index].append(attraction)
  return attractions


# TEST_DATA: destination attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Los Angeles, USA", ["LACMA",["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# print("\n====== ln" + str(inspect.currentframe().f_lineno) + ", attractions")
# print(attractions)


# Lookup destination attractions
# def find_attractions(traveler="Peter Pan", destination="NeverNeverLand", interests="flying, lost boys"):
def find_attractions(traveler_name, traveler_destination, traveler_interests):
  print("\n=====ln" + str(inspect.currentframe().f_lineno) + ", get_traveler_info: ")
  print("traveler_name: ", end=""); print(traveler_name)
  print("traveler_destination: ", end=""); print(traveler_destination)
  print("traveler_interests: ", end=""); print(traveler_interests)
# def find_attractions(destination, interests):
  destination_index = get_destination_index(traveler_destination)
  print("\n====== ln" + str(inspect.currentframe().f_lineno) + ", destination_index: ", end=""); print(destination_index)

  attractions_in_city = attractions[destination_index]
  print("\n====== ln" + str(inspect.currentframe().f_lineno) + ", List of attractions in {destination}:".format(destination=traveler_destination))
  print(attractions_in_city)

  print("\n====== ln" + str(inspect.currentframe().f_lineno) + ", traveler interests:")
  print(traveler_interests)

  attractions_with_interests = []
  for attraction in attractions_in_city:
    possible_attraction, attraction_tags = attraction

    for interest in traveler_interests:
      # FIXME: this repeats with each interst check pass, but we only want to print after no interest == attraction_tags
      # print("\n====== ln" + str(inspect.currentframe().f_lineno) + ", interest check:"); print(interest)
      # print("\n====== ln" + str(inspect.currentframe().f_lineno) + ", attraction_tags check:"); print(attraction_tags)
      # if interest not in attraction_tags:
            # print("Enjoy your time in {destination}. But, we got nothin', {name}.".format(name=traveler_name, destination=traveler_destination))
      if interest in attraction_tags:
        attractions_with_interests.append(possible_attraction)
  return attractions_with_interests

  print("\n====== ln" + str(inspect.currentframe().f_lineno) + ", List of possible attractions:")
  print(attractions_with_interests, end=": "); print(interest)


# travelerinfo = list(get_traveler_info(test_traveler))
# travelerinfo = ['Stuart Smally', 'Paris, France', ['monument']]         ## altcheck good
travelerinfo = ['Scott McCarthy', 'Barcelona, Spain', ['monument']]     ## altcheck bad destination
# travelerinfo = ['Scott McCarthy', 'Los Angeles, USA', ['clubs']]        ## altcheck bad interest
traveler_attractions = find_attractions(*travelerinfo)


# "Hi {name}, we think you'll like these places around {destination}: the {attraction[0]}, the {attraction[1]}."
interest_string = "Hi, " + travelerinfo[0] + "! We think you'll like these places around " + travelerinfo[1] + ": "
for i in range(len(traveler_attractions)):
  if traveler_attractions[-1] == traveler_attractions[i]:
    interest_string += "the " + traveler_attractions[i] + "."
  else:
    interest_string += "the " + traveler_attractions[i] + ", and "
print(interest_string)