import os; os.system('cls')

PETS = []
EVENTOS=[]
ARQUIVO_PETS = 'nomePets.txt'
HUMOR_PETS = 'humor.txt'
METAS = {}
PROGRESSO = {}
quantMC = 1

def CRUD():
    def adicionar():
        while True:    
            try:
                nome = input("Nome do pet: ").capitalize()
                while True:
                    especie = input("Espécie (Cachorro/Gato): ").capitalize()
                    if especie in ["Cachorro", "Gato"]:
                        break
                    else:
                        print("Espécie Inválida! Digite 'Cachorro' ou 'Gato'")
                        especie = input("Espécie (Cachorro/Gato): ").capitalize()
    
                raca = input("Raça: ").capitalize()
                try:
                    data = input("Data de nascimento (DD/MM/AAAA): ")
                    dia, mes, ano = data.split("/",2)
                    int(dia)
                    if not 31>=int(dia)>0:
                        print("Data inválida!")
                        data = input("Data de nascimento (DD/MM/AAAA): ")
                        dia, mes, ano = data.split("/",2)
                        int(dia)
                        int(mes)
                        int(ano)
                    
                    int(mes)
                    
                    if not 12>=int(mes)>0:
                        print("Data inválida!")
                        data = input("Data de nascimento (DD/MM/AAAA): ")
                        dia, mes, ano = data.split("/",2)
                        int(dia)
                        int(mes)
                        int(ano)
                        
                    int(ano)

                    if not 2025>=int(ano)>0:
                        print("Data inválida!")
                        data = input("Data de nascimento (DD/MM/AAAA): ")
                        dia, mes, ano = data.split("/",2)
                        int(dia)
                        int(mes)
                        int(ano)
                
                except (ValueError,KeyboardInterrupt):
                    print("Informação inválida! Digite Novamente.")
                    data = input("Data de nascimento (DD/MM/AAAA): ")
                    dia, mes, ano = data.split("/",2)
                    int(dia)
                    if not int(dia)>0:
                        print("Data inválida!")
                        data = input("Data de nascimento (DD/MM/AAAA): ")
                        dia, mes, ano = data.split("/",2)
                        int(dia)
                        int(mes)
                        int(ano)
                    
                    int(mes)
                    
                    if not int(mes)>0:
                        print("Data inválida!")
                        data = input("Data de nascimento (DD/MM/AAAA): ")
                        dia, mes, ano = data.split("/",2)
                        int(dia)
                        int(mes)
                        int(ano)
                        
                    int(ano)

                    if not int(ano)>0:
                        print("Data inválida!")
                        data = input("Data de nascimento (DD/MM/AAAA): ")
                        dia, mes, ano = data.split("/",2)
                        int(dia)
                        int(mes)
                        int(ano)
                

                     
                try:
                    peso = input("Peso em kg: ")
                    int(peso)
                    if not int(peso)>0:
                        print("Peso inválido!")
                        peso = input("Peso em kg: ")
                        int(peso)
                except (ValueError,KeyboardInterrupt):
                    print("Informação inválida! Digite Novamente.")
                    peso = input("Peso em kg: ")
                    int(peso)

                    
                
                PETS.append({"Nome": nome, "Espécie": especie, "Raça": raca, "Data": data, "Peso": peso})
                print("Pet adicionado com sucesso!")
                file=open(ARQUIVO_PETS, 'a', encoding='utf-8')
                file.write(f"{nome}\n")
                file.close()
                break

            except (ValueError,KeyboardInterrupt):
                print("Informação inválida! Digite Novamente.")
        
        
    def visualizar():
        if not PETS:
            print("Nenhum pet cadastrado!")
        else:
            print("-=-=-=-=Pets Cadastrados-=-=-=-=")
            for dicionarios in PETS:
                print(f"Nome: {dicionarios['Nome']}")
                print(f"Espécie: {dicionarios['Espécie']}")
                print(f"Raça: {dicionarios['Raça']}")
                print(f"Data: {dicionarios['Data']}")
                print(f"Peso: {dicionarios['Peso']}")
                print("-" * 20)
            print("\n")

    def editarnomehumor(nome_antigo, novo_nome):
        try:    
            with open(HUMOR_PETS, 'r', encoding='utf-8') as f:
                linhas = []
                for linha in f:
                    nomepet, humorpet = linha.strip().split(",",1)
                    if nomepet == nome_antigo:
                        linhas.append(f"{novo_nome},{humorpet}")
                    else:
                        linhas.append(linha)
            with open(HUMOR_PETS, 'w', encoding='utf-8') as f2:
                for elemento in linhas:
                    f2.write(elemento + '\n')
        except FileNotFoundError:
            return
    

    def editarnomehumornome(nome_antigo, novo_nome):
        try:    
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                linhas = []
                for linha in f:
                    if linha.strip() == nome_antigo:
                        linhas.append(novo_nome+"\n")
                    else:
                        linhas.append(linha)
            with open(ARQUIVO_PETS, 'w', encoding='utf-8') as f2:
                for elemento in linhas:
                    f2.write(elemento + '\n')
        except FileNotFoundError:
            return


    def editar():
        if not PETS:
            print("Nehum pet cadastrado!")
        else:
            for i in range(len(PETS)):
                print(f"-{PETS[i]["Nome"]}")
            nome_antigo = input("Digite o nome do pet que você deseja editar: ").capitalize()
            nomesparaeditar = []
            for i in range(len(PETS)):
                nomesparaeditar.append(PETS[i]["Nome"])
                if (PETS[i]["Nome"])==nome_antigo:
                    while True:
                        try:    
                            print("NOVOS DADOS")
                            novo_nome = input("Digite o nome do pet: ").capitalize()
                            nova_especie = input("Espécie (Cachorro/Gato): ").capitalize()
                            nova_raca = input("Raça: ").capitalize()
                            nova_data = input("Data de nascimento (DD/MM/AAAA): ")
                            dia, mes, ano = nova_data.split("/",2)
                            int(dia)
                            int(mes)
                            int(ano)
                            novo_peso = input("Peso em kg: ")
                            int(novo_peso)
                            
                            PETS[i]=({"Nome": novo_nome, "Espécie": nova_especie, "Raça": nova_raca, "Data": nova_data, "Peso": novo_peso})
                            print("Pet atualizado com sucesso!")
                            editarnomehumor(nome_antigo, novo_nome)
                            editarnomehumornome(nome_antigo, novo_nome)
                            break 
                        except (ValueError,KeyboardInterrupt):
                            print("Informação inválida! Digite Novamente.")
                            pass
            if nome_antigo not in nomesparaeditar:
                print("Pet não encontrado!")


    def excluirnomehumor(nome_remover):
        try:    
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                linhas_filtradas = []
                for linha in f:
                    linha = linha.strip()
                    if not linha:
                        continue
                    nome, humor = linha.split(',')
                    if nome != nome_remover:
                        linhas_filtradas.append(linha + '\n')
                with open(ARQUIVO_PETS, 'w', encoding='utf-8') as f:
                    f.writelines(linhas_filtradas)
        except FileNotFoundError:
           return


    def excluirnomehumornome(nome_remover):
        try:    
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                linhas_filtradas = []
                for linha in f:
                    linha = linha.strip()
                    if not linha:
                        continue
                    if linha != nome_remover:
                        linhas_filtradas.append(linha + '\n')
                with open(ARQUIVO_PETS, 'w', encoding='utf-8') as f:
                    f.writelines(linhas_filtradas)
        except FileNotFoundError:
           return


    def remover():
        if not PETS:
            print("Nenhum pet cadastrado!")
        else:
            for i in range(len(PETS)):
                print(f"-{PETS[i]["Nome"]}")
            nome_remover = input("Digite o nome do pet que você deseja excluir: ").capitalize()
            for i in range(len(PETS)):
                if PETS[i]["Nome"]==nome_remover: 
                    del PETS[i]
                    print("Pet removido com sucesso!")
                    excluirnomehumor(nome_remover)
                    excluirnomehumornome(nome_remover)
                    break
                else:
                    print("Pet não encontrado.")

    def ler_arquivo():
        PETS.clear()
        try:
            arquivo = open("pets.txt", "r", encoding="utf-8")
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha == '':
                    break
                lista = linha.split(",")
                PETS.append({
                    "Nome": lista[0], 
                    "Espécie": lista[1], 
                    "Raça": lista[2], 
                    "Data": lista[3], 
                    "Peso": lista[4] 
                })
            arquivo.close()
        except FileNotFoundError:
            return

    def gravar_arquivo():
        arquivo = open("pets.txt", "w", encoding="utf-8")
        for dicionario in PETS:
            for chaves in dicionario:
                arquivo.writelines(dicionario[chaves] + ", ")
            arquivo.writelines("\n")
        arquivo.close()

    ler_arquivo()
    while True:
        print("-=-=-=-=CRUD-=-=-=-=")
        print("1- Adicionar Pet")
        print("2- Visualizar Pets Cadastrados")
        print("3- Editar Pet")
        print("4- Excluir Registros do Pet")
        print("5- Sair")
        try:
            escolha=int(input("\nOpção: "))
            if escolha==1:
                adicionar()
                gravar_arquivo()
            elif escolha==2:
                visualizar()
            elif escolha==3:
                editar()
                gravar_arquivo()
            elif escolha==4:
                remover()
                gravar_arquivo()
            elif escolha==5:    
                break
            else:
                print("Opção Inválida. Tente Novamente.")
        except ValueError:
            print("Opção Inválida! Digite um número inteiro.")
            
