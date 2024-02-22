from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'rafael': '123',
#     'ana': '321'
# }

@auth.verify_password
def verificacao(login, senha):
    #print(USUARIOS.get(login) == senha)
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()
    

class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()
            response = {"nome": pessoa.nome,
                        "idade": pessoa.idade,
                        "id": pessoa.id}
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada'
            }

        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }        
        return response
    
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        mensagem = 'Pessoa {} exluida com sucesso'.format(pessoa.nome)
        return mensagem
    
class ListaPessoas(Resource):
    def post(self):
        pessoa = request.json
        print(pessoa['nome'])
        p = Pessoas(nome = pessoa['nome'], idade = pessoa['idade'])
        p.save()

    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        print(response)
        return jsonify(response)
    
class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        print(atividades)
        response = [{'id': i.id, 'nome': i.nome , 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response
    
    def delete(self):
        dados = request.json
        atividade = Atividades.query.filter_by(nome=dados['nome']).first()
        atividade.delete()

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/listapessoas/')
api.add_resource(ListaAtividades, '/atividades')


if __name__ == '__main__':
    app.run(debug=True)