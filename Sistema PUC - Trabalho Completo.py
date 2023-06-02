''' Sistema PUC criado na matéria de Raciocínio Computacional 
    do curso de ADS da PUCPR. Ele atende o cadastro de alunos,
    disciplinas, professores, turmas e matriculas. 
    Criado por Thiago Souza no ano de 2023.
'''
#coding: utf-8
import time
import json

# Declarar as listas
lista_estudantes = []
lista_disciplinas = []
lista_professor = []
lista_turma = []
lista_matricula = []

#Criação das funções 

def carregar_estudante():
    #Tentar abrir o arquivo
    try:
        #Abre um arquivo para leitura (READ)
        with open ("estudantes.json", "r") as f:
            #Trasforma arquivo Json em objeto python
            lista_estudantes = json.load(f)
            return lista_estudantes
    #Caso não encontre o arquivo    
    except FileNotFoundError:
        lista_estudantes = []
        return lista_estudantes    
def salvar_estudante(lista_estudantes): 
    #Abre o arquivo para escrita (WRITE), se não existir ele cria um novo
    with open ("estudantes.json", "w") as f:
        #Transforma a lista em Json e joga para dentro do arquivo
        json.dump(lista_estudantes, f)
def inserir_dados_estudantes():
    # Pedir os dados.
    time.sleep(1)
    nome = input("\nDigite o nome do estudante:")
    time.sleep(1)
    cpf = input("\nDigite o CPF do estudante:")
    time.sleep(1)
    codigo = int(input("\nDigite o código do estudante:"))
    #Criação do dicionario
    novo_estudante = {'nome':nome, 'cpf':cpf, 'codigo':codigo}
    #Adicionar na lista
    lista_estudantes = carregar_estudante()
    lista_estudantes.append(novo_estudante)
    #Salvar a lista no arquivo
    salvar_estudante(lista_estudantes)  
def listar_dados_estudantes():
    lista_estudantes = carregar_estudante()
    if not lista_estudantes:
        print("Não há estudantes cadastrados")
    else:
        c = 1  #contador
        for estudante in lista_estudantes:  #procurando na lista
            #coloque dentro do `{}` o valor de c e os valores de estudante que estão no dicionário
            print("{} - Nome:{} - CPF:{} - Código:{}".format(c, estudante['nome'], estudante['cpf'], estudante['codigo']))
            c = c + 1  #contador acrecenta 1 a cada estudante
def excluir_dados_estudantes():
    #Pedir os dados para confirmação do estudante
    lista_estudantes = carregar_estudante()
    codigo_busca = int(input("\nDigite o código do estudante em que deseja excluir:"))
    for estudante in lista_estudantes: #pesquisa na lista
        if not estudante['codigo'] == codigo_busca:
            print("Código não encontrado\nTente novamente")

        if estudante['codigo'] == codigo_busca:
            print ("Estudante encontrado")
            #Confirmação do estudante
            if input("\nDeseja excluír o aluno '{}' cujo código é {}? (s/n):".format(estudante['nome'], estudante['codigo'] )) == "s".lower():
                #Exclusão dos dados 
                lista_estudantes.remove(estudante)
                salvar_estudante(lista_estudantes)
                print ("Registro Apagado :)")
            break
        else:
            continue
    if not lista_estudantes:
        print("Não há estudantes cadastrados")  
def editar_dados_estudante():

    #Pedir os dados para confirmação do estudante
    lista_estudantes = carregar_estudante()
    codigo_busca = int(input("\nDigite o código do estudante em que deseja alterar:"))

    for estudante in lista_estudantes: #pesquisa na lista
        if not estudante['codigo'] == codigo_busca:
            print("Código não encontrado\nTente novamente")

        if estudante['codigo'] == codigo_busca:
            print ("Estudante encontrado")
        #Confirmação    
        if input("\nDeseja alterar o aluno {} cujo código é {}? (s/n):".format(estudante['nome'], estudante['codigo'] )) == "s".lower():
            #Entrada dos novos dados
            nome = input("\nDigite o nome do estudante:")
            time.sleep(1)
            cpf = input("\nDigite o CPF do estudante:")
            time.sleep(1)
            codigo = int(input("\nDigite o código do estudante:"))
            #Editar o dicionário
            estudante['nome'] = nome 
            estudante['cpf'] = cpf 
            estudante['codigo'] = codigo
            salvar_estudante(lista_estudantes)
            print ("Registros atualizados ;)")
            break
        else:
            continue
    if not lista_estudantes:
        print("Não há estudantes cadastrados")  