def CUIDADOS():
    def eventos():
        nomes = []
        if not PETS:
            print("Nenhum pet cadastrado!")
        else:
            for i in range(len(PETS)):
                nomes.append(PETS[i]["Nome"])
            while True:
                try:
                    escolha=input("Escolha o tipo de evento que você deseja registrar: \n1-Vacinação \n2-Consultas Veterinárias \n3-Aplicação de Remédios\n(Escreva o nome): ").capitalize()
                    if escolha == 'Vacinação' or escolha == 'Consultas Veterinárias' or escolha == 'Aplicação de Remédios':
                        print("-="*30)
                        print("PETS")
                        for i in range(len(PETS)):
                            print(f"-{PETS[i]["Nome"]}")
                        nome=input("\nDigite o nome do pet: ").capitalize()
                        if nome in nomes:
                            try:
                                data = input("Data do evento (DD/MM/AAAA): ")
                                dia, mes, ano = data.split("/",2)
                                int(dia)
                                if not 0<int(dia)<=31:
                                    print("Data inválida!")
                                    data = input("Data do evento (DD/MM/AAAA): ")
                                    dia, mes, ano = data.split("/",2)
                                    int(dia)
                                    int(mes)
                                    int(ano)
                                
                                    int(mes)
                    
                                    if not 0<int(dia)<=12:
                                        print("Data inválida!")
                                        data = input("Data do evento (DD/MM/AAAA): ")
                                        dia, mes, ano = data.split("/",2)
                                        int(dia)
                                        int(mes)
                                        int(ano)
                                        
                                    int(ano)

                                    if not 0<int(dia)<=2025:
                                        print("Data inválida!")
                                        data = input("Data do evento (DD/MM/AAAA): ")
                                        dia, mes, ano = data.split("/",2)
                                        int(dia)
                                        int(mes)
                                        int(ano)
                                
                            except (ValueError,KeyboardInterrupt):
                                    print("Informação inválida! Digite Novamente.")
                                    data = input("Data do evento (DD/MM/AAAA): ")
                                    dia, mes, ano = data.split("/",2)
                                    int(dia)
                                    if not (int(dia)>0 and int(dia)<=31):
                                        print("Data inválida!")
                                        data = input("Data de nascimento (DD/MM/AAAA): ")
                                        dia, mes, ano = data.split("/",2)
                                        int(dia)
                                        int(mes)
                                        int(ano)
                                    
                                    int(mes)
                                    
                                    if not (int(mes)>0 and int(mes)<=12):
                                        print("Data inválida!")
                                        data = input("Data do evento (DD/MM/AAAA): ")
                                        dia, mes, ano = data.split("/",2)
                                        int(dia)
                                        int(mes)
                                        int(ano)
                                        
                                    int(ano)

                                    if not (int(ano)>0 and int(ano)<=2025):
                                        print("Data inválida!")
                                        data = input("Data do evento (DD/MM/AAAA): ")
                                        dia, mes, ano = data.split("/",2)
                                        int(dia)
                                        int(mes)
                                        int(ano)
                
                            observacao=input("Observações: ").capitalize()
                            
                            EVENTOS.append({"Evento": escolha, "Nome": nome, "Data do evento": data, "Observação": observacao})
                            print("Evento adicionado com sucesso!")
                            break
                    else:
                        print("Opção inválida! Digite Novamente.")
                except ValueError:
                    print("Informação inválida! Digite Novamente.")
                    pass  
            
    def visualizar():
        if not EVENTOS:
            print("Nenhum evento registrado!")
        else:
            try:
                for nome in EVENTOS:
                    print("-=-=-=-=Eventos Cadastrados-=-=-=-=")
                    print(f"Evento: {nome['Evento']}")
                    print(f"Nome: {nome['Nome']}")
                    print(f"Data do evento: {nome['Data do evento']}")
                    print(f"Observação: {nome['Observação']}")
                    print("-" * 20)
                print("\n")
            except FileNotFoundError:
                print("Arquivo não encontrado.")



    def acompanhar():
        if not EVENTOS:
            print("Nenhum evento cadastrado!")
        else:
            for i in range(len(EVENTOS)):
                print("-="*30)
                print(f"-{EVENTOS[i]["Nome"]}: {EVENTOS[i]["Evento"]}")
            nome_escolhido=input("Qual o nome do pet de quem você deseja marcar o evento como feito? ").capitalize()
            for i in range(len(EVENTOS)):
                if (EVENTOS[i]["Nome"])==nome_escolhido: 
                    del EVENTOS[i]
                    print(f"Evento de {nome_escolhido} removido com sucesso.")
                    break
                else:
                    print("Registro não encontrado.")
                    

    def gravar_arquivo():
        arquivo = open("eventos.txt", "w", encoding="utf-8")
        for dicionario in EVENTOS:
            for chaves in dicionario:
                arquivo.writelines(dicionario[chaves] + ", ")
            arquivo.writelines("\n")
        arquivo.close()
        
    def ler_eventos():
        try:
            with open("eventos.txt", "r", encoding="utf-8") as file:
                linhas = file.readlines()
                for linha in linhas:
                    if linha.strip() == "": 
                        continue
                    lista = linha.strip().split(",")
                    EVENTOS.append({
                        "Evento": lista[0].strip(),
                        "Nome": lista[1].strip(),
                        "Data do evento": lista[2].strip(),
                        "Observação": lista[3].strip()
                    })
        except FileNotFoundError:
            return

    ler_eventos()
    while True:
        print("-=-=-=-=Cadastro de Cuidados e Eventos-=-=-=-=")
        print("1- Registrar Eventos")
        print("2- Visualizar Eventos")
        print("3- Marcar Eventos como Feitos")
        print("4- Sair")
        try:
                escolha=int(input("\nOpção: "))
                if escolha==1:
                    eventos()
                    gravar_arquivo()
                elif escolha==2:
                    visualizar()
                elif escolha==3:
                    acompanhar()
                    gravar_arquivo()
                elif escolha==4:
                    break
                else:
                    print("Opção Inválida! Tente Novamente.")
            
        except ValueError:
                print("Opção Inválida! Tente Novamente.")

