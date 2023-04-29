from tkinter import Tk
from tkinter import ttk
from tkinter import scrolledtext as scroll
from tkinter import scrolledtext as scroll2
from tkinter import messagebox
from tkinter import filedialog as archivo
from Analizador_lexico import * 
from tkinter import *

class interfaz:
    global activado
    global nuevoarchi
    activado = 0
    nuevoarchi = 0

    def __init__(self):
        #Ventana Principal
        self.ventana = Tk()
        self.ventana.title("Proyecto Final - LFP")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="turquoise4")

        #Posiciona la ventana al centro de la pantalla
        ancho = self.ventana.winfo_screenwidth()
        altura = self.ventana.winfo_screenheight()
        medida1 = round(ancho/2 - 1100/2)
        medida2 = round(altura/2 - 600/2)
        self.ventana.geometry("1100x650"+"+"+str(medida1)+"+"+str(medida2))
        self.Frame1()

        #Barra de herramientas
        lista_menu = Menu(self.ventana)
        self.ventana.config(menu=lista_menu)
        #Opcion de manejo de archivos
        Op_archivo = Menu(lista_menu, tearoff = 0)
        lista_menu.add_cascade(label = "Archivo", menu = Op_archivo)
        Op_archivo.add_command(label = "Nuevo", command = self.Nuevo_archivo)
        Op_archivo.add_command(label = "Abrir", command = self.Abrir_archivo)
        Op_archivo.add_command(label = "Guardar", command = self.Guardar_archivo)
        Op_archivo.add_command(label = "Guardar Como...", command = self.Guardar_ArchivoComo)
        Op_archivo.add_command(label = "Salir", command = self.Despedida)        

        #Opcion de analisis de archivo
        Op_analisis = Menu(lista_menu, tearoff = 0)
        lista_menu.add_cascade(label="Análisis", menu = Op_analisis)
        Op_analisis.add_command(label = "Generar Sentencias MongoDB", command = self.Analizar)

        #Opcion de tokens
        Op_token = Menu(lista_menu, tearoff = 0)
        lista_menu.add_cascade(label="Tokens", menu = Op_token)
        Op_token.add_command(label = "Ver Tokens", command = self.Generar_tokens)
        
        #Opcion de errores
        Op_error = Menu(lista_menu, tearoff = 0)
        lista_menu.add_cascade(label="Errores", menu = Op_error)
        Op_error.add_command(label = "Ver Errores", command = self.Ver_errores)
        global nuevoarchi
        nuevoarchi = 1
        self.ventana.mainloop()

    def Frame1(self):
        self.frame1 = Frame(width=1000, height=600)
        self.frame1.config(bg="DeepSkyBlue2")
        self.frame1.pack(fill="y", expand="True")
        self.frame1.config(bd=20)
        self.frame1.config(relief="ridge")

        label1 = Label(self.frame1, text = "Área de Edición", fg = "lavender", font=("Times New Roman",17,"bold","italic"), bg="steel blue")
        label1.place(x=150,y=30)
        self.scroll = scroll.ScrolledText(self.frame1, width=47, height=30)
        self.scroll.place(x=30,y=80)

        #Separador
        style = ttk.Style()
        style.configure('blue.TSeparator', background='blue')
        ttk.Separator(self.frame1, takefocus=0, orient=VERTICAL, style="blue.TSeparator").place(x=475, y=0, relheight=1)

        label2 = Label(self.frame1, text = "Área de Visualización", fg = "lavender", font=("Times New Roman",17,"bold","italic"), bg="steel blue")
        label2.place(x=600,y=30)
        self.scroll2 = scroll2.ScrolledText(self.frame1, width=47, height=30)
        self.scroll2.place(x=520,y=80)        


    #Sale del programa. ubicado en el boton salir
    def Despedida(self):
        mensaje = messagebox.askyesno("Salir del programa", "¿Desea Salir?")
        if mensaje == True:
            self.ventana.destroy()
            mensaje = messagebox.showinfo("Salida","Pase un buen día...")
        else:
            return      
    
    #Lectura de archivos
    def Abrir_archivo(self):
        global activado
        activado = 1
        linea = ""

        try:
            #Permitira la seleccion de archivos por nombre (.json)
            self.archivo = archivo.askopenfilename(title = 'Seleccionar Archivo', filetypes = [('.json',f'*.json'),('.lfp', f'*.lfp'), ('.txt', f'*.txt')])
            with open(self.archivo, encoding = 'utf-8') as infile: #With, permite establecer un contexto que inicializa un proceso y finaliza extrayendo valores.
                linea = infile.read()
        except: 
            activado = 0
            self.scroll.delete("1.0", END)
            mensaje2 = messagebox.showerror("Error", "Archivo no encontrado...")
            return 

        #Obtendra toda la informacion obtenida en "linea"
        self.texto = linea    

        if self.archivo != '':
                self.scroll.delete("1.0", END)
                nuevo = open(self.archivo, 'r', encoding = 'utf-8')
                contenido = nuevo.read()
                nuevo.close()       
                self.scroll.insert("1.0",contenido)
        
    def Nuevo_archivo(self):
        global activado
        global nuevoarchi
        if activado == 1:
            mensaje3 = messagebox.askyesno("Guardar", "Desea guardar antes de continuar?")
            if mensaje3 == True:
                mensaje3_1 = messagebox.askyesno("Opcion de guardado", "1. Guardar cambios(Yes) \n2. Guardar nuevo archivo(No)")
                if mensaje3_1 == True:
                    self.Guardar_archivo()
                    self.scroll.delete("1.0", END)
                    activado = 0
                else:
                    self.Guardar_ArchivoComo()
                    self.scroll.delete("1.0", END)
                    activado = 0
            else:
                self.scroll.delete("1.0", END)
                activado = 0
        else:
            self.scroll.delete("1.0", END)  
            activado = 0
        nuevoarchi = 1
        

    def Guardar_archivo(self):
        global activado
        if activado == 1:
            archivo = open(self.archivo, "w", encoding="utf-8")
            archivo.write(self.scroll.get("1.0", END))
            archivo.close()
            self.texto = self.scroll.get("1.0", END)
            mensaje4 = messagebox.showinfo("Guardado", "Archivo guardado con éxito...") 
        else:
            mensaje4 = messagebox.showerror("Error", "No es posible realizar algún cambio a un archivo inexistente...")
        
    def Guardar_ArchivoComo(self):
        global activado
        global nuevoarchi
        while activado == 1 or nuevoarchi == 1:
            try:
                self.archivo = archivo.asksaveasfilename(initialdir = "/", title = "Guardar como...", filetypes = [('.json', f'*.json'), ('.lfp', f'*.lfp'),('.txt', f'*.txt')], defaultextension = ".json")
                nuevo = open(self.archivo, 'w', encoding = 'utf-8')
            except FileNotFoundError:
                mensaje6 = messagebox.showerror("Advertencia", "No se ha abierto un archivo a guardar...")
                break
            else:
                nuevo = open(self.archivo, 'w', encoding = 'utf-8')
                nuevo.write(self.scroll.get("1.0", END))
                nuevo.close()   
                doc = open(self.archivo, "r", encoding = "utf-8")
                nuevo_contenido = doc.read()
                doc.close()
                self.scroll.delete("1.0", END)
                self.scroll.insert("1.0", nuevo_contenido)
                self.texto = nuevo_contenido
                mensaje6 = messagebox.showinfo("Archivo guardado", "Archivo guardado con exito...")
                break

        if activado == 0 and nuevoarchi == 0:
            mensaje6 = messagebox.showerror("Advertencia", "No se ha abierto un archivo a guardar...")
        elif activado == 1 and nuevoarchi == 0:
            pass
        elif activado == 0 and nuevoarchi == 1:
            pass
        
        nuevoarchi = 0

    def Analizar(self):
        if activado == 1 or nuevoarchi == 1:
            pass
        if activado == 1 and nuevoarchi == 0:
            pass
        if activado == 0 and nuevoarchi == 1:
            pass
        if activado == 0 and nuevoarchi == 0:    
            mensaje7 = messagebox.showerror("Error", "No existe archivo a analizar...")

    def Generar_tokens(self):
        if activado == 1 and nuevoarchi == 1:
            Lectura(self.texto)
            Tokens()
            mensaje8 = messagebox.showinfo("Éxito", "La tabla de Tokens ha sido creada con éxito...")
        if activado == 1 and nuevoarchi == 0:
            Lectura(self.texto)
            Tokens()
            mensaje8 = messagebox.showinfo("Éxito", "La tabla de Tokens ha sido creada con éxito...")
        if activado == 0 and nuevoarchi == 1:
            Lectura(self.texto)
            Tokens()
            mensaje8 = messagebox.showinfo("Éxito", "La tabla de Tokens ha sido creada con éxito...")
        if activado == 0 and nuevoarchi == 0:    
            mensaje8 = messagebox.showerror("Error", "Se requiere analizar el archivo primero...")

    def Ver_errores(self):
        if activado == 1 and nuevoarchi == 1:
            Lectura(self.texto)
            Errores()
            mensaje9 = messagebox.showinfo("Éxito", "La tabla de errores ha sido creada con éxito...")
        if activado == 1 and nuevoarchi == 0:
            Lectura(self.texto)
            Errores()
            mensaje9 = messagebox.showinfo("Éxito", "La tabla de errores ha sido creada con éxito...")
        if activado == 0 and nuevoarchi == 1:
            Lectura(self.texto)
            Errores()
            mensaje9 = messagebox.showinfo("Éxito", "La tabla de errores ha sido creada con éxito...")
        if activado == 0 and nuevoarchi == 0:    
            mensaje9 = messagebox.showerror("Error", "Se requiere analizar el archivo primero...")

ventana = interfaz()