import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

st.set_page_config(page_title='projeto cs2',page_icon=':gun:')


# criando side bar
st.sidebar.title("Filtro:")



st.markdown("""

# Projeto Analise de dados Jogadores da Furia CS2 na Blast Bounty 2026            

""")


file_upload = st.file_uploader(label="Faça upload dos dados aqui",type=['csv'])

stt1,stt2 = st.columns(2)
 
df = pd.DataFrame()

#Verifica se algum arquivo foi feito um upload
if file_upload:
   df = pd.read_csv(file_upload,
   sep=';')
   df['data_jogo'] = pd.to_datetime(df['data_jogo'])
   st.markdown("### métricas de desempenho dos jogadores:")
   filtro_dinamico = DynamicFilters(df, filters=['FURIA', 'mapa'],
   )
   filtro_dinamico.display_filters(location='sidebar')

   kills,deaths,adr = st.columns(3) 
   swing,rating,kast = st.columns(3)    

   df_dinamico = filtro_dinamico.filter_df()
    
  
   
  
   kills.metric("Total Kills",df_dinamico['Kills'].sum(), border=True)
   deaths.metric("Total Deaths", df_dinamico['Deaths'].sum(), border=True)
   adr.metric("média ADR", df_dinamico['ADR'].mean(), border=True)
   kast.metric("média KAST", df_dinamico['KAST'].mean(),format="%.2f", border=True)
   swing.metric("média swing", df_dinamico['Swing'].mean(),format="%.2f", border=True)
   rating.metric("média rating",df_dinamico['Rating3.0'].mean(),format="%.2f", border=True)    
   

   st.subheader("média de Swing por Partida:")

   chart_data = df_dinamico.pivot_table(index='data_jogo', columns='FURIA', values='Swing')


   #chart_data = df_dinamico.groupby('data_jogo')[['Kills']].sum()
   
   st.line_chart(chart_data)
   
   st.subheader("média de Kills Jogador")
   bar_data = df_dinamico.groupby('FURIA')[['Kills']].mean()
   
   st.bar_chart(bar_data)