def PERSONALIZADO():
        nomes=[]
        def sugestoes():
            print("PETS")
            for i in range(len(PETS)):
                nomes.append(PETS[i]["Nome"])
                print(f"-{PETS[i]["Nome"]}")            
            pet_escolhido = input("\nQual o nome do pet que você deseja obter sugestões de cuidado? ").capitalize()
            if pet_escolhido in nomes:
                for i in range(len(PETS)):
                    if (PETS[i]["Nome"])==pet_escolhido:
                        _, _, ano = PETS[i]["Data"].split("/")
                        idade = 2025 - int(ano)
                        especie=(PETS[i]["Espécie"]).strip()

                        if especie == 'Cachorro':
                            print("\nSugestão de cuidados:")
                            if 0<= idade <= 1:
                                print("\nAlimentação:\n É indicado ração premium para filhotes;" \
                                " com maior teor de proteínas, " \
                                "cálcio e fósforo para o desenvolvimento muscular e ósseo, " \
                                "além de ácidos graxos essenciais que contribum para o desenvolvimento da pelagem do filhote.")
                                print("Brinquedos:\n" \
                                " .Pelúcias, mordedores, bolinhas e brinquedos interativos são ótimos para estimulação, diversão e a prátca de exercícios. " \
                                "\n .Cordas e ossos podem ajudar no desenvolvimento dental e na satisfação da necessidade de morder. ")
                                print("Exercício:\n" \
                                " .Caminhadas curtas, brincadeiras e adestramento.\n" \
                                "OBS: É importante começar gradualmente e aumentar a intensidade e duração do exercício conforme o filhote cresce e se fortalece.")
                            else:
                                print("\nAlimentação:\n" \
                                " .Para cães adultos, as rações Super Premium são geralmente indicadas pelos veterinários devido à sua alta qualidade nutricional.\n" \
                                "A proteína animal de alta qualidade e digestibilidade, além de outros ingredientes benéficos, contribuem para a saúde e longevidade do animal. ")
                                print("Brinquedos:\n" \
                                " .Bolinhas e Frisbees: Para estimular o instinto de caça e gastar energia.\n" \
                                " .Mordedores e Ossos naturais: Para aliviar o estresse e limpar os dentes, além de satisfazer o instinto de mordedura.\n" \
                                " .Kongs recheáveis com petiscos ou ração: para entreter e estimular o cão mentalmente.\n" \
                                " .Labirintos: Para estimular o cão a resolver desafios e obter recompensas. ")
                                print("Exercício:\n" \
                                " .Caminhadas diárias\n" \
                                " .Corridas (dependendo da raça e condição física)\n" \
                                " .Brincadeiras de buscar (como bolinhas e frisbees)\n" \
                                " .Natação")
                            

                        elif especie == 'Gato': 
                            print("\nSugestão de cuidados:")
                            if  0<= idade <= 1:
                                print("\nAlimentação:\n " \
                                " .As rações super premium são recomendadas por sua qualidade e ingredientes, como carnes frescas, sem corantes artificiais e com nutrientes de fontes naturais.\n" \
                                " .Rações úmidas (lata ou sachê) também são boas opções, especialmente para facilitar a ingestão para filhotes com dentinhos ainda em desenvolvimento. ")
                                print("Brinquedos:\n" \
                                " .varinhas com penas ou ratinhos de pelúcia: Estimulam o instinto de caça.\n" \
                                " .Bolinhas, túneis e arranhadores: São brinquedos interativos que podem aliviar o stress do pet.  ")
                                print("Exercício:\n" \
                                " .Caça e Perseguição: Brincadeiras que envolvam perseguir e capturar, como usar um laser pointer, uma varinha com penas ou brinquedos que imitem presas.\n" \
                                " .Brincadeiras Interativas: Brincadeiras de inteligência, esconder pestiscos dentro de brinquedos para que o pet precise manipular os brinquedos para obter a comida, são ótimas para entreter e estimular a mente do pet.")
                                print("Alimentação: Ração adulta e, ocasionalmente, ração úmida.")
                                print("Brinquedos: Arranhadores, túneis, brinquedos com laser.")
                                print("Exercício: Brincadeiras diárias com estímulo físico.")
                            else:
                                print("\nAlimentação: Ração sênior com controle renal.")
                                print("Brinquedos: Leves e acessíveis.")
                                print("Exercício: Estímulo leve com petiscos ou brinquedos de fácil alcance.")
                                
                        else:
                            print("Espécie não reconhecida para sugestões.")

            else:
                print("Pet não encontrado.")
             
        print("-=-=-=-=Sugestões Personalizadas-=-=-=-=")
    
        with open("pets.txt","r",encoding="utf-8") as file:
            if PETS==[]:
                arquivo = open("pets.txt", "r", encoding="utf-8")
                linhas = arquivo.readlines()
                for linha in linhas:
                    if linha == '':
                        break
                    lista = linha.split(",")
                    PETS.append({
                        "Nome": lista[0], 
                        "Espécie": lista[1], 
                        "Raça": lista[2], 
                        "Data": lista[3], 
                        "Peso": lista[4] 
                    })
                arquivo.close()
                sugestoes()
            else:
                sugestoes()

