from flask import Flask, jsonify
import requests
app = Flask(__name__)


@app.route('/hello',methods=['GET'])
def hello():
    return jsonify(message='Olá mundo!'), 200

@app.route('/senai',methods=['GET'])
def senai():
    return jsonify(message='Olá turma python com framework', 
                   message2='Olá como está?'), 200


    if __name__ == '__main__':
        app.run(debug=True)

#endpoint - pesquisar endereço atraves do cep, retorna em formato json
@app.route('/pesquisacep/<cep>',methods=['GET'])
def pesquisacep(cep):
    url = f'http://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    return resposta.json()

@app.route('/pesquisaclima/<SP>',methods=['GET'])
def pesquisaclima(SP):
    url = f'https://api.weatherapi.com/v1/current.json?key=44095951baccdfd271c3b42a49fc7f17=Sao'
    resposta = requests.get(url)
    return resposta.json()