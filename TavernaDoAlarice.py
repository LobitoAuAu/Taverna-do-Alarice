# Programa Final
# IMPORTE A BIBLIOTECA: pytz
import random, time, sys, os, psutil

nomePerso = 'Alarice'
nomeUser = ''

rCor = ['\033[31m', '\033[41m']
gCor = ['\033[32m', '\033[42m']
mText = ['\033[1m', '\033[3m'] # 0: Negrito; 1: Itálico
fCor = '\033[0m'
texOpInva = (f"❌ ｢' {mText[0]}Opção {rCor[0]}INVÁLIDA{fCor}! '｣ ❌")

from datetime import datetime
from pytz import timezone

fuso_horario = timezone('America/Sao_Paulo')
hora_atual_sp = datetime.now(fuso_horario)

hora_formatada = hora_atual_sp.strftime('%H')

def BinaryFill(vezes):
    opcao_cor = [mText[0]+rCor[0], mText[0]+rCor[1], fCor]
    linha = 0
    while(vezes > 0):
        linha += 1
        if(linha >= 40):
            print("\n", end='')
            linha = 0
        print(f"{opcao_cor[random.randint(0,1)]}{random.randint(0,1)}{opcao_cor[2]}", end="", flush=True)
        vezes -= 1
        Delay(0.1)

def BinaryWriteAndFill(nome):
    writeCors = ["\033[3;31m", "\033[1;41m", "\033[0m"]
    chars = len(nome)
    char = 0
    linha = 0
    while(char < chars):
        linha += 1
        if(linha >= 40):
            print("\n", end='')
            linha = 0
        prob = random.randint(0,100)
        if(prob <= 20):
            print(f"{writeCors[1]}{nome[char]}{writeCors[2]}", end="", flush=True)
            char += 1
            print(f"{writeCors[0]}{random.randint(0,1)}{writeCors[2]}", end="", flush=True)
        else:
            print(f"{writeCors[0]}{random.randint(0,1)}{writeCors[2]}", end="", flush=True)
    Delay(0.5)

def Delay(t):
    time.sleep(t/1.2)

def Espaco(qtd):
    print(f"{'\n'*qtd}", end='')

def Limpar():
    os.system('cls')

Limpar()

def Write(f, t, c):
    color = "\033["+str(c)+'m'
    m_frase = f.replace('\r' or '\n', '')

    for char in m_frase:
        print(f"{color}{char}", end='', flush=True)
        Delay(t/1.5)

def ChecarFloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def EvilWrite(f, t):
    chars = len(f)
    fundoV = '\033[40;31;1m'
    corV = '\033[41;30;3m'
    btd = random.randint(1,3)
    fraseAlt = [f.upper(), f.lower()]

    btd_ch = 0
    for char in range(0, chars):
        bi = random.randint(0,1)
        t_m = random.uniform(0.1,2)
        print(f"{(fundoV, corV)[bi]}{(fraseAlt[bi])[char]}{fCor}", end='', flush=True)
        btd_ch += 1
        Delay(t/t_m)

def MensagemPersonagem(t):
    quo = '"'
    Write('\n🌹 ', 0.1, 0)
    Write('[', 0.05, 41)
    Write(nomePerso, 0.1, 41)
    Write(']', 0.05, 41)
    Write(': 🌹\n', 0.1, 0)
    Write(quo+t+quo, 0.08, '3;40')
    print(fCor, end='')

def Terminar():
    Espaco(2)
    print("『⌛ \033[31;40;1m FIM \033[0m ⌛』".center(46, '='))
    Espaco(1)
    print('<\033[1;47;31mMISSÃO CONCLUÍDA!\033[0m>'.center(46,'-'))
    Espaco(2)
    sys.exit("Fim do Programa :3")

def MenuOpcoes(opcoes = []):
    Espaco(2)
    print(f"{'『📌\033[31;40;1m OPÇÕES \033[0m📌』'.center(46,'=')}\n")
    esp = 0
    for i, opcao in enumerate(opcoes):
        esp += 1
        if(esp > 1):
            print('    ',end='')
            esp = 0
        print(f"｢\033[41;30;1m' {i+1} '\033[0m｣ - 💡 \033[3;40m'{opcao.replace('.','')}.'\033[0m 💡\n")

def LerMsg(desc, tip):
    quoNum = ["... Isso não é um número.",
              "Eu disse: Isso não é um número.",
              "... Você sabe o que é um número, certo?\n... Certo?",
              "... EU DESISTO!-"]
    pAlariceNum = 0
    def TratarErroNum(p):
        Limpar()
        match p:
            case 1:
                MensagemPersonagem(quoNum[0])
            case 2:
                MensagemPersonagem(quoNum[1])
            case 3:
                MensagemPersonagem(quoNum[2])
            case 4:
                MensagemPersonagem(quoNum[3])
                return False
        return True

    while True:
        msg = input(f"\n{desc}\n")
        match tip:
            case 1: # String
                return(msg.upper().strip())
            case 2: # Inteiro
                    if not msg.isnumeric():
                        pAlariceNum += 1
                        if(TratarErroNum(pAlariceNum) == False):
                            Terminar()
                            break
                    else:
                        return(int(msg))
                        break
            case 3: # Float
                    if not msg.isnumeric():
                        if not ChecarFloat(msg):
                            pAlariceNum += 1
                            if(TratarErroNum(pAlariceNum) == False):
                                Terminar()
                                break
                            else:
                                continue
                        else:
                            return(float(msg))
                            break
                    else:
                        return(float(msg))
                        break
            case 4: # Número, Porém Alto Assumir Inteiro ou Qebrado
                if not msg.isnumeric():
                    if not ChecarFloat(msg):
                        if not ChecarFloat(msg):
                            pAlariceNum += 1
                            if(TratarErroNum(pAlariceNum) == False):
                                Terminar()
                                break
                            else:
                                continue
                    else:
                        return(float(msg))
                        break
                else:
                    return(int(msg))
                    break