def HUMOR():
    def AcoesHumor(MediaHumor, QuantidadeHumor, NomePet):
        if MediaHumor >= 0 and MediaHumor < 2:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que algo muito grave está acontecendo com {NomePet}. Ele pode estar com dor intensa, prostração extrema ou outro tipo de sofrimento agudo. Não espere: leve imediatamente ao veterinário. Esse estado não é normal e indica alto risco à saúde.")
        elif MediaHumor >= 2 and MediaHumor < 3:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está muito abatido, ainda que não em risco iminente como nos casos anteriores. É essencial agendar uma consulta veterinária com urgência e observar sinais clínicos (falta de apetite, comportamento retraído, vocalizações incomuns).")
        elif MediaHumor >= 3 and MediaHumor < 5:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está claramente desanimado, com menos interesse por atividades e interações. Pode ser tédio, dor leve ou desconforto emocional. Ofereça carinho, melhore o ambiente e monitore com atenção. Se o quadro persistir por mais de um dia, busque orientação profissional.")
        elif MediaHumor >= 5 and MediaHumor < 6:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está em um estado emocional parcialmente equilibrado, faltam demonstrações de alegria. Aproveite para variar os estímulos: um brinquedo novo, um passeio diferente ou um tempo extra de atenção já podem trazer mais ânimo.")
        elif MediaHumor >=6 and MediaHumor <7:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está com boa disposição e responde positivamente aos estímulos. Mantenha a rotina saudável, reforce bons comportamentos e introduza pequenas novidades no dia a dia para manter o bem-estar em alta.")
        elif MediaHumor >=7 and MediaHumor < 8:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está visivelmente bem, interativo e com energia. Aproveite esse bom momento para reforçar o vínculo com brincadeiras mais longas, passeios, comandos com reforço positivo e socialização (caso ele goste)")
        elif MediaHumor >=8 and MediaHumor <9:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} demonstra alegria, conforto e confiança no ambiente. Mantenha tudo que está funcionando: rotina estável, atividades prazerosas e sua presença constante. Pode ser um ótimo momento para ensinar truques ou incluir novos desafios leves.")
        else:
            acao = (f"De acordo com os {QuantidadeHumor} dias que você registrou, concluimos que {NomePet} está no ápice do bem-estar físico e emocional. Ele está ativo, confiante, tranquilo e feliz. Continue com a rotina atual e celebre esse ótimo momento com carinho, atividades que ele adora e até registros (fotos, vídeos) para guardar lembranças.")
        return acao


    def SugestãoHumor():
        nomes = []
        try:
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha = linha.strip()
                        if linha:
                            nomes.append(linha)    
            try:
                with open(HUMOR_PETS, 'r', encoding='utf-8') as f2:
                    conteudo = f2.read().strip()
                    if not conteudo:
                        print("-="*30)
                        print("Nenhum humor registrado! Não é possível sugerir melhorias.")
                        return
            except FileNotFoundError:
                print("-="*30)
                print("Nenhum humor registrado! Não é possível sugerir melhorias.")
                return      

            for pet in nomes:
                soma = 0
                cont = 0
                try:    
                    with open(HUMOR_PETS, 'r', encoding='utf-8') as f2:
                            for linha in f2:
                                linha = linha.strip()
                                if not linha:
                                    continue
                                nomePet, humor_str = linha.split(',')
                                if nomePet == pet:
                                    try:
                                        valor = int(humor_str)
                                        soma += valor
                                        cont += 1
                                    except ValueError:
                                        continue
                except FileNotFoundError:
                    print("-="*30)
                    print("Nenhum humor registrado! Dessa forma não é possivel sugerir melhorias para aumentar ou manter o humor.")
                    return
                if cont>0:
                    media = soma/cont
                    print("-="*30)
                    print("SUGESTÕES")
                    print(AcoesHumor(media, cont, pet))
                    print("-="*30)
                
        except FileNotFoundError:
            print("-="*30)
            print("Nenhum pet registrado!")
            return
                
    def ConfirmacaoExistenciaPet(nome):
        try:    
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                    for linha in f:
                        if linha.strip() == nome:
                            return True
            return False
        except FileNotFoundError:
            return False


    def PerguntaHumor(nome):
        while True:
            try:
                humor = int(input(f"MUITO TRISTE\t\t      MUITO FELIZ\n0  1  2  3  4  5  6  7  8  9  10\nDigite o número de acordo com o humor de {nome} hoje: "))
                if humor>=0 and humor<=10:
                    with open(HUMOR_PETS, 'a', encoding='utf-8') as f:
                        f.write(f"{nome},{humor}\n")
                        print("-="*30)
                        print(f"O humor de {nome} foi registrado com sucesso!")
                    break
                else:
                    print("-="*30)
                    print("Número inválido! Digite número entre 0 e 10.")
            except ValueError:
                print("-="*30)
                print("Resposta inválida! Só é permitido números inteiros entre 0 e 10.")


    def visualizarPet():
        print("-="*30)
        print("PETS")
        try:
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha = linha.strip()
                        if linha:
                            print(f"{linha}")  
        except FileNotFoundError:
            return
        print("-="*30)

    def visualizarPetHumor():
        nomesPet = []
        print("-="*30)
        print("PETS")
        try:
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha = linha.strip()
                        if linha:
                            nomesPet.append(linha)   
        
            for pet in nomesPet:
                soma = 0
                cont = 0
                try:   
                    with open(HUMOR_PETS, 'r', encoding='utf-8') as f2:
                            for linha in f2:
                                linha = linha.strip()
                                if not linha:
                                    continue
                                nomePet, humor_str = linha.split(',')
                                if nomePet == pet:
                                    try:
                                        valor = int(humor_str)
                                        soma += valor
                                        cont += 1
                                    except ValueError:
                                        continue
                except FileNotFoundError:
                    return 
                if cont>0:
                    print(f"{pet}")

        except FileNotFoundError:
            return
        print("-="*30)


    def visualizarHumor():
        nomes = []
        print("-="*30)
        try:
            with open(ARQUIVO_PETS, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha = linha.strip()
                        if linha:
                            nomes.append(linha)   
            nomesvishumor = []
            for pet in nomes:
                soma = 0
                cont = 0
                try:   
                    with open(HUMOR_PETS, 'r', encoding='utf-8') as f2:
                            for linha in f2:
                                linha = linha.strip()
                                if not linha:
                                    continue
                                nomePet, humor_str = linha.split(',')
                                nomesvishumor.append(nomePet)
                                if nomePet == pet:
                                    try:
                                        valor = int(humor_str)
                                        soma += valor
                                        cont += 1
                                    except ValueError:
                                        continue
                except FileNotFoundError:
                    print("Não há registros de humor de nenhum pet!") 
                    return 
                if cont>0:
                    media = soma/cont
                    print(f"Humor médio de {pet}: {media:.2f}")
                if not nomes:
                    print("Nenhum pet registrado! Não foi possível visualizar o humor.") 
            if not nomesvishumor:
                print("Não há registros de humor de nenhum pet!")

        except FileNotFoundError:
            print("Não há nenhum pet registrado! Não foi possível visualizar o humor.")
            return
        print("-="*30)


    def editarHumor(nome_editar):
        try:    
            with open(HUMOR_PETS, 'r', encoding='utf-8') as f:
                linhas = []
                for linha in f:
                    if linha.strip():
                        linhas.append(linha)
        except FileNotFoundError:
            print("-="*30)
            print(f"Não há registros de humor de {nome_editar}.")
            return

        ultimo_idx = None
        for i, linha in enumerate(linhas):
            linha = linha.strip()
            nome_pet, humor_pet = linha.split(',')
            if nome_pet == nome_editar:
                ultimo_idx = i
        if ultimo_idx is None:
            print("-="*30)
            print(f"Não há registros de humor para {nome_editar}.")
        else:
            linhas.pop(ultimo_idx)
            PerguntaHumor(nome_editar)
            ultima = None
            with open(HUMOR_PETS, 'r', encoding='utf-8') as f:
                for linha in f:
                    if linha.strip() != "":
                        ultima = linha
            if ultima is not None:
                linhas.append(ultima)
            
            with open(HUMOR_PETS, 'w', encoding='utf-8') as f:
                for l in linhas:    
                    f.write(l)


    def excluirHumor(nome_remover):
        try:    
            with open(HUMOR_PETS, 'r', encoding='utf-8') as f:
                linhas_filtradas = []
                existir = 0
                for linha in f:
                    linha = linha.strip()
                    if not linha:
                        continue
                    nome, humor = linha.split(',')
                    if nome != nome_remover:
                        linhas_filtradas.append(linha + '\n')
                    else:
                        existir+=1
                with open(HUMOR_PETS, 'w', encoding='utf-8') as f:
                    f.writelines(linhas_filtradas)
                if existir > 0:
                    print("-="*30)
                    print(f"Todos os registros de humor de {nome_remover} foram excluídos!")
                else:
                    print("-="*30)
                    print(f"Não existia nenhum registro de humor de {nome_remover}.")
        except FileNotFoundError:
            print("-="*30)
            print(f"Não existia nenhum registro de humor de {nome_remover}.")
    while True:
        print("-=-=-=-=Humor-=-=-=-=")
        print("1- Registrar Humor")
        print("2- Visualizar Humores Cadastrados")
        print("3- Editar Humor")
        print("4- Excluir Registros de Humor do Pet")
        print("5- Visualizar Sugestões Para Melhorar ou Manter o Humor do Seu Pet")
        print("6- Sair")
        try:
            escolha=int(input("Opção: "))
            if escolha==1:
                visualizarPet()
                nome = input("Digite o nome do pet: ").capitalize()
                if ConfirmacaoExistenciaPet(nome):
                    PerguntaHumor(nome)
                else:
                    print("-="*30)
                    print(f"{nome} ainda não foi registrado.")
            elif escolha==2:
                visualizarHumor()
            elif escolha==3:
                visualizarPetHumor()
                nome = input("Digite o nome do pet: ").capitalize()
                if ConfirmacaoExistenciaPet(nome):
                    editarHumor(nome)
                else:
                    print("-="*30)
                    print(f"{nome} ainda não foi registrado.")
            elif escolha==4:
                visualizarPetHumor()
                nome = input("Digite o nome do pet: ").capitalize()
                if ConfirmacaoExistenciaPet(nome):
                    excluirHumor(nome)
                else:
                    print(f"{nome} ainda não foi registrado.")
            elif escolha==5:
                SugestãoHumor()
            elif escolha==6:
                break 
            else:
                print("Opção Inválida! Tente Novamente.")
        except ValueError:
            print("-="*30)
            print("Opção Inválida! Tente Novamente.")

def ler_arquivo():
        PETS.clear()
        try:
            arquivo = open("pets.txt", "r", encoding="utf-8")
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha == '':
                    break
                lista = linha.split(",")
                PETS.append({
                    "Nome": lista[0], 
                    "Espécie": lista[1], 
                    "Raça": lista[2], 
                    "Data": lista[3], 
                    "Peso": lista[4] 
                })
            arquivo.close()
        except FileNotFoundError:
            pass

def META():
    opc = 0
    global quantMC
    while True:
            print("\n1 - Adicionar / 2 - Atualizar / 3- Visualizar / 4 - Sair ")
            try:
                opc = int(input("\nQual opcao? "))
                if opc == 1:
                    for i in range(len(PETS)):
                        print(f"-{PETS[i]["Nome"]}")
                    escolha = input("\nPara qual pet você quer estabelecer uma meta? ").capitalize()
                    for i in range(len(PETS)):
                        if (PETS[i]["Nome"])==escolha:
                            acao = input(f"\nQual a meta definida para o pet {escolha}? ")
                            relacao_tempo = input("\nEssa meta será diária, semanal, mensal ou anual? (D / S / M / A): ").lower()
                            if relacao_tempo == "d":
                                frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                                METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} {frequencia} vezes por dia")
                            elif relacao_tempo == "s":
                                tipo_semana = int(input("\nEscolha qual tipo será: 1 - por semana / 2 - a cada x semanas "))
                                if tipo_semana == 1:
                                    frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                                    METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} {frequencia} vezes por semana")
                                    print("\nMeta registrada com sucesso!")
                                elif tipo_semana == 2:
                                    frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                                    METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} a cada {frequencia} semanas")
                                    print("\nMeta registrada com sucesso!")
                            elif relacao_tempo == "m":
                                tipo_mes = int(input("\nEscolha qual tipo será: 1 - por mês / 2 - a cada x meses "))
                                if tipo_mes == 1:
                                    frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                                    METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} {frequencia} vezes por mês")
                                    print("\nMeta registrada com sucesso!")
                                elif tipo_mes == 2:
                                    frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                                    METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} a cada {frequencia} meses ")
                                    print("\nMeta registrada com sucesso!")
                            elif relacao_tempo == "a":
                                tipo_ano = int(input("\nEscolha qual tipo será: 1 - por ano / 2 - a cada x anos "))
                                if tipo_ano == 1:
                                    frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                                    METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} {frequencia} vezes por ano")
                                    print("\nMeta registrada com sucesso!")
                                elif tipo_ano == 2: 
                                    frequencia = float(input("\nCom que frequência você quer realizá-la?  "))
                                    METAS[quantMC]=(f"{quantMC}ª META -> {escolha} -> {acao} a cada {frequencia} anos ")
                                    print("\nMeta registrada com sucesso!")
                            else:
                                print("Informação inválida! Digite novamente!")
                            break
                        else:
                            print("Pet não encontrado.")    

                    PROGRESSO[quantMC] = 0
                    print(f"\n {METAS}")
                    quantMC+=1
                    gravar_metas()
                elif opc == 2:
                    if not METAS:
                        print("\nNão há metas registradas.")
                    else:
                        total_feito = 0
                        print("\nMetas: ")
                        for i in METAS:
                            print(f"{i}: {METAS[i]}")
                        numupd = int(input("\nQual meta será atualizada? "))
                        cumprido = float(input("\nQuantos % você ja cumpriu da meta? "))
                        if cumprido >0:
                            PROGRESSO[numupd] += cumprido
                                    
                            if PROGRESSO[numupd] >=100:
                                print("\nParabéns! Você cumpriu a meta!")
                                del METAS[numupd]
                                del PROGRESSO[numupd]
                            else:
                                print(f"\nAinda faltam {100 - PROGRESSO[numupd]} % da meta")
                        else:
                            print("Valor inválido!")
                            continue
                        gravar_metas()
                elif opc==3:
                    if not METAS:
                        print("\nNão há metas registradas.")
                    else:
                        print("\nMetas: ")
                        for i in METAS:
                            print(f"{i}: {METAS[i]}")
                elif opc == 4:
                    break
            except (ValueError, KeyboardInterrupt):
                print("\nInformação inválida! Digite Novamente. ")
                pass
    return METAS , PROGRESSO, quantMC

