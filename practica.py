# consume los datos del archivo de inversiones
# almacena en un dataframe el NOM_EMS, la superficie y el TIPUSSOL
# gráfico de dispersión de los importes de inversiones por TIPUSSOL
# gráfico de barras de la inversión media de los 10 primeros NOM_ENS
# grafico circular de las inversiones de 10 TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt

def consumirSuelo():
    datos=pd.read_csv('suelo.csv')
    print(datos)
    df= datos [['NOM_ENS','SUPERFICIE', 'TIPUSSOL']]
    print (df)

consumirSuelo()

def consumirDispersion():
    datos=pd.read_csv('suelo.csv')
    print(datos)
    df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL','EXTRACCIO']]
    print(df)
    df.plot.scatter(x="EXTRACCIO",y="SUPERFICIE", alpha=0.3)
    plt.show()

consumirDispersion()

def consumirDispersion():
    datos=pd.read_csv('suelo.csv')
    print(datos)
    df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL','EXTRACCIO']]
    print(df)
    df.plot.scatter(x="EXTRACCIO",y="SUPERFICIE", alpha=0.3)
    plt.show()

consumirDispersion()


