# -------------------------- Personajes y posiciones ---------------------------

define c = Character("Celeste", color="#00AAE4", what_color="#8FE7FF", what_slow_cps=30)
define a = Character("Arturo", color="#FFC107", what_color="#FEEDBB", what_slow_cps=30)
define s = Character("Stella", color="#AF5BEB", what_color="#9C85AC", what_slow_cps=30)
define n = Character(what_color="#ffffff", what_slow_cps=35)

transform middleright:
    xalign 0.75
    yalign 0.65
    zoom 0.25

transform middleleft:
    zoom 0.25
    xalign 0.2
    yalign 0.75

transform middlecenter:
    zoom 0.35
    yalign 0.7
    xalign 0.5

# ------------------------------- Arturo ---------------------------------------

image arturo caminando ba = "arturo caminando ba.png"
image arturo caminando bb = "arturo caminando bb.png"
image arturo caminando bc = "arturo caminando bc.png"
image arturo caminando bd = "arturo caminando bd.png"
image arturo caminando fa = "arturo caminando fa.png"
image arturo caminando fb = "arturo caminando fb.png"
image arturo caminando sa = "arturo caminando sa.png"
image arturo caminando sb = "arturo caminando sb.png"
image arturo emocionado = "arturo emocionado.png"
image arturo firmamento = "arturo firmamento.png"
image arturo hablando = "arturo hablando.png"
image arturo leyendo = "arturo leyendo.png"
image arturo normal = "arturo normal.png"
image arturo triste = "arturo preocupado.png"
image arturo sorpresa = "arturo sorpresa.png"
image arturo fondo = "arturo fondo.png"

image arturo thablando:
    "arturo normal"
    pause .2
    "arturo hablando"
    pause .2
    repeat

image arturo fcaminando:
    "arturo caminando fa"
    pause .2
    "arturo caminando fb"
    pause .2
    repeat

image arturo bcaminando:
    "arturo caminando ba"
    pause .2
    "arturo caminando bb"
    pause .2
    repeat

image arturo bbcaminando:
    "arturo caminando bc"
    pause .2
    "arturo caminando bd"
    pause .2
    repeat

image arturo scaminando:
    "arturo caminando sa"
    pause .2
    "arturo caminando sb"
    pause .2
    repeat

# ------------------------------ Celeste ---------------------------------------

image celeste caminando ba = "celeste caminando ba.png"
image celeste caminando bb = "celeste caminando bb.png"
image celeste caminando fa = "celeste caminando fa.png"
image celeste caminando fb = "celeste caminando fb.png"
image celeste caminando sa = "celeste caminando sa.png"
image celeste caminando sb = "celeste caminando sb.png"
image celeste sorpresa = "celeste emocionado.png"
image celeste firmamento = "celeste firmamento.png"
image celeste hablando = "celeste hablando.png"
image celeste normal = "celeste normal.png"
image celeste triste = "celeste preocupado.png"
image celeste fondo = "celeste fondo.png"
image celeste telefonoa = "celeste telefonoa.png"
image celeste telefonob = "celeste telefonob.png"

image celeste thablando:
    "celeste normal"
    pause .2
    "celeste hablando"
    pause .2
    repeat

image celeste fcaminando:
    "celeste caminando fa"
    pause .2
    "celeste caminando fb"
    pause .2
    repeat

image celeste bcaminando:
    "celeste caminando ba"
    pause .2
    "celeste caminando bb"
    pause .2
    repeat

image celeste scaminando:
    "celeste caminando sa"
    pause .2
    "celeste caminando sb"
    pause .2
    repeat

# ------------------------------- Stela ----------------------------------------

image stela abajo = "stela abajo.png"
image stela apagado = "stela apagado.png"
image stela caja = "stela caja.png"
image stela emocionado = "stela emocionado.png"
image stela firmamento = "stela firmamento.png"
image stela normal = "stela normal.png"
image stela sorpresa = "stela sorpresa.png"
image stela fondo = "stela fondo.png"
image stela hablando = "stela hablando.png"
# ----------------------------------------------
image stela carro = "stela carro.png"
image stela avion = "stela avion.png"
# ----------------------------------------------
image stela thablando:
    "stela normal"
    pause .4
    "stela hablando"
    pause .4
    repeat

# ------------------------------ Fondos ----------------------------------------

image bg kville entrada = "kville entrada.jpg" #Entrada casa Celeste
image bg kville patio = "kville patio.jpg" #Patio Celeste dia
image bg kville tarde = "kville tarde.jpg" #Patio Celeste tarde
image bg kville patio noche = "kville patio noche.jpg" #Patio Celeste noche
image bg kville patio arriba = "kville patio arriba.jpg" #Patio Celeste arriba
image bg kville patio pelota = "kville patio pelota.jpg" #Patio Celeste pelota
image bg kville casa = "kville casa.jpg" #Sala Celeste

image bg kville normal = "kville normal.jpg" #Kville dia
image bg kville noche = "kville noche.jpg" #Kville noche
image bg kville noche iluminada = "kville iluminada.jpg" #Kville noche iluminada

image bg kville carretera tarde = "kville carretera tarde.jpg" #Kville carretera tarde
image bg kville carretera = "kville carretera noche.jpg" #Kville carretera noche
image bg kville cielo = "kville normal.jpg" # -----------------------
image bg kville cielo observar = "kville cielo observar.jpg" #Kville cielo luz
image bg kville cielo despejado = "kville cielo despejado.jpg" #Kville cielo despejado
image bg kville cielo volar = "kville cielo volar.jpg" #Kville cielo volar

image bg kville planta = "kville planta.jpg" #Kville planta electrica
image bg kville planta oficina = "kville oficina.jpg" #Kville oficina planta
image bg kville planta oficina2 = "kville oficina2.jpg" #Kville oficina planta
image bg kville planta pasillo = "kville pasillo.jpg" #Kville pasillo planta
image bg kville planta boton = "kville planta boton.jpg" #Kville boton planta
image bg kville planta pc = "bg acertijo.jpg" #Kville boton planta

image bg kville desierto = "kville desierto.jpg" #kville desierto
image bg kville piramides = "kville piramides.jpg" #kville piramides

image constelacion orion = "kville constelacion orion.jpg" #Kville Orion
image constelacion osamayor = "kville constelacion osamayor.jpg" #Kville Osamayor
image constelacion seleccion = "kville constelacion menu.jpg" #Kville Menu

image bg kville saliendo cueva = "kville cueva.jpg" #kville saliendo cueva
image bg kville cueva afuera = "kville cueva afuera.jpg" #kville cueva afuera
image bg kville ciudad afuera = "kville iluminada afuera.jpg" #kville ciudad afuera
image bg kville ciudad afuerab = "kville iluminada afuerab.jpg" #kville ciudad afuera b

