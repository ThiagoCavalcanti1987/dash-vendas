
# 📊 Dashboard Interativo de Vendas

Este projeto implementa um **dashboard interativo para análise de dados de vendas**, desenvolvido em **Python** utilizando **Streamlit**, **Pandas**, **Matplotlib** e **Seaborn**.  
O objetivo é demonstrar, de forma prática, as etapas de **importação, tratamento, análise exploratória e visualização de dados** aplicadas a um contexto de negócios.

---

## 🎯 Objetivo do Projeto

Construir um dashboard interativo para análise de faturamento, permitindo:
- Visualizar a evolução do faturamento ao longo do tempo
- Comparar o faturamento por produto
- Analisar a relação entre quantidade vendida e faturamento
- Observar a distribuição dos valores de faturamento
- Interagir com os dados através de filtros no dashboard

Este projeto faz parte da disciplina de **Análise e Visualização de Dados**.

---

## 🧰 Tecnologias Utilizadas

- Python 3.9+
- Streamlit (dashboard interativo)
- Pandas (tratamento e manipulação de dados)
- Matplotlib (gráficos)
- Seaborn (visualizações estatísticas)

---

## 📂 Estrutura do Projeto

```
dashboard-vendas/
│
├── atividade_final.py
├── vendas_visualizacao_basica_com_nomes.csv
└── README.md
```

---

## 📄 Dataset

O arquivo `vendas_visualizacao_basica_com_nomes.csv` contém os dados de vendas, as seguintes colunas:

- `data_compra`: data da compra
- `produto`: nome do produto
- `quantidade`: quantidade vendida
- `faturamento`: valor da venda

Esses dados são utilizados para gerar as análises e visualizações apresentadas no dashboard.

---

## 🔍 Tratamento e Análise dos Dados

No projeto, são realizadas as seguintes etapas:

- Conversão da coluna de datas para o formato `datetime`
- Ordenação cronológica dos registros
- Criação da variável `mes` para agregações temporais
- Análise exploratória com estatísticas descritivas (ex.: média, mediana, quartis)
- Agrupamentos por mês e por produto para análise de faturamento

---

## 📈 Visualizações Implementadas

O dashboard apresenta os seguintes gráficos:

1. **Faturamento ao longo do tempo (linha)**
2. **Faturamento por produto (barras)**
3. **Quantidade x Faturamento (dispersão)**
4. **Distribuição do faturamento (histograma)**
5. **Boxplot do faturamento (sem outliers)**

---

## 🎛️ Interatividade e Filtros

O dashboard possui **filtro funcional por produto**, permitindo que o usuário selecione quais produtos deseja visualizar.  
Todos os gráficos são atualizados dinamicamente de acordo com o filtro selecionado, caracterizando a interatividade do dashboard.

---

## ▶️ Como Executar o Projeto Localmente

### 0️⃣ Instalar Python
Certifique-se de ter o **Python 3.9+** instalado em sua máquina. Você pode baixar e instalar o Python a partir do site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 1️⃣ Instalar as dependências
```bash
python -m pip install streamlit pandas matplotlib seaborn
```

### 2️⃣ Clonar o repositório

```bash
git clone https://github.com/ThiagoCavalcanti1987/dash-vendas.git
cd dashboard-vendas
python -m streamlit run atividade_final.py
```
