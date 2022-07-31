import re


DIGITO = [str(x) for x in range(10)]
DIGITO_REGEX = "[0-9]*(.[0-9])?(E[+-]?[0-9])?"
ID_REGEX = "[A-Za-z]([A-Za-z]|[0-9])*"
LETRA = [chr(x) for x in range(97,123)] + [chr(x) for x in range(65,91)]
OP_ARIT = ['+','-','*','/']
OP_REL = ['>','<','=','~=','<=','>=']
TABS = ['\t','\n',' ']
tabelaSimb = []
posLinha  = 1 # Numero da linha
totalColunas = 0



def gerarToken(arquivo):

    global posLinha
    global totalColunas

    posColuna = 0 # Numero coluna que começa o lexema
    lexema = ''
    estado = 0
    lookhead = 0

    while(1):
        proxElemento = arquivo.read(1)

        # ESTADO INICIAL
        if estado == 0:
            posColuna = arquivo.tell()

            if proxElemento == 'T':
                estado = 6
            elif proxElemento == 'B':
                estado = 93
            elif proxElemento == 'P':
                estado = 83
            elif proxElemento == 'E':
                estado = 12100
            elif proxElemento == 'W':
                estado = 18
            elif proxElemento == 'D':
                estado = 25
            elif proxElemento == 'R':
                estado = 29
            elif proxElemento == 'C':
                estado = 37
            elif proxElemento == 'I':
                estado = 243
            elif proxElemento == 'F':
                estado = 48
            elif proxElemento in LETRA:
                estado = 55
            elif proxElemento in DIGITO:
                estado = 58
            elif proxElemento == '<':
                estado = 68
            elif proxElemento == '>':
                estado = 69
            elif proxElemento in TABS:
                estado = 106
            elif proxElemento == ':':
                estado = 120
            elif proxElemento == '[':
                estado = 123
            elif proxElemento == ';' or proxElemento == '=' or proxElemento == '(' or proxElemento == ')' or proxElemento == ',' or proxElemento in OP_ARIT: 
                estado = 108

        elif estado == 9 or estado == 15 or estado == 102 or estado == 22 or estado == 26 or estado == 34 or estado == 40 or estado == 45 or estado == 3 or estado == 52 or estado == 90 or estado == 97:

            if proxElemento in LETRA or proxElemento in DIGITO:
                estado = 55
            #lookhead
            else:  
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
                estado = 108
                
        elif estado == 55:
            
            # ID
            if proxElemento in LETRA or proxElemento in DIGITO:
                estado = 55
            #lookhead
            else:

                if not lexema in tabelaSimb:
                    tabelaSimb.append(lexema)
            
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
                estado = 108

        # BEGIN
        elif estado == 93:
            if proxElemento == 'E':
                estado = 94
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 94:
            if proxElemento == 'G':
                estado = 95
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 95:
            if proxElemento == 'I':
                estado = 96
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 96:
            if proxElemento == 'N':
                estado = 97
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1

        # PROGRAMA
        elif estado == 83:
            if proxElemento == 'R':
                estado = 84
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 84:
            if proxElemento == 'O':
                estado = 85
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 85:
            if proxElemento == 'G':
                estado = 86
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 86:
            if proxElemento == 'R':
                estado = 87
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 87:
            if proxElemento == 'A':
                estado = 88
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 88:
            if proxElemento == 'M':
                estado = 89
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 89:
            if proxElemento == 'A':
                estado = 90
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1

        # THEN
        elif estado == 6:
            if proxElemento == 'H':
                estado = 7
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 7:
            if proxElemento == 'E':
                estado = 8
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 8:
            if proxElemento == 'N':
                estado = 9
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1

        # ELSE OU END
        elif estado == 12100:
            if proxElemento == 'L':
                estado = 13
            elif proxElemento == 'N':
                estado = 101
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 13:
            if proxElemento == 'S':
                estado = 14
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 14:
            if proxElemento == 'E':
                estado = 15
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 101:
            if proxElemento == 'D':
                estado = 102
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1

        # WHILE
        elif estado == 18:
            if proxElemento == 'H':
                estado = 19
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 19:
            if proxElemento == 'I':
                estado = 20
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 20:
            if proxElemento == 'L':
                estado = 21
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 21:
            if proxElemento == 'E':
                estado = 22
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1

        # DO
        elif estado == 25:
            if proxElemento == 'O':
                estado = 26
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1

        # REPEAT
        elif estado == 29:
            if proxElemento == 'E':
                estado = 30
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 30:
            if proxElemento == 'P':
                estado = 31
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 31:
            if proxElemento == 'E':
                estado = 32
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 32:
            if proxElemento == 'A':
                estado = 33
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 33:
            if proxElemento == 'T':
                estado = 34
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1

        # CHAR
        elif estado == 37:
            if proxElemento == 'H':
                estado = 38
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 38:
            if proxElemento == 'A':
                estado = 39
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 39:
            if proxElemento == 'R':
                estado = 40
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1

        # INT OU IF
        elif estado == 243:
            if proxElemento == 'N':
                estado = 44
            elif proxElemento == 'F':
                estado = 3
            else: 
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 44:
            if proxElemento == 'T':
                estado = 45
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1

        # FLOAT
        elif estado == 48:
            if proxElemento == 'L':
                estado = 49
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 49:
            if proxElemento == 'O':
                estado = 50
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 50:
            if proxElemento == 'A':
                estado = 51
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1
        elif estado == 51:
            if proxElemento == 'T':
                estado = 52
            else:
                estado = 55
                arquivo.seek(arquivo.tell()-1)
                lookhead = 1

        # NUMERO
        elif estado == 58:
            if proxElemento in DIGITO:
                estado = 58
            elif proxElemento == '.':
                estado = 59
            elif proxElemento == 'E':
                estado = 61
            #lookhead
            else:
                lookhead = 1
                arquivo.seek(arquivo.tell()-1)
                estado = 108
        elif estado == 59:
            if proxElemento in DIGITO:
                estado = 60
        elif estado == 60:
            if proxElemento in DIGITO:
                estado = 60
            elif proxElemento == 'E':
                estado = 61
            #lookhead
            else:
                lookhead = 1
                arquivo.seek(arquivo.tell()-1)
                estado = 108
        elif estado == 61:
            if proxElemento == '+' or proxElemento == '-':
                estado = 62
            elif proxElemento in DIGITO:
                estado = 63
        elif estado == 62:
            if proxElemento in DIGITO:
                estado = 63
        elif estado == 63:
            if proxElemento in DIGITO:
                estado = 63
            #lookhead
            else:
                lookhead = 1
                arquivo.seek(arquivo.tell()-1)
                estado = 108

        # OP_RELAC
        elif estado == 68:
            if proxElemento == '=' or proxElemento == '>':
                estado = 108
            #lookhead
            else:
                lookhead = 1
                arquivo.seek(arquivo.tell()-1)
                estado = 108
        elif estado == 69:
            if proxElemento == '=':
                estado = 108
            #lookhead
            else:
                lookhead = 1
                arquivo.seek(arquivo.tell()-1)
                estado = 108

        # TABS
        elif estado == 106:
            if proxElemento in TABS:
                estado = 106
            #lookhead
            else:
                lookhead = 1
                arquivo.seek(arquivo.tell()-1)
                estado = 0
                lexema = ''
        # :=
        elif estado == 120:
            if proxElemento == '=':
                estado = 108
            #lookhead
            else:
                lookhead = 1
                arquivo.seek(arquivo.tell()-1)
                estado = 108

        elif estado == 123:
            if proxElemento == ']':
                estado = 0
            else:
                estado = 123

        # Evitar que o token venha com o lookhead
        if lookhead == 1:
            lookhead = 0
        else:
            lexema += proxElemento

        # Retornando token
        if estado == 108:
            if lexema in tabelaSimb:
                token = [lexema, tabelaSimb.index(lexema)]
            else:
                token = [lexema, '-']

            print([token,str(posLinha),str(posColuna-totalColunas)])
            return [token,str(posLinha),str(posColuna-totalColunas)]

        if proxElemento == '':
            print([['$','0'],'0','0'])
            return [['$','0'],'0','0']

        if proxElemento == "\n":
            posLinha += 1
            totalColunas = arquivo.tell()

    return 'ERRO'


