# FORMULÁRIO CLASSIFICAÇÃO DE CLIENTE

Realizei um projeto que tem como objetivo gerar uma classificação (BOM, MÉDIO, RUIM) para o cliente inserido no formulário.   
Após preencher o formulário, terá um retorno da sua classificação e automaticamente os dados desse cliente será inserido no arquivo csv. 

### CAMPOS DO FORMULÁRIO
Esses são os campos e as referências de dados que utilizei:

- Nome
- Idade (Entre 18 e 70 anos)
- Renda Mensal (Entre R$1.000 a R$20.000)
- Histórico de Dívidas (Sim/Não)
- Valor das últimas compras (Entre R$100 a R$5.000)
- Atrasos em Pagamentos (Entre 0 a 90 dias)
- Score de Crédito (Entre 300 a 850)


Gerei em torno de 200 dados fictícios com todos os campos preenchidos, inclusive o de classificação, que ficaram armazenados em um arquivo csv.  

### ESTRUTURA DO PROJETO

- Na pasta projeto -> static : Encontra-se dois arquivos, o script.js - usado para enviar/receber os dados e o styles.css - responsável pela estilização do formulário.
- Na pasta projeto -> templates : Encontra-se os arquivos index.html e resultado.html - responsáveis pela estrutura do formulário.
- No arquivo app.py, foi utilizado o Flask (micro-framework), no qual foi possível fazer a integração do modelo de IA treinado e o formulário, para ser possível gerar uma classificação. 
- O arquivo modelo_ml.pkl é o arquivo de treinamento da IA já pronto para ser utilizado no Flask.  
- Por último, o arquivo treinamento.py - onde foi feito o processo de treinamento como, remoção de colunas, correção dos dados e testes de acurácia. 

### BIBLIOTECAS UTILIZADAS
Durante o desenvolvimento do projeto utilizei as seguintes bibliotecas:

- scikit-learn : especifica para o machine learning, no qual utilizei o algoritmo RandomForest para estudar o arquivo e fazer suas previsões. 
- pandas : utilizada para ler os arquivos em csv.
- pickle : utilizada para pegar o modelo treinado e salvar em um arquivo, para quando utilizá-lo, carregar dentro de outro arquivo e funcionar normalmente. 

![Image](https://github.com/user-attachments/assets/3be389e2-0625-44cc-9595-5581f498f4f9)