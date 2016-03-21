import re
import time
from selenium import webdriver
__author__ = 'independence'

n = 0
score = 0
driver = webdriver.Firefox()
Identifiers = dict()
firststate = True
driver.get("http://www.ncbi.nlm.nih.gov/nuccore/?term=rabies%20gene%20n")  # search page opening
elements = driver.find_elements_by_id("EntrezSystem2.PEntrez.Nuccore.Sequence_ResultsPanel.Sequence_DisplayBar.Display")
elements[1].click()  # clicking on "items per page"
time.sleep(1)  # "waiting for panel"
driver.find_element_by_id("ps50").click()  # now 50 per page (optimal for speed)
while 999 < 1000:  # endless cycle^^^
    data = driver.page_source  # getting html
    GBNs = re.findall("accn=\"(\w*).1", data)  # retrieving list of 50 GeneBank numbers
    for GBN in GBNs:
        n += 1
        GBN = GBN + ".1"  # correcting GB number
        string1 = "href=\"/nuccore/" + GBN + ".*" + "class=\"desc\">(.*) bp" + ".*" + GBN
        string2 = GBN + "\" value=\"(\w*)\""
        length = re.findall(string1, data)  # retrieving sequence length
        GI = re.findall(string2, data)  # retrieving GI number
        if len(GI) != 0 and len(length) != 0:  # it made to avoid listindexerror
            lengthstring = re.sub(",", "", length[0])
<<<<<<< HEAD
            if int(lengthstring) >= 1353: #getting rid of too short sequences
=======
            if int(lengthstring) >= 1350:  # getting rid of too short sequences
>>>>>>> a135711f62db717cb6f91571d56a8df398121b29
                Identifiers[GBN] = GI[0]
                score += 1
                print("scored " + str(n) + " " + lengthstring + " " + GBN + " score=" + str(score))
            else:
                print("not scored " + str(n) + " " + lengthstring + " " + GBN + " score=" + str(score))
    next = driver.find_elements_by_id("EntrezSystem2.PEntrez.Nuccore.Sequence_ResultsPanel.Entrez_Pager.Page")
    if len(next) == 8:
        next[2].click()  # clicking on "next" button
    elif firststate is True:
        next[0].click()  # clicking on "next" button first time
        firststate = False
    else:
        print("finished")
        break
file = open("identifiers1350.txt", "w")
for identifier in Identifiers:
    file.write(str(identifier) + " " + str(Identifiers[identifier]) + "\n")
print("total scored " + str(score) + " sequences")
