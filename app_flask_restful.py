from flask import Flask, json, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [{
    'id': 0,
    'nome': 'Ana',
    'linguagens': ['C', 'Java']

}, {
    'id': 1,
    'nome': 'Pedro',
    'linguagens': 'Python'
}]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de id {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}

        return response
    
    def put(self, id):
        try:
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return dados
        except:
            return 'Erro'

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro exluído'}
    
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    
api.add_resource(Desenvolvedor, '/dev/<int:id>')     
api.add_resource(ListaDesenvolvedores, '/dev/')  

if __name__ == '__main__':
    app.run(debug=True)