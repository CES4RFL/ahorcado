#Solicita el ingreso de una cadena
palabra=input("Ingresa la palabra para adivinar\t")
#La variable es declarada para almacenar el resultado construido por las letras 
#que van siendo ingresadas
tupalabra=''
#Configuracion de vidas
vidas=5

#Se mantiene el ciclo mientras las vidas sean mayor a 0
while vidas >0:

    #variable que contiene el numero de elementos que aun no han sido adivinados
    faltantes=0
    
    #itera sobre cada una de las letras de la palabra que debe adivinar
    for letra in palabra:
        #Si la letra esta en la cadena de letras que ha ingresado el usuario
        #el programa pinta la letra
        #De lo contrario pinta un asterisco y pinta un simbolo *
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            faltantes+=1

    #Si la variable de los faltantes es 0 manda un mensaje de felicitacion y finaliza el ciclo while
    if faltantes==0:
        print("\nFelicidades, ganaste")
        break

    #Solicita el ingreso de una letra
    tuletra=input("\nintroduce solo una letra: ")

    #Si la longitud de la entrada es 1 continua con la evaluacion de la palabra
    #De lo contrario manda un error ya que ha ingresado mas de un caracter 
    #Mostrando un mensaje y restando una de las vidas a la variable que mantiene el ciclo
    if(len(tuletra)==1):

        #La letra es agregada a la cadena de las letras ingresadas
        tupalabra+=tuletra

        #Si la no se encuentra en la palabra original entonces se manda un mensaje 
        #y se resta una vida al contador
        if tuletra not in palabra:  
            vidas-=1
            print("Equivocacion")
            print("Tu tienes",+vidas," vidas")
    else:
        #Resta una vida e informa que solo debe ser un caracter a la vez
        vidas-=1
        print("Solo una letra por favor")
        print("Equivocacion")
        print("Tu tienes",+vidas," vidas")
    
    #Si las vidas llegan a 0 muestra un mensaje
    if vidas == 0:
        print("Perdiste!!")
                