def carregar_disciplina():
    #Tentar abrir o arquivo
    try:
        #Abre um arquivo para leitura (READ)
        with open ("disciplinas.json", "r") as f:
            #Trasforma arquivo Json em objeto python
            lista_disciplinas = json.load(f)
            return lista_disciplinas
    #Caso não encontre o arquivo    
    except FileNotFoundError:
        lista_disciplinas = []
        return lista_disciplinas    
def salvar_disciplina(lista_disciplinas): 
    #Abre o arquivo para escrita (WRITE), se não existir ele cria um novo
    with open ("disciplinas.json", "w") as f:
        #Transforma a lista em Json e joga para dentro do arquivo
        json.dump(lista_disciplinas, f)
def inserir_dados_disciplinas():
    # Pedir os dados.
    time.sleep(1)
    nome = input("\nDigite o nome da disciplina:")
    time.sleep(1)
    codigo = int(input("\nDigite o código da disciplina:"))
    #Criação do dicionario
    nova_disciplina = {'nome':nome,'codigo':codigo}
    #Adicionar na lista
    lista_disciplinas = carregar_disciplina()
    lista_disciplinas.append(nova_disciplina)
    #Salvar a lista no arquivo
    salvar_disciplina(lista_disciplinas)  
def listar_dados_disciplinas():
    lista_disciplinas = carregar_disciplina()
    if not lista_disciplinas:
        print("Não há disciplinas cadastradas")
    else:
        c = 1  #contador
        for disciplina in lista_disciplinas:  #procurando na lista
            #coloque dentro do `{}` o valor de c e os valores de estudante que estão no dicionário
            print("{} - Nome:{} - Código:{}".format(c, disciplina['nome'], disciplina['codigo']))
            c = c + 1  #contador acrecenta 1 a cada estudante
def excluir_dados_disciplinas():
    #Pedir os dados para confirmação 
    codigo_busca = int(input("\nDigite o código da disciplina em que deseja excluir:"))
    lista_disciplinas = carregar_disciplina()
    for disciplina in lista_disciplinas: #pesquisa na lista
        if not disciplina['codigo'] == codigo_busca:
            print("Código não encontrado\nTente novamente")

        if disciplina['codigo'] == codigo_busca:
            print ("Disciplina encontrada")
            #Confirmação do procediemnto
            if input("\nDeseja excluír a disciplina '{}' cujo código é {}? (s/n):".format(disciplina['nome'], disciplina['codigo'] )) == "s".lower():
                #Exclusão dos dados 
                lista_disciplinas.remove(disciplina)
                salvar_disciplina(lista_disciplinas)
                print ("Registro Apagado :)")
            break
        else:
            continue
    if not lista_estudantes:
        print("Não há disciplinas cadastradas")                
def editar_dados_disciplina():
    #Pedir o código do estudante
    lista_disciplinas = carregar_disciplina()
    codigo_busca = int(input("\nDigite o código da disciplina em que deseja alterar:"))

    for disciplina in lista_disciplinas: #Busca na lista
        if not disciplina['codigo'] == codigo_busca:
            print("Código não encontrado\nTente novamente")

        if disciplina['codigo'] == codigo_busca:
            print ("Disciplina encontrada")
            #Confirmação    
            if input("\nDeseja alterar a disciplina '{}' cujo código é {}? (s/n):".format(disciplina['nome'], disciplina['codigo'] )) == "s".lower():
                #Entrada dos novos dados
                nome = input("\nDigite o nome da disciplina:")
                time.sleep(1)
                codigo = int(input("\nDigite o código da disciplina:"))
                #Editar o dicionário
                disciplina['nome'] = nome 
                disciplina['codigo'] = codigo
                salvar_disciplina(lista_disciplinas)
                print ("Registros atualizados ;)")
                break
        else:
            continue 
    if not lista_estudantes:
        print("Não há disciplinas cadastradas")

