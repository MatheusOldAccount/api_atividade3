from aula_07_parte_2_persistencia_banco_dados.api_atividade.models import Pessoas, Usuarios



# Insere dados na tabela pessoa
def insere_pessoas():
    # pessoa = Pessoas(nome='Rafael', idade=29)
    pessoa = Pessoas(nome='Galeani', idade=25)
    print(pessoa)
    pessoa.save()


# Realiza consulta na tabela pessoa
def consulta_pessoas():
    # pessoa = Pessoas.query.all()
    '''
    pessoa = Pessoas.query.all()
    for i in pessoa:
        print(i.nome)
    '''
    """pessoa = Pessoas.query.filter_by(nome='Galeani')
    for p in pessoa:
        print(p)
    # print(pessoa)"""
    # pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    # print(pessoa.idade)
    # pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    # print(pessoa.idade)
    pessoa = Pessoas.query.all()
    for i in pessoa:
        print(i.nome)


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.idade = 21
    '''pessoa = Pessoas.query.filter_by(nome='Galeani').first()
    pessoa.nome = "Felipe" '''
    pessoa.save()


# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galeani').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('rafael', '1234')
    insere_usuario('galeani', '4321')
    consulta_todos_usuarios()
'''    exclui_pessoa()
    consulta_pessoas()'''

