import json

gebruiker_gegevens={
    "naam": "John Doe",
    "leeftijd": "25",
    "stad": "New York",
    "e-mail": "john@example.com"
}
with open("gebruiker.json",'w') as json_bestand:
    json.dump(gebruiker_gegevens, json_bestand)

with open('gebruiker.json','r') as json_bestand:
    gegevens=json.load(json_bestand)
    print(gegevens)
gegevens['stad']='San Francisco'
with open('gebruiker.json','w') as json_bestand:
    json.dump(gegevens, json_bestand)
print(gegevens)
