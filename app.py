from flask import Flask, render_template, request 
import pickle
import pandas as pd 

app = Flask(__name__, template_folder="projeto/templates", static_folder="projeto/static")

#Carregando o modeo treinado
with open("modelo_ml.pkl","rb") as arquivo: modelo = pickle.load(arquivo)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prever',methods=["POST"])
def prever():
    try:
        df_clientes = pd.read_csv("clientes.csv")
        if not df_clientes.empty:
            ultimo_id = df_clientes["ID_Cliente"].max()
            if isinstance(ultimo_id, str): 
                try:
                  ultimo_id = df_clientes["ID_Cliente"].astype(int).max()
                except ValueError:
                  ultimo_id = 0
            if pd.isna(ultimo_id): 
                ultimo_id = 0
        else:
            ultimo_id = 0
    except FileNotFoundError:
        ultimo_id = 0

    # Incrementa o maior ID
    novo_id = ultimo_id + 1
    id_cliente = str(novo_id)
    nome = request.form["Nome"]
    idade=int (request.form["Idade"])
    renda=float(request.form["Renda Mensal"])
    dividas = request.form["Histórico de Dívidas"]
    if dividas == "Sim":
        dividas = 1
    elif dividas == "Não":
        dividas = 0
    else:
        dividas=-1
    compras=float(request.form["Valor das Últimas Compras"])
    atrasos = int(request.form["Atrasos em Pagamentos"])
    score = int(request.form["Score de Crédito"])

    novo_cliente = pd.DataFrame([[idade, renda, dividas, compras, atrasos, score]],
columns=["Idade","Renda Mensal","Histórico de Dívidas", "Valor das Últimas Compras", 
         "Atrasos em Pagamentos","Score de Crédito"])
    
    novo_cliente.insert(0, "ID_Cliente", id_cliente)
    novo_cliente.insert(1,"Nome",nome)

#Fazendo a previsão
    resultado = modelo.predict(novo_cliente[["Idade", "Renda Mensal", "Histórico de Dívidas", "Valor das Últimas Compras", "Atrasos em Pagamentos", "Score de Crédito"]])
    traducao={0:"RUIM",1:"MÉDIO",2:"BOM"}
    classificacao=traducao[resultado[0]]

    novo_cliente["Classificação"]=classificacao
    novo_cliente.to_csv("clientes.csv",mode="a",header= not pd.io.common.file_exists("clientes.csv"),index=False)
    return render_template("resultado.html", classificacao= classificacao)

if __name__ == '__main__':
    app.run(debug=True)