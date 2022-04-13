import csv
import random
import pyodbc
from datetime import date

# função para formatar o titulo e menu _________________________
def titulo(msg):
    print("=" * 48)
    print(msg.center(48))
    print("=" * 48)


def linha(msg):
    print("=-=" * 16)
    print(msg.center(48), )
    print("=-=" * 16)


def subtitulo(msg):
    print("." * 48)
    print(msg.center(48))
    print("¨" * 48)


def formatar(menu):
    for menu in menu:
        print(menu)


# MANIPULA O BACKGROUD DO PRINT -------------------------------
def bk_gree(msg):
    # cor verde!!!
    print()
    print('\x1b[6;30;42m' + msg.center(48) + '\x1b[0m')
    print()


def bk_white(msg):
    print()
    print("\n\033[47m\033[30m" + msg.center(48) + "\033[0;0m\n")
    print()


def bk_red(msg):
    print()
    print("\n\033[41m\033[30m" + msg.center(48) + "\033[0;0m\n")
    print()


def bk_yellow(msg):
    print()
    print("\n\033[43m\033[30m" + msg.center(48) + "\033[0;0m\n")
    print()


# MANUPULANDO ARQUIVOS --------------------------------------------
def Salvar(arquivo, bd_str):
    with open(arquivo, 'a') as arq:
        arq.write(str(bd_str))
        arq.close()


def visualizar(arquivo,):
    with open(arquivo):
        for linha in visualizar:
            print(linha)


# FUNCIONANDO CSV ------------------------------------------------------
def add_item(base_csv, item):
    with open(base_csv, 'a', newline='', encoding='utf-8') as bd_csv:
        gravar = csv.writer(bd_csv, delimiter=';')
        ide = item[0] = str(random.randrange(1000000, 9000000))
        gravar.writerow(item)


def ler_item(base_csv):
    with open(base_csv, 'r+', newline='') as bd_csv:
        ler = csv.reader(bd_csv,  delimiter=',')

        print(ler)
        for i, linha in enumerate(ler):
            print(linha)


def ler_item_not(base_csv):
    with open(base_csv, 'r+', newline='') as bd_csv:
        ler = csv.reader(bd_csv,  delimiter=';')

        for a, b, c, d, e, f in ler:
            print(f'NOTEBOOK ID {a} {b}, Modelo {c}, {d}, VALOR R${e}, IMB {f}')


# MANIPULANDO BANCO DE DADOS SQL ---------------------------------------------------

def conectar_mssql(usuario, senha):
    con = pyodbc.connect(
        # Driver que será utilizado na conexão
        'DRIVER={ODBC Driver 17 for SQL Server};'
        # IP ou nome do servidor.
        'SERVER=10.6.32.140;'
        # Porta
        'PORT=1433;'
        # Banco que será utilizado.
        'DATABASE=estoque_ti;'
        # Nome de usuário.
        f'UID={usuario};'
        # Senha.
        f'PWD={senha}')

    # Criando o cursor que irá executar os comandos SQL (instruções DML, DDL, etc).
    cur = con.cursor()
    return cur


'''o fetchall() pega todas as linhas de sua tabela e as coloca em uma tupla, todas elas dentro de uma lista.
   Então é só colocar o len para contar quantos valores tem dentro dessa lista. :)'''




