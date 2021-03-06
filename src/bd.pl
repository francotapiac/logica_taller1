sintoma('falta de aire').
sintoma('dolor de pecho').
sintoma('insomnio').
sintoma('tos').
sintoma('desorientacion').
sintoma('silvido al respirar').
sintoma('fatiga').
sintoma('fiebre').
sintoma('escalofrios').
sintoma('vomito').
sintoma('diarrea').
sintoma('produccion de esputo').
sintoma('dolor de garganta').
sintoma('goteo nasal').
sintoma('molestar general').
sintoma('congestion').
sintoma('estornudos').
sintoma('amigdalas inflamadas').
sintoma('parches blancos').
sintoma('dolor al tragar').
sintoma('mal aliento').
sintoma('dolor de cabeza').
sintoma('glandulas salivales inflamadas').
sintoma('perdida de apetito').
sintoma('dolor encias').
sintoma('glanglios linfaticos inflamados').
sintoma('inflamacion nasal').
sintoma('secrecion postnasal').
sintoma('dolor alrededor de ojos,nariz y/o frente').
sintoma('reduccion de olfato y gusto').
sintoma('dolor de oido').

enfermedad('asma').
enfermedad('neumonia').
enfermedad('bronquitis').
enfermedad('resfrio comun').
enfermedad('renitis no alergica').
enfermedad('amigdalitis').
enfermedad('paperas').
enfermedad('herpes labial').
enfermedad('sinusitis cronica').
enfermedad('influenza aviar').

relacion(enfermedad('asma'),sintoma('falta de aire')).
relacion(enfermedad('asma'),sintoma('dolor de pecho')).
relacion(enfermedad('asma'),sintoma('insomnio')).
relacion(enfermedad('asma'),sintoma('tos')).
relacion(enfermedad('asma'),sintoma('silvido al respirar')).

relacion(enfermedad('neumonia'),sintoma('falta de aire')).
relacion(enfermedad('neumonia'),sintoma('dolor de pecho')).
relacion(enfermedad('neumonia'),sintoma('tos')).
relacion(enfermedad('neumonia'),sintoma('desorientacion')).
relacion(enfermedad('neumonia'),sintoma('fatiga')).
relacion(enfermedad('neumonia'),sintoma('fiebre')).
relacion(enfermedad('neumonia'),sintoma('escalofrios')).
relacion(enfermedad('neumonia'),sintoma('vomito')).
relacion(enfermedad('neumonia'),sintoma('diarrea')).

relacion(enfermedad('bronquitis'),sintoma('falta de aire')).
relacion(enfermedad('bronquitis'),sintoma('dolor de pecho')).
relacion(enfermedad('bronquitis'),sintoma('tos')).
relacion(enfermedad('bronquitis'),sintoma('fatiga')).
relacion(enfermedad('bronquitis'),sintoma('fiebre')).
relacion(enfermedad('bronquitis'),sintoma('escalofrios')).
relacion(enfermedad('bronquitis'),sintoma('produccion de esputo')).

relacion(enfermedad('resfrio comun'),sintoma('tos')).
relacion(enfermedad('resfrio comun'),sintoma('fiebre')).
relacion(enfermedad('resfrio comun'),sintoma('dolor de garganta')).
relacion(enfermedad('resfrio comun'),sintoma('goteo nasal')).
relacion(enfermedad('resfrio comun'),sintoma('malestar general')).
relacion(enfermedad('resfrio comun'),sintoma('congestion')).
relacion(enfermedad('resfrio comun'),sintoma('estornudos')).

relacion(enfermedad('renitis no alergica'),sintoma('tos')).
relacion(enfermedad('renitis no alergica'),sintoma('produccion de esputo')).
relacion(enfermedad('renitis no alergica'),sintoma('goteo nasal')).
relacion(enfermedad('renitis no alergica'),sintoma('congestion')).
relacion(enfermedad('renitis no alergica'),sintoma('estornudos')).

relacion(enfermedad('amigdalitis'),sintoma('fiebre')).
relacion(enfermedad('amigdalitis'),sintoma('dolor de garganta')).
relacion(enfermedad('amigdalitis'),sintoma('amigdalas inflamadas')).
relacion(enfermedad('amigdalitis'),sintoma('parches blancos')).
relacion(enfermedad('amigdalitis'),sintoma('dolor al tragar')).
relacion(enfermedad('amigdalitis'),sintoma('mal aliento')).
relacion(enfermedad('amigdalitis'),sintoma('dolor de cabeza')).

relacion(enfermedad('paperas'),sintoma('fatiga')).
relacion(enfermedad('paperas'),sintoma('fiebre')).
relacion(enfermedad('paperas'),sintoma('malestar general')).
relacion(enfermedad('paperas'),sintoma('dolor al tragar')).
relacion(enfermedad('paperas'),sintoma('dolor de cabeza')).
relacion(enfermedad('paperas'),sintoma('glandulas salivales inflamadas')).
relacion(enfermedad('paperas'),sintoma('perdida apetito')).

