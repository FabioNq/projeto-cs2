
from seleniumbase import Driver
from selenium.webdriver.common.by import By
import pandas as pd
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://www.hltv.org/results?team=8297"

#Criacao dos dataframes que serão utilizados para inserir os dados no final
df = pd.DataFrame()
df_dados_players = pd.DataFrame()
andandorTabelas=3

# Aqui estamos pedindo ao driver para abrir o navegador chrome
navegador = Driver(uc=True)
# Abrindo o site que queremos extrair as informações
navegador.get(url)
# Selecionando todos os elementos que são stats-button
all_matches = navegador.find_elements(By.CLASS_NAME,'a-reset')

#blast-bounty-2026-season-1
# Agora sim selecionando todos os links que tem partidas disponíveis
all_matches = [link.get_attribute('href') for link in all_matches]
#'blast-bounty-2026-season-1'
#buscando apenas as partidas realizadas na Blast-bounty 2026
links_das_partidas_blast = []
for match in all_matches:
    if re.search(r'blast-bounty-2026-season-1', match):
        links_das_partidas_blast.append(match)
        print(match)
    else:
        break

#for para percorrer todas as partidas jogadas
for link in links_das_partidas_blast:
    navegador.get(link)
    
    #Selecionando o menu com o nome dos mapas  
    total_mapas = navegador.find_element(By.XPATH,'//*[@id="match-stats"]/div[2]').text
    
    #limpa os nomes do menu que não serão utilizados, como All maps e Detailed stats
    limpo = total_mapas.replace("All maps", "").replace("Detailed stats", "").strip()
    
    #cria uma lista com o nome dos mapas recolhidos no menu 
    lista_mapas=limpo.split()
    
    #cria uma variavel que será utilizada como contador para percorrer por cada um deles. 
    qtdTotalMapas = len(lista_mapas)
    
  
    #for para percorrer todos os mapas jogados 
    for i in range(qtdTotalMapas):
        navegador.find_element(By.XPATH,f'//*[@id="match-stats"]/div[2]/div[1]/div[{i+2}]/div').click()
        
        
        
        #Data do jogo 
        
        
        #variavel que pega o nome do mapa para poder inserir ao dataFrame
        nome_mapa = navegador.find_element(By.XPATH,f'//*[@id="match-stats"]/div[2]/div[1]/div[{i+2}]/div').text
        
        data_jogo = navegador.find_element(By.XPATH, 
        '/html/body/div[3]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]').text
        print(data_jogo)
        
        #cria variavel na qual guarda a pagina em html
        tabela_elemento = WebDriverWait(navegador, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="match-stats"]'))
        )
        
        
        #cria uma variavel na qual guarda a pagina em html.
        html_da_tabela = tabela_elemento.get_attribute('outerHTML')
    
        #ler pagina html guardada pela variavel html_da_tabela,e busca apenas as tabelas que possuem o nome FURIA,pois só queremos buscar apenas de status da Furia por mapa. 
        df = pd.read_html(html_da_tabela,header=0,match='FURIA')[andandorTabelas]
        print("valor de i:", i)
        print("valor total mapas:",len(lista_mapas))
        print("valor andadorTabelas",andandorTabelas)
        
        #cria nova coluna no dataframe para 
        df['mapa'] = nome_mapa
        df['data_jogo'] = data_jogo
        
         #condicional para acessar cada tabela e linkar com os mapas que foram jogados, o andadadorTabelas é para buscar o indice das tabelas que eu quero.  
        if len(lista_mapas) != i+1:
            andandorTabelas += 3     
        else:
            andandorTabelas = 3
            
        #vai adicionando as tabelas encontradas ao dataframe df_dados_players.    
        df_dados_players = pd.concat([df,df_dados_players],ignore_index=True)
 
#fecha o navegador do selenium
navegador.close()


#exporta o dataframe a um csv.
df_dados_players.to_csv("dados_Furia_2025.csv",sep=';',index=False)