import random

def jogar():    
    print_start()
    palavra_secreta = import_word()
    
    palavra_digitada = ["_" for letra in palavra_secreta]
            
    enforcou = False
    acertou = False
    respostas_erradas = 0       
   
    print('A palavra tem : ' + str(len(palavra_secreta)) + ' letras')
    print(palavra_digitada)
      
    while(not enforcou and not acertou):
        chute = get_chute()        
        if(chute in palavra_secreta):
            palavra_digitada = marca_chute(palavra_secreta, palavra_digitada, chute)
        else:
            respostas_erradas +=1
            desenha_forca(respostas_erradas)
        
        enforcou = respostas_erradas == 7
                
        if(not '_' in palavra_digitada):                        
            print_vencedor()
            novo_jogo = input('Você quer jogar de novo ? [S ou N]?')
            if novo_jogo.upper() == "S":
                palavra_secreta = "banana"
                palavra_digitada = "------"                            
                enforcou = False
                acertou = False
                respostas_erradas = 0                               
            else:
                acertou = True
                
        print(palavra_digitada)        
                    
    if (enforcou):            
        print_perdedor(palavra_secreta)

def print_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def print_perdedor(palavra_secreta):    
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
def print_start():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print('Você tem que advinhar a palavra da forca:')            

def import_word():    
    with open('palavras.txt') as arquivo:
        palavras = [p.strip() for p in arquivo]    
     
    r = random.randrange(0, len(palavras))
    return palavras[r].upper()    

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def get_chute():
    chute = input('Digite uma letra para advinhar a forca: ')                
    return chute.strip().upper()
        

def marca_chute(palavra_secreta, palavra_digitada,chute):
    index = 0            
    for letra in palavra_secreta:            
        if (chute.upper() == letra.upper()):                    
            palavra_digitada[index] = chute                                    
        index += 1
    return palavra_digitada


if(__name__ == "__main__"):
    jogar()    