sintoma(fiebre).
sintoma(tos).
sintoma(escalofrios).
sintoma('no muerte').

enfermedad('resfrio comun').
enfermedad('resfrio mortal').

poblacionRiesgo(adulto).
poblacionRiesgo(infante).
poblacionRiesgo('adulto mayor').

relacion(enfermedad('resfrio comun'),sintoma(tos)).
relacion(enfermedad('resfrio comun'),sintoma(fiebre)).
relacion(enfermedad('resfrio comun'),sintoma('no muerte')).

relacion(enfermedad('resfrio mortal'),sintoma(tos)).
relacion(enfermedad('resfrio mortal'),sintoma(fiebre)).
relacion(enfermedad('resfrio mortal'),sintoma(escalofrios)).
relacion(enfermedad('resfrio mortal'),sintoma(muerte)).

significativa(enfermedad('resfrio mortal'),sintoma(muerte)).
significativa(enfermedad('resfrio comun'),sintoma('no muerte')).

tratamiento(enfermedad('resfrio comun'),poblacionRiesgo(infante),'Ahhh se morira el cabro chico').
tratamiento(enfermedad('resfrio comun'),poblacionRiesgo(adulto),'Ahhh se morira el adulto').
tratamiento(enfermedad('resfrio comun'),poblacionRiesgo('adulto mayor'),'Ahhh se morira el adulto mayor').