def carregar_professor():
    #Tentar abrir o arquivo
    try:
        #Abre um arquivo para leitura (READ)
        with open ("professores.json", "r") as f:
            #Trasforma arquivo Json em objeto python
            lista_professor = json.load(f)
            return lista_professor
    #Caso não encontre o arquivo    
    except FileNotFoundError:
        lista_professor = []
        return lista_professor    
def salvar_professor(lista_professor): 
    #Abre o arquivo para escrita (WRITE), se não existir ele cria um novo
    with open ("professores.json", "w") as f:
        #Transforma a lista em Json e joga para dentro do arquivo
        json.dump(lista_professor, f)
def inserir_dados_professor():
    # Pedir os dados.
    time.sleep(1)
    nome = input("\nDigite o nome do professor:")
    time.sleep(1)
    cpf = input("\nDigite o CPF do professor:")
    time.sleep(1)
    codigo = int(input("\nDigite o código do professor:"))
    #Criação do dicionario
    novo_professor = {'nome':nome, 'cpf':cpf, 'codigo':codigo}
    #Adicionar na lista
    lista_professor = carregar_professor()
    lista_professor.append(novo_professor)
    #Salvar a lista no arquivo
    salvar_professor(lista_professor)  
def listar_dados_professor():
    lista_professor = carregar_professor()
    if not lista_professor:
        print("Não há professores cadastrados")
    else:
        c = 1  #contador
        for professor in lista_professor:  #procurando na lista
            #coloque dentro do `{}` o valor de c e os valores de estudante que estão no dicionário
            print("{} - Nome:{} - CPF:{} - Código:{}".format(c, professor['nome'], professor['cpf'], professor['codigo']))
            c = c + 1  #contador acrecenta 1 a cada estudante
def excluir_dados_professor():
    #Pedir os dados para confirmação 
    codigo_busca = int(input("\nDigite o código do professor em que deseja excluir:"))
    lista_professor = carregar_professor()
    for professor in lista_professor: #pesquisa na lista
        if not professor['codigo'] == codigo_busca:
            print("Código não encontrado\nTente novamente")

        if professor['codigo'] == codigo_busca:
            print ("Professor encontrado")
            #Confirmação do procediemnto
        if input("\nDeseja excluír o professor '{}' cujo código é {}? (s/n):".format(professor['nome'], professor['codigo'] )) == "s".lower():
            #Exclusão dos dados 
            lista_professor.remove(professor)
            salvar_professor(lista_professor)
            print ("Registro Apagado :)")
            break
        else:
            continue 
    if not lista_estudantes:
        print("Não há professores cadastrados")    
def editar_dados_professor():
    #Pedir o código do estudante
    lista_professor = carregar_professor()
    codigo_busca = int(input("\nDigite o código do professor em que deseja alterar:"))

    for professor in lista_professor: #Busca na lista
        if not professor['codigo'] == codigo_busca:
            print("Código não encontrado\nTente novamente")

        if professor['codigo'] == codigo_busca:
            print ("Professor encontrado")
        #Confirmação    
        if input("\nDeseja alterar o professor '{}' cujo código é {}? (s/n):".format(professor['nome'], professor['codigo'] )) == "s".lower():
            #Entrada dos novos dados
            nome = input("\nDigite o nome do professor:")
            time.sleep(1)
            cpf = input("\nDigite o CPF do professor:")
            time.sleep(1)
            codigo = int(input("\nDigite o código do professor:"))
            #Editar o dicionário
            professor['nome'] = nome 
            professor['cpf'] = cpf 
            professor['codigo'] = codigo
            salvar_professor(lista_professor)
            print ("Registros atualizados ;)")
            break
        else:
            continue 
    if not lista_estudantes:
        print("Não há professores cadastrados")   

def carregar_turma():
    #Tentar abrir o arquivo
    try:
        #Abre um arquivo para leitura (READ)
        with open ("turmas.json", "r") as f:
            #Trasforma arquivo Json em objeto python
            lista_turma = json.load(f)
            return lista_turma
    #Caso não encontre o arquivo    
    except FileNotFoundError:
        lista_professor = []
        return lista_professor    
