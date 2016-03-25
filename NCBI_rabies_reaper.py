import time
from selenium import webdriver
__author__ = 'independence'

process = 0
problems = 0
Rabies = list()
Rabies_extended = list()
driver = webdriver.Firefox()
input_data = open("Selected_identifiers.txt", "r").read().split("\n")
todo = len(input_data)
for string in input_data:
    process += 1
    print(str(process) + " of " + str(todo))
    words = string.split(" ")
    link = "http://www.ncbi.nlm.nih.gov/nuccore/" + words[0] + "?report=fasta&log$=seqview&format=text"
    driver.get(link)
    data = "Loading ..."
    while data == "Loading ...":
        time.sleep(0.1)
        try:
            data = driver.find_element_by_id("viewercontent1").text
        except:
            time.sleep(10)
            driver.get(link)
    data = data.split("\n")
    if len(data[1]) != 70:
        print(str(process) + " string" + "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        problems += 1
    text = ">" + string + "\n"
    for i in range(1, len(data)):
        text = text + data[i] + "\n"
    text += "\n"
    if len(data[20]) == 23:
        Rabies.append(text)
    else:
        Rabies_extended.append(text)
output_file = open("Rabies.fasta", "w")
for genome in Rabies:
    output_file.write(genome)
output_file = open("Rabies_extended.fasta", "w")
for genome in Rabies_extended:
    output_file.write(genome)
print("Finished with " + str(problems) + " problems")