relacion(enfermedad('herpes labial'),sintoma('fiebre')).
relacion(enfermedad('herpes labial'),sintoma('dolor de garganta')).
relacion(enfermedad('herpes labial'),sintoma('malestar general')).
relacion(enfermedad('herpes labial'),sintoma('dolor de cabeza')).
relacion(enfermedad('herpes labial'),sintoma('dolor encias')).
relacion(enfermedad('herpes labial'),sintoma('glanglios linfaticos inflamados')).

relacion(enfermedad('sinusitis cronica'),sintoma('tos')).
relacion(enfermedad('sinusitis cronica'),sintoma('fatiga')).
relacion(enfermedad('sinusitis cronica'),sintoma('dolor de garganta')).
relacion(enfermedad('sinusitis cronica'),sintoma('goteo nasal')).
relacion(enfermedad('sinusitis cronica'),sintoma('congestion')).
relacion(enfermedad('sinusitis cronica'),sintoma('mal aliento')).
relacion(enfermedad('sinusitis cronica'),sintoma('inflamacion nasal')).
relacion(enfermedad('sinusitis cronica'),sintoma('secrecion postnasal')).
relacion(enfermedad('sinusitis cronica'),sintoma('dolor alrededor de ojos,nariz y/o frente')).
relacion(enfermedad('sinusitis cronica'),sintoma('reduccion de olfato y gusto')).
relacion(enfermedad('sinusitis cronica'),sintoma('dolor de oido')).

relacion(enfermedad('influenza aviar'),sintoma('tos')).
relacion(enfermedad('influenza aviar'),sintoma('fiebre')).
relacion(enfermedad('influenza aviar'),sintoma('dolor de garganta')).
relacion(enfermedad('influenza aviar'),sintoma('malestar general')).
relacion(enfermedad('influenza aviar'),sintoma('dolor de cabeza')).

significativa(enfermedad('asma'),sintoma('silvido al respirar')).
significativa(enfermedad('neumonia'),sintoma('desorientacion')).
significativa(enfermedad('amigdalitis'),sintoma('parches blancos')).
significativa(enfermedad('amigdalitis'),sintoma('amigdalas inflamadas')).
significativa(enfermedad('paperas'),sintoma('glandulas salivales inflamadas')).
significativa(enfermedad('herpes labial'),sintoma('glanglios linfaticos inflamados')).
significativa(enfermedad('sinusitis cronica'),sintoma('inflamacion nasal')).