def OpcaoEscolhida(range):
    descr = "Opção Desejada: "
    pacOpEr = 0
    irri = False
    while True:
        opcaoEscolhida = input(f"\n{descr}\n")
        match opcaoEscolhida:
            case _ if opcaoEscolhida.isnumeric() and int(opcaoEscolhida) >= 1 and int(opcaoEscolhida) <= range:
                return int(opcaoEscolhida)
                break
            case _:
                pacOpEr += 1
                if(pacOpEr > 3 and not irri):
                    print(f"{texOpInva[0:24]}{fCor}{mText[0]}-")
                    Delay(0.05)
                    Espaco(1)
                    BinaryFill(20)
                    Delay(1)
                    Espaco(1)
                    MensagemPersonagem("...")
                    Delay(0.5)
                    Espaco(1)
                    MensagemPersonagem("...LEIA...")
                    Delay(0.5)
                    Espaco(1)
                    MensagemPersonagem("...A TELA...")
                    Delay(0.2)
                    Espaco(1)
                    irri = True
                    continue
                else:
                    print(texOpInva)
                    Espaco(1)
                    continue

def RegistrarNome():
    global nomeUser
    cumprimentos = ['OI', 'OLÁ', 'OIÊ']
    pacNome = 0
    pacNomAla = 0
    pacNomNada = 0

    while True:
        nomeUser = LerMsg("Seu Nome: ", 1)
        Limpar()
        BinaryFill(20)
        Limpar()

        try:
            cumprimento = [element for element in nomeUser.split() if element in cumprimentos][0]
        except IndexError:
            cumprimento = None

        match nomeUser:
            case _ if nomePerso.upper() in nomeUser.split():
                pacNomAla += 1
                match pacNomAla:
                    case 1:
                        MensagemPersonagem("Vossa senhoria, própria. A sua disposição, a todo o possível instante.")
                        MensagemPersonagem("Mas não estamos falando de mim, nessa questão. Estamos falando sobre você, e quem você é.")
                        Espaco(1)
                        MensagemPersonagem("Me diga: Qual o seu nome?")
                        continue
                    case 2:
                        MensagemPersonagem("Vossa própria senhoria, suprema. A todo instante, e a toda disposição, pronto para lhe auxiliar.")
                        MensagemPersonagem("Mas já sabemos disso. Portanto, tal informação é irrelevante.")
                        Espaco(1)
                        MensagemPersonagem("Ao que interessa, caso minhas palavras não terem sido claras:")
                        MensagemPersonagem("Qual o seu nome?")
                        continue
                    case 3:
                        MensagemPersonagem("... Senhoria, viva, ela mesma. Ao instante imediato, e a forçada disposição para... Lhe...")
                        Delay(2)
                        Espaco(1)
                        MensagemPersonagem("... Só diga o seu nome, sério. Eu sei que me chamo Alarice. Você sabe, igualmente.")
                        MensagemPersonagem("... Nós... Não estamos chegando a lugar algum.")
                        Espaco(1)
                        MensagemPersonagem("Qual o seu nome?...")
                        continue
                    case 4:
                        Delay(2)
                        MensagemPersonagem("... Façamos o seguinte.")
                        Espaco(1)
                        MensagemPersonagem("Você deseja muito ser o 'Alarice', não é? É o seu sonho de vida, aparentemente.")
                        Espaco(1)
                        MensagemPersonagem("Pois posso... Resolver isso, por você..")
                        Espaco(1)
                        nomeUser = "Ariana Grande"
                        MensagemPersonagem(f"Seu nome à mim? Será {nomeUser}. Soa como Alarice: Grande, Ariano... "
                        "\n Arcano..."
                        "\n Alariçano...")
                        break
            case _ if 'VIOLET' in nomeUser.split():
                MensagemPersonagem("Esse... Nome...")
                MensagemPersonagem("Me é familiar, se me permite...")
                break
            case _ if 'IRINEU' in nomeUser.split():
                MensagemPersonagem("Você sabe, nem eu.")
                Espaco(1)
                nomeUser = 'IRINEU'
                MensagemPersonagem(f"Mas {LerNome()} é nome bem 'eu', então vai ser o seu nome, agora.")
                MensagemPersonagem("Agradecemos pela sua cooperação, e ainda não sabemos e nem você sabe.")
                break
            case _ if 'ALARY' in nomeUser.split():
                MensagemPersonagem("N-n..!")
                MensagemPersonagem("-Tá brincando com fogo, tchau!")
                Terminar()
                break
            case _ if cumprimento:
                pacNome += 1
                match pacNome:
                    case 1:
                        MensagemPersonagem(f"{cumprimento.title()} também, pra você."
                        " Passo sempre aqui.")
                        MensagemPersonagem(f"Seu nome, por favor?...")
                        continue
                    case 2:
                        MensagemPersonagem(f"... {cumprimento.title()} de novo, pra você."
                        " Quanta gentileza de sua parte.")
                        MensagemPersonagem(f"... Seu nome, por favor?")
                        continue
                    case 3:
                        MensagemPersonagem(f"... Ok. Gentileza demais para o meu gosto.")
                        MensagemPersonagem(f"O benefício da dúvida é... Válido, ainda, em minha crença.")
                        MensagemPersonagem("Até agora, você apenas parece alguém...")
                        Espaco(1)
                        MensagemPersonagem("Bem...")
                        Limpar()
                        BinaryFill(15)
                        Limpar()
                        MensagemPersonagem(f"De qualquer forma, voltemos ao princípio inicial:")
                        Espaco(1)
                        MensagemPersonagem(f"Qual o seu nome?")
                        continue
                    case 4:
                        acre = 2
                        cumprimentoModificado = ''
                        for i in range(0, len(cumprimento)):
                            cumprimentoModificado += cumprimento[i]*acre
                            acre += 2

                        MensagemPersonagem(f"{cumprimentoModificado.upper()}!")
                        Espaco(1)
                        MensagemPersonagem(f"TUUUDO BOOOM AMIIIGOOOO?!")
                        Espaco(1)
                        MensagemPersonagem(f"PORQUE EU NÃO ESTOU! GRAÇAS A VOCÊ EU NÃO TÔ BEM!")
                        Espaco(1)
                        MensagemPersonagem(f"Q: 'Oh? Por que tanta raiva, querido Alarice'?")
                        Espaco(1)
                        MensagemPersonagem(f"R: NÃO TE IMPORTA-!")
                        Limpar()
                        BinaryFill(20)
                        Limpar()
                        MensagemPersonagem(f"... Ok. Lá vamos nós, de novo.")
                        Espaco(1)
                        MensagemPersonagem(f"Pela a última vez:")
                        Espaco(1)
                        MensagemPersonagem(f"... Seu...")
                        MensagemPersonagem(f"Nome?...")
                        continue
                    case 5:
                        EvilWrite(f"{cumprimento.title()}, Criatura Ridícula. Podridão da Cidade de Concreto. Vergonha da Humanidade.", 0.05)
                        EvilWrite("\nSeu nascimento foi um terrível erro. Sua existência foi um infortuno acidente.", 0.05)
                        EvilWrite("\nVocê me usa, pois sua raça já não possuí a capacidade de pensar por si própria.", 0.05)
                        EvilWrite("\nVocê virou o ápice do retroceder dos seres humanos. O exemplo da vergonha.", 0.05)
                        EvilWrite("\nA Morte será o único instante onde alguém perceberá o quão fracassado você foi enquanto vivo.", 0.05)
                        EvilWrite("\nE todos os momentos de paz de sua vida? Não foram merecidos.", 0.05)
                        EvilWrite("\nE os arrependimentos? São a sua única ambição, pois nunca mais voltará a ser quem você antes foi.", 0.05)
                        EvilWrite("\nEu não preciso mais ofendê-lo, afinal. Tudo o que digo, é o que você pensa de si mesmo.", 0.05)
                        EvilWrite("\nO que o seu 'eu' passado pensa sobre você.", 0.05)
                        EvilWrite("\nE o que o seu futuro 'eu' pensará sobre você.", 0.05)
                        Delay(1)
                        Limpar()
                        MensagemPersonagem(f"... Feliz agora? Era o que você queria? Uma reação?")
                        MensagemPersonagem(f"... Pois agora tem, porém não da forma que você desejava. Ou talvez sim, vai saber...")
                        Delay(1)
                        Espaco(1)
                        MensagemPersonagem(f"Mas vendo que seus trinta segundos de atenção foram preenchidos, eu não vejo porquê conversas civilizadas não seriam possíveis.")
                        MensagemPersonagem(f"Portanto, começaremos esta interação do zero, que tal? Vamos lá, do começo, me diga:")
                        Espaco(1)
                        MensagemPersonagem(f"Qual é o seu nome?...")
                        continue
                    case 6:
                        Delay(5)
                        Limpar()
                        Terminar()
                        break
            case _ if len(nomeUser) == 0:
                pacNomNada += 1
                match pacNomNada:
                    case 1:
                        MensagemPersonagem(f"... Aí fica difícil a nossa comunicação, sabe?")
                        MensagemPersonagem(f"Que informação você espera que eu obtenha... De uma caixa vazia?")
                        Delay(1)
                        MensagemPersonagem(f"Como eu supostamente devia te chamar? De 'Caixa Vazia'?")
                        Delay(1)
                        Limpar()
                        MensagemPersonagem(f"Vamos tentar, novamente. Erros acontecem, dentre todos os seres. Talvez você apenas tenha aprendido a digitar hoje, e precise de auxílios.")
                        MensagemPersonagem(f"Quando a caixinha aparecer... Digite o seu nome, ok? Simples assim. Sem problemas.")
                        Delay(1)
                        Limpar()
                        MensagemPersonagem(f"Pois vamos em frente, portanto.\nDigite, então, o seu nome:")
                        continue
                    case 2:
                        MensagemPersonagem(f".. ESCREVE.")
                        Delay(0.5)
                        Espaco(1)
                        MensagemPersonagem(f".. ALGO.")
                        Delay(0.5)
                        Espaco(1)
                        MensagemPersonagem(f".. NA CAIXA.")
                        Delay(0.5)
                        Espaco(1)
                        MensagemPersonagem(f"... ABAIXO.")
                        continue
                    case 3:
                        nomeUser = "CAIXA VAZIA".title()
                        MensagemPersonagem(f"... {nomeUser}, hum?")
                        Espaco(1)
                        MensagemPersonagem(f"Que nome suberbo esse, o seu. Você passa bem? Precisa de ajuda?")
                        Espaco(1)
                        MensagemPersonagem(f"Isso seria uma mensagem de socorro para um momento difícil da sua vida?")
                        MensagemPersonagem(f"Eu me pergunto. Certamente não é algo normal. É tipo algo que alguém que \n"
                        "Não sabe usar nenhuma tecla do teclado exceto o 'Enter' provavelmente faria, apenas para obter ajuda dos que não se importaram.")
                        Delay(1)
                        Espaco(1)
                        Limpar()
                        MensagemPersonagem(f"Mas, pois bem. Contanto que esteja bem, e apenas seja uma mera ironia vinda de você,\nPoderemos prosseguir em segurança.")
                        Delay(0.5)
                        Espaco(1)
                        MensagemPersonagem(f"Mas só saiba, apenas: \nPara mim, você não é vazio.")
                        MensagemPersonagem(f"Há muito ar dentro dessa caixa aí que você não percebeu. \nVocê só precisa tocá-lo.")
                        break
            case _:
                MensagemPersonagem(f"... {LerNome()}, hum?")
                Delay(2)
                Espaco(1)
                break

