import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Limpar console
os.system('CLS')

# Titulo da aplicação
st.title("Dashboard simples de vendas")

# Carregar os dados
df = pd.read_csv("vendas_visualizacao_basica_com_nomes.csv")

#Tratando os dados
df["data_compra"] = pd.to_datetime(df['data_compra'], errors='coerce')
df = df.sort_values(by="data_compra", ascending=True)
df["mes"] = df["data_compra"].dt.to_period("M").astype(str)

st.sidebar.title("Filtros")
produtos = df["produto"].unique().tolist()
produto_selecionado = st.sidebar.multiselect(
    "Selecione o(s) produto(s):",
    options=produtos,
    default=produtos
)

# >>> ALTERAÇÃO: DATAFRAME FILTRADO COM BASE NO FILTRO
df_filtrado = df[df["produto"].isin(produto_selecionado)]

#1) Linha - Faturamento ao longo do tempo
fat_produto = df_filtrado.groupby("mes")["faturamento"].sum().reset_index()

fig, eixo = plt.subplots()
eixo.plot(fat_produto["mes"], fat_produto["faturamento"])

eixo.set_title("Faturamento ao longo do tempo")
eixo.set_xlabel("Data")
eixo.set_ylabel("Faturamento (R$)")

plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

#2) Barras - Faturamento por produto
fat_produto = df.groupby("produto")["faturamento"].sum().reset_index()

fig, eixo = plt.subplots()
eixo.bar(fat_produto["produto"], fat_produto["faturamento"])

eixo.set_title("Faturamento por produto")
eixo.set_xlabel("Produto")  
eixo.set_ylabel("Faturamento (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

#3) Dispersão - Quantidade x Faturamento
fig, eixo = plt.subplots()

eixo.scatter(df["quantidade"], df["faturamento"])

eixo.set_title("Quantidade x Faturamento")
eixo.set_xlabel("Quantidade")
eixo.set_ylabel("Faturamento (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

#4) Histograma - Distribuição do faturamento
fig, eixo = plt.subplots()

plt.figure()
sns.histplot(df["faturamento"], bins=20, kde=True)

eixo.set_title("Distribuição do faturamento")
eixo.set_xlabel("Faturamento (R$)")
eixo.set_ylabel("Frequência")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt.gcf())
plt.close()

#X) Boxplot - Distribuição do faturamento
#plt.figure()
#sns.boxplot(x=df["faturamento"])
#plt.title("Boxplot do faturamento")
#st.pyplot(plt.gcf())
#plt.close()

#5) Boxplot - Distribuição do faturamento sem outliers
fig, ax = plt.subplots(figsize=(10, 2))
sns.boxplot(x=df["faturamento"], showfliers=False, ax=ax)
ax.set_title("Boxplot do faturamento (sem outliers)")
st.pyplot(fig)
plt.close(fig)