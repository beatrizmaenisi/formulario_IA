import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle 

#Importando a base de dados
tabela = pd.read_csv("clientes.csv")
#print(tabela.head())

#Preparação dos dados
    #Remoção das colunas que não são úteis
tabela_nova = tabela.drop(["ID_Cliente","Nome"],axis=1)
    #Conversão da coluna 'Histórico de dívidas' em números (0 - Não, 1 - Sim) 
tabela_nova["Histórico de Dívidas"] = tabela_nova["Histórico de Dívidas"].replace({"Sim":1,"Não":0}).astype(int)
    #Conversão da coluna 'Classificação' em números (Ruim - 0, Médio - 1, Bom - 2)
tabela_nova["Classificação"] = tabela_nova["Classificação"].replace({"RUIM":0,"MÉDIO":1,"BOM":2}).astype(int)
#print(tabela_nova.dtypes)

#Separando os dados em treino e teste
x  = tabela_nova.drop(columns=["Classificação"])
y = tabela_nova["Classificação"]

x_treino, x_teste, y_treino, y_teste = train_test_split(x,y,test_size=0.2,random_state=42)

#Usando o algoritmo Random Forest
modelo_arvore = RandomForestClassifier(n_estimators=100,random_state=42)
modelo_arvore.fit(x_treino,y_treino)

#Testando
previsao_arvore = modelo_arvore.predict(x_teste)
precisao_arvore = accuracy_score(y_teste,previsao_arvore)
#print(f"Precisão do modelo: {precisao_arvore*100:.2f}")

#Testando
# novo_cliente =[[30,8000,0,1200,1,520]]
# resultado = modelo_arvore.predict(novo_cliente)
# traducao = {0: "RUIM",1:"MÉDIO",2:"BOM"}
# print(f"Classificação do cliente: {traducao[resultado[0]]}")

#Salva o modelo treinado
with open("modelo_ml.pkl","wb") as arquivo: pickle.dump(modelo_arvore,arquivo)