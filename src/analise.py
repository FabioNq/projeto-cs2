#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
#%%
os.getcwd()

#%%
df_bruto = pd.read_csv("projeto_cs2/dados/dados_Furia_2026.csv", sep=';')

#%%
df_bruto.head()

#%%
df_bruto.info()

#%%
#RESUMINDO NOME JOGADORES
df_bruto['FURIA'] = df_bruto['FURIA'].apply(lambda x: x.strip().split()[-1])
    
#%%
df_bruto.head()

#%%
#FUNCOES

#GRAFICO DE LINHA
def graficoLinhaPorJogadores(inf:str):
    """graficoLinhaPorJogadores:função responsavel por gerar o grafico de linha da média do desempenho dos jogadores a partir da variavel passada como parametro.
    
    :param inf: coluna do dataframe que queira realizar  a visualização da média no grafico de linha
    """
    plt.figure(figsize=(12, 6))
    dados = df_analise.groupby(['FURIA','data_jogo'])[['Kills','Deaths','Swing','ADR','KAST','Rating3.0','eK','eD']].mean().reset_index()
    
    for jogador in dados['FURIA'].unique():
        dados_jogador = dados[dados['FURIA'] == jogador]
    # Plota a linha (x = Data, y = Kills ou outra variavel)
        plt.plot(dados_jogador['data_jogo'], 
             dados_jogador[inf], 
             marker='o',        # Adiciona pontos nos dias das partidas
             label=jogador,     # Nome para a legenda
             linewidth=2)       # Espessura da linha
    # descreve informações no grafico, titulo, tamanho e tipo da fonte
    #informacao no eixo x e y 
    plt.title(f'media de {inf} por Jogador', fontsize=14, fontweight='bold')
    plt.xlabel('Data da Partida')
    plt.ylabel('Quantidade de Kills')

    # criacao da legenda, local da legenda por coordenada x,y por posição
    plt.legend(title='Jogadores', bbox_to_anchor=(1.05, 1), loc='upper left') # Legenda fora do gráfico
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.gcf().autofmt_xdate() 
    # Inclina as datas automaticamente para não sobrepor
    plt.tight_layout()
    plt.show()
    
# GRAFICO DE BARRA    
def graficoBarrasPartidas(inf:str):
    """graficoBarrasPartidas:função responsavel por gerar o grafico de Barras da média do desempenho dos jogadores a partir da variavel passada como parametro.
    
    :param inf: coluna do dataframe que queira realizar  a visualização da distribuição do dado de cada jogador.
    """
    
    #cria dataframe recebendo df_analise com a media de cada variavel
    dataframe=df_analise.groupby(['FURIA'])[['Kills','Deaths','Swing','ADR','KAST','Rating3.0','eK','eD','difF_KD']].mean().reset_index()    
    
    #cria o grafico de barra
    fig, ax = plt.subplots()
    bar_container = ax.bar(dataframe['FURIA'],dataframe[inf],color='#2ECC71') 
    
    #condicional só para alterar o eixo y, caso o parametro passado seja a variavel Swing o eixo y vai começar com valor negativo caso contrario o eixo y começa de 0.
    if   inf == 'Swing' or inf == 'difF_KD'  :
        ax.set(ylabel='valor', title=f'media de {inf} por jogador', ylim=(min(dataframe[inf]*1.1),max(dataframe[inf]*1.1)))
        ax.bar_label(bar_container)
        plt.show()   
          
    else:
        ax.set(ylabel='valor', title=f'media de {inf} por jogador', ylim=(0,max(dataframe[inf]*1.1)))
        ax.bar_label(bar_container)
    
        plt.show()   

# BOXPLOT
def gboxplot(data,inf: str,grupo:str):
    """gboxplot:função responsavel por gerar o grafico boxplot e verificar a distribuição dos dados de cada jogador, de acordo com o parametro inf.
    :param inf: coluna do dataframe que queira realizar  a visualização da média no grafico de Barras
    """     
         
    #cria boxplot baseado no dataframe passado pelo parametro inf e agrupado pelo parametro grupo       
    data.boxplot(column=inf,by=grupo,figsize=(10,6)) 
    plt.title(f'Distribuicao {inf} por {grupo}')
    plt.suptitle('')
    plt.xticks(rotation=45, ha='right')        
    plt.ylabel(f"valor {inf}")
    plt.xlabel('')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()


#CORRELACAO 
def gcorrelacao(data,x:float ,y:float):
    """
    função responsavel por verificar a correlação entre duas variaveis.
    :param data: dataframe com as variaveis disponiveis
    :param x: variavel x disponivel no dataframe informado
    :param y: variavel x disponivel no dataframe informado
    """
    
    
    #realiza o calculo do coeficiente de pearson (0.7 ate 1 ou -0.7 ate -1 correlacao forte)
    correlacao = np.corrcoef(df_analise[x], df_analise[y])[0,1]
    
    #cria o grafico de dispersão pelo comando scatter passando o paramentro x e y para verificar a relação entre as duas variaveis.
    plt.figure(figsize=(8, 6))
    plt.scatter(df_analise[x], df_analise[y], color='blue', alpha=0.7)
    plt.title(f'Gráfico de Dispersão(Corr: {correlacao:.2f})')
    plt.xlabel(f'Variável {x}')
    plt.ylabel(f'Variável {y}')
    plt.grid(True)
    plt.show()




