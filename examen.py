#Importamos las libererías necesarioas
from pandas import panda as pd 


#Lectura de archivos csv con panda 
df_navegaciones = pd.read_csv(r"navegaciones.csv", sep = ";")
df_conversiones = pd.read_cv(r"conversiones.csv", sep=";")