image bg ciudad iluminada:
    "bg kville patio noche" with Dissolve(1.2)
    pause 1.0
    "bg kville noche" with Dissolve(1.2)
    pause 1.0
    "bg kville noche iluminada" with Dissolve(1.2)
    pause 1.0
    "bg kville patio noche" with Dissolve(1.0)

# ----------------------------- Animación --------------------------------------

transform salir_derecha:
    linear 2.0  xalign 1.5

transform salir_izquierda:
    linear 2.0  xalign -0.5

# ------------------------------ Inicio ----------------------------------------

label start:
    show bg kville normal:
        size (1280, 720)

    n "Los exploradores estelares, compuesto por Stela la androide, Celeste y
        Arturo viajarán por el mundo conociendo la Astronomía dentro de la
        historia de la humanidad."

    n "Acompañalos a esta increíble aventura, en la que irás acumulando
    conocimientos milenarios."

    show bg kville entrada

    show arturo emocionado:
        yalign 1.0
        xalign 0.5
        zoom 0.6
        block:
            "arturo bcaminando"
            linear 4.0 yalign 0.58 zoom 0.1
        block:
            "arturo scaminando"
            linear 2.5 xalign 0.25
        block:
            zoom 0

    n "Es el inicio de las vacaciones en todas la escuelas. Arturo fue de visita a
    la casa de Celeste, su mejor amiga. Al llegar encontró la puerta medio
    abierta, se dirigió directamente al patio. Allí se encontraba Celeste jugando
    en su télefono"

    hide arturo emocionado


    show bg kville jardin:
        size (1280, 720)
        "bg kville entrada"
        "bg kville patio" with Dissolve(1.0)

    show celeste telefonoa at middleleft:
        xzoom -1.0

    show arturo thablando at middleright
    a "¡Holaaaaaaaaaaaaaaaaa!"
    show arturo normal
    n "Exclamó Arturo en un fuerte grito que tomó por sorpresa a Celeste."

    n "La niña echó un grito, de lo inesperado que había aparecido el niño."
    show celeste telefonob at middleleft
    c "¡Ahhhhh!."

    show arturo thablando at middleright
    a "Jajajajaja, que concentrada estabas."
    a "Mira{w}, es un nuevo libro que me dio mi padre antes de viajar."
    a "Es para saber en qué parte del cielo están ubicadas las constelaciones,
    lo traje porque una vez dijiste que querías ser astronauta."
    show arturo normal

    show celeste thablando at middleleft
    c "Eso era antes{w}, cuando no sabía que me gustaba."
    show celeste normal

    show arturo thablando at middleright
    a "Y entonces{w}, ¿qué te gusta?"
    show arturo normal

    show celeste thablando at middleleft
    c "Buena pregunta{w}, creo que me gustaría algo relacionado con internet o videojuegos."
    show celeste firmamento at middlecenter:
        zoom 0.6
        xzoom 1.0
        yalign 0.8


    hide arturo normal
    # --------------------------- Mañana Tarde ---------------------------------
    show bg tarde:
        size (1280, 720)
        "bg kville patio"
        "bg kville tarde" with Dissolve(1.0)

    n "Celeste se levanta del prado, dirige su mirada al hermoso cielo naranja y
    mira hacia el oeste. Un sol enorme cayendo por la línea del horizonte."

    show celeste thablando at middleleft:
        zoom 0.9
        xzoom -1.0
        xalign 0.4
    c "¡Que hermoso se ve el cielo!{w}, ¿No lo crees Arturo?"
    show celeste normal

    show arturo normal at middleright:
        zoom 0.9
        yalign 0.7

    n "Mamá de Celeste: ¡Celeste!{w}, ¿Dónde estás? Ven rápido{w}, te tenemos
    una sorpresa."
    n "Gritaba la mujer con emoción y alegría."

    show celeste thablando
    c "Es mamá{w}, acompañame Arturo"
    show celeste normal

    show arturo scaminando:
        xzoom -1.0
        middleright
        salir_derecha
        zoom 0.5
    show celeste scaminando:
        middleleft
        salir_derecha
        zoom 0.5

    n "Los dos chicos atravesaron el jardín y entraron a la casa."

    # ---------------------------- Tarde Casa ----------------------------------
    show bg casa:
        size (1280, 720)
        "bg kville tarde"
        "bg kville casa" with Dissolve(1.0)

    show arturo fondo:
        zoom 0.3
        xalign 0.06
        yalign 1.0
    show celeste fondo:
        zoom 0.3
        xalign 0.01
        yalign 0.7
    show stela caja behind arturo:
        xalign 0.2
        yalign 0.95
        zoom 0.5
    show papa fondo:
        xalign 0.65
        yalign 0.95
        xzoom -1.0
        zoom 0.6

    n "Una caja gigante estaba enfrente de la entrada principal, llegaba casi
    al techo."
    n "El padre de Celeste estaba parado junto a esa caja con una gran sonrisa."

    show papa celeste
    n "Papá de Celeste: Es un regalo para ti, pequeña"

    show celeste sorpresa

    n "Celeste miró sorprendida la gran caja que tapaba la puerta. Corrió hacia
    a ella y con ayuda de Arturo, empezaron a quitarle la cinta."
    n "Levantaron las tapas y cayó todo el  relleno de espuma. Un cuerpo brillante
    y metálico, de casi dos metros con apariencia humana brillo en la sala de Celeste."

    show stela abajo:
        zoom 0.4
        xalign 0.3
        xzoom -1.0
    show papa fondo
    show arturo thablando
    show celeste thablando

    n "¡Es un robot!."

    show arturo fondo
    show celeste fondo
    show papa celeste

    n "El papá de celeste, había traído un nuevo modelo de robot diseñado para
    cuidar a los niños. Pasaba muchas horas fuera de casa y pensó que un robot
    sería una excelente niñera."

    hide papa celeste
    show stela abajo
    show arturo normal
    show celeste normal

    n "Los dos niños con gran velocidad revisaron las instrucciones para configurar
    el robot. Minutos más tarde. Los padres de Celestes se despedían de los pequeños
    para cumplir la cena de trabajo que tenían."
    n "Los niños trabajaron toda la tarde hasta completar la configuración del robot."

    # ---------------------------------------------------------------------------

    # Quiźa algo que simule unir cables o incluso darle nombre al robot
    hide stela abajo
    call fifteen

    # ---------------------------------------------------------------------------

    show stela apagado:
        zoom 0.4
        yalign 0.95
        xalign 0.3
        xzoom -1.0
    show celeste thablando
    c "Creo que ya está."
    show celeste normal

    show stela normal

    n "El robot levantó su cabeza."

    show stela thablando
    s "Hola, soy Stela. Vengo a tener aventuras con ustedes dos y a llenarlos de
    mucha diversión."
    show stela fondo

    show arturo thablando
    show celeste thablando
    n "¡Que guay!"
    show arturo fondo
    show celeste fondo

    show stela normal
    s "Ya es de noche. ¿Algo especial que quieran hacer pequeños exploradores?"
    show stela fondo

    show arturo thablando
    a "Sí{w}, ¿quieres ayudarnos a buscar constelaciones?{w}. Somos nuevos en esto."
    show arturo normal

    show arturo scaminando:
        xzoom 1.0
        salir_izquierda
    show celeste scaminando:
        xzoom 1.0
        salir_izquierda
    show stela normal:
        xzoom -1.0
        salir_izquierda

    n "Salieron apresuradamente al patio trasero."

    # ---------------------------- Casa Noche ----------------------------------
    show bg jardin noche:
        size (1280, 720)
        "bg kville casa"
        "bg kville patio noche" with Dissolve(1.0)

    show stela firmamento at middlecenter
    n "Stela puso cada uno de sus ojos en forma de catalejo."

    show celeste normal:
        middleleft
        xzoom -1.0
    show arturo normal at middleright
    n "Arturo abrió su libro y junto a Celeste buscaban una constelación."

    # ---------------------------------------------------------------------------

    # Hacer algo que parezca un libro donde salgan las constelaciones e información
    # de ella, y poder seleccionar la que se quiere ver.

    #call variables
    $ constelation = 0
    call constelaciones

    # ---------------------------------------------------------------------------

    show arturo firmamento at middleright
    show celeste firmamento at middleleft

    if constelation == 4:
        n "Al final eligieron la constelación de la Osa Mayor por la historia que la acompañaba, les parecía
        interesante y a Arturo le llamó la atención porque había leído que desde la Osa Mayor podía localizar con
        facilidad otras constelaciones."
    else:
        n "Al final eligieron la constleación de Orión por la historia que la acompañaba, les parecía
        interesante y a Celeste le llamó la atención por los mitos griegos donde nombraban al gigante."

    # Mostar solo una imágen del cielo y quitar al resto, quizá hacer el efecto de zoom y explorar
    # la imagen de cielo mostrada.
    show celeste firmamento at middleleft:
        yalign 1.5
        zoom 1.5
    show arturo firmamento at middleright:
        yalign 1.5
        zoom 1.5
    show stela firmamento at middlecenter:
        yalign 2.5
        zoom 1.5

    show bg kville cielo observar:
        size (1280, 720)

        linear 1.4 crop (800, 200, 800, 500)
        linear 1.4 crop (400, 500, 700, 450)
        linear 1.4 crop (100, 200, 600, 400)

    "{size=+50}{w=1.0}.{w=1.3}.{w=1.3}.{/size}"

    hide celeste firmamento
    hide arturo firmamento
    hide stela firmamento
    hide bg kville cielo observar

    show bg kville patio noche:
        size(1280, 720)

    show celeste thablando at middleleft:
        xzoom -1.0
    c "No veo nada,{w} se ve vacío."
    show celeste firmamento at middleleft

    show arturo thablando at middleright
    a "¿El libro nos engañó?,{w} tal vez es de fantasía."
    show arturo firmamento at middleright

    show stela thablando at middlecenter
    s "Sí, está muy vacío{w}. Saben, esto no sucedía un par de siglos atrás."
    s "Antes, todos los humanos podían contemplar el firmamento desde sus casas."
    show stela fondo at middlecenter

    show arturo thablando at middleright
    a "¿Viviste hace más 100 años?"
    show arturo fondo at middleright

    show celeste thablando at middleleft
    c "¿Por qué ahora no lo vemos?"
    show celeste fondo at middleleft

    show stela thablando at middlecenter
    # Mostrar una ciudad o varias muy iluminadas
    show bg ciudad iluminada
    s "Es debido al exceso de luz artificial que desbordan las ciudades{w}, también
    conocida como contaminación lumínica, opacando la luz de las estrellas."
    show stela fondo at middlecenter

    show bg kville patio noche
    show arturo thablando at middleright
    a "¡Ahhhh!, ya no podremos ver el firmamento"
    show arturo triste at middleright

    show celeste thablando at middleleft
    c "¡Tengo una idea!{w}, Vamos a hacer que toda Kville pueda contemplar el firmamento."
    show celeste normal at middleleft

    n "El plan de Celeste era adentrarse en la planta eléctrica de la ciudad y apagarla
    para que su amigo Arturo y los habitantes de Kville pudieran apreciar el firmamento"
    n "Stela tomó la forma de un pequeño y moderno auto."

    # ---------------------------------------------------------------------------

    # Seguir un patron mostrado en pantalla para completar la transformación del robot

    hide arturo triste
    hide celeste normal
    call simon

    # ---------------------------------------------------------------------------

    show stela carro:
        zoom 0.2
        yalign 0.9
        xalign 0.5
        parallel:
            linear 1.3 xalign -0.6
        parallel:
            linear 1.1 yalign 0.7
    show bg kville carretera

    n "El auto se conduce solo a toda velocidad por la ciudad, al llegar a la planta,
    Stela volvió a su forma de robot."

    # --------------------------- Calle Planta ---------------------------------

    show bg kville planta

    show stela normal:
        xalign 0.55
        yalign 0.5
        zoom 0.3
    show celeste fondo:
        xzoom -1.0
        xalign 0.35
        yalign 0.7
        zoom 0.25
    show arturo fondo:
        xalign 0.8
        yalign 0.5
        zoom 0.25

    show stela normal
    n "Después, Stela hackeo el código de la entrada, los dos niños entraron. El
    robot se quedó afuera para hacer guardia."
    show stela thablando
    n "Pero antes de entrar, Stela le mencionó a los niños que tenían que presionar dos
    botones rojos, los cuales apagarían la planta."
    # Mostar las imágenes de los botones y de la caja
    n "Pero uno de esos botones se encontraba en una caja, la cual solo podrían
    abrir escribiendo un código secreto."
    n "Además, todo debían hacerlo con mucha precaución, sin que los guardias se
    dieran cuenta."

    hide stela fondo
    hide arturo fondo

    show celeste fondo

    # Mostrar a Celeste y el boton
    show bg jardin noche:
        size (1280, 720)
        "bg kville planta"
        "bg kville planta oficina2" with Dissolve(1.0)

    show celeste normal:
        xalign 0.0
        yalign 0.92
        zoom 0.3

    n "Celeste fue en busca de uno de los botones, el cual se encontraba resguardado en una
    oficina."

    show celeste scaminando:
        xzoom -1.0
        salir_derecha
    n "Con gran astucia Celeste logro escabullirse por la oficina y llegar al botón"
    hide celeste scaminando

    show bg kville planta boton:
        crop (0, 0, 1920, 1080)
        size (1280, 720)

        linear 1.0 crop (351, 137, 1280, 720)

    c "¡Genial!. Solo falta Arturo."
    hide bg kville planta boton

    show bg kville planta pasillo:
        size (1280, 720)

    show arturo preocupado:
        xalign 0.5
        yalign 1.0
        zoom 0.3
    n "El pequeño niño nervioso fue en busca del último botón el cual estaba protegido
    con un código secreto."

    show arturo preocupado:
        block:
            xalign 0.1
            yalign 0.85
            zoom 0.28
            xzoom 1.0
            pause 0.8
        block:
            xalign 0.9
            yalign 0.85
            zoom 0.28
            xzoom -1.0
            pause 0.8
        block:
            xalign 0.32
            yalign 0.62
            zoom 0.15
            xzoom 1.0
            pause 0.8
        block:
            xalign 0.68
            yalign 0.62
            zoom 0.15
            xzoom -1.0
            pause 0.8
        block:
            xalign 0.5
            yalign 0.58
            zoom 0.13


    n "El pequeño tropezó y casi es descubierto, entró a diferentes habitaciones
    de un pasillo, pero no encontraba nada."

    hide arturo preocupado
    # Animación de ir al final del pasillo
    show bg kville planta pasillo:
        crop (0, 0, 1920, 1080)
        size (1280, 720)

        linear 1.0 crop (650, 380, 580, 300)

    n "Finalmente llego al la última puerta del pasillo, una gran puerta estaba frente al joven Arturo."

    show arturo caminando ba with Dissolve(0.8):
        xalign 0.5
        yalign 5.0
        zoom 0.6

    n "Finalmente, Arturo se aventuró a abrir la puerta."

    hide bg kville planta pasillo
    show bg kville planta oficina:
        size(1280, 720)

    n "La puerta escondia una oficina, Arturo decidio acercarse al computador que
    reposaba en el escritorio y echar un vistazo."

    show bg kville planta pc:
        size(1280, 720)

    # ---------------------------------------------------------------------------

    # Input para recibir el nombre de la constelación o las cuatro posibles opciones de respuesta
    call acertijo

    # ---------------------------------------------------------------------------

    hide bg kville planta pc
    show bg kville planta boton:
        zoom -1.0
        crop (0, 0, 1920, 1080)
        size (1280, 720)

        linear 1.0 crop (351, 137, 1280, 720)

    hide arturo emocionado
    n "Abrió la caja, y presionó el botón"

    hide bg kville planta boton
    show bg kville planta oficina:
        size(1280, 720)

    show arturo thablando at middleleft:
        xzoom -1.0
        zoom 1.5
    a "Fue más fácil de lo que esperaba."
    hide arturo emocionado

    # Cambio de ciudad iluminada a ciudad apagada
    show bg cambio luz:
        "bg kville noche iluminada"
        pause 1.0
        "bg kville noche" with Dissolve(1.0)


    n "La ciudad perdió todo su brillo. Todo se detuvo."

    # Otra imágen de ciudad apagada, quiźa transiciones con la mezcla primitiva

    show bg cueva luz:
        "bg kville saliendo cueva"
        pause 1.0
        "bg kville cueva afuera" with Dissolve(1.0)

    s "Cuando los humanos salieron de las cuevas y empezaron a observar más su
    entorno, dejaron de ser nómadas."

    # Ciudad apagada con gente saliendo a la calle
    show bg ciudad luz:
        "bg kville cueva afuera"
        "bg kville ciudad afuera" with Dissolve(1.0)
        pause 1.0
        "bg kville ciudad afuerab" with Dissolve(1.0)

    n "Todos los habitantes de Kville salieron de sus hogares, para ver qué sucedía"

    # Otro fondo
    show bg gente luz:
        "bg kville ciudad afuerab"
        "bg kville cueva afuera" with Dissolve(1.0)
        pause 1.0
        "bg kville ciudad afuerab" with Dissolve(1.0)

    s "Se unieron en comunidades y empezaron a observar el cielo, a tratar de
    entender el movimiento de los astros."

    # Ciudad apagda y gente mirando arriba
    show bg gente luz:
        "bg kville ciudad afuerab"
        pause 1.0
        "bg kville cielo despejado" with Dissolve(1.0)

    n "Los habitantes de Kville, alzaron su cabeza y por primera vez vieron cómo
    se iluminaba el cielo. Maravillados todos los habitantes, gozaron de un espectáculo nocturno."

    show stela emocionado at middlecenter:
        yalign 0.95
    show arturo emocionado at middleright:
        yalign 0.95

    show celeste thablando at middleleft:
        yalign 0.95
        xzoom -1.0
    c "¡Lo logramos!"
    show celeste emocionado

    show arturo thablando
    a "Esto es mejor de lo que esperaba."
    show arturo emocionado

    hide arturo emocionado
    hide celeste emocionado
    hide stela emocionado

    # Transición a cambio de día
    n "Al día siguiente..."
    show bg kville dia:
        size (1280, 720)
        "bg kville noche"
        "bg kville normal" with Dissolve(1.0)

    n "Al día siguiente..."

    show bg kville entradac:
        size (1280, 720)
        "bg kville normal"
        "bg kville entrada" with Dissolve(1.0)

    show arturo normal:
        xalign 0.5
        yalign 1.0
        zoom 0.6

    n "Arturo llegó temprano a la casa de Celeste, lleno de emoción y con ganas
    de vivir nuevas aventuras."

    show bg kville entrada

    show arturo emocionado:
        yalign 1.0
        xalign 0.5
        zoom 0.6
        block:
            "arturo bcaminando"
            linear 4.0 yalign 0.58 zoom 0.1
        block:
            "arturo scaminando"
            linear 2.5 xalign 0.25
        block:
            zoom 0

    n "De nuevo la puerta estaba entreabierta, Arturo corrió al patio donde
    Celeste jugaba al ponchado junto a Stela."
    hide arturo emocionado
    show bg kville patio arriba

    show celeste emocionado:
        zoom 0.3
        block:
            xzoom -1.0
            "celeste scaminando"
            linear 1.3 xalign 0.8
        block:
            "celeste fcaminando"
            linear .9 yalign 0.9 zoom 0.35
        block:
            xzoom 1.0
            "celeste scaminando"
            linear 1.3 xalign 0.2
        block:
            "celeste bcaminando"
            linear .9 yalign 0.05 zoom 0.25
        repeat

    show stela emocionado:
        zoom 0.3
        block:
            xzoom 1.0
            linear 1.5 xalign 1.05
        block:
            xzoom -1.0
            linear .7 yalign 1.1 zoom 0.35
        block:
            linear 1.5 xalign -0.05
        block:
            xzoom 1.0
            linear .7 yalign -0.1 zoom 0.25
        repeat

    n "Stela perseguía a Celeste por todo el patio, de repente, lanzó la pelota."

    hide celeste emocionado
    hide arturo emocionado
    hide stela emocionado
    show bg kville patio pelota
    show arturo sorpresa:
        xalign 1.0
    show celeste emocionado:
        xalign -0.3
        xzoom -1.0

    n "Celeste rápidamente se agacho y la pelota continuo a toda velocidad hasta que
    chocó con el árbol dejando un hueco en este."

    show bg kville patio
    show arturo fondo at middleright
    show stela fondo at middlecenter
    show celeste thablando at middleleft:
        xzoom -1.0
    c "Oye Oliver Atom, ten cuidado. Vas a destruir la casa."
    show celeste fondo

    show arturo thablando
    a "Eso estuvo cerca."
    show arturo fondo

    show stela thablando
    s "Arturo, que bueno es verte."
    show stela fondo

    show arturo thablando at middleright
    a "Quiero que me enseñes más sobre el cielo{w}, ¿Qué pasó después de que los
    humanos empezaron a observar el firmamento?"
    show arturo fondo

    show stela thablando at middlecenter
    s "Tenemos que ir a un lugar lejano."
    show stela fondo

    show celeste thablando at middleleft
    c "Vamos a ver que tienes para hoy Stela."
    show celeste emocionado

    show arturo emocionado at middleright
    show stela emocionado at middlecenter

    n "Los niños presionan los comandos del robot y esta se convirtió en una pequeña nave."

    # ---------------------------------------------------------------------------

    # Seguir un patron mostrado en pantalla para completar la transformación del robot
    call simon

    # ---------------------------------------------------------------------------

    hide arturo emocionado
    hide celeste emocionado
    show stela avion at middlecenter
    # --- Animación de moviento
    show stela avion:
        zoom 0.05
        yalign 0.6
        xalign 0.3
        block:
            linear 1.3 xalign 0.4 yalign 0.1 zoom 0.2
        block:
            linear 1.3 xalign 0.48 yalign 0.48 zoom 0.07
    show bg kville cielo volar

    n "Los dos niños subieron y Stela despegó a toda velocidad. Cuando ya llegaba
    el atardecer, los niños miraron por las ventanas."

    hide stela avion
    show bg kville desierto

    show celeste thablando:
        xzoom -1.0
        xalign -0.2
        yalign -2.0
        zoom 0.8
        alpha 0.7
    c "¿Nos trajiste a un desierto?{w}, espera{w}..."

    show bg kville piramides

    c "¿Esas son las  pirámides?"
    show celeste preocupado

    show arturo thablando:
        xalign 1.2
        yalign -2.0
        zoom 0.8
        alpha 0.7
    a "¿Y esa es la esfinge?"
    show arturo sorpresa

    show celeste thablando
    c "¿Acaso estamos en Egipto?"
    show celeste preocupado

    show stela thablando:
        xalign 0.5
        yalign 0.0
        zoom 1.5
        alpha 0.7
    s "Es correcto"
    show stela emocionado

    show celeste emocionado
    show arturo thablando
    a "¡Esto es muy cool!"
    show arturo emocionado

    n "Se bajaron lentamente de la nave, sintiendo gran sorpresa por estar en aquel
    milenario lugar. Celeste tomaba todas las fotos que podía."

    hide stela emocionado
    hide celeste emocionado
    hide arturo emocionado

    show arturo fondo at middleright:
        yalign 0.92
    show stela fondo at middlecenter:
        yalign 0.92
        xzoom -1.0

    show celeste thablando at middleleft:
        yalign 0.92
        xzoom -1.0
    c "Egipto no se visita todo los días."
    show celeste fondo

    # --- Caminado por el desierto
    show arturo emocionado:
        block:
            "arturo bcaminando"
            middleright
            yalign 0.92
            linear 5.0 yalign 0.9 xalign 0.501 zoom 0.0
    show celeste emocionado:
        block:
            "celeste bcaminando"
            middleleft
            yalign 0.92
            xzoom -1.0
            linear 5.0 yalign 0.9 xalign 0.499 zoom 0.0
    show stela emocionado:
        block:
            middlecenter
            yalign 0.92
            xzoom -1.0
            linear 5.0 yalign 0.9 xalign 0.5 zoom 0.0

    n "La robot y los niños decidieron adentrarse en las pirámides y dar comienzo a la exploración."

    hide arturo fondo
    hide stela fondo
    hide celeste fondo
    # --- Mostrar obelisco

    image tallado piramide = "tallado piramide.png"
    image bg negro = "#000000"

    show bg negro
    show tallado piramide at middlecenter:
        yalign 0.5
        zoom 1.1
    n "En un gran ladrillo de arena se encontraban unas extrañas inscripciones talladas."

    show stela sorpresa:
        xalign 0.15
        yalign 0.8
        zoom 0.6
    n "Stela se quedó observando detenidamente los escritos para lograr descifrar
    las palabras que estos albergan."

    show stela thablando
    s "Este texto está escrito en una lengua muy antigua{w}, parece hablar de una
    de las constelaciones más importantes del antiguo reino de Egipto, aquella época
    en que las pirámides aún eran jóvenes y los faraones reinaban en la tierra."

    s "Hablan de una antigua tableta la cual al ordenar sus piezas relatan parte de batalla
    entre el dios Osiris y su hermano Seth."
    show stela fondo

    show arturo fondo at middleright
    show celeste thablando at middleleft:
        xzoom -1.0
    "Cerca del lugar encontraron una antigua tableta que parecía coincidir con lo narrado por Stela y decidieron intentarlo."

    c "¡Vamos a ordenarla Arturo!"
    show celeste fondo

    show arturo normal at middleright
    n "Arturo tomó con sus manos cada una de las piezas, buscando que encajaran en la tableta."

    show arturo sorpresa at middleright
    n "Su frente sudaba por el intenso calor, mientras trataba de buscar el orden
    correcto de las constelaciones."

    # ---------------------------------------------------------------------------

    # Rompecabezas

    call puzzle4

    # ---------------------------------------------------------------------------

    hide whole
    show bg kville piramides:
        size(1280, 720)

    show arturo sorpresa at middleright
    n "Cansado y con los labios resecos, pasó su brazo para secar el sudor de la frente."

    show arturo thablando at middleright
    a "¡Lo logre!"
    show arturo emocionado

    n "Continuara..."


    return

