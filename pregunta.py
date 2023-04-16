"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = pd.read_csv("solicitudes_credito.csv", sep=";").drop(columns=['Unnamed: 0'])
    
    
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df["sexo"] = df.sexo.str.lower().astype(str).str.strip()
    df["tipo_de_emprendimiento"] = df.tipo_de_emprendimiento.str.lower().astype(str).str.strip()
    df["idea_negocio"] = df.idea_negocio.str.replace("-"," ", regex=True).str.replace("_"," ", regex=True).str.lower()
    df["barrio"] = df.barrio.str.replace("_","-", regex=True).str.replace("-"," ", regex=True).str.lower()
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True)
    df['monto_del_credito'] = df['monto_del_credito'].map(lambda x: x.lstrip('$'))
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '')
    df.monto_del_credito = pd.to_numeric(df.monto_del_credito, errors='coerce')
    df["línea_credito"] = df.línea_credito.str.replace("-"," ")
    df["línea_credito"] = df.línea_credito.str.replace("_"," ")
    df["línea_credito"] = df.línea_credito.str.lower()

    df = df.drop_duplicates().dropna()
    
    return df
