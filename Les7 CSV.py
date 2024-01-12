import csv
# with open('names.csv','r') as csv_file:
#     csv_reader=csv.reader(csv_file, delimiter='\t')
#     for line in csv_reader:
#         print(line)

# import csv
# with open('boeken.csv','r') as csv_file:
#         csv_reader=csv.reader(csv_file, delimiter='\t')
#         for line in csv_reader:
#             print(line)
# nieuwe_data=['De Bijbel','Jesus','Klassieker','0.00']
# with open('boeken.csv', 'a', newline='') as bestand:
#     csv_writer = csv.writer(bestand, delimiter='\t')
#     csv_writer.writerow(nieuwe_data)

# def aantal_landen():     
#     with open('landen.csv','r') as csv_file:
#         csv_reader=csv.reader(csv_file)
#         next(csv_reader)
#         print(sum(1 for line in csv_reader))
# aantal_landen()

# def grootste_bevolking():
#     grootste_land = ""
#     max_bevolking = 0
#     with open('landen.csv','r') as csv_file:
#         csv_reader=csv.reader(csv_file)
#         next(csv_reader)
#         for line in csv_reader:
#             land, bevolking=line
#             if int(bevolking) > int(max_bevolking):
#                 max_bevolking = bevolking
#                 grootste_land = land
#     print(f"Het land met het grootste bevolkingsaantal is {grootste_land} met {max_bevolking} inwoners.")
# grootste_bevolking()

# def gemiddelde_bevolking():
#     totale_bevolking = 0
#     aantal_landen = 0
#     with open('landen.csv','r') as csv_file:
#         csv_reader=csv.reader(csv_file)
#         next(csv_reader)
#         for line in csv_reader:
#             land, bevolking=line
#             totale_bevolking += int(bevolking)
#             aantal_landen +=1
#     gemiddelde = totale_bevolking / aantal_landen
#     print(f"Het gemiddelde van het aantal inwoners over alle landen is: {gemiddelde}")
# gemiddelde_bevolking()


def totale_verkoopwaarde():
    totale_verkoop = 0
    with open('winkelverkocht.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            datum,product,hoeveelheid,verkoopwaarde=line
            totale_verkoop += float(verkoopwaarde)
    print(f"De totale verkoopwaarde is: {totale_verkoop}")
totale_verkoopwaarde()

def meest_verkocht_product():
    producten_hoeveelheden = {}
    with open('winkelverkocht.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            datum,product,hoeveelheid,verkoopwaarde=line
            if product in producten_hoeveelheden:
                producten_hoeveelheden[product] += hoeveelheid
            else:
                producten_hoeveelheden[product] = hoeveelheid

    meest_verkocht_product = max(producten_hoeveelheden, key=producten_hoeveelheden.get)
    print(f"Het meest verkochte procduct is: {meest_verkocht_product}")
meest_verkocht_product()

def dag_met_hoogste_verkoop():
    hoogste_verkoopwaarde = 0
    beste_dag = ''
    with open('winkelverkocht.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            datum,product,hoeveelheid,verkoopwaarde=line
            if float(verkoopwaarde) > float(hoogste_verkoopwaarde):
                hoogste_verkoopwaarde = verkoopwaarde
                beste_dag = line[0]
    print(f"De dag met de meeste verkoop is: {beste_dag}")
dag_met_hoogste_verkoop()

def gemiddelde_verkoopwaarde_per_dag():
    totaal=0
    aantal=0
    with open('winkelverkocht.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            datum,product,hoeveelheid,verkoopwaarde=line
            totaal+=float(verkoopwaarde)
            aantal+=1
    gemiddelde=totaal/aantal
    print(f"Het gemiddelde van de dagelijkse totale verkoopwaarde is: {gemiddelde}")
gemiddelde_verkoopwaarde_per_dag()