"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    
    #Fecha
    df['fecha_de_beneficio']= pd.to_datetime (df['fecha_de_beneficio'], dayfirst=True)
    
    df.dropna(axis='index', inplace=True)
    df.drop_duplicates(inplace=True)
    
    #Minusculas
    df['sexo'] = df['sexo'].str.lower().astype(str).str.strip()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().astype(str)
    df['idea_negocio'] = df['idea_negocio'].str.lower().astype(str)
    df['barrio'] = df['barrio'].str.lower().astype(str)
    df['línea_credito'] = df['línea_credito'].str.lower().astype(str)
    
    #Blancos, ocultos
    df['idea_negocio'] = df['idea_negocio'].str.replace('_',' ').str.replace('-',' ').str.strip()
    df['barrio'] = df['barrio'].str.replace('_',' ').str.replace('-',' ').str.strip()
    df['línea_credito'] = df['línea_credito'].str.replace('_',' ').str.replace('-',' ').str.strip()
    
    #Montos
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','').str.replace('$','',regex=False).str.replace(' ','').str.strip().astype(float)
    
    #Otras
    df['línea_credito'] = df['línea_credito'].str.replace('soli daria','solidaria')
    df['idea_negocio'] = df['idea_negocio'].str.replace('[^a-zA-Z0-9 \n\.]',' ',regex=True).str.replace('organizaci n','organizacion').str.replace('pa alera','pañalera')
    df['barrio'] = df['barrio'].str.replace('[^a-zA-Z0-9 \n\.]',' ',regex=True).str.replace('bel n','belen').str.replace('san jos  de la monta a','san jose de la montana').str.replace('antonio nari  o','antonio narino').str.replace('antonio nari o','antonio narino')
    
    df.drop_duplicates(inplace=True)
    
    return df
