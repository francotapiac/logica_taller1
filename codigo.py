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

def obtenerEnefermedades(lista):
    lista_aux = []
    for i in range(len(lista)):
        lista_aux.append(lista[i]["X"])
    return lista_aux

#Lista de sintomas presentes + Lista de sintomas que no tiene
listaA = list(prolog.query("que_enfermedad([tos,fiebre,'no muerte'],['escalofrios'],X)"))

#100% de los sintomas
listaB = list(prolog.query("cumple_condicion_a([tos,fiebre,'no muerte'],X)"))

#70% de los sintomas + significativo
listaC = list(prolog.query("cumple_condicion_b([tos,fiebre,'escalofrios'],X)"))

print(obtenerEnefermedades(listaA))
print(obtenerEnefermedades(listaB))
print(obtenerEnefermedades(listaC))

#AHHH Holi