#---------------- Puzzles ------------------------------------------------------

init python:
    def piece_dragged(drags, drop):

        if not drop:
            return

        p_x = drags[0].drag_name[0]
        p_y = drags[0].drag_name[1]
        t_x = drop.drag_name[0]
        t_y = drop.drag_name[1]

        if p_x == t_x and p_y == t_y:
            renpy.music.play("Pickup_Coin.ogg", channel="sound")
            my_x = int(p_x)*100+25
            my_y = int(p_y)*100+25
            drags[0].snap(my_x,my_y)
            drags[0].draggable = False
            placedlist[int(p_x),int(p_y)] = True
            for i in range(6):
                for j in range(4):
                    if placedlist[i,j] == False:
                        return
            return True
        return

screen jigsaw:

    draggroup:

        for i in range(6):
            for j in range(4):
                $ name = "%s%s"%(i,j)
                $ my_x = i*100+50
                $ my_y = j*100+50
                drag:
                    drag_name name
                    child "blank_space.png"
                    draggable False
                    xpos my_x ypos my_y


        for i in range(6):
            for j in range(4):
                $ name = "%s%s piece"%(i,j)
                drag:
                    drag_name name
                    child imagelist[i,j]
                    droppable False
                    dragged piece_dragged
                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]

label puzzle:
    call screen jigsaw
    jump win

