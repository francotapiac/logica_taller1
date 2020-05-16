from pyswip import Prolog
from pyswip import Functor


prolog = Prolog()

prolog.consult("bd.pl")

#Serie de preguntas.
#   No cambian su orden, ni cantidad
#   Siempre las mismas

#Usted tiene fiebre
#   Si
#Usted tiene escalofrios
#   Si


#prolog.assertz("que_enfermedad([],10)")
#prolog.assertz("que_enfermedad([A|B],X):- que_enfermedad(B,X)")

prolog.assertz("primero(X,Y):- X = [Z|_], Y = Z")


prolog.assertz("que_enfermedad([], [], E)")
prolog.assertz("que_enfermedad([], [N|Ns], E):- not(relacion(enfermedad(E), sintoma(N))), que_enfermedad([],Ns,E)")
prolog.assertz("que_enfermedad([X|Xs],N,E):-    relacion(enfermedad(E), sintoma(X)), que_enfermedad(Xs,N,E)")



def obtenerEnefermedades(lista):
    lista_aux = []
    for i in range(len(lista)):
        lista_aux.append(lista[i]["X"])
    return lista_aux

lista = list(prolog.query("que_enfermedad([tos,fiebre],[],X)"))
print(obtenerEnefermedades(lista))

#FUNCION DE INTERNET PARA TRASPASAR ATOM'S
#   error de version de pyswip
def format_value(value):
    output = ""
    if isinstance(value, list):
        output = "[ " + ", ".join([format_value(val) for val in value]) + " ]"
    elif isinstance(value, Functor) and value.arity == 2:
        output = "{0}{1}{2}".format(value.args[0], value.name, value.args[1])
    else:
        output = "{}".format(value)

    return output


def format_result(result):
    result = list(result)

    if len(result) == 0:
        return "false."

    if len(result) == 1 and len(result[0]) == 0:
        return "true."

    output = ""
    for res in result:
        tmpOutput = []
        for var in res:
            tmpOutput.append(var + " = " + format_value(res[var]))
        output += ", ".join(tmpOutput) + " ;\n"
    output = output[:-3] + " ."

    return output
#END FUNCION DE INTERNET PARA TRASPASAR ATOM'S