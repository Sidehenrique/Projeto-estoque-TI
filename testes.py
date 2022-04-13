import pyodbc
import mod

cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
cursor.execute(f"""SELECT * FROM celular;""")
row = cursor
for ide, nome, marca, modelo, condicao, valor, imei, email, numero, data in row:
    print(ide, nome, marca, modelo, condicao, valor, imei, email, numero, data)
cursor.close()
print()
selecion = input('DIGITE A ID DO NOTEBOOK DESEJADO: ')
print('[1]TREINAMENTO    [2]PROVISÓRIO    [3]DEFINITIVO')
status = input('DIGITE O MOTIVO DA SAIDA: ')
print()
if status == '1':
    status = 'TREINAMENTO'
elif status == '2':
    status = 'PROVISÓRIO'
elif status == '3':
    status = 'DEFINITIVO'
else:
    print('** OPÇÃO INVALIDA **')

cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
cursor.execute(f"""SELECT * from celular where id={selecion};""")
row = cursor
for ide, nome, marca, modelo, condicao, valor, imei, email, numero, data in row:
    print(ide, nome, marca, modelo, condicao, valor, imei, email, numero, data)
finalizar = input('DESEJA REALMENTE FINALIZAR A OPERAÇÃO? Y OU N ').upper()
if finalizar == 'Y':
    dataa = mod.date.today()
    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
    cursor.execute(f"""INSERT INTO historico VALUES('{status}', '{nome}', '{marca}', '{modelo}', {valor}, '{dataa}')
        DELETE celular WHERE id={selecion};""")
    cursor.commit()
    print('OPERAÇÃO FINALIZADA COM SUCESSO!')

elif finalizar == 'N':
    print('OPERAÇÃO CANCELADA ')

else:
    print(f'A ID {selecion} NÃO É VALIDA OU NÃO EXISTE')

# except ValueError('Algo deu errado entre em contato com o administrador'):
#     pass

# def conectar_mssql(usuario, senha):
#     con = pyodbc.connect(
#         # Driver que será utilizado na conexão
#         'DRIVER={ODBC Driver 17 for SQL Server};'
#         # IP ou nome do servidor.
#         'SERVER=10.6.32.140;'
#         # Porta
#         'PORT=1433;'
#         # Banco que será utilizado.
#         'DATABASE=estoque_ti;'
#         # Nome de usuário.
#         f'UID={usuario};'
#         # Senha.
#         f'PWD={senha}')
#
#     # Criando o cursor que irá executar os comandos SQL (instruções DML, DDL, etc).
#     cur = con.cursor()
#     return cur
#
#
# cursor = conectar_mssql(usuario='sa', senha='sicoob')
# cursor.execute(f"""SELECT * FROM celular;""")
# row = cursor
# for ide, nome, marca, modelo, condicao, valor, imei, email, numero, data in row:
#     print(ide, nome, marca, modelo, condicao, valor, imei, email, numero, data)
#
#
# cursor = conectar_mssql(usuario='sa', senha='sicoob')
# cursor.execute(f"""SELECT * FROM celular;""")
#
# '''o fetchall() pega todas as linhas de sua tabela e as coloca em uma tupla, todas elas dentro de uma lista.
# Então é só colocar o len para contar quantos valores tem dentro dessa lista. :)'''
#
# count = len(cursor.fetchall())
# print(count)
# cursor.close()


# con = pyodbc.connect(
#     # Driver que será utilizado na conexão
#     'DRIVER={ODBC Driver 17 for SQL Server};'
#     # IP ou nome do servidor.
#     'SERVER=10.6.32.140;'
#     # Porta
#     'PORT=1433;'
#     # Banco que será utilizado.
#     'DATABASE=BD_SICOOB;'
#     # Nome de usuário.
#     'UID=sa;'
#     # Senha.
#     'PWD=sicoob;')
#
# marca = input('Digite a marca: ')
# modelo = input('Digite o modelo: ')
# condicao = input('Digite a condição: ')
# valor = input('Digite o valor: ')
# imb = input('Digite o imobilizado: ')
#
# cursor = con.cursor()
# cursor.execute(f"""INSERT INTO notebook VALUES ('{marca}', '{modelo}', '{condicao}', {valor}, {imb});""")
# cursor.commit()


# # teste de conexão com o servidor
# cursor.execute("SELECT @@version;")
# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()


#
# count = cursor.execute("""
# INSERT INTO celular (marca, modelo, condicao, valor, imb)
# VALUES ('a','b','c','d','e')"""; 'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0,).rowcount
# con.commit()
# print('Rows inserted: ' + str(count))
#


# def conectar_mssql_docker(usuario, senha):
#     con = pyodbc.connect(
#         # Driver que será utilizado na conexão
#         'DRIVER={ODBC Driver 17 for SQL Server};'
#         # IP ou nome do servidor.
#         'SERVER=10.6.32.140;'
#         # Porta
#         'PORT=1433;'
#         # Banco que será utilizado.
#         'DATABASE=BD_SICOOB;'
#         # Nome de usuário.
#         f'UID={usuario};'
#         # Senha.
#         f'PWD={senha}')
#
#     # Criando o cursor que irá executar os comandos SQL (instruções DML, DDL, etc).
#     cur = con.cursor()
#     return cur
#
#
# if __name__ == "__main__":
#     usuario = str(input('Usuario: '))
#     print(usuario)
#     senha = str(input('Senha: '))
#     print(senha)
#
#     cursor = conectar_mssql_docker(usuario=usuario, senha=senha)
#     cursor.execute("SELECT @@version;")
#     row = cursor.fetchone()
#
#     print(row[0])
