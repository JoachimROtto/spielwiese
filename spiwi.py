import json
from dateutil.parser import parse






















numbers1=[1, 6, 15, 21, 36, 41]
numbers2 = [6, 14, 20, 23, 32, 44]
numbers3=[9, 14, 22, 25, 34, 46]
numbers4=[19, 25, 27, 29, 35, 46]
SZ=4
def checknumbers(lotto, schein):
    richtige=0
    for number in lotto:
        if number in schein:
            richtige=richtige+1
    return richtige

def checkScheine(lotto, datum, schein):
    right = checknumbers(lotto, schein)
    if right > 2:
        print(f"{right} , {datum}, {lotto}")

with open('../Lottonumbers_complete.json') as file:
    d = json.loads(file.read())
    file.close()
for i in d['data']:
    if parse(i['date']).year >2020:
        # hier 4er Schleife/Vlock und jeweils einen Zettel abgleichen
        # Also lotto und numberX an eine funktion weiterleiten und dort die
        # nächsten 3 Zeilen
        checkScheine(i['Lottozahl'], i['date'], numbers1)
        checkScheine(i['Lottozahl'], i['date'], numbers2)
        checkScheine(i['Lottozahl'], i['date'], numbers3)
        checkScheine(i['Lottozahl'], i['date'], numbers4)