#%%
#convertendo a data em texto para formato de data
df_bruto['data_jogo'] = df_bruto['data_jogo'].str.replace(r'(st|nd|rd|th|of)','',regex=True)
df_bruto['data_jogo'] = pd.to_datetime(df_bruto['data_jogo']) 

#%%
df_bruto.info()

#%%
#convertendo as colunas swing, kast e ekast em float
colunas_com_porcentagem = ['Swing','KAST','eKAST']
for col in colunas_com_porcentagem:
    df_bruto[col] = df_bruto[col].str.replace('%','').astype(float)

df_bruto.info()
#%%
#separar  K-D e eK-eD em duas colunas diferentes K,D e eK,eD
df_bruto[['Kills','Deaths']] = df_bruto['K-D'].str.split('-',expand=True).astype(int)
df_bruto[['eK','eD']] = df_bruto['eK-eD'].str.split('-',expand=True).astype(int)
df_bruto.info()

#%%
df_bruto.drop(['K-D', 'eK-eD',], axis=1, inplace=True)

#%%
#utiliza dataframe df_analise para realização de mudanças
df_analise = df_bruto.copy()

df_analise['difF_KD'] = df_analise['Kills'] - df_analise['Deaths']



#%%
df_analise.to_csv('dado_Furia_Ajustado.csv',sep=';',index=False)


#%%
#Funcao melhor mapa do jogador
def melhormapajogador(nomejogador:str,variavelDesempenho:str):
    df_desempenhoPorMapa = df_analise.groupby(['FURIA','mapa'])[['Kills','Deaths','ADR','Swing','KAST','Rating3.0']].max().reset_index()
    
    df_filtro = df_desempenhoPorMapa[df_desempenhoPorMapa['FURIA'] == nomejogador]
    
    max_filtro = df_filtro[variavelDesempenho].max()
    df_maxDesempenho = df_filtro[df_filtro[variavelDesempenho] == max_filtro]
    
    df_final = pd.DataFrame(df_maxDesempenho)
    return df_final

#%%
#Funcao lista de melhor mapa dos jogadores
def listamelhormapajogadores(metrica):
    df_nomes = df_analise['FURIA'].copy()
    df_nomes = df_nomes.drop_duplicates().reset_index()
    df_melhorMapaJogadores = pd.DataFrame()
    for i in df_nomes['FURIA']:
        df_melhorMapaJogadores = pd.concat([df_melhorMapaJogadores,pd.DataFrame(melhormapajogador(i,metrica))],ignore_index=True)
    return df_melhorMapaJogadores



#Melhor desempenho por mapa (menos a métrica Deaths pode ser o pior d)
#%%
listamelhormapajogadores('Kills')

#%%
listamelhormapajogadores('ADR')

#%%
listamelhormapajogadores('KAST')

#%%
listamelhormapajogadores('Rating3.0')

#%%
listamelhormapajogadores('Swing')

############### GRAFICOS DE LINHA ###############

#%%
#comparativo media de kills por jogador
graficoLinhaPorJogadores('Kills')

#%%
#comparativo media de mortes por jogador 
graficoLinhaPorJogadores('Deaths')

#%%
#media ADR
graficoLinhaPorJogadores('ADR')

#%%
#mediana Swing
graficoLinhaPorJogadores('Swing')

#%%
#media KAST
graficoLinhaPorJogadores('KAST')

#%%
graficoLinhaPorJogadores('Rating3.0')

#%%


############### GRAFICOS BOXPLOT ###############


#%%
gboxplot(df_analise,'Swing','mapa')

#%%
gboxplot(df_analise,'Kills','mapa')

#%%
gboxplot(df_analise,'Deaths','mapa')


#%%
gboxplot(df_analise,'ADR','mapa')

#%%
gboxplot(df_analise,'KAST','mapa')

#%%
gboxplot(df_analise,'Rating3.0','mapa')

#%%
gboxplot(df_analise,'difF_KD','mapa')


#%%
gboxplot(df_analise,'difF_KD','FURIA')



#################  GRAFICO DE BARRA ###################

#%%
graficoBarrasPartidas('Kills')

#%%
graficoBarrasPartidas('Deaths')

#%%
graficoBarrasPartidas('Swing')

#%%
graficoBarrasPartidas('KAST')

#%%
graficoBarrasPartidas('ADR')

#%%
graficoBarrasPartidas('Rating3.0')

#%%
graficoBarrasPartidas('difF_KD')

############ CORRELACAO ################

#%%
gcorrelacao(df_analise,'Swing','difF_KD')

