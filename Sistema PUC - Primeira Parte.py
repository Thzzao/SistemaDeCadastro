'''Sistema PUC de cadastro de alunos, matérias e etc'''
#coding: utf-8 
import time


#Declarar as listas 
lista_estudantes = []

#Criação do menu principal
op = 1
while op >=1 and op <=6:
    print ("\n>> Olá, bem vindo ao Sistema PUC <<\n"
        "\nPrimeiramente selecione uma categoria da qual deseja alterar:\n")

    time.sleep(2)
    print("1. Estudante")
    #time.sleep(1)
    print("2. Disciplina")
    #time.sleep(1)
    print("3. Professor")
    #time.sleep(1)
    print("4. Turma")
    #time.sleep(1)
    print("5. Matrícula")
    #time.sleep(1)
    print("6. SAIR")
    

    #Entrada da opção desejada
    op = int(input("\nDigite a opção desejada: ")) 

    if op == 1:
        print ("\n === ESTUDANTES ===")
    elif op == 2:
        print ("\n === DISCIPLINAS ===")
    elif op == 3:
        print ("\n === PROFESSORES ===")
    elif op == 4:
        print ("\n === TURMAS ===")
    elif op == 5:
        print ("\n === MATRÍCULAS ===")
    elif op == 6:
        print ("\nDesconectando...\n")      
        break  
    else:
        print ("Opção Inválida")
        op = 1
        continue

    #Criação do menu de operações
    op2 = 1
    while op2 >=1 and op2 <=5:
        print ("O que você gostaria de fazer?\n")

        time.sleep(1)      
        print("1. Incluir novo registro")
        print("2. Listar registros")
        print("3. Excluir registro")
        print("4. Alterar um registro")
        print("5. Voltar ao menu inicial")

        #Entrada da opção desejada
        op2 = int(input("\nDigite a opção desejada: "))

    #Interações com ESTUDANTE    
        #Incluir estudante
        while op2 == 1 and op == 1:
            #Pedir o dado
            estudante_nome = input("Digite o nome do estudante:")
            #Adicionar na lista 
            lista_estudantes.append(estudante_nome)
            print ("Adicionado com sucesso\n")
            if input("Deseja cadastrar um novo estudante? (s/n): ") == "s".lower():
                continue
            else:
                break
    
        #Listar estudantes
        if op2 == 2 and op == 1:
            print ("\n>>> LISTA DOS ESTUDANTES <<<")
            c = 1 #contador
            for estudante in lista_estudantes:
                #coloque dentro do `{}` o valor de c e o valor de estudante
                print("{}- {}".format (c, estudante))
                c = c + 1 

            if not lista_estudantes:  
                print ("Não há estudantes cadastrados\n") 

        #Excluir estudante*******
        elif op2 == 3 and op == 1:
            #matrícula = int(input("Qual o número da matrícula?")) #se informado número válido permite a exclusão. Pedir confirmação do usuário 
            print("Em desenvolvimento...") 

        #Atualizar estudante********
        elif op2 == 4 and op == 1:
            #matrícula = int(input("Qual o número da matrícula?")) #se correto permite entrar com dados como nome, idade, turma.
            print("Em desenvolvimento...")

        elif op2 == 5 and op == 1:
            print ("Voltando...")
            break

        #else:
            #print ("Opção Inválida")
        
    #Interações com  DISCIPLINA    
        if op == 2:
            print("Em desenvolvimento...")


    #Interações com PROFESSOR   
        if op == 3:
            print("Em desenvolvimento...")


    #Interações com TURMA 
        if op == 4:
            print("Em desenvolvimento...")


    #Interações com MATRÍCULA    
        if op == 5:
            print("Em desenvolvimento...")


'''
#Modificações em relação a ESTUDANTE    

    #Incluir estudante
    if op2 == 1: 

        def solicitar_dados_estudante():
            nome = input("Digite o nome do estudante: ")
            cpf = input("Digite o CPF do estudante: ")
            return nome, cpf
        
        def incluir_estudante (estudantes):
            estudante = solicitar_dados_estudante()
            pesquisa = pesquisar_estudante(estudante, estudantes)
            if pesquisa[1]:
                if estudante == pesquisa:
                    return False and print ("Estudante já cadastrado")
            estudantes.add(estudante)
            return True and print ("Estudante cadastrado com sucesso")

    #Listar estudantes    
    elif op2 == 2:
        def listar_estudantes(estudantes):
            print("***Lista de Estudantes***")
        for estudante in estudantes:
            print(estudante)
        print("*** Fim da Lista ***") 

    #Excluir estudante
    #elif op2 == 3:

    #Aletrar estudante
        elif op2 == 4:
            def alterar_estudante (nome, estudantes):
                pesquisa = pesquisar_estudante(nome, estudantes)
                if pesquisa[1]:
                    nome = input(f"Digite o nome a ser trocado: ")
                    if (posicao = estudantes.index(nome)):
                        estudantes[posicao] = nome
                    return True
                else:
                    return False    
    elif op2 == 5:
        menu()

    else:
        print ("Tente novamente...")         
            
   

def solicitar_dados_estudante():
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")
    return nome, cpf

def incluir_estudante (estudantes):
    estudante = solicitar_dados_estudante()
    pesquisa = pesquisar_estudante(estudante, estudantes)
    if pesquisa[1]:
        if estudante == pesquisa:
            return False
    estudantes.add(estudante)
    return True

def pesquisar_estudante(nome, estudantes):
    if nome in estudantes:
        return estudantes[nome], True
    else:
        return "", False

def listar_estudantes(estudantes):
    print("***Lista de Estudantes***")
    for estudante in estudantes:
        print(estudante)
    print("*** Fim da Lista ***") 

def excluir_estudante(nome,estudantes):

def alterar_estudante (nome, estudantes):
    pesquisa = pesquisar_estudante(nome, estudantes)
    if pesquisa[1]:
        nome = input(f"Digite o nome a ser trocado: ")
        if (posicao = estudantes.index(nome)):
           estudantes[posicao] = nome
        return True
    else:
        return False
    
'''