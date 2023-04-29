# Define the distances between each pair of cities
distances = {
  ('Edoras', 'Helm\'s Deep'): 90,
  ('Helm\'s Deep', 'Edoras'): 90,
  ('Edoras', 'Aldburg'): 75,
  ('Aldburg', 'Edoras'): 75,
  ('Edoras', 'Eastfold'): 65,
  ('Eastfold', 'Edoras'): 65,
  ('Edoras', 'Westfold'): 80,
  ('Westfold', 'Edoras'): 80,
  ('Helm\'s Deep', 'Aldburg'): 50,
  ('Aldburg', 'Helm\'s Deep'): 50,
  ('Helm\'s Deep', 'Eastfold'): 70,
  ('Eastfold', 'Helm\'s Deep'): 70,
  ('Helm\'s Deep', 'Westfold'): 55,
  ('Westfold', 'Helm\'s Deep'): 55,
  ('Aldburg', 'Eastfold'): 45,
  ('Eastfold', 'Aldburg'): 45,
  ('Aldburg', 'Westfold'): 60,
  ('Westfold', 'Aldburg'): 60,
  ('Eastfold', 'Westfold'): 50,
  ('Westfold', 'Eastfold'): 50,
}

all_city = ['Westfold', 'Eastfold', 'Aldburg', 'Helm\'s Deep', 'Edoras']
# Define the starting city
start_city = 'Edoras'
citynumber = len(all_city)
mindistance=9999999
minroad=[]

current_distance = 0

# Create a set of all the cities


def find_shortest_path(y, visit_city,
                       current_distance):  #x==cureent distance ,y ==next city
  #print(visit_city,current_distance)
  #if  len(visit_city)==0:
  #  visit_city.append(start_city)
  if len(visit_city) == citynumber and visit_city[0] != y:
    return

  if len(visit_city) == citynumber and visit_city[0] == y:
    visit_city.append(start_city)
    current_distance += distances[(visit_city[-2], y)]
    print(current_distance, visit_city)
    
    return
  if visit_city[0] == y and len(visit_city) != citynumber:
    return
  if y in visit_city:
    return 
  if (visit_city[-1], y) in distances:
    current_distance += distances[(visit_city[-1], y)]
    visit_city.append(y)
  else:
    return 
  for i in range(len(all_city)):
    find_shortest_path(all_city[i], visit_city, current_distance)
  return
  

for i in range(len(all_city)):
  if all_city[i]==start_city:
    continue
  visit_city = []
  visit_city.append(start_city)
  find_shortest_path(all_city[i], visit_city, current_distance)
