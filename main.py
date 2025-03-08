import pandas as pd
import os
import sqlite3

files = os.listdir('BBDD')
dataframes = {}
for file in files:
    name = file.strip('.txt')
    dataframes[name] = pd.read_csv('BBDD/' + file, sep='\t')
    

master = dataframes["PUB_EMPRESAS_PJ_2020_A_2024"]

for name, df in dataframes.items():
    if "PUB_EMPRESAS_PJ" in name and name != "PUB_EMPRESAS_PJ_2020_A_2024":
        master = pd.concat([master, df])



names_code = pd.merge(dataframes["PUB_NOMBRES_PJ"], 
                      dataframes["CODIGO_TIPO_SUBTIPO"],
                      left_on="COD_SUBTIPO",
                      right_on="COD_SUBTIPO")

master = pd.merge(master, names_code, on="RUT")

num_sucursales = dataframes["PUB_NOM_SUCURSAL"]["RUT"].value_counts().reset_index()
master = pd.merge(master, num_sucursales, on="RUT")
master["Num_sucursales"] = master["count"]
master.drop(columns=["count"], inplace=True)

# Create a connection to a new SQLite database
conn = sqlite3.connect('master_database.db')

# Convert the master DataFrame to a SQL table
master.to_sql('master_table', conn, if_exists='replace', index=False)

# Confirm table creation
print("Table 'master_table' created successfully.")

# Close the connection
conn.close()