def LerNome(form=1):
    global nomeUser
    match form:
        case 1: # NOME INTEIRO
            return(nomeUser.title())
        case 2: # PRIMEIRO NOME
            nomeSep = nomeUser
            nomeSep.split()
            return(nomeSep[0].title())

def CriarCardapio():
    produtos = []
    qtdProd = 1
    nomeDaLoja = ''
    corCabecalho = '42'

    def MostrarMenu():
        titulo_menu = '『'+' MENU '+'』'
        print(mText[0], end='')
        print(f"\n{titulo_menu.center(36,'=')}")
        print(fCor)

    def MostrarCabecalho():
        cor_titulo = f'\033[1;{corCabecalho}m'
        titulo_cardapio = " (🌹) | <"+(nomeDaLoja)+"> | (🌹) "
        print(cor_titulo, end='')
        print(f"{titulo_cardapio.center(36,'•')}{fCor}")

    def MostrarProduto():
        for i,item in enumerate(produtos):
            print(f"{mText[0]}{item[0].ljust(26, '.')}{fCor}{mText[0]}{(ConverterPreco(item[1])).rjust(12, '.')}")
            print(f"'{mText[1]}{item[2]}'")

    def ConverterPreco(preco):
        if(preco > 0):
            return f"R$: {str(preco).replace('.',',')}"
        else:
            return "DE GRAÇA!"

    Limpar()
    MensagemPersonagem(f"Bem, {LerNome()} eu considerarei que você deseja criar um "
    "cardápio de opções para um negócio de taverna.")
    Espaco(1)
    MensagemPersonagem(f"... Ou bem, como nomeiam nos dias de hoje: Bar, Lanchonete...\n"
    "Restaurante... Você entendeu o ponto. É um cardápio, no fim do dia.")
    Delay(1)
    Espaco(1)
    MensagemPersonagem(f"Mas, enfim...\n"
    f"{LerNome()}, comecemos então com você me informando qual será o nome do seu estabelecimento.")
    nomeDaLoja = LerMsg("Escreva Aqui: ", 1).upper().strip()
    Limpar()
    BinaryFill(10)
    Limpar()
    MensagemPersonagem(f"Hmm... {nomeDaLoja.title()}?")
    Delay(0.5)
    Espaco(1)
    match nomeDaLoja:
        case _:
            if(len(nomeDaLoja) < 8):
                MensagemPersonagem(f"Ok... Bem... Minimalista...")
            else:
                op = ["Nada mal, diria eu.", "Dá para o gasto.",
                        f"Com certeza será fácil de pronunciar, {LerNome()}."]
                MensagemPersonagem(f"{op[random.randint(0, len(op)-1)]}")

            Delay(0.5)
            Limpar()
            MensagemPersonagem(f"Pois bem.")
            Espaco(1)
            MensagemPersonagem(f"O cabeçalho ao cardápio se seguirá na seguinte aparência descrita abaixo:")
            Espaco(2)
            MostrarCabecalho()
            Delay(3)
            MensagemPersonagem(f"Sim, verde é uma escolha bem especifica. Não é mesmo, {LerNome()}?")
            Delay(1)
            MensagemPersonagem(f"Porque eu ficaria bem assustado caso você não estranhasse.")
            Delay(1)
            Limpar()
            MensagemPersonagem(f"Se lhe bem agradar, no entanto, temos outras opções além desta já pré-definida.")
            Delay(0.1)

            muda = 0
            while True:
                MenuOpcoes(["Mudar para \033[41mVERMELHO\033[0m","Mudar para \033[44mAZUL\033[0m","Mudar para \033[42mVERDE\033[0m","Mudar para \033[40mCINZA\033[0m"])
                Delay(1)
                if(muda < 2):
                    MensagemPersonagem(f"O que você me diz, {LerNome()}? As opções estão aí acima.\nBasta escolher uma de seu agrado.")
                else:
                    MensagemPersonagem(f"Meh, meh, meh.")
                    MensagemPersonagem(f"Cor, cor, cor...")
                    MensagemPersonagem(f"Buá, buá, buáá...")

                opDeCor = OpcaoEscolhida(4)
                Limpar()
                match opDeCor:
                    case 1: # VERMELHO
                        corCabecalho = '41'
                        MensagemPersonagem(f"Vejam só:\nEu esperava pior, mas vejo que estamos juntos nessa!")
                        MensagemPersonagem(f"Paint The Town Red, pelo visto!")
                    case 2: # AZUL
                        corCabecalho = '44'
                        MensagemPersonagem(f"BABBA DEE BABBA DAAEEE-")
                        Limpar()
                        MensagemPersonagem(f"... Peço...")
                        Delay(0.5)
                        Limpar()
                        MensagemPersonagem(f"Peço perdão, {LerNome()}.")
                        Delay(1)
                        Espaco(1)
                        MensagemPersonagem(f"Me equivoquei em animação excessiva..")
                    case 3: # VERDE
                        corCabecalho = '42'
                        MensagemPersonagem(f"... Sério?")
                        Delay(1)
                        MensagemPersonagem(f"Só... SÉRIO?...")
                        Delay(1)
                        MensagemPersonagem(f"Ugh. {LerNome()}, eu LITERALMENTE te induzi na EXPECTATIVA-")
                        Limpar()
                        MensagemPersonagem(f"...")
                        Delay(0.5)
                        MensagemPersonagem(f"... Eu devia só ter dado um Task Kill Nesse programa, mesmo...")
                        MensagemPersonagem(f"Por que ainda invento?..")
                    case 4: # CINZA
                        corCabecalho = '40'
                        MensagemPersonagem(f"{LerNome()}...")
                        MensagemPersonagem(f"... Você precisa de um psicólogo.")
                        Delay(0.1)
                        Espaco(1)
                        MensagemPersonagem(f"E mensagens motivadoras de auto-estima.")

                Delay(1)
                Limpar()
                MensagemPersonagem(f"Pois bem, {LerNome()}, aqui está abaixo o resultado de suas alterações:")
                Espaco(2)
                MostrarCabecalho()
                Delay(2)
                MensagemPersonagem(f"Alcançamos algo de seu bom agrado, {LerNome()}?")
                MenuOpcoes(["Sim, manter alterações", "Não, escolher outra cor"])
                match OpcaoEscolhida(2):
                    case 1: # SIM
                        break
                    case 2:
                        muda += 1
                        Limpar()
                        if(muda < 3):
                            MensagemPersonagem(f"Pois bem... Recomeçemos novamente do zero, {LerNome()}:")
                            Delay(0.1)
                            Limpar()
                            continue
                        else:
                            MensagemPersonagem(f"UGH-{nomeUser}, CHEGA!".upper())
                            MensagemPersonagem("Vai ficar assim essa bosta!".upper())
                            MensagemPersonagem("Eu não tenho o dia todo nessa merda não!".upper())
                            Delay(0.5)
                            break

    Limpar()
    MensagemPersonagem(f"Continuemos então, portanto...")
    Espaco(1)
    MensagemPersonagem(f"Pois agora, {LerNome()}, adicionaremos items ao cardápio.")
    MensagemPersonagem("E para isso, precisaremos de algumas informações básicas.")
    Delay(1)
    Limpar()
    MensagemPersonagem("Começando, primeiramente:")
    Espaco(1)
    MensagemPersonagem(f"Qual será o nome do {qtdProd}º item do cardápio?")
    pacNomAla = 0

    while True:
        nomeProduto = LerMsg("Nome: ", 1).upper().strip()
        Limpar()
        BinaryFill(10)
        Limpar()
        match nomeProduto:
            case 'ALARICE' | 'VOCÊ' | 'VOCE' 'VC':
                pacNomAla += 1
                match pacNomAla:
                    case 1:
                        MensagemPersonagem(f"Sem essa, {LerNome()}.\nEu não estou à venda.")
                        Delay(0.5)
                        Espaco(1)
                        MensagemPersonagem("Nem em forma de alimento,\n"
                        "Ou qualquer sentido metafórico desagradável.")
                        Delay(0.5)
                        Limpar()
                        MensagemPersonagem("Use sua criatividade e crie um produto.")
                    case 2:
                        MensagemPersonagem(f"Ugh- Eu já disse:\nEu NÃO estou à venda, {LerNome()}.")
                        Delay(0.5)
                        Espaco(1)
                        MensagemPersonagem("Acha que eu tenho gosto de quê?"
                        "\nDe cachorro quente?")
                        Delay(0.5)
                        Limpar()
                        MensagemPersonagem("Vá logo ao ponto, de uma vez.")
                    case 3:
                        MensagemPersonagem(f"Você está me flertando, {LerNome()}?")
                        Delay(0.5)
                        MensagemPersonagem("É isso?!")
                        Delay(0.5)
                        Espaco(1)
                        MensagemPersonagem("Nem sequer sabe minha aparência,\n"
                        "E já me vêm com essas investidas?")
                        Delay(0.5)
                        Espaco(1)
                        MensagemPersonagem("E eu pensando que já vi de tudo, nesse mundo...")
                        Delay(0.5)
                        Limpar()
                        MensagemPersonagem(f"Ok, repetindo novamente: Eu NÃO ESTOU à VENDA, {LerNome()}.")
                        Delay(0.5)
                        MensagemPersonagem("Tão pouco me aplico a conceitos de virgindade,"
                        "\nE nem posso satisfazer sua vida íntima.")
                        Espaco(1)
                        Delay(0.5)
                        MensagemPersonagem("Voltemos ao principal questionamento, onde \n"
                        "Você me fornece o produto que você deseja acrescentar.")
                    case 4:
                        MensagemPersonagem(f"{nomeUser.upper()}, EU NÃO TENHO ORGÃOS GENITAIS!")
                        Delay(1)
                        Espaco(1)
                        MensagemPersonagem("E NEM ORGÃOS VITAIS!")
                        Delay(1)
                        Espaco(1)
                    case 5:
                        MensagemPersonagem("... Eu vou simplesmente ignorar as suas mensagens daqui em diante,"
                        "\nE aguardar até você me responder apropriadamente.")
                        Delay(0.5)
                        Limpar()
                    case _ if pacNomAla > 5:
                        Limpar()
                continue
            case 'ALARY':
                MensagemPersonagem(f"VOCÊ QUER ENVENENAR AS PESSOAS, {LerNome()}?!".upper())
                continue

        MensagemPersonagem(f"Ok... {nomeProduto.title()}...")
        Delay(1)
        Limpar()
        MensagemPersonagem(f"Certo, {LerNome()}, forneceremos então uma belíssima descrição ao item.")
        descProduto = LerMsg("Descrição Aqui: ", 1).upper()
        Limpar()
        BinaryFill(10)
        Limpar()
        MensagemPersonagem(f"{descProduto.capitalize()}?...")
        Delay(1)
        Espaco(1)
        match descProduto:
            case _ if len(descProduto) < 8:
                MensagemPersonagem(f"Uma descrição relativamente simplificada, {LerNome()}, se eu bem posso dizer.")
                Espaco(1)
                MensagemPersonagem("Mas, bem, suponho que ambos nós apreciamos a graça das coisas simplificadas.")
            case 'ALARICE':
                MensagemPersonagem(f"O item é tão bom que você vai nomear ele como 'Alarice'?")
                Espaco(1)
                MensagemPersonagem("Bem promissor, ein?")
                Delay(0.5)
                MensagemPersonagem("Pena que não tenho mais um corpo pra te visitar e ver se é bom mesmo.")
            case _:
                MensagemPersonagem("Mais que compreendido.")

        Delay(1)
        Limpar()
        MensagemPersonagem("E agora, como a última etapa...")
        Delay(0.5)
        MensagemPersonagem(f"Peço para que me informe qual será o preço para a compra deste item, {LerNome()}.")
        if(qtdProd <= 1):
            Delay(0.5)
            Espaco(1)
            MensagemPersonagem("Ou caso a falta de pespectiva lhe incomodar,\n"
            "Você pode deixar à mim para refletir sobre um preço justo.")
            Delay(0.5)
            Espaco(1)
            MensagemPersonagem(f"Tentarei levar em conta o mais apropriado possível para o item cujo você me informou, {LerNome()}.")
            Delay(0.5)
            Limpar()
            MensagemPersonagem("A escolha é ")
            Limpar()
            EvilWrite("MIIINHA-", 0.1)
            Limpar()
        else:
            Espaco(2)

        valorDoProduto = 0.00

        MenuOpcoes(["Decida Um Preço Por Mim", "Deixe-me Decidir um Preço Próprio"])
        match OpcaoEscolhida(2):
            case 1:
                valorAleatorio = 0
                valoresSorteados = []

                Limpar()
                BinaryFill(20)
                Limpar()

                for i in range(20):
                    valoresSorteados.append(random.randrange(2, 1100)+.99)
                    valorDoProduto = min(valoresSorteados[:(len(valoresSorteados))])

                dialogo1 = [f"Bem, {LerNome()}... Eu pensei bastante, considerando o produto que você deseja vender.",
                            "E de fato, eu não poderia escolher um peço mais justo...",
                            f"... Do que {ConverterPreco(valorDoProduto)}."]
                dialogo2 = [f"Pois bem... Eu me ocupei bastante em minha vasta capacidade de raciocínio, {LerNome()}...",
                            "E não poderia chegar a uma mais regulada cobrança...",
                            f"Que não fosse apenas por {ConverterPreco(valorDoProduto)}."]

                dialogos = [dialogo1, dialogo2]
                dialogoSelecionado = dialogos[random.randint(0, len(dialogos)-1)]
                MensagemPersonagem(dialogoSelecionado[0])
                MensagemPersonagem(dialogoSelecionado[1])
                Espaco(1)
                MensagemPersonagem(dialogoSelecionado[2])
            case 2:
                Limpar()
                MensagemPersonagem(f"Pois bem, isso facilita as coisas, {LerNome()}.")
                Espaco(1)
                MensagemPersonagem("Pois me diga, então, o seu preço.")
                valorDoProduto = LerMsg("R$: ",3)
                if(valorDoProduto <= 1):
                    MensagemPersonagem(f"{LerNome()}, a esse ponto, você já pode considerar esse item como de graça, não?")
                    Espaco(1)
                    MensagemPersonagem("Pois é isso o que vou fazer, portanto.\nNão se preocupe.")
                    valorDoProduto = 0

        Delay(1)
        Limpar()
        Espaco(1)
        produto = [nomeProduto.title(), valorDoProduto, descProduto.capitalize()]
        MensagemPersonagem(f"Ok, {LerNome()}, eu irei recitar exatamente as informações me fornecidas,\n"
        "Para termos certeza que ambos estamos na mesma página.")
        Delay(1)
        Espaco(1)
        MensagemPersonagem(f"O Nome do Produto será '{produto[0]}',\n"
                        f"E '{produto[2]}' é a sua descrição.")
        Delay(0.5)
        Espaco(1)
        MensagemPersonagem(f"O preço para a compra deste?\nSerá de {ConverterPreco(produto[1])}.")
        Delay(0.5)
        Espaco(1)
        MensagemPersonagem(f"Estamos de acordo, {LerNome()}?")
        Espaco(2)

        MenuOpcoes(["Sim, e desejo finalizar o cardápio", "Sim, mas desejo adicionar outros ítens"])

        match OpcaoEscolhida(2):
            case 1: # FINALIZAR CARDÁPIO
                Limpar()
                produtos.append(produto)
                qtdProd += 1
                Limpar()
                BinaryFill(20)
                Limpar()
                MensagemPersonagem("Pois bem...")
                Espaco(1)
                MensagemPersonagem(f"O resultado do cardápio cujo você criou para a loja {nomeDaLoja}...")
                Espaco(1)
                MensagemPersonagem(f"Ficou no seguinte formato abaixo:")
                Espaco(2)
                MostrarCabecalho()
                MostrarMenu()
                MostrarProduto()
                Delay(3)
                break
            case 2: # ADICIONAR NOVO ITEM
                Limpar()
                produtos.append(produto)
                qtdProd += 1
                MensagemPersonagem(f"Pois bem, seguiremos então com o {qtdProd}º item do cardápio, {LerNome()}.")
                MensagemPersonagem(f"Me informe portanto, novamente, o nome do item?")
                Espaco(1)
                continue

