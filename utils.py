from models import Pessoas, Atividades, db_session, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Antonio', idade=25)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    for i in pessoa:
        print(i)

def consulta_pessoa_nome():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)


def altera_pessoa():
    p2 = Pessoas.query.filter_by(nome='Rafael').first()
    p2.nome = 'Felipe'
    p2.save()

def deleta_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Pedro').first()
    pessoa.delete()

def insere_atividade():
    atividade = Atividades(nome='Estudar', pessoa_id=1)
    pessoa = Pessoas.query.filter_by(id=atividade.pessoa_id).first()
    print(pessoa)
    if pessoa:
        db_session.add(atividade)
        db_session.commit()
    else:
        print("Pessoa nao existe")

def consulta_atividade():
    atividades = Atividades.query.all()
    for i in atividades:
        print(i)

def insere_usuario(login, senha):
    usuario = Usuarios(login= login, senha = senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':

    insere_usuario('paulo', '1234')
    insere_usuario('ana', '321')
    consulta_todos_usuarios()
    # consulta_pessoas()
    # insere_pessoas()
    # consulta_pessoas()
    #altera_pessoa()
    #deleta_pessoa()
    #insere_atividade()
    #consulta_atividade()