def salvar_turma(lista_turma): 
    #Abre o arquivo para escrita (WRITE), se não existir ele cria um novo
    with open ("turmas.json", "w") as f:
        #Transforma a lista em Json e joga para dentro do arquivo
        json.dump(lista_turma, f)
def inserir_dados_turma():
    # Pedir os dados.
    time.sleep(1)
    codigo_turma = int(input("\nDigite o código da turma:"))
    time.sleep(1)
    codigo_professor = int(input("\nDigite o código do professor:"))
    time.sleep(1)
    codigo_disciplina = int(input("\nDigite o código da disciplina:"))
    #Criação do dicionario
    nova_turma = {'código da turma':codigo_turma, 'código do professor':codigo_professor, 'código da disciplina':codigo_disciplina}
    #Adicionar na lista
    lista_turma = carregar_turma()
    lista_turma.append(nova_turma)
    #Salvar a lista no arquivo
    salvar_turma(lista_turma)  
def listar_dados_turma():
    lista_turma = carregar_turma()
    if not lista_turma:
        print("Não há turmas cadastradas")
    else:
        c = 1  #contador
        for turma in lista_turma:  #procurando na lista
            #coloque dentro do `{}` o valor de c e os valores que estão no dicionário
            print("{} - Código da turma:{} - Código do professor:{} - Código da disciplina:{}".format(c, turma['ódigo da turma'], turma['código do professor'], turma['código da disciplina']))
            c = c + 1  #contador acrecenta 1 a cada estudante
def excluir_dados_turma():
    #Pedir os dados para confirmação 
    codigo_busca = int(input("\nDigite o código da turma em que deseja excluir:"))
    lista_turma = carregar_turma()
    for turma in lista_turma: #pesquisa na lista
        if not turma['codigo'] == codigo_busca:
            print("Código não encontrado\nTente novamente")

        if turma['codigo'] == codigo_busca:
            print ("Turma encontrada")
            #Confirmação do procediemnto
        if input("\nDeseja excluír a turma cujo código é {}? (s/n):".format(turma['Código da turma'])) == "s".lower():
            #Exclusão dos dados 
            lista_turma.remove(turma)
            salvar_turma(lista_turma)
            print ("Registro Apagado :)")
            break
        else:
            continue 
    if not lista_turma:
        print("Não há turmas cadastradas")    
def editar_dados_turma():
    #Pedir o código da turma
    lista_turma = carregar_turma()
    codigo_busca = int(input("\nDigite o código da turma em que deseja alterar:"))

    for turma in lista_turma: #Busca na lista
        if not turma['codigo'] == codigo_busca:
            print("Código não encontrado\nTente novamente")

        if turma['codigo'] == codigo_busca:
            print ("Turma encontrada")
        #Confirmação    
        if input("\nDeseja alterar a turma cujo código é {}? (s/n):".format(turma['Código da turma'])) == "s".lower():
            #Entrada dos novos dados
            codigo_turma = int(input("\nDigite o código da turma:"))
            time.sleep(1)
            codigo_professor = int(input("\nDigite o código do professor:"))
            time.sleep(1)
            codigo_disciplina = int(input("\nDigite o código da disciplina:"))
            #Editar o dicionário
            turma['código da turma'] = codigo_turma
            turma['código do professor'] = codigo_professor
            turma['código da disciplina'] = codigo_disciplina
            salvar_turma(lista_turma)
            print ("Registros atualizados ;)")
            break
        else:
            continue 
    if not lista_turma:
        print("Não há turmas cadastradas")   

def carregar_matricula():
    #Tentar abrir o arquivo
    try:
        #Abre um arquivo para leitura (READ)
        with open ("matriculas.json", "r") as f:
            #Trasforma arquivo Json em objeto python
            lista_matricula = json.load(f)
            return lista_matricula
    #Caso não encontre o arquivo    
    except FileNotFoundError:
        lista_professor = []
        return lista_professor    
def salvar_matricula(lista_matricula): 
    #Abre o arquivo para escrita (WRITE), se não existir ele cria um novo
    with open ("matriculas.json", "w") as f:
        #Transforma a lista em Json e joga para dentro do arquivo
        json.dump(lista_matricula, f)
