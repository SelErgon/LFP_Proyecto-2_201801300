from fpdf import FPDF

#Diccionario de lexemas (Tipo de funcion a usar)
Sentencias_clave = {
    "CrearBD": "CREAR_BD",
    "EliminarBD": "ELIMINAR_BD",
    "CrearColeccion": "CREAR_COLECCION",
    "EliminarColeccion": "ELIMINAR_COLECCION",
    "InsertarUnico": "INSERTAR_UNICO",
    "ActualizarUnico": "ACTUALIZAR_UNICO",
    "EliminarUnico": "ELIMINAR_UNICO",
    "BuscarTodo": "BUSCAR_TODO",
    "BuscarUnico": "BUSCAR_UNICO",
    "nueva": "NUEVA",
    "$set": "SET",
    '---' : 'COMENTARIO_CORTO',
    '/*' : 'COMENTARIO_LARGOPT1',
    '*/' : 'COMENTARIO_LARGOPT2',
    
}

#Tokens de simbolos
Simbolos = ['(', ')', '"', ';', ':', '{', '}',',']
Simb_Asig = {
            "=": "ASIGNACION"
        }

#variables globales
global lineas
global columnas
global listado_lexemas
global pdf_error
global pdf_token
global error

#Se les asigna valor a las variables globales
listado_lexemas = []


