import random

def Jogar():

    MensagemInicio()
    palavra_secreta = PegarPalavra()
    lista_palavra_secreta = RetornaLista(palavra_secreta)
    
    #print('Palavra Secreta',palavra_secreta)
    
    InicializaChute(lista_palavra_secreta,palavra_secreta)


    
#------------------------------------------------------
# Exibe mensagem de inicio
#------------------------------------------------------
def MensagemInicio():
    print('*************************')
    print('*     JOGO INICIADO     *')
    print('*************************\n')

#------------------------------------------------------
# Tratamento que ocorre várias vezes no script
#------------------------------------------------------
def Tratamento(x):
    x = x.upper().strip().replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U').replace('Ã','A').replace('Õ','O').replace('Ç','C')
    return x

#------------------------------------------------------
# Pegar Palavra Secreta Aleatoriamente
#------------------------------------------------------
def PegarPalavra():
    #pegar lista de palavras do arquivo palavras.txt
    palavras = []
    arquivo = open('palavras.txt','r',encoding='utf8')
    for n in arquivo:
        palavras.append(TratarPalavras(n))
    arquivo.close()
    
    #selecionar palavra aleatoriamente
    indice = random.randrange(0,len(palavras))
    palavra_selecionada = palavras[indice]
    return palavra_selecionada

def TratarPalavras(palavra):
    palavra_secreta = Tratamento(palavra)
    return palavra_secreta

#------------------------------------------------------
# Cria Lista com Palavra Secreta
#------------------------------------------------------
def RetornaLista(x):
    lista = []
    for l in x:
        lista.append(l)
    return lista

def RetornaNome(lista):
    result = ''.join(lista)
    print(result)

#====================================================================================================
#------------------------------------------------------
# Realiza processo de Chute
#------------------------------------------------------
def InicializaChute(lista_palavra_secreta,palavra_secreta):
    lista_chutes = []
    lista_acerto = ['_']  * len(lista_palavra_secreta)
    acertos_atualizado = []

    tentativas = 7
    while tentativas > 0:
        chute = RealizaChute()
        lista_chutes.append(chute)
        print('Chutes: ',lista_chutes)
        if Acertou(chute,lista_palavra_secreta) == True:
            pass
        else:
            tentativas -= 1
            pass
        print(f'Restam {tentativas} tentativas')
        acertos = VerificaAcerto(chute,lista_palavra_secreta)

        acertos_atualizado = AtualizaListaAcertos(acertos,lista_acerto)
        print(acertos_atualizado)
        if acertos_atualizado == lista_palavra_secreta:
            print('Você Venceu o jogo!')
            print(f'A palavra é {palavra_secreta}')
            break

    if acertos_atualizado != lista_palavra_secreta:
        print('Você Perdeu o jogo!')
        print(f'A palavra secreta era {palavra_secreta}')
        

#------------------------------------------------------
# Recebe a letra do chute e verifica se é válido
#------------------------------------------------------
def RealizaChute():
    chute = input('\nDigite a letra: ')
    if len(chute) == 1:
        return Tratamento(chute)
    else:
        print('\nApenas uma letra.\nTente novamente.')
        RealizaChute()

#------------------------------------------------------
# Verifica se a letra chutada está correta
#------------------------------------------------------
def Acertou(chute,lista_palavra_secreta):
    for i in lista_palavra_secreta:
        if chute == i:
            return True
        else:
            return False
    

def VerificaAcerto(chute,lista_palavra_secreta):
    tamanho = len(lista_palavra_secreta)
    dict_acertos = {}
    for n in range(0,tamanho):
        if chute == lista_palavra_secreta[n]:
            dict_acertos[n]=chute
    return dict_acertos # retorna a posição e letra do acerto em uma dict

def AtualizaListaAcertos(dict_acertos,lista_acerto):
    for chave, valor in dict_acertos.items():
        lista_acerto.pop(chave)
        lista_acerto.insert(chave,valor)
    return lista_acerto
    



Jogar()


