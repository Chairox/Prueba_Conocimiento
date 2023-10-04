import sys
textoamorse = {
    "A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....",
    "I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.",
    "Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-",
    "Y": "-.--","Z": "--..","0": "-----","1": ".----","2": "..---","3": "...--","4": "....-",
    "5": ".....","6": "-....","7": "--...","8": "---..","9": "----."
    }

morseatexto = {}
for key, value in textoamorse.items():
    morseatexto[value] = key

def proyectoMorse():
    respuesta = input("""Por favor escoga: 
    1 - Morse a texto
    2 - Texto a morse
    """)

    if respuesta == '1':
        print("Ingrese el código morse a traducir: ")
        morse = input("> ")
        texto =  morse_a_texto(morse)
        print("TRADUCCIÓN (Morse a texto)")
        print(f"""La traduccion del codigo {morse}
    es: {texto}""")

    elif respuesta == '2':
        print("Ingrese el texto a traducir: ")
        texto = input("> ").upper()
        morse = texto_a_morse(texto)
        print ("TRADUCCIÓN (Texto a morse)")
        print (f"""La traducción del texto {texto}
    es: {morse}""")
    
    else:
        print(f"La opción '{respuesta}' no existe, por favor indique una de las existentes")
        proyectoMorse()
    preg3 = input("""¿Desea seguir traduciendo?
    1 - Sí
    2 - No
    """)
    if preg3 == '1':
        proyectoMorse()
    elif preg3 == '2':
        print('Hasta la próxima')
        sys.exit()
    else:
        print(f"La opción '{preg3}' no existe, retomando a menu principal")
        proyectoMorse()
def texto_a_morse(mensaje):
    morse = []
    for char in mensaje:
        if char in textoamorse:
            morse.append(textoamorse[char])
    return " ".join(morse)
def morse_a_texto(mensaje):
    mensaje = mensaje.split(" ")
    texto = []
    for codigo in mensaje:
        if codigo in morseatexto:
            texto.append(morseatexto[codigo])
    return " ".join(texto)