tratamiento(enfermedad('asma'),'
Los tipos de medicamentos de alivio rapido son los siguientes:
* Agonistas beta de accion rapida, tales como salbutamol (ProAir HFA, Ventolin HFA y otros) o levalbuterol (Xopenex). Los cuales deben inhalarse mediante una mascarilla o una boquilla, para situaciones de bajo riesgo.
* Ipratropio (Atrovent) para relajar de inmediato las vias respiratorias al tener sintomas de mediana gravedad.
* Corticoesteroides orales e intravenosos para tratar los sintomas intensos de asma.
Consulte al medico para evaular tratamientos a largo plazo (en el caso de ser una condicion cronica)

').
tratamiento(enfermedad('neumonia'),'
Los tratamientos especificos dependen del tipo y la gravedad de la neumonia:
* Antibioticos. Estos medicamentos se usan para el tratamiento de la neumonia bacteriana. Si los sintomas no mejoran, el medico puede recomendarte un antibiotico diferente.
* Medicamentos para la tos. Estos medicamentos pueden usarse para calmar la tos a fin de que puedas descansar. Se recomienda usar la dosis mas baja posible.
* Antifebriles/analgesicos tales como la aspirina, el ibuprofeno (Advil, Motrin IB, otros) y el paracetamol. Estos deben usarse solo para para aliviar la fiebre y el malestar.
').
tratamiento(enfermedad('bronquitis'),'
La mayoria de los casos de bronquitis aguda mejoran sin tratamiento, generalmente despues de un par de semanas.
En el caso de querer alivar los sintomas, se sugiere utilizar:
* Medicamento para la tos. Si la tos no te deja dormir, puedes probar con inhibidores de la tos a la hora de dormir.
* Tambien se puede usar inhalador y otros medicamentos para disminuir la inflamacion y abrir las vias estrechadas de tus pulmones.
').
tratamiento(enfermedad('resfrio comun'),'
No hay cura para el resfriado comun. Los antibioticos no son utiles contra los virus del resfriado y no deben utilizarse a menos que haya una infeccion bacteriana. El tratamiento esta dirigido a aliviar los signos y sintomas, este incluye el uso de:
* Analgesicos. Para aliviar la fiebre, el dolor de garganta y el dolor de cabeza, paracetamol (Tylenol, otros)
* Aerosoles nasales descongestionantes. Considerar que el uso prolongado (mas de 5 dias) puede causar un efecto rebote.
* Jarabes para la tos.
Se recomienda combinar una dieta liviana (liquidos, sopas, alimentos bajos en grasas) junto con un desanso prolongado.
').
tratamiento(enfermedad('renitis no alergica'),'
Para los casos leves, la combinacion de un tratamiento casero y descanso puede ser suficiente. Para los sintomas mas molestos, existen los siguientes medicamentos:
* Aerosoles nasales salinos o una solucion casera de agua salada para enjuagar los irritantes de la nariz.
* Aerosoles nasales con corticoesteroides para ayudan a prevenir y tratar la inflamacion asociada con algunos tipos de rinitis no alergica. Los posibles efectos secundarios incluyen sequedad nasal, sangrado nasal, dolores de cabeza y sequedad de garganta.
* Aerosoles nasales antihistaminicos como la azelastina (Astelin, Astepro) y el hidrocloruro de olopatadina (Patanase).
* Aerosol nasal anticolinergicos tal como antigoteo ipratropium (Atrovent). Los efectos secundarios pueden incluir sangrado nasal y sequedad en el interior de la nariz.
* Descongestivos como pseudoefedrina (Sudafed) y fenilefrina (Afrin). Estos ayudan a reducir la congestion nasal- Los posibles efectos secundarios incluyen presion arterial alta, palpitaciones e inquietud.
').

tratamiento(enfermedad('amigdalitis'),'
Si la amigdalitis esta provocada por una infeccion bacteriana, el medico recetara una serie de antibioticos, tal comar penicilina por via oral durante 10 dias.
Si se sospecha que la amigdalitis esta provocada por un virus, estas estrategias son el unico tratamiento:
* Reposo 
* Beber mucha agua, con tal de mantener la garganta humeda y prevenir la deshidratacion.
* Bebidas calientes (te, infusiones), y bocadillos frescos (paletas de helado)
* Prepara gargaras con agua salada.
* Humedecer el aire para eliminar el aire seco
* Pastillas medicadas para alivio de garganta
* Trata el dolor y la fiebre con ibuprofeno (Advil) o paracetamol (Tylenol) para minimizar el dolor de garganta y 
controlar la fiebre.
Estos tratamientos aplican de igual forma para la infeccion tipo bacteriana.
').

tratamiento(enfermedad('paperas'),'
Las paperas son provocadas por un virus, por lo cual los antibioticos no son efectivos. La mayoria de los casos de paperas se curan sin complicaciones en unas pocas semanas.
Las personas con paperas normalmente ya no contagian y pueden regresar al trabajo o a la escuela alrededor de cinco  dias luego de la aparicion de los signos y sintomas.
Pero puedes tomar algunas medidas para aliviar el dolor y las molestias y evitar que otros se infecten. Intenta lo siguiente:
* Aislamiento para evitar la trasmision de la enfermedad a otros, por un tiempo minimo de 5 dias.
* Uso de como el paracetamol (por ejemplo, Tylenol), o un medicamento antiinflamatorio tal como ibuprofeno (Advil, Motrin IB u otros), para aliviar los sintomas.
* Utilizar una compresa caliente o fria para aliviar dolor de las glandulas inflamadas.
* Utilizar un suspensorio atletico o comprensas frias para aliviar dolor de la sensibilidad testicular.
* Sopas a base de caldo o alimentos blandos, como pure de papas o avena.
* Evitar los alimentos acidos
* Beber mucho liquido.
').

tratamiento(enfermedad('herpes labial'),'
El herpes labial, por lo general, desaparece sin tratamiento en el plazo de una a cuatro semanas. Diversos tipos de medicamentos antivirales con receta pueden acelerar el proceso de curacion. Por ejemplo:
* Aciclovir (Xerese, Zovirax)
* Valaciclovir (Valtrex)
* Famciclovir (Famvir)
* Penciclovir (Denavir)
Algunos de estos productos vienen en forma de pildoras para tragar. Otros son cremas para aplicar en las aftas varias veces por dia. En general, las pildoras funcionan mejor que las cremas. En el caso de infecciones muy graves,  se pueden aplicar algunos medicamentos antivirales mediante una inyeccion.
').


tratamiento(enfermedad('sinusitis cronica'),'
Estos son algunos de los tratamientos contra la sinusitis cronica:
* Corticoesteroides nasales tales como fluticasona, triamcinolona, budesonida, mometasona y beclometasona. Estos aerosoles nasales ayudan a prevenir y tratar la inflamacion.
* La irrigacion nasal salina, con aerosoles o soluciones nasales, reduce el drenaje y elimina los irritantes y las alergias.
* Corticosteroides orales o inyectables. Estos medicamentos se usan para aliviar la inflamacion de la sinusitis grave, especialmente si tambien tienes polipos nasales.
* Tratamiento de desensibilizacion con aspirina, si tienes reacciones a la aspirina que causan sinusitis
Si tienes una infeccion bacteriana, algunas veces es necesario usar antibioticos para tratar la sinusitis.
').
tratamiento(enfermedad('influenza aviar'),'
Muchos virus de la influenza se han vuelto resistentes a los efectos de una categoria de medicamentos antivirales, entre ellos amantadina y rimantadina (Flumadine). Las autoridades de salud publica recomiendan el uso de oseltamivir (Tamiflu) o, en caso de no poder usarlo, zanamivir (Relenza). Se pueden tomar estos medicamentos en un plazo de dos dias despues de la aparicion de los sintomas.
').