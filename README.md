## 🎮 Projeto: Análise de Desempenho de Jogadores - CS2

📝 Visão Geral
Este projeto tem como objetivo realizar a extração via webScraping do site Hltv e analisar dados de desempenho dos jogadores de Counter-Strike 2 da Furia no campeonato Blast-Bounty-season-1-2026



## Dicionario de Dados 

| Colunas | Tipo | Função | 
| :--- | :--- | :--- |
| **FURIA** | `string` | coluna na qual tem os nomes dos jogadores | 
| **mapa** | `string` |  coluna com a informação do mapa que foi jogado |
| **Kills** | `int` | coluna informa o numero de inimigos abatidos do jogador |
| **Deaths** | `int` | coluna informa o numero de mortes do jogador | 
| **Swing** | `float` | coluna que represente o quanto em media em %, o jogador mudou o round baseado na economia do time, lado(CT ou TR), Kills, Deaths, Dano, Trocas, assistencia de Flash bang |                     
| **ADR** | `float` | coluna que representa a média de dano por round |
| **KAST** | `float` | coluna que representa a  contribuição de um jogador em % por round, no qual fez kill,assitencia,sobreviveu ou foi eliminado e o companheiro vingou a morte em sequencia |  
| **Rating3.0** | `float` | coluna que representa  se o desempenho do jogador foi acima ou abaixo da média 1.0 representa a média.



🚀 Objetivos
verificar a média dos jogadores em relação a todas as partidas
verificar qual melhor mapa da equipe
verificar qual o melhor mapa de cada jogador
verificar desempenho a cada dia de campeonato.


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

### Analise dos dados 







💡 Próximos Passos
- [ ] Tarefa concluída [ ] adquirir mais dados durante os campeonatos de 2026 e fazer .
- [ ] Criar um Dashboard interativo usando Streamlit.
- [ ] criar um modelo de machine learning a partir do desempenho da equipe no ano de 2025 e verificar como será o desempenho da equipe em 2026.

](https://github.com/FabioNq/projeto-cs2/edit/main/README.md)
