import re
import time
from selenium import webdriver
__author__ = 'independence'


score = 0
process = 0
normal = True
identifiers = dict()
Manual_unknown = list()
Manual_unprecise = list()
Wrong_identifiers = list()
Selected_identifiers = list()
driver = webdriver.Firefox()
Eurasia = ["China", "India", "Indonesia", "Pakistan", "Bangladesh", "Russia", "Japan", "Philippines", "Vietnam",
           "Germany", "Iran", "Turkey", "Thailand", "United Kingdom", "France", "Italy", "Myanmar", "South Korea",
           "Spain", "Ukraine", "Poland", "Iraq", "Saudi Arabia", "Uzbekistan", "Malaysia", "Nepal", "Afghanistan",
           "Yemen", "North Korea", "Taiwan", "Syria", "Sri Lanka", "Romania", "Kazakhstan", "Netherlands", "Cambodia",
           "Belgium", "Greece", "Czech Republic", "Portugal", "Hungary", "Sweden", "Azerbaijan", "Belarus",
           "United Arab Emirates", "Austria", "Tajikistan", "Israel", "Switzerland", "Hong Kong", "Bulgaria",
           "Serbia", "Jordan", "Laos", "Kyrgyzstan", "Denmark", "Singapore", "Finland", "Slovakia", "Norway",
           "Turkmenistan", "Palestine", "Ireland", "Lebanon", "Croatia", "Oman", "Kuwait", "Bosnia and Herzegovina",
           "Georgia", "Moldova", "Mongolia", "Armenia", "Lithuania", "Albania", "Qatar", "Macedonia", "Slovenia",
           "Latvia", "Kosovo", "Bahrain", "Estonia", "Timor-Leste", "Cyprus", "Bhutan", "Macau", "Montenegro",
           "Luxembourg", "Malta", "Brunei", "Maldives", "Iceland Jersey", "Isle of Man", "Andorra", "Guernsey",
           "Faroe Islands", "Monaco", "Liechtenstein", "Gibraltar", "San Marino", "Åland Islands",
           "Svalbard and Jan", "Mayen", "Vatican City"]
Large_countries = ["China", "India", "Russia", "Iran", "Saudi Arabia", "Kazakhstan", "Mongolia"]
input_data = open("identifiers.txt", "r").read().split("\n")
for string in input_data:
    string = string.split(" ")
    identifiers[string[0]] = string[1]  # now we have a list of Genbank numbers
todo = len(identifiers)
for identifier in identifiers:
    process += 1
    link = "http://www.ncbi.nlm.nih.gov/nuccore/" + identifier
    driver.get(link)  # opening page of this strain
    fstring = "feature_" + identifiers[identifier] + "_source_0"
<<<<<<< HEAD
    time.sleep(1)  # waiting for javascript execution
    ct = 0
    while 8 < 9:
        ct += 1
        if ct >= 100:  # if something like "page not exist"
            normal = False
            break
        try:
            features = driver.find_element_by_id(fstring).text
        except:  # in case of too slow execution
            print(ct)
            time.sleep(0.1)
        else:
            break
    if normal is False:
        print("Broken identifier!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! " + identifier)
        Wrong_identifiers.append(identifier)
        normal = True
        continue
=======
    time.sleep(2)  # waiting for javascript execution
    features = driver.find_element_by_id(fstring).text
>>>>>>> a135711f62db717cb6f91571d56a8df398121b29
    location = re.findall("/country=\"(.*)\"", features)
    year = re.findall("/collection_date=\"(.*)\"", features)
    if len(year) != 0 and len(location) != 0:  # getting rid of samples without location or year
        country = location[0].split(":")  # obtaining only countryname from precision location
        if country[0] in Eurasia:  # getting rid of non-eurasian samples
            isolate = re.findall("/isolate=\"(.*)\"", features)
            organism = re.findall("/organism=\"(.*)\"", features)
            if len(isolate) != 0 and len(organism) != 0:  # getting rid of sampes without or organism isolate name
                if organism[0] == "Rabies virus":
                    Result_string = identifier + " Rabies virus isolate " + isolate[0] + " " + \
                                    location[0] + " " + year[0] + "\n"
<<<<<<< HEAD
                    if country[0] in Large_countries and len(country) == 1:
                        Manual_unprecise.append(Result_string)  # for manual examination
                        print(str(process) + " of " + str(todo) + " Not scored: unprecise location [" +
                              location[0] + " " + year[0] + "]")
                    else:
                        Selected_identifiers.append(Result_string)  # saving targeted data
                        score += 1
                        print(str(process) + " of " + str(todo) + " Scored: " + Result_string + " score = " + str(score))
=======
                    Selected_identifiers.append(Result_string)  # saving targeted data
                    score += 1
                    print(str(process) + " of " + str(todo) + " Scored: " + Result_string + " score = " + str(score))
>>>>>>> a135711f62db717cb6f91571d56a8df398121b29
                else:
                    Result_string = identifier + " " + location[0] + " " + year[0] + "\n"
                    print(str(process) + " of " + str(todo) + " Not scored: unknown organism [" +
                          location[0] + " " + year[0] + "]")
<<<<<<< HEAD
                    Manual_unknown.append(Result_string)  # for manual examination
=======
                    Manual.append(identifier)  # for manual examination
>>>>>>> a135711f62db717cb6f91571d56a8df398121b29
            else:
                Result_string = identifier + " " + location[0] + " " + year[0] + "\n"
                print(str(process) + " of " + str(todo) + " Not scored: unknown isolate or organism [" +
                      location[0] + " " + year[0] + "]")
<<<<<<< HEAD
                Manual_unknown.append(Result_string)  # for manual examination
=======
                Manual.append(identifier)  # for manual examination
>>>>>>> a135711f62db717cb6f91571d56a8df398121b29
        else:
            print(str(process) + " of " + str(todo) + " Not scored: non Eurasian [" + location[0] + " " + year[0] + "]")
    else:
        print(str(process) + " of " + str(todo) + " Not scored: unknown location or year")
output_file = open("Selected_identifiers.txt", "w")
for identifier in Selected_identifiers:
    output_file.write(identifier + "\n")
output_file = open("Manual_unprecise.txt", "w")
for identifier in Manual_unprecise:
    output_file.write(identifier + "\n")
output_file = open("Manual_unknown.txt", "w")
for identifier in Manual_unknown:
    output_file.write(identifier + "\n")
print("Total selected " + str(len(Selected_identifiers)) + " of " + str(todo))
print(str(len(Manual_unprecise)) + " Data with unprecised location")
print(str(len(Manual_unknown)) + " Unknown isolates or organisms")
print(str(len(Wrong_identifiers)) + " identifiers are broken:")
print(Wrong_identifiers)