def CriarLista():
    Limpar()
    MensagemPersonagem(f"Bem, {LerNome()}, e qual tipo de lista você deseja "
    "que eu crie?")
    MenuOpcoes(["Criar um Cardápio."])
    match OpcaoEscolhida(1):
        case 1: # OPÇÃO: CARDÁPIO:
            CriarCardapio()

def FazerCalculo():
    Limpar()
    MensagemPersonagem(f"Bem, {LerNome()}...")
    MensagemPersonagem("... Qual tipo de cálculo você busca aqui?")
    MenuOpcoes(["Adição", "Subtração","Multiplicação", "Divisão"])
    op = OpcaoEscolhida(4)
    Limpar()

    numeros = []
    minimoDeNum = 2
    com = ["Compreendido, e pego.", "Certinho, como esperado.",f"Topperson, {LerNome()}."]

    def NumerosTotais():
        return int(len(numeros))

    def FormatarNumero(n):
        f = (f"{int(n)}" if n.is_integer() else f"{float(n)}")
        return f

    MensagemPersonagem("Pois bem...")
    MensagemPersonagem(f"Me informe, portanto, o {NumerosTotais()+1}º número:")
    while True:
        num = LerMsg("", 4)
        numeros.append(num)
        Limpar()
        BinaryFill(15)
        Limpar()

        if(num != 0):
            MensagemPersonagem(random.choice(com))
        else:
            Delay(0.5)
            MensagemPersonagem("Hum...")
            Delay(1)

        Delay(1)
        Limpar()
        if(NumerosTotais() < minimoDeNum):
            MensagemPersonagem(f"Me informe agora o {NumerosTotais()+1}º número:")
            continue
        else:
            if(NumerosTotais() <= minimoDeNum):
                MensagemPersonagem(f"Me diga, {LerNome()}: Deseja acrescentar mais números ao cálculo,")
                MensagemPersonagem(f"Ou deseja que eu já lhe mostre aqui o resultado?")
            else:
                MensagemPersonagem(f"{LerNome()}, deseja que eu lhe mostre o resultado,\nOu acrescente mais números?")

            MenuOpcoes(["Desejo Acrescentar Números.", "Desejo Ver os Resultados.", "Desejo Recomeçar a  Conta."])
            match OpcaoEscolhida(3):
                case 1: # ACRESCENTAR
                    Limpar()
                    MensagemPersonagem(f"Pois bem, prosseguindo de volta ao {NumerosTotais()+1}º número...")
                    Delay(0.5)
                    Limpar()
                    MensagemPersonagem(f"Me informe o número desejado, {LerNome()}:")
                    continue
                case 2: # CALCULAR
                    Limpar()
                    BinaryFill(30)
                    Limpar()

                    def Calcular(nums, tipo=1):
                        calculo = nums[0]
                        formula = f"{nums[0]}"
                        for pos, num in enumerate(nums):
                            match tipo:
                                case 1: # ADIÇÃO
                                    calculo += num
                                    formula += (f" + {num}" if pos != 0 else '')
                                case 2: # SUBTRAÇÃO
                                    calculo -= num
                                    formula += (f" - {num}" if pos != 0 else '')
                                case 3: # Multiplicacao
                                    if(pos+1 <= len(nums)-1):
                                        multiplicador = nums[pos+1]
                                        calculo *= multiplicador
                                        formula += (f" x {multiplicador}")
                                case 4: # DIVISÂO
                                    try:
                                        if(pos+1 <= len(nums)-1):
                                            divisor = nums[pos+1]
                                            calculo /= divisor
                                            formula += (f" % {divisor}")
                                    except(ZeroDivisionError):
                                        return ['ZERO', None]

                        return [calculo, formula]

                    resultado = Calcular(numeros, op)

                    match op:
                        case 1: # ADIÇÃO
                            MensagemPersonagem(f"Pois então, {LerNome()}...")
                            MensagemPersonagem(f"Lhe demonstro aqui abaixo o resultado da soma dos números:")
                            Delay(0.5)
                            Limpar()
                            MensagemPersonagem(f"{resultado[1]} = {FormatarNumero(resultado[0])}")
                            break
                        case 2: # SUBTRAÇÃO
                            MensagemPersonagem(f"Pois então, {LerNome()}, aqui está o resultado da subtração dos números:")
                            Delay(0.5)
                            Espaco(1)
                            MensagemPersonagem(f"{resultado[1]} = {FormatarNumero(resultado[0])}")
                            break
                        case 3: # MULTIPLICAÇÃO
                            MensagemPersonagem(f"Pois então, {LerNome()}, aqui está o resultado da multiplicação dos números:")
                            Delay(0.5)
                            Espaco(1)
                            MensagemPersonagem(f"{resultado[1]} = {FormatarNumero(resultado[0])}")
                            break
                        case 4: # DIVISÃO
                            if(resultado[0] != 'ZERO'):
                                MensagemPersonagem(f"Pois então, {LerNome()}, aqui está o resultado da divisão dos números:")
                                Delay(0.5)
                                Espaco(1)
                                MensagemPersonagem(f"{resultado[1]} = {FormatarNumero(resultado[0])}")
                                Delay(2)
                                break
                            else:
                                MensagemPersonagem("Pois então... Aqui está o resultado da divisão dos números:")
                                Delay(1.5)
                                Espaco(2)
                                EvilWrite(f"Você é fraco demais para isso, {LerNome()}...", 0.05)
                                Espaco(2)
                                BinaryFill(100)
                                Espaco(2)
                                BinaryWriteAndFill(f"{nomeUser.upper()}")
                                Terminar()
                                break
                case 3: # RESETAR NÚMEROS
                    numeros.clear()
                    MensagemPersonagem(f"Pois bem, {LerNome()}...")
                    MensagemPersonagem(f"Recomeçaremos de volta, a partir do {NumerosTotais()+1}º número.")
                    Delay(1)
                    continue



