from seleniumbase import Driver
from selenium.webdriver.common.by import By
import pandas as pd
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = 'https://www.hltv.org/stats/teams/matches/8297/furia'

df_resultado_partidas = pd.DataFrame()

navegador = Driver(uc=True)
# Abrindo o site que queremos extrair as informações
navegador.get(url)


#cria variavel na qual guarda a pagina em html
tabela_partidas = WebDriverWait(navegador, 5).until(
EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[6]/div[2]/div[1]/div[2]/table'))
)

#cria uma variavel na qual guarda a pagina em html.
html_da_tabela = tabela_partidas.get_attribute('outerHTML')


df_resultado_partidas = pd.read_html(html_da_tabela)[0]
print(df_resultado_partidas)


navegador.close()

#df_resultado_partidas.to_csv('resultados_Furia2.csv',sep=';',index=False)