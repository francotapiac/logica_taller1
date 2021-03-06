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


# Lista de sintomas
sintomas = ["falta de aire",
            "dolor de pecho",
            "insomnio",
            "tos",
            "desorientacion",
            "silvido al respirar",
            "fatiga",
            "fiebre",
            "escalofrios",
            "vomito",
            "diarrea",
            "produccion de esputo",
            "dolor de garganta",
            "goteo nasal",
            "malestar general",
            "congestion",
            "estornudos",
            "amigdalas inflamadas",
            "parches blancos",
            "dolor al tragar",
            "mal aliento",
            "dolor de cabeza",
            "glandulas salivales inflamadas",
            "perdida apetito",
            "dolor encias",
            "glanglios linfaticos inflamados",
            "inflamacion nasal",
            "secrecion postnasal",
            "dolor alrededor de ojos,nariz y/o frente",
            "reduccion de olfato y gusto",
            "dolor de oido"]


# Lista de preguntas
preguntas = ["¿Siente una dificultad para respirar similar a una falta de aire?",
             "¿Ha sentido algun tipo de dolor en el pecho?",
             "¿Ha sufrido de insomnio ultimamente?",
             "¿Tose frecuentemente?",
             "¿Ha padecido de una sensación de desorientación?",
             "¿Escucha un leve silbido al respirar?",
             "¿Se siente o ha sentido fatigado ultimamente?",
             "¿Su temperatura es superior a los 37,2 grados celcius?",
             "¿Ha sufrido de escalofríos ultimamente?",
             "¿Ha experimentado una sensacion de vomito?",
             "¿Ha sufrido de diarrea?",
             "¿Se ha producido esputo en su garganta durante los primeros dias?",
             "¿Siente un dolor constante en la garganta?",
             "¿Su nariz gotea constantemente?",
             "¿Ha sentido un malestar general recientemente?",
             "¿Tiene congestion nasal?",
             "¿Estornuda frecuentemente?",
             "¿Se han inflamado sus amigdalas?",
             "¿Puede ver placas blancas al interior de su garganta?",
             "¿Siente dolor al tragar?",
             "¿Ha tenido problemas de mal aliento ultimamente?",
             "¿Siente un dolor de cabeza?",
             "¿Siente sus glandulas salivales inflamadas?",
             "¿Ha notado una perdida de apetito?",
             "¿Sufre de un dolor en sus encias?",
             "¿Siente un dolor en el area interior de sus labios o mejillas?",
             "¿Se ha inflamado el interior de su nariz?",
             "¿Siente una sensacion de goteo en su garganta?",
             "¿Sufre de un dolor localizado cerca de sus ojos, nariz y/o frente?",
             "¿Tiene problemas para percibir olores y sabores?",
             "¿Padece de dolor de oidos?"]

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
sinFactores = list(range(0,31))
fumador = list(range(0,17)) + [20] + list(range(26,31)) + list(range(17,20)) + list(range(21,26))
joven = [0, 1, 3, 4] + list(range(6,11)) + list(range(12,22)) + [2, 5, 11] + list(range(22,31))
viejo = [0, 1, 3, 4] + list(range(6,11)) + [2, 5] + list(range(11,31))
sobrepeso = [0, 1, 2, 3, 5, 4] + list(range(6,31))

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


#Funciones para frontend
def listaPreguntas():
    return preguntas

def listaFumador():
    return fumador

def listaJoven():
    return joven

def listaViejo():
    return viejo

def listaSobrePeso():
    return sobrepeso

def listaSimtomas():
    return sintomas

def listatoString(lista):
    string = "["
    for sintoma in lista:
        string+="'"
        string += sintoma
        string+="'"
        string+=","
    final = string[:-1]
    final+="]"
    if (len(lista) == 0):
        return "[]"
    else:
        return final

def condicionA(lista):
    query = listatoString(lista)
    condicion = list(prolog.query("cumple_condicion_a("+query+",X)"))
    return obtenerEnefermedades(condicion)

def condicionB(lista):
    query = listatoString(lista)
    condicion = list(prolog.query("cumple_condicion_b("+query+",X)"))
    return obtenerEnefermedades(condicion)

def getTratamiento(enfermedad):
    consulta = list(prolog.query("tratamiento(enfermedad('"+ enfermedad +"'),X)"))
    tratamiento = obtenerEnefermedades(consulta)[0]
    return tratamiento

def getEnfermedades(lista1, lista2):
    sinSintomas = listatoString(lista2)
    lista_aux = []
    string = "'"
    for sintoma in lista1:
        temp1 = list(prolog.query("que_enfermedad(["+string+sintoma+string+"]," + sinSintomas + ",X)"))
        for enfermedad in temp1:
            if not(enfermedad in lista_aux):
                lista_aux.append(enfermedad)
    return obtenerEnefermedades(lista_aux)


#Test
#listaAux = ['falta de aire','dolor de pecho','insomnio','tos','silvido al respirar']
#listaVacia = []
#listquery = listatoString(listaAux)

#Lista de sintomas presentes + Lista de sintomas que no tiene

#print(getEnfermedades(sintomas,listaVacia))




#100% de los sintomas
#listaB = list(prolog.query("cumple_condicion_a(['falta de aire','dolor de pecho','insomnio','tos','silvido al respirar'],X)"))
#70% de los sintomas + significativo
#listaC = list(prolog.query("cumple_condicion_b(['dolor de pecho',insomnio,tos,'silvido al respirar'],X)"))

#print(obtenerEnefermedades(listaA))
#print(obtenerEnefermedades(listaB))
#print(obtenerEnefermedades(listaC))

#listatemp = getEnfermedades(['tos','fiebre'],['escalofrios','dolor de pecho','silvido al respirar'])

#print(listatemp)


#listaD = list(prolog.query("relacion(enfermedad('sinusitis cronica'),sintoma(X))"))
#listaE = list(prolog.query("tratamiento(enfermedad('sinusitis cronica'),X)"))
#print(obtenerEnefermedades(listaD))
#print(obtenerEnefermedades(listaE)[0])