label puzzle4:
    scene bg kville desierto:
        size (1280, 720)
    image whole = "constelacion toro.jpg"
    python:
        mainimage = im.Composite((650, 450),(25, 25), "constelacion toro.jpg")
        piecelist = dict()
        imagelist = dict()
        placedlist = dict()
        for i in range(6):
            for j in range(4):
                piecelist[i,j] = [renpy.random.randint(0, 600)+600, renpy.random.randint(0, 480)]
                tempimage = im.AlphaMask(mainimage,"puzzle_pieces/%s_%s.png"%(j+1,i+1))
                imagelist[i,j] = im.Crop(tempimage, i*100,j*100, 150, 150)
                placedlist[i,j] = False
    jump puzzle

label win:
    scene bg kville desierto:
        size (1280, 720)
    show whole at Position(xalign=0.5,yalign=0.5)
    "¡Bien hecho explorador!"
    menu:
        "¡Lo hiciste fabuloso!"

        "Volver a alinear la constelación":
            jump puzzle4

        "Continuar con la aventura":
            return

label simon:
    init python:

        def simon_say(secuence):
            for i in range(6):
                secuence.append(renpy.random.randint(1, 9))
            return secuence

        def simon_check(sec, check_sec, round):
            for i in range(len(check_sec)):
                if sec[i] != check_sec[i]:
                    return 0
            if len(check_sec) == len(sec):
                return 1
            if round == len(check_sec) and round < len(sec):
                return 2

        class PongDisplayable(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)

                # Cube size
                self.CUBE_WIDTH = 150
                self.CUBE_HEIGHT = 150

                # Cube
                self.filter_cube = Solid("#008F3980", xsize=self.CUBE_WIDTH, ysize=self.CUBE_HEIGHT)

                # Variables
                self.secuence = []
                self.check_secuence = []
                self.round = 1
                self.playing = False
                self.res = -1
                self.stuck = True
                self.end = False

            # Recomputes the position of the ball, handles bounces, and
            # draws the screen.
            def render(self, width, height, st, at):
                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                if self.playing:
                    # Mostar animacion de la secuencia
                    filter = renpy.render(self.filter_cube, width, height, st, at)
                    if self.cont == 0:
                        renpy.time.sleep(0.3)
                    else:
                        renpy.time.sleep(0.6)


                    if self.cont < self.round and self.pausa:
                        if self.secuence[self.cont] == 1:

                            self.filter_cube = Solid("#008F3980", xsize=399, ysize=399)
                            filter = renpy.render(self.filter_cube, width, height, st, at)
                            r.blit(filter, (59, 67))

                        if self.secuence[self.cont] == 2:

                            self.filter_cube = Solid("#008F3980", xsize=399, ysize=147)
                            filter = renpy.render(self.filter_cube, width, height, st, at)
                            r.blit(filter, (59, 496))

                        if self.secuence[self.cont] == 3:

                            self.filter_cube = Solid("#008F3980", xsize=208, ysize=208)
                            filter = renpy.render(self.filter_cube, width, height, st, at)
                            r.blit(filter, (522, 67))

                        if self.secuence[self.cont] == 4:

                            self.filter_cube = Solid("#008F3980", xsize=208, ysize=208)
                            filter = renpy.render(self.filter_cube, width, height, st, at)
                            r.blit(filter, (777, 67))

                        if self.secuence[self.cont] == 5:

                            self.filter_cube = Solid("#008F3980", xsize=208, ysize=208)
                            filter = renpy.render(self.filter_cube, width, height, st, at)
                            r.blit(filter, (1007, 67))

                        if self.secuence[self.cont] == 6:

                            self.filter_cube = Solid("#008F3980", xsize=208, ysize=208)
                            filter = renpy.render(self.filter_cube, width, height, st, at)
                            r.blit(filter, (522, 277))

                        if self.secuence[self.cont] == 7:

                            self.filter_cube = Solid("#008F3980", xsize=208, ysize=208)
                            filter = renpy.render(self.filter_cube, width, height, st, at)
                            r.blit(filter, (777, 277))

                        if self.secuence[self.cont] == 8:

                            self.filter_cube = Solid("#008F3980", xsize=208, ysize=208)
                            filter = renpy.render(self.filter_cube, width, height, st, at)
                            r.blit(filter, (1007, 277))

                        if self.secuence[self.cont] == 9:

                            self.filter_cube = Solid("#008F3980", xsize=692, ysize=147)
                            filter = renpy.render(self.filter_cube, width, height, st, at)
                            r.blit(filter, (522, 498))


                        self.cont  += 1
                        self.pausa = False
                    else:
                        r.blit(filter, (2000, 2000))
                        self.pausa = True
                        if self.cont == self.round:
                            self.playing = False
                            self.cont = 0

                    renpy.timeout(0)

                # Ask that we be re-rendered ASAP, so we can show the next
                # frame.
                renpy.redraw(self, 0)

                # Return the Render object.
                return r

            # Handles events.
            def event(self, ev, x, y, st):

                import pygame

                # Mousebutton down == start the game by setting stuck to
                # false.
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    # Ensure the screen updates.
                    renpy.restart_interaction()

                    if self.res == 2 and not self.playing:
                        self.check_secuence = []
                        self.res = -1
                        self.playing = True
                        self.cont = 0

                    elif self.stuck:
                        self.stuck = False
                        self.playing = True
                        self.secuence = []
                        simon_say(self.secuence)
                        self.check_secuence = []
                        self.round = 1
                        self.res = -1
                        self.end = False
                        self.cont = 0
                        self.pausa = True

                    elif not self.playing:
                        x, y = pygame.mouse.get_pos()

                        if 59 <= x <= 458 and 67 <= y <= 465:
                            self.check_secuence.append(1)

                        if 59 <= x <= 458 and 496 <= y <= 643:
                            self.check_secuence.append(2)

                        if 522 <= x <= 730 and 67 <= y <= 275:
                            self.check_secuence.append(3)

                        if 777 <= x <= 983 and 67 <= y <= 275:
                            self.check_secuence.append(4)

                        if 1007 <= x <= 1214 and 67 <= y <= 275:
                            self.check_secuence.append(5)

                        if 522 <= x <= 730 and 277 <= y <= 484:
                            self.check_secuence.append(6)

                        if 777 <= x <= 983 and 277 <= y <= 484:
                            self.check_secuence.append(7)

                        if 1007 <= x <= 1214 and 277 <= y <= 484:
                            self.check_secuence.append(8)

                        if 522 <= x <= 1214 and 498 <= y <= 645:
                            self.check_secuence.append(9)

                        self.res = simon_check(self.secuence, self.check_secuence, self.round)

                        if self.res == 0:
                            self.stuck = True
                            self.playing = False
                        elif self.res == 1:
                            self.end = True
                        elif self.res == 2:
                            self.round += 1
                            self.playing = False


                # If the player win, return. Otherwise, ignore
                # the current event.
                if self.end:
                    return self.end
                else:
                    raise renpy.IgnoreEvent()


    screen pong():

        default pong = PongDisplayable()

        add "bg simon field":
            size (1280, 720)

        add pong

        text _("Ronda [pong.round]"):
            xpos 240
            xanchor 0.5
            ypos 18
            size 40

        text _("Ronda [pong.round]"):
            xpos (1280 - 240)
            xanchor 0.5
            ypos 18
            size 40

        if pong.stuck:
            text _("Click to Begin"):
                xalign 0.5
                ypos 20
                size 40


        if pong.res == 0:
            text _("Has Fallado aventurero, da clik para volver a intentarlo."):
                xalign 0.5
                ypos 350
                size 40
        elif pong.res == 1:
            text _("Lo lograste, bien hecho."):
                xalign 0.5
                ypos 350
                size 40
        elif pong.res == 2:
            text _("Bien hecho, da click para continuar con la siguiente ronda."):
                xalign 0.5
                ypos 350
                size 40


    label play_pong:
        window hide  # Hide the window and quick menu while in pong
        $ quick_menu = False

        call screen pong

        $ quick_menu = True
        window show

    return

