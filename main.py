import pandas as pd
import os

files = os.listdir('BBDD')
dataframes = {}
for file in files:
    name = file.strip('.txt')
    dataframes[name] = pd.read_csv('BBDD/' + file, sep='\t')
    try:
        if name != "PUB_NOM_SUCURSAL":
            dataframes[name].drop_duplicates(subset=["RUT"], keep='first', inplace=True)      
    except:
        pass

master = dataframes["PUB_EMPRESAS_PJ_2020_A_2024"]

names_code = pd.merge(dataframes["PUB_NOMBRES_PJ"], 
                      dataframes["CODIGO_TIPO_SUBTIPO"],
                      left_on="COD_SUBTIPO",
                      right_on="COD_SUBTIPO")

master = pd.merge(master, names_code, on="RUT")

num_sucursales = dataframes["PUB_NOM_SUCURSAL"]["RUT"].value_counts().reset_index()
master = pd.merge(master, num_sucursales, on="RUT")
master["Num_sucursales"] = master["count"]
master.drop(columns=["count"], inplace=True)



