import os
import sqlite3
from sqlite3 import Error

####CONEXÃO

def ConexaoBanco():
    caminho = r'D:\curso Python\SQLite, Banco de dados e tabelas - 27\Banco.db'
    conexao = None
    
    try:
        conexao = sqlite3.connect(caminho)
    except Error as erro:
        print(erro)

    return conexao

# Recebe a conexão do banco de dados
vconexao = ConexaoBanco()

# Percorrer o banco de dados
def query(conexao, sql):
    try: 
        c = conexao.cursor()
        c.execute(sql)
        # Persistência no banco de dados
        conexao.commit()
    except Error as erro:
        print(erro)
    finally:
        print("Operação Realizada com sucesso")
        # Fechar a conexão
        # conexao.close()


# fINALIDADE DE FAZER CONSULTA.
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    # Para fazer a consulta
    resultado = c.fetchall()
    
    return resultado

#### FIM CONEXÃO

def MenuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registros")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")


def menuInserir():
    os.system("cls")

    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+nome+"', '"+telefone+"', '"+email+"')"

    # Chamando a consulta
    query(vconexao, vsql)


def menuDeletar():
    os.system("cls")

    variavel_id = input("Digite o ID do registro a ser deletado: ")
    
    vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO=" + variavel_id
    
    query(vconexao, vsql)
    

def menuAtualizar():
    os.system("cls")

    variavel_id = input("Digite o ID do registro a ser alterado: ")
    
    registro = consultar(vconexao, "SELECT * FROM tb_contatos WHERE N_IDCONTATO=" + variavel_id)

    registro_nome = registro[0][1]
    registro_telefone = registro[0][2]
    registro_email = registro[0][3]

    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    # Caso não decida mudar um dos campos, ficará o registro atual
    if(len(nome) == 0):
        nome = registro_nome
    if(len(telefone) == 0):
        telefone = registro_email
    if(len(email) == 0):
        email = registro_email

    vsql = "UPDATE tb_contatos SET T_NOMECONTATO='"+nome+"', T_TELEFONECONTATO='"+telefone+"', T_EMAILCONTATO='"+email+"' WHERE N_IDCONTATO=" + variavel_id

    query(vconexao, vsql)


def menuConsultar():
    vsql = "SELECT * FROM tb_contatos"

    registro = consultar(vconexao, vsql)
    
    # Limitador e contador
    limite = 10
    contador = 0

    for i in registro:
        print("ID:{0:_<3} Nome:{1:_<30} Telefone: {2:_<14} E_mail:{3:_<30}".format(i[0], i[1], i[2], i[3]))

        contador += 1

        if(contador >= limite):
            contador = 0
            os.system("pause")
            os.system("cls")
    
    print("Fim da lista")
    os.system("pause")


def menuConsultarNomes():
    nome = input("Digite o nome: ")

    vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+nome+"%'"

    registro = consultar(vconexao, vsql)
    
    # Limitador e contador
    limite = 10
    contador = 0

    for i in registro:
        print("ID:{0:_<3} Nome:{1:_<30} Telefone: {2:_<14} E_mail:{3:_<30}".format(i[0], i[1], i[2], i[3]))

        contador += 1

        if(contador >= limite):
            contador = 0
            os.system("pause")
            os.system("cls")
    
    print("Fim da lista")
    os.system("pause")

opcao = 0

while opcao != 6:
    MenuPrincipal()

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        menuInserir()
    
    elif opcao == 2:
        menuDeletar()

    elif opcao == 3:
        menuAtualizar()

    elif opcao == 4:
        menuConsultar()

    elif opcao == 5:
        menuConsultarNomes()

    elif opcao == 6:
        os.system("cls")
        print("Programa finalizado")

    else:
        os.system("cls")
        print("opção invalida")
        os.system("pause")

# Fechamento do banco de dados é importante.
vconexao.close()

os.system("pause")
    