def inserir_dados_matricula():
    # Pedir os dados.
    time.sleep(1)
    codigo_turma = int(input("\nDigite o código da turma:"))
    time.sleep(1)
    codigo_estudante = int(input("\nDigite o código do estudante:"))
    #Criação do dicionario
    nova_matricula = {'código da turma':codigo_turma, 'código do estudante':codigo_estudante}
    #Adicionar na lista
    lista_matricula = carregar_matricula()
    lista_matricula.append(nova_matricula)
    #Salvar a lista no arquivo
    salvar_matricula(lista_matricula)  
def listar_dados_matricula():
    lista_matricula = carregar_matricula()
    if not lista_matricula:
        print("Não há matrículas cadastradas")
    else:
        c = 1  #contador
        for matricula in lista_matricula:  #procurando na lista
            #coloque dentro do `{}` o valor de c e os valores que estão no dicionário
            print("{} - Código da turma:{} - Código do estudante:{}".format(c, matricula['código da turma'], matricula['código do estudante']))
            c = c + 1  #contador acrecenta 1 a cada estudante
def excluir_dados_matricula():
    #Pedir os dados para confirmação 
    codigo_busca = int(input("\nDigite o código da matrícula em que deseja excluir:"))
    lista_matricula = carregar_matricula()
    for matricula in lista_matricula: #pesquisa na lista
        if not matricula['codigo'] == codigo_busca:
            print("Código não encontrado\nTente novamente")

        if matricula['codigo'] == codigo_busca:
            print ("Matrícula encontrada")
            #Confirmação do procediemnto
        if input("\nDeseja excluír a matrícula cujo código da turma é {}? (s/n):".format(matricula['Código da turma'])) == "s".lower():
            #Exclusão dos dados 
            lista_matricula.remove(matricula)
            salvar_matricula(lista_matricula)
            print ("Registro Apagado :)")
            break
        else:
            continue 
    if not lista_matricula:
        print("Não há matrículas cadastradas")    
def editar_dados_matricula():
        #Pedir o código da turma
    lista_matricula = carregar_matricula()
    codigo_busca = int(input("\nDigite o código da matrícula em que deseja alterar:"))

    for matricula in lista_matricula: #Busca na lista
        if not matricula['codigo'] == codigo_busca:
            print("Código não encontrado\nTente novamente")

        if matricula['codigo'] == codigo_busca:
            print ("Matrícula encontrada")
        #Confirmação    
        if input("\nDeseja alterar a matrícula cujo código da turma é {}? (s/n):".format(matricula['Código da turma'])) == "s".lower():
            #Entrada dos novos dados
            codigo_turma = int(input("\nDigite o código da turma:"))
            time.sleep(1)
            codigo_estudante = int(input("\nDigite o código do estudante:"))
            time.sleep(1)
            #Editar o dicionário
            matricula['código da turma'] = codigo_turma
            matricula['código do professor'] = codigo_estudante

            salvar_matricula(lista_matricula)
            print ("Registros atualizados ;)")
            break
        else:
            continue 
    if not lista_matricula:
        print("Não há matrículas cadastradas")   




#Criação do menu principal
op = 1

while op >= 1 and op <= 6:
    print("\n>>>>>> Olá, bem vindo ao Sistema PUC <<<<<<\n"
    "\nPrimeiramente selecione uma categoria da qual deseja alterar:\n")

    time.sleep(2)
    print("1. Estudante")
    # time.sleep(1)
    print("2. Disciplina")
    # time.sleep(1)
    print("3. Professor")
    # time.sleep(1)
    print("4. Turma")
    # time.sleep(1)
    print("5. Matrícula")
    # time.sleep(1)
    print("6. SAIR")

    #Entrada da opção desejada
    op = int(input("\nDigite a opção desejada: "))

    if op == 1:
        print("\nBem vindo a área dos ESTUDANTES")
    elif op == 2:
        print("\nBem vindo a área das DISCIPLINAS")
    elif op == 3:
        print("\nBem vindo a área dos PROFESSORES")
    elif op == 4:
        print("\nBem vindo a área das TURMAS")
    elif op == 5:
        print("\nBem vindo a área das MATRÍCULAS")
    elif op == 6:
        print("\nDesconectando...\n")
        break
    else:
        print("Opção Inválida")
        op = 1
        continue

    #Criação do menu de operações
    op2 = 1
    while op2 >= 1 and op2 <= 4:
        print("\nO que você gostaria de fazer?\n")

        time.sleep(1)
        print("1. Incluir novo registro")
        print("2. Listar registros")
        print("3. Excluir registro")
        print("4. Alterar um registro")
        print("5. Voltar ao menu inicial")

        #Entrada da opção desejada
        op2 = float(input("\nDigite a opção desejada: "))

