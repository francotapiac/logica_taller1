from pyswip import Prolog
from pyswip import Functor

prolog = Prolog()
prolog.consult("bd.pl")

prolog.assertz("contar_sintomas(E,Contador):- findall(X, relacion(enfermedad(E),sintoma(X)),L), length(L,Contador)")

prolog.assertz("obtener_porcentaje([],E,Contador,P):- contar_sintomas(E,ContadorTotalSintomas), P is div(Contador*100,ContadorTotalSintomas)")
prolog.assertz("obtener_porcentaje([X|Xs],E,Contador,P):- relacion(enfermedad(E), sintoma(X)),ContadorSiguiente is Contador + 1, obtener_porcentaje(Xs,E,ContadorSiguiente,P)")
prolog.assertz("obtener_porcentaje([X|Xs],E,Contador,P):- not(relacion(enfermedad(E), sintoma(X))), obtener_porcentaje(Xs,E,Contador,P)")

prolog.assertz("posee_significativa([],Contador,E):- Contador == 1")
prolog.assertz("posee_significativa([X|Xs],Contador,E):- not(significativa(enfermedad(E), sintoma(X))), posee_significativa(Xs,Contador,E)")
prolog.assertz("posee_significativa([X|Xs],Contador,E):- significativa(enfermedad(E), sintoma(X)), Posee is Contador + 1, posee_significativa(Xs,Posee,E)")

prolog.assertz("cumple_condicion_a([X|Xs],E):- relacion(enfermedad(E), sintoma(X)), obtener_porcentaje([X|Xs],E,0,Porcentaje), Porcentaje == 100")
prolog.assertz("cumple_condicion_b([X|Xs],E):- relacion(enfermedad(E), sintoma(X)), obtener_porcentaje([X|Xs],E,0,Porcentaje), Porcentaje >= 70, posee_significativa([X|Xs],0,E)")

prolog.assertz("que_enfermedad([], [], E)")
prolog.assertz("que_enfermedad([], [N|Ns], E):- not(relacion(enfermedad(E), sintoma(N))), que_enfermedad([],Ns,E)")
prolog.assertz("que_enfermedad([X|Xs],N,E):-    relacion(enfermedad(E), sintoma(X)), que_enfermedad(Xs,N,E)")

#prolog.assertz("cumple_condicion_a([X|Xs], E):- relacion(enfermedad(E),sintoma(X), )")

#Lista de preguntas

preguntas = ["Siente una dificultad para respirar similar a una falta de aire?",
             "Ha sentido algun tipo de dolor en el pecho?",
             "Ha sufrido de insomnio ultimamente?",
             "Tose frecuentemente?",
             "Ha padecido de una sensación de desorientación?",
             "Escucha unleve silbido al respirar?",
             "Se siente o ha sentido fatigado ultimamente?",
             "Su temperatura es superior a los 37,2 grados celcius?",
             "Ha sufrido de escalofríos ultimamente?",
             "Ha experimentado una sensacion de vomito?",
             "Ha sufrido de diarrea?",
             "Se ha producido esputo en su garganta durante los primeros dias?",
             "Siente un dolor constante en la garganta?",
             "Su nariz gotea constantemente?",
             "Ha sentido un malestar general recientemente?",
             "Tiene congestion nasal?",
             "Estornuda frecuentemente?",
             "Se han inflamado sus amigdalas?",
             "Puede ver marcas blancas en su piel?",
             "Siente dolor al tragar?",
             "Ha tenido problemas de mal aliento ultimamente?",
             "Siente un dolor de cabeza?",
             "Siente sus glandulas salivales inflamadas?",
             "Ha notado una perdida de apetito?",
             "Siente un dolor en sus encias?",
             "Siente un dolor en el area interior de sus labios o mejillas?",
             "Siente una sensacion de goteo en su garganta?",
             "Sufre de un dolor localizado cerca de sus labios, nariz y/o frente?",
             "Tiene problemas para percibir olores y sabores?",
             "Padece de un dolor de oidos?"]

# Orden de preguntas (Se recomienda recorrer la lista de preguntas utlizando estos indices)

def mixOrder(factorA, factorB):
    lista = []
    i = 0
    while (i < len(factorA)):
        if (factorA[i] == factorB[i]):
            if not (factorA[i] in lista):
                lista.append(factorA[i])
                
        elif (factorA[i] > factorB[i]):
            if not (factorB[i] in lista):
                lista.append(factorB[i])
            if not (factorA[i] in lista):
                lista.append(factorA[i])
        else:
            if not (factorA[i] in lista):
                lista.append(factorA[i])
            if not (factorB[i] in lista):
                lista.append(factorB[i])
        i += 1
    return lista

# 1 factor
sinFactores = list(range(1,32))
fumador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 27, 28, 29, 30, 31, 18, 19, 20, 22, 23, 24, 25, 26]
joven = [1, 2, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 3, 6, 12, 23, 24, 25, 26, 27, 28, 29, 30, 31]
viejo = [1, 2, 4, 5, 7, 8, 9, 10, 11, 3, 6, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
sobrepeso = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

# 2 factores (Se excluye la combinacion joven-viejo)
fumadorJoven = mixOrder(fumador, joven)
fumadorViejo = mixOrder(fumador, viejo)
fumadorSobrepeso = mixOrder(fumador, sobrepeso)
jovenSobrepeso = mixOrder(joven, sobrepeso)
viejoSobrepeso = mixOrder(viejo, sobrepeso)

# 3 factores 
fumadorJovenSobrepeso = mixOrder(fumador, mixOrder(joven, sobrepeso))
fumadorViejoSobrepeso = mixOrder(fumador, mixOrder(viejo, sobrepeso))

def obtenerEnefermedades(lista):
    lista_aux = []
    for i in range(len(lista)):
        lista_aux.append(lista[i]["X"])
    return lista_aux

#Lista de sintomas presentes + Lista de sintomas que no tiene
#listaA = list(prolog.query("que_enfermedad([tos,fiebre,'no muerte'],['escalofrios'],X)"))
#100% de los sintomas
#listaB = list(prolog.query("cumple_condicion_a([tos,fiebre,'no muerte'],X)"))
#70% de los sintomas + significativo
#listaC = list(prolog.query("cumple_condicion_b([tos,fiebre,'escalofrios'],X)"))

#print(obtenerEnefermedades(listaA))
#print(obtenerEnefermedades(listaB))
#print(obtenerEnefermedades(listaC))

#listaD = list(prolog.query("relacion(enfermedad('sinusitis cronica'),sintoma(X))"))
#listaE = list(prolog.query("tratamiento(enfermedad('sinusitis cronica'),X)"))
#print(obtenerEnefermedades(listaD))
#print(obtenerEnefermedades(listaE)[0])