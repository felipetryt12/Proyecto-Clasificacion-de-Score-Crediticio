import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 


pd.set_option('display.max_columns', 33)




#Funcion para 
def analisis_grafico_variables_numericas(df):
    columna_numerica= df.select_dtypes(include=['number'])
    for columna in columna_numerica:
        plt.figure(figsize=(15,10))
        plt.subplot(1,3,1)
        sns.histplot(df[columna].dropna(), kde=True, bins=30)
        plt.title(f'Distrubucion de {columna}')
        plt.xlabel(columna)
        plt.ylabel('Frecuencia')
        
        plt.subplot(1,3,2)
        sns.boxplot(x=df[columna].dropna())
        plt.title(f'Boxplot de {columna}')
        plt.xlabel(columna)
        
        plt.subplot(1,3,3)
        sns.kdeplot(df[columna].dropna(), fill=True)
        plt.title(f'Grafico de densidad de {columna}')
        plt.xlabel(columna)
        plt.ylabel('Densidad')
        
        plt.tight_layout()
        plt.show()
        
#Calcula las frecuencias de todas las variables categoricas
def calculo_frecuencia_var_categoricas(df):
    resultados = {}
    
    for columna in df.select_dtypes(include='object').columns:
        absoluta = df[columna].value_counts()
        relativa = df[columna].value_counts(normalize=True)
        
        df_frecuencia = pd.DataFrame({
            'Variable': columna,
            'Categoría': absoluta.index,
            'Frecuencia Absoluta': absoluta.values,
            'Frecuencia Relativa': relativa.values
        })
        
        resultados[columna] = df_frecuencia
    
    return resultados

#Muestra las frecuencias de todas las variables categoricas en forma
#de data frame para cada una, funciona en conjunto con calculo de frecuencias

def mostrar_frecuencia_categoricas(df):
    df_frecuencia_total = calculo_frecuencia_var_categoricas(df)
    
    for columna, df_frecuencia in df_frecuencia_total.items():
        print(f"Tablero de frecuencias de la característica: {columna}")
        display(df_frecuencia)
    
    return df_frecuencia_total




