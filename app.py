from flask import Flask, jsonify, render_template
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
    #return resposta.json()

#@app.route('/pesquisaclima/<SP>',methods=['GET'])
#def pesquisaclima(SP):
#    url = f'https://api.weatherapi.com/v1/current.json?key=7fdc3dc9c75ab87956c81054efae21be=Sao'
#    resposta = requests.get(url)
#    return resposta.json()

@app.route('/climatempo', methods=['GET'])
def climatempo():
    key = 'c4380707dde242f4b78202712252204'
    cidade = "Presidente Prudente"
    url = f'https://api.weatherapi.com/v1/current.json?key={key}&q={cidade}&lang=pt'
    resposta = requests.get(url)
    result = resposta.json()
    
    temperatura = result['current']['temp_c']
    umidade = result['current']['humidity']
    Região = ['location']['region']
    Horario = ['location']['localtime']
    vis_km = ['current']['vis_km']
    Pressão = ['current']['pressure_mb']

    return render_template('tempo.html',temp=temperatura, umid=umidade, region=Região, localtime=Horario, vis_km=vis, pressure_mb=Pressão )
    #return resposta.json()


if __name__ == '__main__':
        app.run(debug=True)