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




# Esta funcion muestra 3 heatmaps para ver el tipo de correlacion de las variables, tomando en cuenta pearson
#spearman y kendall, para identificar magnitud y tipo de correlacion de nuestras caracteristicas con la variable 
#objetivo, se utiliza para identificar el mejor metodo de reduccion de dimensionalidad


def heatmaps_tipo_correlacion(data, variable_objetivo):
    corr_pearson = data.corr(method='pearson')
    corr_spearman = data.corr(method='spearman')
    corr_kendall = data.corr(method='kendall')
    
    cols = [variable_objetivo] + [col for col in data.columns if col != variable_objetivo]
    corr_pearson = corr_pearson.loc[cols, cols]
    corr_spearman = corr_spearman.loc[cols, cols]
    corr_kendall = corr_kendall.loc[cols, cols]
    
    num_columns = len(data.columns)
    fig, axs = plt.subplots(3, 1, figsize=(num_columns * 1.2, 10 + num_columns // 2))
    
    sns.heatmap(corr_pearson, annot=True, cmap='coolwarm', center=0, ax=axs[0],
                cbar_kws={"shrink": 0.8}, linewidths=.5)
    axs[0].set_title('Correlación de Pearson')
    axs[0].get_xticklabels()[0].set_color('red')
    axs[0].get_yticklabels()[0].set_color('red')
    
    sns.heatmap(corr_spearman, annot=True, cmap='coolwarm', center=0, ax=axs[1],
                cbar_kws={"shrink": 0.8}, linewidths=.5)
    axs[1].set_title('Correlación de Spearman')
    axs[1].get_xticklabels()[0].set_color('red')
    axs[1].get_yticklabels()[0].set_color('red')
    
    sns.heatmap(corr_kendall, annot=True, cmap='coolwarm', center=0, ax=axs[2],
                cbar_kws={"shrink": 0.8}, linewidths=.5)
    axs[2].set_title('Correlación de Kendall')
    axs[2].get_xticklabels()[0].set_color('red')
    axs[2].get_yticklabels()[0].set_color('red')
    
    plt.tight_layout()
    plt.show()
