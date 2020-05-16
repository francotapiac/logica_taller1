from pyswip import Prolog
from pyswip import Functor

prolog = Prolog()
prolog.consult("bd.pl")

prolog.assertz("que_enfermedad([], [], E)")
prolog.assertz("que_enfermedad([], [N|Ns], E):- not(relacion(enfermedad(E), sintoma(N))), que_enfermedad([],Ns,E)")
prolog.assertz("que_enfermedad([X|Xs],N,E):-    relacion(enfermedad(E), sintoma(X)), que_enfermedad(Xs,N,E)")


def obtenerEnefermedades(lista):
    lista_aux = []
    for i in range(len(lista)):
        lista_aux.append(lista[i]["X"])
    return lista_aux

lista = list(prolog.query("que_enfermedad([tos,fiebre,'no muerte'],[],X)"))
print(obtenerEnefermedades(lista))