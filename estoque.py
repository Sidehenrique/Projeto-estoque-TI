import mod


# INICIO DO MODULO DE ESTOQUE _____________________________________
def modulo_estoque():
    print()
    mod.titulo('CONTROLE DE ESTOQUE v1.6')
    while True:
        mod.bk_white('-** OQUE DESEJA FAZER? **-')
        print('[E] Entrada\n'
              '[S] Saida\n'
              '[V] Visualizar\n'
              '[F] Fechar\n')
        menu_pai = input('>>> ENTRE COM UM COMANDO: ').upper()

        if menu_pai == 'E':
            print('[1] Notebook\n'
                  '[2] Celular\n'
                  '[3] Memoria\n'
                  '[4] Disco\n'
                  '[5] Periféricos\n'
                  '[6] Chaves\n'
                  '[7] Outros\n'
                  '[8] Voltar')
            print()
            menu_filho = input('>>> ESCOLHA UMA OPÇÃO: ')
            if menu_filho == '1':
                print()
                print('>>> ENTRADA DE NOTEBOOK ')
                nome = 'NOTEBOOK'
                marca = input('Digite a marca: ')
                modelo = input('Digite o modelo: ')
                condicao = input('Digite a condição: ')
                valor = input('Digite o valor: ')
                imb = input('Digite o imobilizado: ')
                data = mod.date.today()
                dados = [nome, marca, modelo, condicao, valor, imb]
                print(dados)
                escolha = input('DESEJA SALVA Y OU N: ').upper()
                if escolha == 'Y':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(
                        f"""INSERT INTO notebook VALUES ('{nome}', '{marca}', '{modelo}', '{condicao}', {valor}, {imb}, '{data}')
                        INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                    cursor.commit()

                    print('Cadastrado com Sucesso!')
                    print()
                    continue

                elif escolha == 'N':
                    print('O item foi Descartado (X)')
                    continue

                else:
                    print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                    continue

            elif menu_filho == '2':
                print()
                print('>>> ENTRADA DE CELULAR ')
                nome = 'CELULAR'
                marca = input('Digite a marca: ')
                modelo = input('Digite o modelo: ')
                condicao = input('Digite a condição: ')
                valor = input('Digite o valor: ')
                imei = input('Digite o IMEI: ')
                email = input('Digite o e-mail: ')
                numero = input('Digite o numero: ')
                data = mod.date.today()
                dados = [nome, marca, modelo, condicao, valor, imei, email, numero]
                print(dados)
                escolha = input('DESEJA SALVA Y OU N: ').upper()
                if escolha == 'Y':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(
                        f"""INSERT INTO celular VALUES ('{nome}', '{marca}', '{modelo}', '{condicao}', {valor}, {imei}, '{email}',
                        {numero}, '{data}')
                        INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                    cursor.commit()
                    print('Cadastrado com Sucesso!')
                    print()
                    continue

                elif escolha == 'N':
                    print('O item foi Descartado (X)')
                    continue

                else:
                    print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                    continue

            elif menu_filho == '3':
                print()
                print('>>> ENTRADA DE MEMORIA ')
                nome = 'MEMORIA'
                marca = input('Digite a marca: ')
                modelo = input('DDR3 OU DDR4 ').upper()
                plataforma = input('Plataforma: ')
                condicao = input('Digite a condição: ')
                tamanho = input('Digite o tamanho: ')
                valor = input('Digite o valor: ')
                data = mod.date.today()
                dados = [nome, marca, modelo, plataforma, condicao, tamanho, valor]
                print(dados)
                escolha = input('DESEJA SALVA Y OU N: ').upper()
                if escolha == 'Y':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(
                        f"""INSERT INTO memoria VALUES ('{nome}', '{marca}', '{modelo}', 
                        '{plataforma}', '{condicao}', {tamanho}, {valor}, '{data}')
                        INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")

                    cursor.commit()
                    print('Cadastrado com Sucesso!')
                    print()
                    continue

                elif escolha == 'N':
                    print('O item foi Descartado (X)')
                    continue

                else:
                    print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                    continue

            elif menu_filho == '4':
                print()
                print('>>> ENTRADA DE DISK')
                nome = 'DISCO'
                marca = input('Digite a marca: ')
                modelo = input('HDD OU SSD ')
                plataforma = input('DESKTOP OU NOTEBOOK: ')
                condicao = input('Digite a condição: ')
                tamanho = input('Digite o tamanho: ')
                valor = input('Digite o valor: ')
                data = mod.date.today()
                dados = [nome, marca, modelo, plataforma, condicao, tamanho, valor]
                print(dados)
                escolha = input('DESEJA SALVA Y OU N: ').upper()
                if escolha == 'Y':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(
                        f"""INSERT INTO disco VALUES ('{nome}', '{marca}', '{modelo}', '{plataforma}', '{condicao}', {tamanho}, 
                        {valor}, '{data}')INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                    cursor.commit()
                    print('Cadastrado com Sucesso!')
                    print()
                    continue

                elif escolha == 'N':
                    print('O item foi Descartado (X)')
                    continue

                else:
                    print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                    continue

            elif menu_filho == '5':
                print('[1]Mouse\n'
                      '[2]Teclado\n'
                      '[3]Mouse Pad\n'
                      '[4]Suporte\n'
                      '[5]Voltar\n')
                sub_menu = input('>>> ESCOLHA UMA OPÇÃO: ')
                if sub_menu == '1':
                    print('>>> ENTRADA DE MOUSE')
                    nome = 'MOUSE'
                    marca = input('Digite a marca: ')
                    modelo = input('Digite o modelo ').upper()
                    condicao = input('Digite a condição: ')
                    valor = input('Digite o valor: ')
                    data = mod.date.today()
                    dados = [nome, marca, modelo, condicao, valor]
                    print(dados)
                    escolha = input('DESEJA SALVA Y OU N: ').upper()

                    if escolha == 'Y':
                        cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                        cursor.execute(
                            f"""INSERT INTO mouse VALUES ('{nome}', '{marca}', '{modelo}', '{condicao}', {valor}, '{data}')
                            INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                        cursor.commit()
                        print('Cadastrado com Sucesso!')
                        print()
                        continue

                    elif escolha == 'N':
                        print('O item foi Descartado (X)')
                        continue

                    else:
                        print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                        continue

                elif sub_menu == '2':
                    print('>>> ENTRADA DE TECLADO')
                    nome = 'TECLADO'
                    marca = input('Digite a marca: ')
                    modelo = input('Digite o modelo ').upper()
                    condicao = input('Digite a condição: ')
                    valor = input('Digite o valor: ')
                    dados = [nome, marca, modelo, condicao, valor]
                    data = mod.date.today()
                    print(dados)
                    escolha = input('DESEJA SALVA Y OU N: ').upper()

                    if escolha == 'Y':
                        cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                        cursor.execute(
                            f"""INSERT INTO teclado VALUES ('{nome}', '{marca}', '{modelo}', '{condicao}', {valor}, '{data}')
                            INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                        cursor.commit()
                        print('Cadastrado com Sucesso!')
                        print()
                        continue

                    elif escolha == 'N':
                        print('O item foi Descartado (X)')
                        continue

                    else:
                        print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                        continue

                elif sub_menu == '3':
                    print('>>> ENTRADA DE MOUSE PAD')
                    nome = 'MOUSE PAD'
                    marca = input('Digite a marca: ')
                    modelo = input('Digite o modelo ').upper()
                    condicao = input('Digite a condição: ')
                    valor = input('Digite o valor: ')
                    data = mod.date.today()
                    dados = [nome, marca, modelo, condicao, valor]
                    print(dados)

                    escolha = input('DESEJA SALVA Y OU N: ').upper()
                    if escolha == 'Y':
                        cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                        cursor.execute(
                            f"""INSERT INTO mouse_pad VALUES ('{nome}', '{marca}', '{modelo}', '{condicao}', {valor}, '{data}')
                            INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                        cursor.commit()
                        print('Cadastrado com Sucesso!')
                        print()
                        continue

                    elif escolha == 'N':
                        print('O item foi Descartado (X)')
                        continue

                    else:
                        print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                        continue

                elif sub_menu == '4':
                    print('>>> ENTRADA DE SUPORTE')
                    nome = 'SUPORTE'
                    marca = input('Digite a marca: ')
                    modelo = input('Digite o modelo ').upper()
                    valor = input('Digite o valor: ')
                    data = mod.date.today()
                    dados = [nome, marca, modelo, valor]
                    print(dados)

                    escolha = input('DESEJA SALVA Y OU N: ').upper()
                    if escolha == 'Y':
                        cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                        cursor.execute(
                            f"""INSERT INTO suporte VALUES ('{nome}', '{marca}', '{modelo}', {valor}, '{data}')
                            INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                        cursor.commit()
                        print('Cadastrado com Sucesso!')
                        print()
                        continue

                    elif escolha == 'N':
                        print('O item foi Descartado (X)')
                        continue

                    else:
                        print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                        continue

                elif sub_menu == '5':
                    print('<<< Voltar ao menu anterior')
                    continue

            elif menu_filho == '6':
                print('[1]Windows\n'
                      '[2]Office\n')

                chave_menu = input('>>> QUAL A CHAVE: ')
                if chave_menu == '1':
                    print()
                    print('>>> ENTRADA CHAVE WINDOWS')
                    nome = 'WINDOWS'
                    marca = 'Microsoft'
                    modelo = input('Qual a versão do windows: ')
                    codigo = input('Digite o código: ')
                    valor = input('Digite o valor: ')
                    data = mod.date.today()
                    dados = [nome, marca, modelo, codigo, valor]
                    print(dados)
                    escolha = input('DESEJA SALVA Y OU N: ').upper()
                    if escolha == 'Y':
                        cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                        cursor.execute(
                            f"""INSERT INTO windows VALUES ('{nome}', '{marca}', '{modelo}', '{codigo}', {valor}, '{data}')
                            INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                        cursor.commit()
                        print('Cadastrado com Sucesso!')
                        print()
                        continue

                    elif escolha == 'N':
                        print('O item foi Descartado (X)')
                        continue

                    else:
                        print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                        continue

                if chave_menu == '2':
                    print()
                    print('>>> ENTRADA CHAVE OFFICE')
                    nome = 'OFFICE'
                    marca = 'microsoft'
                    modelo = input('Qual a versão do Office: ')
                    codigo = input('Digite o código: ')
                    valor = input('Digite o valor: ')
                    data = mod.date.today()
                    dados = [nome, marca, modelo, codigo, valor]
                    print(dados)
                    escolha = input('DESEJA SALVA Y OU N: ').upper()
                    if escolha == 'Y':
                        cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                        cursor.execute(
                            f"""INSERT INTO office VALUES ('{nome}', '{marca}', '{modelo}', '{codigo}', {valor}, '{data}')
                            INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                        cursor.commit()
                        print('Cadastrado com Sucesso!')
                        print()
                        continue

                    elif escolha == 'N':
                        print('O item foi Descartado (X)')
                        continue

                    else:
                        print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                        continue

            elif menu_filho == '7':
                print('>>> OUTROS')
                nome = input('Digite o Nome: ')
                marca = input('Digite a Marca: ')
                modelo = input('Digite o Modelo ')
                condicao = input('Digite a Condição: ')
                valor = input('Digite o Valor: ')
                data = mod.date.today()
                dados = [nome, marca, modelo, condicao, valor]
                print(dados)
                escolha = input('DESEJA SALVA Y OU N: ').upper()
                if escolha == 'Y':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(
                        f"""INSERT INTO outros VALUES ('{nome}', '{marca}', '{modelo}', '{condicao}', {valor}, '{data}')
                        INSERT INTO historico VALUES('ENTRADA', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                    cursor.commit()
                    print()
                    print('Cadastrado com Sucesso!')
                    continue

                elif escolha == 'N':
                    print('O item foi Descartado (X)')
                    continue

                else:
                    print(mod.subtitulo('*** OPÇÃO INVALIDA ***'))
                    continue

            elif menu_filho == '8':
                print('<<< Voltar ao menu anterior')
                continue

            else:
                print('** OPÇÃO INVALIDA **')
                continue

        elif menu_pai == 'S':
            print('[1] Notebook\n'
                  '[2] Celular\n'
                  '[3] Memoria\n'
                  '[4] Disco\n'
                  '[5] Periféricos\n'
                  '[6] Chaves\n'
                  '[7] Outros\n'
                  '[8] Voltar')
            menu_saida = input('>>> ENTRE COM UM COMANDO: ')
            if menu_saida == '1':
                cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                cursor.execute(f"""SELECT * FROM notebook;""")
                row = cursor
                for ide, nome, marca, modelo, condicao, valor, imb, data in row:
                    print(ide, nome, marca, modelo, condicao, valor, imb, data)
                cursor.close()

                selecion = input('DIGITE A ID DO NOTEBOOK DESEJADO: ')
                print('[1]TREINAMENTO    [2]PROVISÓRIO    [3]DEFINITIVO')
                status = input('DIGITE O MOTIVO DA SAIDA: ')

                try:
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""DELETE celular WHERE id={selecion}
                    INSERT INTO historico VALUES('{status}', '{nome}', '{marca}', '{modelo}', {valor}, '{data}');""")
                    cursor.commit()
                except:
                    print(f'A ID {selecion} NÃO É VALIDA')

                print('Cadastrado com Sucesso!')
                print()
                escolher = input('>>> QUAL A SAIDA: ')

            else:
                print()
                print('NENHUM ITEM NO ESTOQUE.')

        elif menu_pai == 'V':
            print('[1] Histórico\n'
                  '[2] Estoque\n')

            menu_v = input('>>> OQUE DESEJA VISUALIZAR? ').upper()

            if menu_v == '1':
                print('HISTÓRICO DE PROCESSOS DO ESTOQUE')
                print()
                cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                cursor.execute(f"""SELECT * FROM historico;""")
                row = cursor
                for status, nome, marca, modelo, valor, data in row:
                    print(status, nome, marca, modelo, valor, data)
                cursor.close()

                cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                cursor.execute(f"""SELECT * FROM historico;""")

                count = len(cursor.fetchall())
                if count != 0:
                    print()
                    print(f'FORAM FEITAS {count} ALTERAÇÕES DE STATUS.')
                else:
                    print()
                    print('NENHUMA MOVIMENTAÇÃO FOI FEITA AINDA.')

            elif menu_v == '2':
                print('[1] Notebook\n'
                      '[2] Celular\n'
                      '[3] Memoria\n'
                      '[4] Disco\n'
                      '[5] Chaves\n'
                      '[6] Mouse\n'
                      '[7] Teclado\n'
                      '[8] Mouse Pad\n'
                      '[9] Suporte\n'
                      '[O] Outros\n'
                      '[V] Voltar\n'
                      )

                ver = input('>>> ENTRE COM UMA OPÇÃO: ').upper()

                if ver == '1':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM notebook;""")
                    row = cursor
                    for ide, nome, marca, modelo, condicao, valor, imb, data in row:
                        print(ide, nome, marca, modelo, condicao, valor, imb, data)
                    cursor.close()

                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM notebook;""")

                    count = len(cursor.fetchall())
                    if count != 0:
                        print()
                        print(f'A QUANTIDADE TOTAL DE NOTEBOOKS É DE {count} UNIDADES.')
                    else:
                        print()
                        print('NENHUM ITEM NO ESTOQUE.')

                elif ver == '2':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM celular;""")
                    row = cursor
                    for ide, nome, marca, modelo, condicao, valor, imei, email, numero, data in row:
                        print(ide, nome, marca, modelo, condicao, valor, imei, email, numero, data)
                    cursor.close()

                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM celular;""")

                    count = len(cursor.fetchall())
                    if count != 0:
                        print()
                        print(f'A QUANTIDADE TOTAL DE CELULARES É DE {count} UNIDADES.')
                    else:
                        print()
                        print('NENHUM ITEM NO ESTOQUE.')

                elif ver == '3':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM memoria;""")
                    row = cursor
                    for ide, nome, marca, modelo, plataforma, condicao, tamanho, valor, data in row:
                        print(ide, nome, marca, modelo, plataforma, condicao, tamanho, valor, data)
                    cursor.close()

                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM memoria;""")

                    count = len(cursor.fetchall())
                    if count != 0:
                        print()
                        print(f'A QUANTIDADE TOTAL DE MEMORIAS É DE {count} UNIDADES.')
                    else:
                        print()
                        print('NENHUM ITEM NO ESTOQUE.')

                elif ver == '4':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM disco;""")
                    row = cursor
                    for ide, nome, marca, modelo, plataforma, condicao, tamanho, valor, data in row:
                        print(ide, nome, marca, modelo, plataforma, condicao, tamanho, valor, data)
                    cursor.close()

                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM disco;""")

                    count = len(cursor.fetchall())
                    if count != 0:
                        print()
                        print(f'A QUANTIDADE TOTAL DE DISCOS É DE {count} UNIDADES.')
                    else:
                        print()
                        print('NENHUM ITEM NO ESTOQUE.')

                elif ver == '5':
                    print('[1] Windows\n'
                          '[2] Office\n')

                    menu_cha = input('ENTRE COM UMA OPÇÃO: ')
                    if menu_cha == '1':
                        cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                        cursor.execute(f"""SELECT * FROM windows;""")
                        row = cursor
                        for ide, nome, marca, modelo, codigo, valor, data in row:
                            print(ide, nome, marca, modelo, codigo, valor, data)
                        cursor.close()

                        cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                        cursor.execute(f"""SELECT * FROM windows;""")

                        count = len(cursor.fetchall())
                        if count != 0:
                            print()
                            print(f'A QUANTIDADE TOTAL DE CHAVES WINDOWS É DE {count} UNIDADES.')
                        else:
                            print()
                            print('NENHUM ITEM NO ESTOQUE.')

                    elif menu_cha == '2':
                        cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                        cursor.execute(f"""SELECT * FROM office;""")
                        row = cursor
                        for ide, nome, marca, modelo, codigo, valor, data in row:
                            print(ide, nome, marca, modelo, codigo, valor, data)
                        cursor.close()

                        cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                        cursor.execute(f"""SELECT * FROM office;""")

                        count = len(cursor.fetchall())
                        if count != 0:
                            print()
                            print(f'A QUANTIDADE TOTAL DE CHAVES OFFICE É DE {count} UNIDADES.')
                        else:
                            print()
                            print('NENHUM ITEM NO ESTOQUE.')

                elif ver == '6':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM mouse;""")
                    row = cursor
                    for ide, nome, marca, modelo, condicao, valor, data in row:
                        print(ide, nome, marca, modelo, condicao, valor, data)
                    cursor.close()

                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM mouse;""")

                    count = len(cursor.fetchall())
                    if count != 0:
                        print()
                        print(f'A QUANTIDADE TOTAL DE MOUSE É DE {count} UNIDADES.')
                    else:
                        print()
                        print('NENHUM ITEM NO ESTOQUE.')

                elif ver == '7':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM teclado;""")
                    row = cursor
                    for ide, nome, marca, modelo, condicao, valor, data in row:
                        print(ide, nome, marca, modelo, condicao, valor, data)
                    cursor.close()

                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM teclado;""")

                    count = len(cursor.fetchall())
                    if count != 0:
                        print()
                        print(f'A QUANTIDADE TOTAL DE TECLADO É DE {count} UNIDADES.')
                    else:
                        print()
                        print('NENHUM ITEM NO ESTOQUE.')

                elif ver == '8':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM mouse_pad;""")
                    row = cursor
                    for ide, nome, marca, modelo, condicao, valor, data in row:
                        print(ide, nome, marca, modelo, condicao, valor, data)
                    cursor.close()

                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM mouse_pad;""")

                    count = len(cursor.fetchall())
                    if count != 0:
                        print()
                        print(f'A QUANTIDADE TOTAL DE MOUSE É DE {count} UNIDADES.')
                    else:
                        print()
                        print('NENHUM ITEM NO ESTOQUE.')

                elif ver == '9':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM suporte;""")
                    row = cursor
                    for ide, nome, marca, modelo, valor, data in row:
                        print(ide, nome, marca, modelo, valor, data)
                    cursor.close()

                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM suporte;""")

                    count = len(cursor.fetchall())
                    if count != 0:
                        print()
                        print(f'A QUANTIDADE TOTAL DE MOUSE É DE {count} UNIDADES.')
                    else:
                        print()
                        print('NENHUM ITEM NO ESTOQUE.')

                elif ver == '0':
                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM outros;""")
                    row = cursor
                    for ide, nome, marca, modelo, condicao, valor, data in row:
                        print(ide, nome, marca, modelo, condicao, valor, data)
                    cursor.close()

                    cursor = mod.conectar_mssql(usuario='sa', senha='sicoob')
                    cursor.execute(f"""SELECT * FROM outros;""")

                    count = len(cursor.fetchall())
                    if count != 0:
                        print()
                        print(f'A QUANTIDADE TOTAL DE MOUSE É DE {count} UNIDADES.')
                    else:
                        print()
                        print('NENHUM ITEM NO ESTOQUE.')

                elif ver == 'V':
                    continue

                else:
                    print('* OPÇÃO INVALIDA *')
                    continue

            else:
                print('** OPÇÃO INVALIDA **')
                continue

        elif menu_pai == 'F':
            print('Obrigado por ultilizar o Software!')
            break

        else:
            print('* OPÇÃO INVALIDA *')
            continue

    return


modulo_estoque()
