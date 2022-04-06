#in questo script, trasformo il dataset dei patent da lista di file txt (xml) 
# come un unico csv

import pandas as pd
from os import listdir
from os.path import isfile, join

path = "data/AI Patent Dataset"
files = [f for f in listdir(path) if isfile(join(path, f))]

len(files)

#df = pd.concat([pd.read_xml(x) for x in files], ignore_index=True)

#print(df.head())

import xml.etree.ElementTree as ET

list_of_dict = []
for file in files:
  if "csv" in file: continue
  try:
    dizionario = dict()
    dizionario["filename"] = file
    for el in ET.parse(join(path, file)).getroot():
      dizionario[el.tag] = el.text[1:-1] #rimuovo anche i \n iniziali e finali
  except:
    print(F"file {file} non valido")
    
  
  list_of_dict.append(dizionario)

df = pd.DataFrame(list_of_dict)

print(df)

df.to_csv(join("data", "data_prepared.csv"), index=None)

print(len(df))