#>>>>> ESTUDANTE

        #Incluir estudante
        while op2 == 1 and op == 1:
            #Chamada da função
            inserir_dados_estudantes()            
            if input("\nDeseja cadastrar um novo estudante? (s/n): ") == "s".lower():
                continue
            else:
                break

        #Listar estudantes
        if op2 == 2 and op == 1:
            print("\n>>> LISTA DOS ESTUDANTES <<<")
            listar_dados_estudantes()

        #Excluir estudante
        elif op2 == 3 and op == 1:
            excluir_dados_estudantes()            

        #Atualizar estudante
        elif op2 == 4 and op == 1:
            editar_dados_estudante()

#>>>>> DISCIPLINA

        #Incluir disciplina 
        while op2 == 1 and op == 2:
            #Chamada da função 
            inserir_dados_disciplinas()
            if input("\nDeseja cadastrar uma nova disciplina? (s/n): ") == "s".lower():
                continue
            else:
                break

        #Listar disciplinas        
        if op2 == 2 and op == 2:
            print("\n>>> LISTA DAS DISCIPLINAS <<<")
            #Chamada da função
            listar_dados_disciplinas()

        #Excluir disciplina
        elif op2 == 3 and op == 2:
            excluir_dados_disciplinas()          

        #Atualizar estudante
        elif op2 == 4 and op == 2:
            editar_dados_disciplina()

#>>>>> PROFESSOR           

        #Incluir professor
        while op2 == 1 and op == 3:
            #Chamada da função 
            inserir_dados_professor()
            if input("\nDeseja cadastrar um novo professor? (s/n): ") == "s".lower():
                continue
            else:
                break

        #Listar professores        
        if op2 == 2 and op == 3:
            print("\n>>> LISTA DOS PROFESSORES <<<")
            #Chamada da função
            listar_dados_professor()

        #Excluir professor
        elif op2 == 3 and op == 3:
            excluir_dados_professor()          

        #Atualizar professor
        elif op2 == 4 and op == 3:
            editar_dados_professor()

#>>>>> TURMAS          

        #Incluir turma
        while op2 == 1 and op == 4:
            #Chamada da função 
            inserir_dados_turma()
            if input("\nDeseja cadastrar uma nova turma? (s/n): ") == "s".lower():
                continue
            else:
                break

        #Listar turmas        
        if op2 == 2 and op == 4:
            print("\n>>> LISTA DAS TURMAS <<<")
            #Chamada da função
            listar_dados_turma()

        #Excluir turma
        elif op2 == 3 and op == 4:
            excluir_dados_turma()          

        #Atualizar turmas
        elif op2 == 4 and op == 4:
            editar_dados_turma()

#>>>>> MATRÍCULAS          

        #Incluir matrícula
        while op2 == 1 and op == 5:
            #Chamada da função 
            inserir_dados_matricula()
            if input("\nDeseja cadastrar uma nova matrícula? (s/n): ") == "s".lower():
                continue
            else:
                break

        #Listar matrículas        
        if op2 == 2 and op == 5:
            print("\n>>> LISTA DAS MATRÍCULAS <<<")
            #Chamada da função
            listar_dados_matricula()

        #Excluir matrícula
        elif op2 == 3 and op == 5:
            excluir_dados_matricula()          

        #Atualizar matrícula
        elif op2 == 4 and op == 5:
            editar_dados_matricula()
        
        #Voltar para o menu de operações    
        if op2 == 5:
            continue

