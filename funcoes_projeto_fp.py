def criacao_de_treino():
    try:    
        arquivo=open('treino.txt','a')
        treino=input('Digite o tipo do treino: ')
        arquivo.write('Tipo de treino: '+treino+"\n")
        data=input('Digite a data de início do treino: ')
        arquivo.write('Data de termino: '+data+"\n")
        tempo_de_duracao=input('Digite o tempo de duração do treino em minutos: ')
        arquivo.write('tempo de duração: '+tempo_de_duracao+"\n")
        quantidade_de_exercícios=int(input('Digite quantos exercícios terá o seu treino: '))
        for i in range(quantidade_de_exercícios):
            exercicios=input('Digite o exercício e a faixa de repetições: ')
            arquivo.write(exercicios+'\n')
        arquivo.write('\n')
        arquivo.close()
    except ValueError:
        print("Erro: Digite um número válido para a quantidade de exercícios.")
    except Exception as e:
        print(f"Erro ao criar treino: {e}")

def visualizacao_do_arquivo():
    try:
        arquivo = open('treino.txt', 'r')
        print(arquivo.read())
        arquivo.close()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")

def edicao_do_conteudo():
    try:
        arquivo = open('treino.txt', 'r')
        file = arquivo.readlines()
        arquivo.close()
        print(file)
        delet = int(input('Digite o índice que será apagado: '))
        if delet <=len(file):
            file.pop(delet)
            add = input('O que você deseja adicionar: ')
            file.insert(delet, add + '\n')
            arquivo = open('treino.txt', 'w')
            arquivo.write(''.join(file))
            arquivo.close()
        else:
            print('indice não existente')
    except ValueError:
        print("Erro: Digite um número inteiro válido.")
    except FileNotFoundError:
        print("Arquivo 'treino.txt' não encontrado.")
    except Exception as e:
        print(f"Erro na edição: {e}")

def excluir_conteudo():
    try:
        arquivo = open('treino.txt', 'r')
        file = arquivo.readlines()
        arquivo.close()
        print(file)
        excluir = int(input('Digite o índice que será apagado: '))
        file.pop(excluir)
        arquivo = open('treino.txt', 'w')
        arquivo.write(''.join(file))
        arquivo.close()
    except ValueError:
        print("Erro: Digite um número inteiro válido.")
    except IndexError:
        print("Erro: Índice fora do intervalo.")
    except FileNotFoundError:
        print("Arquivo 'treino.txt' não encontrado.")
    except Exception as e:
        print(f"Erro ao excluir conteúdo: {e}")

def adicionar_conteudo():
    try:
        arquivo = open('treino.txt', 'a')
        adicionar_elemento = input('Digite algo que você gostaria de adicionar: ')
        arquivo.write('\n'+adicionar_elemento + '\n')
        arquivo.close()
    except Exception as e:
        print(f"Erro ao adicionar conteúdo: {e}")


def filtrar_conteudo():
    try:
        termo = input('Digite o termo que deseja buscar (tipo, data, exercício, etc): ').strip().lower()
        arquivo = open('treino.txt', 'r')
        conteudo = arquivo.read()
        arquivo.close()
        treinos = conteudo.split("\n\n")
        encontrados = [treino.strip() for treino in treinos if termo in treino.lower()]
        if encontrados:
            print("\nResultados encontrados:")
            for treino in encontrados:
                print(f"\n{treino}")
        else:
            print("Nenhum treino encontrado com esse termo.")
    except FileNotFoundError:
        print("Arquivo não encontrado ou não existente")
    except Exception as e:
        print(f"Erro ao filtrar conteúdo: {e}")