label constelaciones:
    screen show_book:
        textbutton _("Siguiente"):
            xalign 1.0
            yalign 0.5
            text_color "#FFF"
            text_hover_color "#636B2C"
            action Jump("suma")
            background "#000"

    screen show_book2:
        textbutton _("Anterior"):
            xalign 0.0
            yalign 0.5
            text_color "#FFF"
            text_hover_color "#636B2C"
            action Jump("resta")
            background "#000"
        textbutton _("Siguiente"):
            xalign 1.0
            yalign 0.5
            text_color "#FFF"
            text_hover_color "#636B2C"
            action Jump("suma")
            background "#000"

    if constelation == 0:
        show constelacion orion:
            size(1280, 720)
        call screen show_book
    elif constelation == 1:
        show constelacion osamayor:
            size(1280, 720)
        call screen show_book2
    elif constelation == 2:
        show constelacion seleccion:
            size(1280, 720)
        menu:
            "¿Qué constelación deseas observar?"

            "Constelación de Orión":
                call orion

            "Constelación de Osa Mayor":
                call osa

    hide constelacion osamayor
    return constelation

label suma:
    $ constelation += 1
    call constelaciones
    return

label resta:
    $ constelation -= 1
    call constelaciones
    return

label osa:
    $ constelation = 4
    call constelaciones
    return

