# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 01:21:31 2020

@author: ABDOULAYE
"""

import sqlite3
import pandas as p
import csv 
#Récuperation du fichier csv
pop= p.read_csv('Densite.csv',delimiter=";",encoding='utf-8')
#Ajoute des densités
liste1=[]
i=int(len(pop.POP84))
for j in range(i):
    dens=round(pop.POP84[j]/pop.SUPERFICIE[j],2)
    lis1=liste1.append(dens)
pop['DENSITE84'] =liste1

liste2=[]
i=int(len(pop.POP86))
for j in range(i):
    dens=round(pop.POP86[j]/pop.SUPERFICIE[j],2)
    lis=liste2.append(dens)
pop['DENSITE86'] =liste2

liste=[]
i=int(len(pop.POP88))
for j in range(i):
    dens=round(pop.POP88[j]/pop.SUPERFICIE[j],2)
    lis=liste.append(dens)
pop['DENSITE88'] =liste

#Creation et connexion a la base de données
connexion=sqlite3.connect("database.db")
connexion=sqlite3.connect(":memory:")
cur=connexion.cursor()

 #Création de la table(peuple) dans la base de donnée
cur.execute("CREATE TABLE peuple(NUMERO integer,PAYS text,REGION text,SUPERFICIE text,POP84 integer,POP88 integer,POP86 integer,DENSITE84 integer,DENSITE88 integer ,DENSITE86 integer )")
connexion.commit()
for i in range(1,len(pop)):   
    values=(i,pop.PAYS[i],pop.REGION[i],int(pop.SUPERFICIE[i]),int(pop.POP84[i]),int(pop.POP88[i]),int(pop.POP86[i]),pop.DENSITE84[i],pop.DENSITE88[i],pop.DENSITE86[i]) 
    cur.execute("INSERT INTO peuple VALUES (?, ?, ?, ?,  ?,  ?, ?,  ?,  ?,  ?)",values)
pf=p.read_sql_query("SELECT * FROM peuple;", connexion)
connexion.commit()

#Création du fichier csv(CompteRendu.csv) et ajout de la table dans le fichier
cur.execute("SELECT * FROM peuple") 
with open("CompteRendu.csv", "w",encoding='utf-8', newline='') as csv_file:    
    csv_writer = csv.writer(csv_file, delimiter=";")
    csv_writer.writerow([i[0] for i in cur.description])
    csv_writer.writerows(cur)

cur.close()
connexion.close()





        