def ler_metas():
    try:
        file = open("meta.txt", "r", encoding="utf-8")
        linhas = file.read().splitlines()
        for linha in linhas:
            if "ª META" in linha:
                numero = int(linha.split("ª")[0])
                METAS[numero] = linha
            elif ":" in linha:
                numero, valor = linha.split(":")
                PROGRESSO[int(numero)] = float(valor)
        file.close()
    except FileNotFoundError:
        pass

def gravar_metas():
    file = open("meta.txt", "w", encoding="utf-8")
    for chave in METAS:
        file.writelines(METAS[chave] + '\n')
    for chave in PROGRESSO:
        file.writelines(f"{chave}:{PROGRESSO[chave]}\n")
    file.close()

ler_metas()

ler_arquivo()
while True:
    print("-=-=-=-=Vida Pet-=-=-=-=")
    print("1- CRUD")
    print("2- Cuidados e Eventos")
    print("3- Metas e Atualizações")
    print("4- Sugestões Personalizadas")
    print("5- Humor")
    print("6- Sair")
    try:
            escolha=int(input("\nOpção: "))
            if escolha==1:
                CRUD()
            elif escolha==2:
                CUIDADOS()
            elif escolha==3:
                META()
            elif escolha==4:
                PERSONALIZADO()
            elif escolha==5:
                HUMOR()
            elif escolha==6:
                break
            else:
                print("Opção Inválida! Tente Novamente.")
    except (ValueError, KeyboardInterrupt):
            print("Opção Inválida! Digite um número.")
