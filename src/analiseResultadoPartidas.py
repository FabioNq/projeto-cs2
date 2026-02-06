#%%
import pandas as pd

#%%
df = pd.read_csv('projeto_cs2/dados/resultados_Furia2.csv',sep=';')

#%%
df = df.drop('Event.1',axis=1)
#%%
df.info()