def Lectura(cadena):
    global lineas
    global columnas
    global listado_lexemas
    global pdf_token
    global pdf_error
    global error

    lineas = 1
    columnas = 1
    error = 0
    indicador = 0
    Cant_tokens = 0
    No_token = 0
    No_error = 1

    #Genera la tabla de tokens en un pdf (Todo aquello que tenga la variable pdf_token)
    pdf_token = FPDF(orientation = 'P', unit = 'mm', format='A4') 
    pdf_token.add_page()
    pdf_token.image('Usac_logo.png', x = 15, y = 17, w = 40, h = 40)
    pdf_token.set_font('Times', 'BI', 14)
    pdf_token.text(x = 57, y = 27, txt = "Universidad de San Carlos de Guatemala")
    pdf_token.text(x = 57, y = 35, txt = "Facultad de Ingeniería")
    pdf_token.text(x = 57, y = 43, txt = "Escuela de Ciencias y Sistemas")
    pdf_token.text(x = 57, y = 51, txt = "Lenguajes Formales y de Programación")
    pdf_token.set_font("Times", 'BI', 14)
    pdf_token.text(x = 20, y = 70, txt = "Nombre: ")
    pdf_token.set_font("Times", 'I', 12)
    pdf_token.text(x = 40, y = 70, txt = "Selim Idair Ergon Castillo")
    pdf_token.set_font("Times", 'BI', 14)
    pdf_token.text(x = 90, y = 70, txt = "Carnet: ")
    pdf_token.set_font("Times", 'I', 12)
    pdf_token.text(x = 110, y = 70, txt = "201801300")
    pdf_token.cell(0, 70, border = False, ln = True)

    pdf_token.set_font('Times', 'Bi', 18)
    pdf_token.cell(w = 130, h = 15, txt = 'Lista de Tokens', border = 1, ln = True, align = 'C', fill = 0)
    pdf_token.set_font('Times', 'BI', 13)
    pdf_token.cell(w = 30, h = 15, txt = 'No. de token', border = 1, align = 'C', fill = 0)
    pdf_token.cell(w = 50, h = 15, txt = 'Tipo de Token', border = 1, align = 'C', fill = 0)
    pdf_token.cell(w = 50, h = 15, txt = 'Lexema', border = 1, ln = True, align = 'C', fill = 0)

    #Genera la tabla de tokens en un pdf (Todo aquello que tenga la variable pdf_token)
    pdf_error = FPDF(orientation = 'P', unit = 'mm', format='A4') 
    pdf_error.add_page()
    pdf_error.image('Usac_logo.png', x = 15, y = 17, w = 40, h = 40)
    pdf_error.set_font('Times', 'BI', 14)
    pdf_error.text(x = 57, y = 27, txt = "Universidad de San Carlos de Guatemala")
    pdf_error.text(x = 57, y = 35, txt = "Facultad de Ingenieria")
    pdf_error.text(x = 57, y = 43, txt = "Escuela de Ciencias y Sistemas")
    pdf_error.text(x = 57, y = 51, txt = "Lenguajes Formales y de Programacion")
    pdf_error.set_font("Times", 'BI', 14)
    pdf_error.text(x = 20, y = 70, txt = "Nombre: ")
    pdf_error.set_font("Times", 'I', 12)
    pdf_error.text(x = 40, y = 70, txt = "Selim Idair Ergon Castillo")
    pdf_error.set_font("Times", 'BI', 14)
    pdf_error.text(x = 90, y = 70, txt = "Carnet: ")
    pdf_error.set_font("Times", 'I', 12)
    pdf_error.text(x = 110, y = 70, txt = "201801300")
    pdf_error.cell(0, 70, border = False, ln = True)

    pdf_error.set_font('Times', 'Bi', 18)
    pdf_error.cell(w = 180, h = 15, txt = 'Lista de Errores', border = 1, ln = True, align = 'C', fill = 0)
    pdf_error.set_font('Times', 'BI', 13)
    pdf_error.cell(w = 36, h = 15, txt = 'No. Error', border = 1, align = 'C', fill = 0)
    pdf_error.cell(w = 36, h = 15, txt = 'Lexema', border = 1, align = 'C', fill = 0)
    pdf_error.cell(w = 36, h = 15, txt = 'Descripcion', border = 1, align = 'C', fill = 0)
    pdf_error.cell(w = 36, h = 15, txt = 'Linea', border = 1, align = 'C', fill = 0)
    pdf_error.cell(w = 36, h = 15, txt = 'Columna', border = 1, ln = True, align = 'C', fill = 0)

    #Lectura de una cadena de texto para detectar que tokens reconoce la interfaz
    while indicador < len(cadena):
        #Si el caracter actual es un simbolo de puntuacion, se le reconoce como un token
        if cadena[indicador] in Simbolos:
            listado_lexemas.append((cadena[indicador], "Simbolo"))
            columnas += 1
            No_token += 1
            #Recopila los tokens SIMBOLOS
            pdf_token.cell(w = 30, h = 9, txt = str(No_token), border = 1, align = 'C', fill = 0)
            pdf_token.cell(w = 50, h = 9, txt = "SIMBOLO", border = 1, align = 'C', fill = 0)
            pdf_token.cell(w = 50, h = 9, txt = cadena[indicador], border = 1, ln = True,align = 'C', fill = 0)
            indicador += 1
            Cant_tokens += 1
            continue

        elif cadena[indicador] in Simb_Asig:
            listado_lexemas.append((cadena[indicador], Simb_Asig[cadena[indicador]]))
            columnas +=1
            No_token += 1
            pdf_token.cell(w = 30, h = 9, txt = str(No_token), border = 1, align = 'C', fill = 0)
            pdf_token.cell(w = 50, h = 9, txt = "SIMBOLO", border = 1, align = 'C', fill = 0)
            pdf_token.cell(w = 50, h = 9, txt = cadena[indicador], border = 1, ln = True, align = 'C', fill = 0)            
            indicador += 1
            Cant_tokens += 1
            continue

        #Si el caracter actual es el $, reconocera la palabra reservada ($set); si no es asi, indicara un error
        if cadena[indicador] == '$':
            palabra = ""
            if cadena[indicador:indicador+4] == '$set':
                while indicador < len(cadena) and cadena[indicador] != ':':
                    palabra += cadena[indicador]
                    indicador += 1
                    columnas +=1
                listado_lexemas.append((palabra, "Palabra Reservada"))
                No_token += 1
                pdf_token.cell(w = 30, h = 9, txt = str(No_token), border = 1, align = 'C', fill = 0)
                pdf_token.cell(w = 50, h = 9, txt = "Palabra Reservada", border = 1, align = 'C', fill = 0)
                pdf_token.cell(w = 50, h = 9, txt = palabra, border = 1, ln = True, align = 'C', fill = 0)
                Cant_tokens +=1
                continue

        #Si el caracter actual es una letra, lee el lexema e identifica si es una palabra reservada o no
        if cadena[indicador].isalpha():
            palabra = ""
            #Si se encuentra el caso de que una variable tenga un numero o guion bajo. Si no lo hay, es una palabra reservada
            while indicador < len(cadena) and (cadena[indicador].isalnum() or cadena[indicador] == "_"):
                palabra += cadena[indicador]
                indicador += 1
                columnas += 1
            if palabra in Sentencias_clave:
                listado_lexemas.append((palabra, Sentencias_clave[palabra]))
                No_token += 1
                pdf_token.cell(w = 30, h = 9, txt = str(No_token), border = 1, align = 'C', fill = 0)
                pdf_token.cell(w = 50, h = 9, txt = "Palabra Reservada", border = 1, align = 'C', fill = 0)
                pdf_token.cell(w = 50, h = 9, txt = palabra, border = 1, ln = True, align = 'C', fill = 0)
                Cant_tokens += 1
            else:
                listado_lexemas.append((palabra, "ID"))
                No_token += 1
                pdf_token.cell(w = 30, h = 9, txt = str(No_token), border = 1, align = 'C', fill = 0)
                pdf_token.cell(w = 50, h = 9, txt = "ID", border = 1, align = 'C', fill = 0)
                pdf_token.cell(w = 50, h = 9, txt = palabra, border = 1, ln = True, align = 'C', fill = 0)
                Cant_tokens += 1
            continue

        #Si el caracter actual es un número, lo reconoce como un digito
        if cadena[indicador].isdigit():
            numero = ""
            while indicador < len(cadena) and cadena[indicador].isdigit():
                numero += cadena[indicador]
                indicador += 1
                columnas += 1
            listado_lexemas.append((numero, "Digito"))
            No_token += 1
            pdf_token.cell(w = 30, h = 9, txt = str(No_token), border = 1, align = 'C', fill = 0)
            pdf_token.cell(w = 50, h = 9, txt = "NUMERO", border = 1, align = 'C', fill = 0)
            pdf_token.cell(w = 50, h = 9, txt = numero, border = 1, ln = True, align = 'C', fill = 0)
            Cant_tokens += 1
            continue

        #Si el caracter actual es un comentario, ignorará la cadena de texto hasta encontrar un salto de linea
        if cadena[indicador:indicador+3] == "---":
            indicador += 3
            while indicador < len(cadena) and cadena[indicador] != '\n':
                indicador += 1
                columnas = 1
            lineas += 1
            continue 

        #Si el caracter actual es un comentario largo, ignorará la cadena de texto hasta encontrar un simbolo de cierre (*/)
        if cadena[indicador:indicador+2] == "/*":
            indicador += 2
            while indicador < len(cadena) and (cadena[indicador:indicador+2] != '*/' or cadena[indicador] == '\n'):
                indicador += 1
                columnas += 1
            continue

        #Si encuentra un */, ignorarlo
        if cadena[indicador:indicador+2] == '*/':
                indicador += 2
                columnas += 2

        if cadena[indicador] == '\n':
            indicador +=1
            columnas = 1
            lineas += 1
        elif cadena[indicador] == '\t':
            indicador +=4
            columnas += 4
        elif cadena[indicador] == ' ':
            indicador += 1
            columnas += 1
        else:
            #Si existe un caracter no reconocible por el sistema, creara la tabla de error
            columnas += 1
            pdf_error.cell(w = 36, h = 9, txt = str(No_error), border = 1, align = 'C', fill = 0)

            if cadena[indicador] == '“' or cadena[indicador] == '”':
                pdf_error.cell(w = 36, h = 9, txt = "\"", border = 1, align = 'C', fill = 0)
            else:
                pdf_error.cell(w = 36, h = 9, txt = cadena[indicador], border = 1, align = 'C', fill = 0)
            pdf_error.cell(w = 36, h = 9, txt = 'Error Léxico', border = 1, align = 'C', fill = 0)
            pdf_error.cell(w = 36, h = 9, txt =str(lineas), border = 1, align = 'C', fill = 0)
            pdf_error.cell(w = 36, h = 9, txt = str(columnas), border = 1, ln = True, align = 'C', fill = 0)
            No_error += 1
            indicador += 1  
            error = 1 

    pdf_token.cell(w=70, h=10, txt = "Cantidad de tokens: "+ str(Cant_tokens))   
    return listado_lexemas

def Tokens():
    global pdf_token
    pdf_token.output('Lista_Tokens.pdf') 

def Errores():
    global pdf_error
    global error
    if error == 0:
        pdf_error.cell(w=70, h=10, txt = "No hay errores léxicos")
        pdf_error.output('Lista_Errores.pdf')
    else:
        pdf_error.output('Lista_Errores.pdf')