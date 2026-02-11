## 🎮 Projeto: Análise de Desempenho de Jogadores - CS2

📝 Visão Geral
Este projeto tem como objetivo realizar a extração via webScraping do site Hltv e analisar dados de desempenho dos jogadores de Counter-Strike 2 da Furia no campeonato Blast-Bounty-season-1-2026

## 🛠️ Tecnologias e Dependências

O projeto foi desenvolvido utilizando o ecossistema Python, focando em automação de coleta de dados (Web Scraping) e análise estatística.

### 🧰 Stack Principal
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Selenium](https://img.shields.io/badge/-selenium-%2343B02A?style=for-the-badge&logo=selenium&logoColor=white)

### 📋 Versões das Bibliotecas

| Tecnologia | Versão | 
| :--- | :--- |
| **Python** | `3.14.2` |
| **Pandas** | `3.0.0` | 
| **NumPy** | `2.4.2` | |
| **Matplotlib** | `3.10.8` |
| **Selenium** | `4.40.0` | 
| **SeleniumBase** | `4.46.0` |
---

### ⚙️ Instalação das Dependências

Para replicar o ambiente deste projeto, você pode instalar todas as bibliotecas de uma vez utilizando o gerenciador de pacotes `pip`:

`bash`

`pip install -r requirements.txt` 



## 🚀 Objetivos
verificar a média dos jogadores em relação a todas as partidas
verificar qual melhor(es) mapa(s) da equipe
verificar qual o melhor mapa de cada jogador


## Dicionario de Dados 

| Colunas | Tipo | Função | 
| :--- | :--- | :--- |
| **FURIA** | `string` | coluna na qual tem os nomes dos jogadores | 
| **data_jogo** | `datetime` | coluna na qual informa a data da partida |
| **mapa** | `string` |  coluna com a informação do mapa que foi jogado |
| **Kills** | `int` | coluna informa o numero de inimigos abatidos do jogador |
| **Deaths** | `int` | coluna informa o numero de mortes do jogador | 
| **Swing** | `float` | coluna que represente o quanto em media em %, o jogador mudou o round baseado na economia do time, lado(CT ou TR), Kills, Deaths, Dano, Trocas, assistencia de Flash bang |                     
| **ADR** | `float` | coluna que representa a média de dano por round |
| **KAST** | `float` | coluna que representa a  contribuição de um jogador em % por round, no qual fez kill,assitencia,sobreviveu ou foi eliminado e o companheiro vingou a morte em sequencia |  
| **Rating3.0** | `float` | coluna que representa  se o desempenho do jogador foi acima ou abaixo da média 1.0 representa a média.




## Analise dos dados: 

no dia 16/01/2026 a equipe de CS2 Furia realizou seu primeiro campeonato do ano a Blast Bounty 2026, neste campeonato a Furia realizou 4 partidas e jogou 10 mapas, 
chegando até a semifinal do campeonato, então a partir desse momento resolvi realizar a analise dos dados do desempenho dos jogadores da Furia por mapa, independente da vitória ou da derrota.

começando com a analise de desempenho por jogos, fiz um grafico bloxplot para verificar como estão distribuidos os dados de cada jogador baseado em suas Kills,Deaths,ADR,KAST,Rating3,0 e Swing
deixei na imagem abaixo a distribuição dos dados baseado no Swing pois contribui bastante para saber se o jogador desempenhou bem ou não durante o jogo. 

<img width="878" height="563" alt="distribuicao por Jogador" src="https://github.com/user-attachments/assets/704d6e7c-181c-4c2e-851b-3890b0d71f45" />

o boxplot é ótimo para verificar a distribuição dos dados dos jogadores, mostra a consistencia de cada jogador, um destaque para o jogador Molodoy, a caixa do boxplot representando o jogador é grande, representando o quanto ta
espalhado os dados variando do percentil 25% entre -1 ou -2  e o percentil 75% em 8 ou 9, com seu limite superior chegando a 10 e o limite inferior em -5. outro ponto é a linha de 50% está acima da média, ou seja em algum mapa ou partida 
o desempenho do molodoy puxou sua média para baixo, isso também acontece com o jogador Yekindar no qual seu percentil de 50% está acima da média. 


Alem de fazer o boxplot por jogadores fiz também um para saber a distribuição do desempenho por mapa para verificar qual o mapa que a equipe desempenhou melhor.

<img width="878" height="558" alt="distribuicao por mapa" src="https://github.com/user-attachments/assets/fa9d377c-3a30-4bc8-ac9e-5f67657e5ccc" />

verificando o boxplot entre o desempenho da equipe entre os mapas, temos destaque positivos nos mapa Dust e Nuke e inferno no qual o percentil 50% todos estão acima do 0 de swing então possui uma contribuição maior da equipe. 
ja os mapas overpass e Mirage foram destaques negativos, no qual toda a caixa do boxplot está abaixo do  Swing 0, então a % de um jogador mudar o rumo da partida não aconteceram nesses dois mapas.


Analisando os dados através do grafico de Linha durante os dias de competição temos : 



### Grafico de Linha Média de Kills geral por Jogador:
<img width="1190" height="590" alt="media de Kills" src="https://github.com/user-attachments/assets/bbb965f8-78c6-456b-b137-37305731b91c" />


### Grafico de Linha Média de Swing geral por Jogador:
<img width="1190" height="590" alt="media de Swing" src="https://github.com/user-attachments/assets/3155d75a-94a0-4e78-9047-dfcf2658e190" />

mais uma vez destaque para o jogador molodoy que teve excelentes médias de desempenho durante os dias de competição porém na fase semi final seu desempenho foi abaixo do que ele é capaz de desempenhar.



Realizando a analise através do grafico de barras, temos : 

### Média de Kills geral por Jogador:
<img width="576" height="435" alt="média de kills por jogadores" src="https://github.com/user-attachments/assets/137f42ed-d3e5-433a-ac60-91af96221f03" />

### Média de ADR geral por Jogador:
<img width="562" height="435" alt="ADR dos jogadores" src="https://github.com/user-attachments/assets/0f0fef32-ab7a-4baf-aea2-cb5b6638a686" />


### Média de KAST geral por Jogador:
<img width="562" height="435" alt="média KAST por jogadores" src="https://github.com/user-attachments/assets/1b460f36-f2d8-494d-93a2-964715bfbffb" />

### Média de Rating 3.0 geral por Jogador:
<img width="567" height="435" alt="Rating3 0 dos jogadores" src="https://github.com/user-attachments/assets/ff026140-6a13-454d-9042-e6a3ee2ecfa5" />

### Média de Swing geral por Jogador:
<img width="565" height="435" alt="Swing por jogadores" src="https://github.com/user-attachments/assets/0bc669aa-6751-4f41-8050-067e2f3875fd" />


### mapas que os jogadores tiveram melhor desempenho de acordo com o Swing:

<img width="578" height="196" alt="melhor performace por mapa de cada jogador" src="https://github.com/user-attachments/assets/62e9630f-ffde-4e48-a761-b6e5a890a63a" />

Esse dado é muito interessante pois os jogadores YEKINDAR e FalleN mesmo com -1 de diferença em Kills e Deaths ele tiveram uma contribuição para mudar o rumo da partida
e com o KAST de bem elevado contribuindo significante bem no rumo da partida. 


💡 Próximos Passos
- [ ] adquirir mais dados durante os campeonatos de 2026 e fazer mais analises sobre os jogadores.
- [X] Criar um Dashboard interativo usando Streamlit.
- [ ] baseado na extração via WebScraping, realizar a extração de dados dos campeonatos de 2025 e realizar predições para 2026.

 📖 Referências:
- [TeoMeWhy Streamlit](https://www.youtube.com/playlist?list=PLvlkVRRKOYFRYA40hJ_V8e_iC5Lu6YPyn)
- [larissa.eleterio](https://medium.com/@larissa.eleterio/analisando-o-desempenho-de-um-time-de-cs-go-no-campeonato-cs-summit-f641534411e2)
- [Michael Kitas](https://www.youtube.com/watch?v=txsdyYkvj0Y)

    