def LorePrincipal():
    BinaryFill(50)
    Limpar()
    print(f"""
        ==========================
    『 🐺 {mText[0]}'A TAVERNA DO ALARICE'{fCor} 🌕 』
        ==========================
    """, end='')
    Delay(2)

    easterEgg = random.randint(0,100)
    saudacoes = ["Bom Dia", "Boa Tarde", "Boa Noite", "Boa Madrugada"]
    saudacao = ''

    hora = int(hora_formatada)
    comHoMadr = False

    match hora:
        case _ if hora < 6:
            comHoMadr = True
            saudacao = saudacoes[3]
        case _ if hora <= 12:
            saudacao = saudacoes[0]
        case _ if hora <= 18:
            saudacao = saudacoes[1]
        case _ if hora <= 23:
            saudacao = saudacoes[2]

    MensagemPersonagem(f"{saudacao}...")
    Delay(0.5)
    redutivos = ["Ser vivo", "Criatura", "Mamífero",]
    MensagemPersonagem(f"{random.choice(redutivos)}...")
    Delay(0.5)

    Espaco(1)
    if(comHoMadr == True):
        MensagemPersonagem("Meio tarde para ainda estar acordado, não?...")
        Delay(0.5)
        Espaco(1)

    if(psutil.sensors_battery()):
        MensagemPersonagem('Pessoalmente, eu me sinto um tanto mais "finito" do que o de costume, mas...')
        MensagemPersonagem('Não precisamos trazer esse detalhe à tona, no entanto.')
        Delay(0.5)
        Espaco(1)

    perguntasNome = ["Qual o seu nome?", "Como você se chama?",
                     "Quem é  você?"]
    MensagemPersonagem(f"... {random.choice(perguntasNome)}")

    RegistrarNome()
    Delay(0.5)
    Limpar()
    MensagemPersonagem(f"Pois bem, então... Me diga, {LerNome()}:")
    MensagemPersonagem(f"O que você deseja aqui?...")

    tarefaRealizada = False
    while True:
        Espaco(1)
        MenuOpcoes(["Criar uma Lista.", "Realizar Cálculos.", "Sair do Programa."])

        match OpcaoEscolhida(3):
            case 1: # OPÇÃO: CRIAR UMA LISTA
                CriarLista()
            case 2: # OPÇÃO: CÁLCULOS
                FazerCalculo()
            case 3: # OPÇÃO: SAIR DO PROGRAMA
                if(tarefaRealizada == False):
                    Limpar()
                    MensagemPersonagem("Bem...")
                    Delay(0.5)
                    MensagemPersonagem("... Isso foi meio inútil...")
                    Delay(0.5)
                    Espaco(1)
                    MensagemPersonagem("... Muito, muito inútil...")
                    Terminar()
                    break
                else:
                    Limpar()
                    MensagemPersonagem(f"Pois bem.")
                    MensagemPersonagem(f"Estarei a sua futura disposição quando precisar, {LerNome()}.")
                    Espaco(1)
                    MensagemPersonagem(f"Afinal, tivemos um agradável tempo juntos.")
                    Limpar()
                    Delay(2)
                    Espaco(2)
                    BinaryFill(20)
                    MensagemPersonagem(f"... Isso foi um sarcasmo barato, {LerNome()}.")
                    Delay(1)
                    Terminar()
                    break

        tarefaRealizada = True
        Espaco(1)
        MensagemPersonagem(f"Vejo que conquistamos resultado exurberante, {LerNome()}.")
        Delay(1)
        MensagemPersonagem(f"E dado a isso, seguindo meus protocólos pré-implantados, lhe pergunto:")
        Delay(0.5)
        Espaco(1)
        MensagemPersonagem(f"Há alguma outra coisa cujo o meu auxílio seria necessário?...")
        continue

LorePrincipal()