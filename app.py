from flask import Flask, json, jsonify, request

app = Flask(__name__)

desenvolvedores = [{
    'id': 0,
    'nome': 'Ana',
    'linguagens': ['C', 'Java']

}, {
    'id': 1,
    'nome': 'Pedro',
    'linguagens': 'Python'
}]

@app.route('/')
def hello():
    return 'Hello'

@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_dev_by_id(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        
        except IndexError:
            mensagem = f'Desenvolvedor de id {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}

        return jsonify(response)
    
    elif request.method == 'PUT':
        try:
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return jsonify(dados)
        except:
            return 'Erro'

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro exluído'}
    
@app.route('/dev', methods=['POST', 'GET'])
def devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    if request.method == 'GET':
        return desenvolvedores

if __name__ == '__main__':
    app.run(debug= True)