label orion:
    $ constelation = 5
    call constelaciones
    return

label acertijo:
    $ respuesta = 0
    $ pregunta = "Una madre seguida de sus tres ozesnos, algunos dicen que tiene forma de cucharon."
    if constelation == 5:
        $ pregunta = "Es un gran cazador que ostenta un famoso cinturon."

    menu:
        n "[pregunta]"

        "Contelación de la Osa Mayor":
            $ respuesta = 4
        "Constelación deOrión":
            $ respuesta = 5

    if constelation == respuesta:
        return
    else:
        n "Parece que esa no es la respuesta correcta, vuelve a intentar"
        call acertijo

label fifteen:
    ##### The game screen.
    screen fifteen_scr:

        ##### Timer.
        if timer_on:
            timer 1.0 action If(fifteen_timer > 0, [SetVariable("fifteen_timer", fifteen_timer-1), Return("smth")], Return("time_is_up") ) repeat True
            text str(fifteen_timer) xalign 0.1 yalign 0.1

        ##### Game field.
        frame:
            xalign 0.5 yalign 0.5
            background Solid("#ccc") #Frame("pic_1.png", 5, 5) # The background might be set as a solid color or a frame, that uses predefined displayable or file name, also you can delete this line to have default frame background.

            grid grid_width grid_height spacing 0:
                for every_tile in tiles_list:
                    if every_tile["tile_value"] == empty_tile_value and not fifteen_is_solved:
                        null

                    else:
                        button:
                            #####
                            #
                            # To use just numbers (classic fifteen game) - uncomment next 4 lines and comment out lines that are used to show an image.
                            # It is neccessary to set the size of buttons.
                            # (The background might be set as a solid color or a frame, that uses predefined displayable or file name, also you can delete this line to have default button background.)
                            #xminimum 70 xmaximum 70
                            #yminimum 70 ymaximum 70
                            #background Solid("#c00")
                            #text str(every_tile["tile_value"]) xalign 0.5 yalign 0.5
                            #
                            #####


                            #####
                            #
                            # Next lines are used to show an image.
                            left_padding 0 right_padding 0 top_padding 0 bottom_padding 0
                            left_margin 0 right_margin 0 top_margin 0 bottom_margin 0
                            add LiveCrop( ( (every_tile["tile_value"]-1)%grid_width*tile_width,
                                            (every_tile["tile_value"]-1)//grid_width*tile_height,
                                            tile_width,
                                            tile_height),
                                            chosen_img)
                            #
                            #####


                            action [ If (every_tile["tile_number"] not in top_row,
                                       true = If (tiles_list[every_tile["tile_number"]-grid_width]["tile_value"] == empty_tile_value,
                                         true = [SetDict( tiles_list[every_tile["tile_number"]-grid_width], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                         false = None),
                                       false = None),
                                     If (every_tile["tile_number"] not in bottom_row,
                                       true = If (tiles_list[min(len(tiles_list)-1, every_tile["tile_number"]+grid_width)]["tile_value"] == empty_tile_value,
                                         true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+grid_width))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                         false = None),
                                       false = None),
                                     If (every_tile["tile_number"] not in left_column,
                                       true = If (tiles_list[every_tile["tile_number"]-1]["tile_value"] == empty_tile_value,
                                         true = [SetDict( tiles_list[every_tile["tile_number"]-1], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                         false = None),
                                       false = None),
                                     If (every_tile["tile_number"] not in right_column,
                                       true = If (tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))]["tile_value"] == empty_tile_value,
                                         true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                         false = None),
                                       false = None), Return("smth")
                                   ]

        ##### A button that will show the whole image, should be used only if game uses images (not numbers).
        textbutton "Mostrar/ocultar imagen" action If( renpy.get_screen("full_image"), Hide("full_image"), Show("full_image") ) xalign 0.5 yalign 0.1 text_color "#FFF" text_hover_color "#636B2C" background "#000"


    ##### Screen that contains an image to show (not useful in classic fifteen game).
    #
    screen full_image:
        add chosen_img xalign 0.5 yalign 0.5 at pic_trans


    transform pic_trans:
        alpha 0.0 zoom 0.7
        on show:
            parallel:
                linear 1.0 alpha 1.0
            parallel:
                linear 0.6 zoom 1.2
                linear 0.4 zoom 1.0
        on hide:
            linear 0.5 alpha 0.0
    #
    #####


    label fifteen_game:

        ##### Game settings.
        #
        # Let's set the size of game field in tiles, for example 9 tiles (3 x 3).
        $ grid_width = 4
        $ grid_height = 4

        # Next 4 lines are used to set an image to solve (could be deleted for clasic fifteen game).
        # It is recommended that all images will be smaller than screen size.
        $ chosen_img = "cable puzzle.png" #renpy.random.choice ( ("ShizukaClassroom_6X4.jpg") )
        $ chosen_img_width, chosen_img_height = renpy.image_size(chosen_img)
        $ tile_width = chosen_img_width/grid_width
        $ tile_height = chosen_img_height/grid_height
        #

        # Some useful calculations:
        $ top_row = []
        python:
            for i in range(0, grid_width):
                top_row.append (i)
        $ bottom_row = []
        python:
            for i in range(0, grid_width):
                bottom_row.append ( (grid_width*(grid_height-1)+i) )
        $ left_column = []
        python:
            for i in range(0, grid_height):
                left_column.append (grid_width*i)
        $ right_column = []
        python:
            for i in range(0, grid_height):
                right_column.append (grid_width*(i+1)-1)


        # Let's set the game field - all the tiles are on their places.
        $ tiles_list = []
        python:
            for i in range (0, grid_height):
                for j in range (0, grid_width):
                    tiles_list.append ( {"tile_number":(i*grid_width+j), "tile_value":(i*grid_width+(j+1))} )


        # Let's set a missed tile - it can be a random one or the last one (as in classic fifteen game).
        $ empty_tile_value = renpy.random.randint ( 1, grid_width*grid_height )
        #$ empty_tile_value = grid_width*grid_height
        #

        # Some variables:
        # will let us control if the missed tile should be shown
        $ fifteen_is_solved = False
        # sets the timer to make game more difficult
        $ fifteen_timer = 1000
        # will let us control the timer
        $ timer_on = False

        # This will show the game screen.
        show screen fifteen_scr

        # To be sure that puzzle can be solved, just randomly move some tiles.
        # This process could be shown to player - uncomment the line that sets the pause between moves.
        # The number of moves should be great enought to shuffle tiles good,
        # also it should be odd to avoid situation when random moves will bring all the tiles back on their starting positions.
        $ shuffle_moves = 80
        label tiles_shuffle:
            if shuffle_moves > 0:
                python:
                    possible_moves_list = []
                    for j in tiles_list:
                        if j["tile_value"] == empty_tile_value:
                            if j["tile_number"] not in top_row:
                                possible_moves_list.append ("top")
                            if j["tile_number"] not in bottom_row:
                                possible_moves_list.append ("bottom")
                            if j["tile_number"] not in left_column:
                                possible_moves_list.append ("left")
                            if j["tile_number"] not in right_column:
                                possible_moves_list.append ("right")
                            move_tile = renpy.random.choice (possible_moves_list)
                            if move_tile == "top":
                                tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-grid_width]["tile_value"]
                                tiles_list[j["tile_number"]-grid_width]["tile_value"] = empty_tile_value
                            elif move_tile == "bottom":
                                tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+grid_width]["tile_value"]
                                tiles_list[j["tile_number"]+grid_width]["tile_value"] = empty_tile_value
                            elif move_tile == "left":
                                tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-1]["tile_value"]
                                tiles_list[j["tile_number"]-1]["tile_value"] = empty_tile_value
                            elif move_tile == "right":
                                tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+1]["tile_value"]
                                tiles_list[j["tile_number"]+1]["tile_value"] = empty_tile_value
                            shuffle_moves -= 1
                            renpy.pause(0.01)           # If used pause should be not so long.
                            renpy.jump("tiles_shuffle")

        # Now we can start the timer.
        $ timer_on = True

        # The game loop.
        label fifteen_game_loop:
            $ result = ui.interact()
            $ fifteen_timer = fifteen_timer
            if result == "time_is_up":
                jump fifteen_lose
            python:
                for j in tiles_list:
                    if j["tile_value"]-1 != j["tile_number"]: # will continue the game if at least one tile is not in its place
                        renpy.jump("fifteen_game_loop")
            jump fifteen_win

    label fifteen_win:
        # This will turn off the timer.
        $ timer_on = False
        $ renpy.pause(0.1, hard = True)
        $ renpy.pause(0.1, hard = True)

        # This will show the missed tile in its place.
        $ fifteen_is_solved = True

        "Lo has logrado!"
        hide screen fifteen_scr
        menu:
            "¿Qué deseas hacer?"

            "Volver a ensamblar a Stela":
                call fifteen

            "Continuar con la aventura":
                return
        return

    label fifteen_lose:
        $ timer_on = False
        $ renpy.pause(0.1, hard = True)
        $ renpy.pause(0.1, hard = True)
        "No te rindas volvamos a intentarlo."
        hide screen fifteen_scr
        call fifteen