def procedimento_fator():
    
    global proxToken
    global arq

    if proxToken[0][1] != '-' or bool(re.match(DIGITO_REGEX, proxToken[0][0])):
        proxToken = gerarToken(arq)

    elif proxToken[0][0] == '(':
        proxToken = gerarToken(arq)
        procedimento_operacaoarit1()
        if proxToken[0][0] == ')':
            proxToken = gerarToken(arq)
        else:
            print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <)>")
    else:
        print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <ID> ou <NUMERO> ou <(>")

    

def procedimento_term2():
    
    global proxToken
    global arq

    while proxToken[0][0] == "*" or proxToken[0][0] == "/":
        proxToken = gerarToken(arq)
        procedimento_fator()


def procedimento_term1():

    procedimento_fator()
    procedimento_term2()


def procedimento_operacaoarit2():
    
    global proxToken
    global arq

    while proxToken[0][0] == "+" or proxToken[0][0] == "-":
        proxToken = gerarToken(arq)
        procedimento_term1()


def procedimento_operacaoarit1():
    
    procedimento_term1()
    procedimento_operacaoarit2()


def procedimento_operacaorel():
    
    global proxToken
    global arq

    procedimento_fator()

    if proxToken[0][0] in OP_REL:
        proxToken = gerarToken(arq);
        procedimento_fator()
    else:
        print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <OP_REL>")


def procedimento_ifelse2():
    
    global proxToken
    global arq

    if proxToken[0][0] == "ELSE":
        proxToken = gerarToken(arq)
        procedimento_bloco()


def procedimento_ifelse1():
    
    global proxToken
    global arq

    if proxToken[0][0] == "IF":
        proxToken = gerarToken(arq)
        if proxToken[0][0] == "(":
            proxToken = gerarToken(arq)
            procedimento_operacaorel()
            if proxToken[0][0] == ")":
                proxToken = gerarToken(arq)
                if proxToken[0][0] == "THEN":
                    proxToken = gerarToken(arq)
                    procedimento_bloco()
                    procedimento_ifelse2()
                    procedimento_cmd()
                else:
                    print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <THEN>")
            else:
                print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <)>")
        else:
            print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <(>")
    else:
        print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <IF>")



def procedimento_dowhile():
    
    global proxToken
    global arq

    if proxToken[0][0] == "WHILE":
        proxToken = gerarToken(arq)
        if proxToken[0][0] == "(":
            proxToken = gerarToken(arq)
            procedimento_operacaorel()
            if proxToken[0][0] == ")":
                proxToken = gerarToken(arq)
                if proxToken[0][0] == "DO":
                    proxToken = gerarToken(arq)
                    procedimento_bloco()
                    procedimento_cmd()
                else:
                    print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <DO>")
            else:
                print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <)>")
        else:
            print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <(>")
    else:
        print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <WHILE>")


def procedimento_whiledo():
    
    global proxToken
    global arq

    if proxToken[0][0] == "REPEAT":
        proxToken = gerarToken(arq)
        procedimento_bloco()
        if proxToken[0][0] == "WHILE":
            proxToken = gerarToken(arq)
            if proxToken[0][0] == "(":
                proxToken = gerarToken(arq)
                procedimento_operacaorel()
                if proxToken[0][0] == ")":
                    proxToken = gerarToken(arq)
                    procedimento_cmd()
                else:
                    print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <)>")
            else:
                print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <(>")
        else:
            print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <WHILE>")
    else:
        print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <REPEAT>")


def procedimento_loop():

    global proxToken
    
    if proxToken[0][0] == "REPEAT":
        procedimento_whiledo()
    elif proxToken[0][0] == "WHILE":
        procedimento_dowhile()



def procedimento_tipo():
    
    global proxToken
    global arq

    if proxToken[0][0] == "INT":
        proxToken = gerarToken(arq)
    elif proxToken[0][0] == "FLOAT":
        proxToken = gerarToken(arq)
    elif proxToken[0][0] == "CHAR":
        proxToken = gerarToken(arq)
    else:
        print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <INT> ou <FLOAT> ou <CHAR>")


def procedimento_listaids():
    
    global proxToken
    global arq

    while(1):

        if proxToken[0][1] != '-':
            proxToken = gerarToken(arq)
        else:
            print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <ID>")
            break

        if proxToken[0][0] == ",":
            proxToken = gerarToken(arq)
        else:
            break


def procedimento_variavel():
    
    global proxToken
    global arq

    procedimento_tipo()

    if proxToken[0][0] == ":":
        proxToken = gerarToken(arq)
        procedimento_listaids()

        if proxToken[0][0] == ";":
            proxToken = gerarToken(arq)
            procedimento_cmd()
        else:
            print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <;>")
    else:
        print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <:>")


def procedimento_atribuicao():
    
    global proxToken
    global arq

    if proxToken[0][1] != '-':
        proxToken = gerarToken(arq)
        if proxToken[0][0] == ":=":
            proxToken = gerarToken(arq)
            procedimento_operacaoarit1()
            if proxToken[0][0] == ";":
                proxToken = gerarToken(arq)
                procedimento_cmd()
            else:
                print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <;>")
        else:
            print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <:=>")
    else:
        print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <ID>")


def procedimento_cmd():
    
    global proxToken
    global arq

    if proxToken[0][0] in ["INT", "FLOAT", "CHAR"]:
        procedimento_variavel()
    elif proxToken[0][0] in ["WHILE", "REPEAT"]:
        procedimento_loop()
    elif proxToken[0][0] == "IF":
        procedimento_ifelse1()
    elif proxToken[0][1] != '-':
        procedimento_atribuicao()


def procedimento_bloco():
    
    global proxToken
    global arq

    if proxToken[0][0] == "BEGIN":
        proxToken = gerarToken(arq)
        procedimento_cmd()

        if proxToken[0][0] == "END":
            proxToken = gerarToken(arq)
        else:
            print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <END>")
    else:
        print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <BEGIN>")


def procedimento_prog():
    
    global proxToken
    global arq
    
    if proxToken[0][0] == "PROGRAMA":
        proxToken = gerarToken(arq)
        if proxToken[0][1] != '-':
            proxToken = gerarToken(arq)
            procedimento_bloco()
        else:
            print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <ID>")
    else:
        print("Erro LINHA " +proxToken[1]+ " COLUNA " +proxToken[2]+" Era esperado <PROGRAMA>")


'''
arq = open("teste.txt", "r")

x = gerarToken(arq)


while(x[0][0] != "$"):

    x = gerarToken(arq)

arq.close()
'''
arq = open("CodigoFonte.txt", 'r')
proxToken = gerarToken(arq)
procedimento_prog()

if proxToken[0][0] == "$":
    print("Cadeia aceita")
else:
    print("Cadeia rejeitada")

arq.close()
