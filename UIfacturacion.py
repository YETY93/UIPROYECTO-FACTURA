#!/usr/bin/python
import sys
from tkinter import *
import tabla1

##### FUNCIONES DE CLICK

def hacer_click():
    try:
        _valor = int (entrada_texto.get())
        comision_1 = 12000
        comision_2 = 14000
        comision_3 = 16000
        comision_4 = 18000
        comision_5 = 21000
        comision_6 = 27000
        comision_7 = 28000
        comision_8 = 30000
        comision_9 = 35000
        
        if (_valor >= 20000 and _valor <= 62338):
            print ("El valor de la comision es de :", comision_1)
            resta_1 = _valor - comision_1
            print("El precio del equipo es: ","\t\t",resta_1)
            
        elif (_valor >= 62339 and _valor <= 93600):
            print ("El valor de la comision es de :", comision_2)
            resta_1 = _valor - comision_2
            print("El precio del equipo es: ","\t\t",resta_1)

        elif (_valor >= 93601 and _valor <= 99999) or (_valor >= 100000 and _valor <= 109200) :
            print ("El valor de la comision es de :", comision_3)
            resta_1 = _valor - comision_3
            print("El precio del equipo es: ","\t\t",resta_1)
            
        elif(_valor >= 109201 and _valor <= 124800):
            print ("El valor de la comision es de :", comision_4)
            resta_1 = _valor - comision_4
            print("El precio del equipo es: ","\t\t",resta_1)
            
        elif(_valor >= 124801 and _valor <= 156000):
            print ("El valor de la comision es de :", comision_5)
            resta_1 = _valor - comision_5
            print("El precio del equipo es: ","\t\t",resta_1)        

        elif(_valor >= 156001 and _valor <= 358800):
            print ("El valor de la comision es de :", comision_6)
            resta_1 = _valor - comision_6
            print("El precio del equipo es: ","\t\t",resta_1)        

        elif(_valor >= 358801 and _valor <= 530400):
            print ("El valor de la comision es de :", comision_7)
            resta_1 = _valor - comision_7
            print("El precio del equipo es: ","\t\t",resta_1)        

        elif(_valor >= 530401 and _valor <= 624000):
            print ("El valor de la comision es de :", comision_8)
            resta_1 = _valor - comision_8
            print("El precio del equipo es: ","\t\t",resta_1)       

        elif(_valor >= 624000 and _valor <= 999999) or  (_valor >= 1000000 and _valor <= 1999999):
            print ("El valor de la comision es de :", comision_9)
            resta_1 = _valor - comision_9
            print("El precio del equipo es: ","\t\t",resta_1)
            
        _valor = resta_1
        etiqueta.config(text = _valor)
    except ValueError:
        etiqueta.config(text="Introduce un \n valor numerico")

    except UnboundLocalError:
        etiqueta.config(text="Introduce un \n valor > 20000")

def hacer_click2():
    try:
        _valor2 = int (entrada_texto2.get())
        comision_1 = 12000
        comision_2 = 14000
        comision_3 = 16000
        comision_4 = 18000
        comision_5 = 21000
        comision_6 = 27000
        comision_7 = 28000
        comision_8 = 30000
        comision_9 = 35000
        
        if (_valor2 >= 20000 and _valor2 <= 62338):
            print ("El valor de la comision es de :", comision_1)
            resta_2 = _valor2 - comision_1
            print("El precio del equipo es: ","\t\t",resta_2)
        elif (_valor2 >= 62339 and _valor2 <= 93600):
            print ("El valor de la comision es de :", comision_2)
            resta_2 = _valor2 - comision_2
            print("El precio del equipo es: ","\t\t",resta_2)

        elif (_valor2 >= 93601 and _valor2 <= 99999) or (_valor2 >= 100000 and _valor2 <= 109200) :
            print ("El valor de la comision es de :", comision_3)
            resta_2 = _valor2 - comision_3
            print("El precio del equipo es: ","\t\t",resta_2)
            
        elif(_valor2 >= 109201 and _valor2 <= 124800):
            print ("El valor de la comision es de :", comision_4)
            resta_2 = _valor2 - comision_4
            print("El precio del equipo es: ","\t\t",resta_2)
            
        elif(_valor2 >= 124801 and _valor2 <= 156000):
            print ("El valor de la comision es de :", comision_5)
            resta_2 = _valor2 - comision_5
            print("El precio del equipo es: ","\t\t",resta_2)        

        elif(_valor2 >= 156001 and _valor2 <= 358800):
            print ("El valor de la comision es de :", comision_6)
            resta_2 = _valor2 - comision_6
            print("El precio del equipo es: ","\t\t",resta_2)        

        elif(_valor2 >= 358801 and _valor2 <= 530400):
            print ("El valor de la comision es de :", comision_7)
            resta_2 = _valor2 - comision_7
            print("El precio del equipo es: ","\t\t",resta_2)        

        elif(_valor2 >= 530401 and _valor2 <= 624000):
            print ("El valor de la comision es de :", comision_8)
            resta_2 = _valor2 - comision_8
            print("El precio del equipo es: ","\t\t",resta_2)       

        elif(_valor2 >= 624000 and _valor2 <= 999999) or  (_valor2 >= 1000000 and _valor2 <= 1999999):
            print ("El valor de la comision es de :", comision_9)
            resta_2 = _valor2 - comision_9
            print("El precio del equipo es: ","\t\t",resta_2)
            
        _valor2 = resta_2
        etiqueta4.config(text = _valor2)
    except ValueError:
        etiqueta4.config(text="Introduce un \n valor numerico")

    except UnboundLocalError:
        etiqueta4.config(text="Introduce un \n valor > 20000")
        

def hacer_click3():
    try:
        _valor3 = int (entrada_texto3.get())
        comision_1 = 12000
        comision_2 = 14000
        comision_3 = 16000
        comision_4 = 18000
        comision_5 = 21000
        comision_6 = 27000
        comision_7 = 28000
        comision_8 = 30000
        comision_9 = 35000
        
        if (_valor3 >= 20000 and _valor3 <= 62338):
            print ("El valor de la comision es de :", comision_1)
            resta_3 = _valor3 - comision_1
            print("El precio del equipo es: ","\t\t",resta_3)
        elif (_valor3 >= 62339 and _valor3 <= 93600):
            print ("El valor de la comision es de :", comision_2)
            resta_3 = _valor3 - comision_2
            print("El precio del equipo es: ","\t\t",resta_3)

        elif (_valor3 >= 93601 and _valor3 <= 99999) or (_valor3 >= 100000 and _valor3 <= 109200) :
            print ("El valor de la comision es de :", comision_3)
            resta_3 = _valor3 - comision_3
            print("El precio del equipo es: ","\t\t",resta_3)
            
        elif(_valor3 >= 109201 and _valor3 <= 124800):
            print ("El valor de la comision es de :", comision_4)
            resta_3 = _valor3 - comision_4
            print("El precio del equipo es: ","\t\t",resta_3)
            
        elif(_valor3 >= 124801 and _valor3 <= 156000):
            print ("El valor de la comision es de :", comision_5)
            resta_3 = _valor3 - comision_5
            print("El precio del equipo es: ","\t\t",resta_3)        

        elif(_valor3 >= 156001 and _valor3 <= 358800):
            print ("El valor de la comision es de :", comision_6)
            resta_3 = _valor3 - comision_6
            print("El precio del equipo es: ","\t\t",resta_3)        

        elif(_valor3 >= 358801 and _valor3 <= 530400):
            print ("El valor de la comision es de :", comision_7)
            resta_3 = _valor3 - comision_7
            print("El precio del equipo es: ","\t\t",resta_3)        

        elif(_valor3 >= 530401 and _valor3 <= 624000):
            print ("El valor de la comision es de :", comision_8)
            resta_3 = _valor3 - comision_8
            print("El precio del equipo es: ","\t\t",resta_3)       

        elif(_valor3 >= 624000 and _valor3 <= 999999) or  (_valor3 >= 1000000 and _valor3 <= 1999999):
            print ("El valor de la comision es de :", comision_9)
            resta_3 = _valor3 - comision_9
            print("El precio del equipo es: ","\t\t",resta_3)
            
        _valor3 = resta_3
        etiqueta7.config(text = _valor3)
    except ValueError:
        etiqueta7.config(text="Introduce un \n valor numerico")
    except UnboundLocalError:
        etiqueta7.config(text="Introduce un \n valor > 20000")   
def hacer_click4():
    try:
        _valor4 = int (entrada_texto4.get())
        comision_1 = 12000
        comision_2 = 14000
        comision_3 = 16000
        comision_4 = 18000
        comision_5 = 21000
        comision_6 = 27000
        comision_7 = 28000
        comision_8 = 30000
        comision_9 = 35000
        
        if (_valor4 >= 20000 and _valor4 <= 62338):
            print ("El valor de la comision es de :", comision_1)
            resta_4 = _valor4 - comision_1
            print("El precio del equipo es: ","\t\t",resta_4)
        elif (_valor4 >= 62339 and _valor4 <= 93600):
            print ("El valor de la comision es de :", comision_2)
            resta_4 = _valor4 - comision_2
            print("El precio del equipo es: ","\t\t",resta_4)

        elif (_valor4 >= 93601 and _valor4 <= 99999) or (_valor4 >= 100000 and _valor4 <= 109200) :
            print ("El valor de la comision es de :", comision_3)
            resta_4 = _valor4 - comision_3
            print("El precio del equipo es: ","\t\t",resta_4)
            
        elif(_valor4 >= 109201 and _valor4 <= 124800):
            print ("El valor de la comision es de :", comision_4)
            resta_4 = _valor4 - comision_4
            print("El precio del equipo es: ","\t\t",resta_4)
            
        elif(_valor4 >= 124801 and _valor4 <= 156000):
            print ("El valor de la comision es de :", comision_5)
            resta_4 = _valor4 - comision_5
            print("El precio del equipo es: ","\t\t",resta_4)        

        elif(_valor4 >= 156001 and _valor4 <= 358800):
            print ("El valor de la comision es de :", comision_6)
            resta_4 = _valor4 - comision_6
            print("El precio del equipo es: ","\t\t",resta_4)        

        elif(_valor4 >= 358801 and _valor4 <= 530400):
            print ("El valor de la comision es de :", comision_7)
            resta_4 = _valor4 - comision_7
            print("El precio del equipo es: ","\t\t",resta_4)        

        elif(_valor4 >= 530401 and _valor4 <= 624000):
            print ("El valor de la comision es de :", comision_8)
            resta_4 = _valor4 - comision_8
            print("El precio del equipo es: ","\t\t",resta_4)       

        elif(_valor4 >= 624000 and _valor4 <= 999999) or  (_valor4 >= 1000000 and _valor4 <= 1999999):
            print ("El valor de la comision es de :", comision_9)
            resta_4 = _valor4 - comision_9
            print("El precio del equipo es: ","\t\t",resta_4)


        _valor4 = (resta_4 )
        etiqueta9.config(text = _valor4)
        
    except ValueError:
        etiqueta9.config(text="Introduce un \n valor numerico")

    except UnboundLocalError:
        etiqueta9.config(text="Introduce un \n valor > 20000")

#### FUNCION PARA SUMAR EL VALOR FINAL

def Valor_Total():
    _valor =  int (entrada_texto.get())
    _valor2 = int (entrada_texto2.get())
    _valor3 = int (entrada_texto3.get())
    _valor4 = int (entrada_texto4.get())
    
    comision_1 = 12000
    comision_2 = 14000
    comision_3 = 16000
    comision_4 = 18000
    comision_5 = 21000
    comision_6 = 27000
    comision_7 = 28000
    comision_8 = 30000
    comision_9 = 35000

    
####### VALOR 
    if (_valor >= 20000 and _valor <= 62338):
        resta_1 = _valor - comision_1
        
    elif (_valor >= 62339 and _valor <= 93600):
        resta_1 = _valor - comision_2

    elif (_valor >= 93601 and _valor <= 99999) or (_valor >= 100000 and _valor <= 109200) :
        resta_1 = _valor - comision_3
        
    elif(_valor >= 109201 and _valor <= 124800):
        resta_1 = _valor - comision_4
        
    elif(_valor >= 124801 and _valor <= 156000):
        resta_1 = _valor - comision_5
       
    elif(_valor >= 156001 and _valor <= 358800):
        resta_1 = _valor - comision_6
       
    elif(_valor >= 358801 and _valor <= 530400):
        resta_1 = _valor - comision_7
      
    elif(_valor >= 530401 and _valor <= 624000):
        resta_1 = _valor - comision_8
    
    elif(_valor >= 624000 and _valor <= 999999) or  (_valor >= 1000000 and _valor <= 1999999):
        resta_1 = _valor - comision_9

    _valor = resta_1

######### DECLARACION DE IVA
    
    iva1 = int((_valor * 0.16) / 1.16)   

    sub_total1 = (_valor - iva1)

########### VALOR 2
    if (_valor2 >= 20000 and _valor2 <= 62338):
        resta_2 = _valor2 - comision_1
        
    elif (_valor2 >= 62339 and _valor2 <= 93600):
        resta_2 = _valor2 - comision_2

    elif (_valor2 >= 93601 and _valor2 <= 99999) or (_valor2 >= 100000 and _valor2 <= 109200) :
        resta_2 = _valor2 - comision_3
        
    elif(_valor2 >= 109201 and _valor2 <= 124800):
        resta_2 = _valor2 - comision_4
        
    elif(_valor2 >= 124801 and _valor2 <= 156000):
        resta_2 = _valor2 - comision_5
       
    elif(_valor2 >= 156001 and _valor2 <= 358800):
        resta_2 = _valor2 - comision_6
       
    elif(_valor2 >= 358801 and _valor2 <= 530400):
        resta_2 = _valor2 - comision_7
      
    elif(_valor2 >= 530401 and _valor2 <= 624000):
        resta_2 = _valor2 - comision_8
    
    elif(_valor2 >= 624000 and _valor2 <= 999999) or  (_valor2 >= 1000000 and _valor2 <= 1999999):
        resta_2 = _valor2 - comision_9
    

    _valor2 = resta_2

    suma2 = (_valor + _valor2)

######## IVA Y SUBTOTAL DE SUMA 2
    
    iva2 = int((suma2 * 0.16) / 1.16)   

    sub_total2 = (suma2 - iva2)
    
########### VALOR 3
    if (_valor3 >= 20000 and _valor3 <= 62338):
        resta_3 = _valor3 - comision_1
        
    elif (_valor3 >= 62339 and _valor3 <= 93600):
        resta_3 = _valor3 - comision_2

    elif (_valor3 >= 93601 and _valor3 <= 99999) or (_valor3 >= 100000 and _valor3 <= 109200) :
        resta_3 = _valor3 - comision_3
        
    elif(_valor3 >= 109201 and _valor3 <= 124800):
        resta_3 = _valor3 - comision_4
        
    elif(_valor3 >= 124801 and _valor3 <= 156000):
        resta_3 = _valor3 - comision_5
       
    elif(_valor3 >= 156001 and _valor3 <= 358800):
        resta_3 = _valor3 - comision_6
       
    elif(_valor3 >= 358801 and _valor3 <= 530400):
        resta_3 = _valor3 - comision_7
      
    elif(_valor3 >= 530401 and _valor3 <= 624000):
        resta_3 = _valor3 - comision_8
    
    elif(_valor3 >= 624000 and _valor3 <= 999999) or  (_valor3 >= 1000000 and _valor3 <= 1999999):
        resta_3 = _valor3 - comision_9

    _valor3 = resta_3


    suma3 = (suma2 + _valor3)

######## IVA Y SUBTOTAL DE SUMA 2
    
    iva3 = int((suma3 * 0.16) / 1.16)   

    sub_total3 = (suma3 - iva3)
    

######### VALOR 4
    
    if (_valor4 >= 20000 and _valor4 <= 62338):
        resta_4 = _valor4 - comision_1
        
    elif (_valor4 >= 62339 and _valor4 <= 93600):
        resta_4 = _valor4 - comision_2

    elif (_valor4 >= 93601 and _valor4 <= 99999) or (_valor4 >= 100000 and _valor4 <= 109200) :
        resta_4 = _valor4 - comision_3
       
    elif(_valor4 >= 109201 and _valor4 <= 124800):
        resta_4 = _valor4 - comision_4
        
    elif(_valor4 >= 124801 and _valor4 <= 156000):
        resta_4 = _valor4 - comision_5   

    elif(_valor4 >= 156001 and _valor4 <= 358800):
        resta_4 = _valor4 - comision_6     

    elif(_valor4 >= 358801 and _valor4 <= 530400):
        resta_4 = _valor4 - comision_7    

    elif(_valor4 >= 530401 and _valor4 <= 624000):
        resta_4 = _valor4 - comision_8
    
    elif(_valor4 >= 624000 and _valor4 <= 999999) or  (_valor4 >= 1000000 and _valor4 <= 1999999):
        resta_4 = _valor4 - comision_9


    suma_total= (resta_4 + resta_3 + resta_2 + resta_1)


    _valor4 = (suma_total )

    etiqueta11.config(text = _valor4)  

    
    suma4 = (suma3 + _valor4)

######## IVA Y SUBTOTAL DE SUMA 2
    
    iva4 = int((suma4 * 0.16) / 1.16)   

    sub_total4 = (suma4 - iva4)


      

#####################################################################

app = Tk()
app.title("FACTURACION A SUB")
app.geometry("1150x450+50+50")
app.config(bg="brown1")

imagen = PhotoImage(file="logo.gif")
my_image = Label(app, image=imagen).place(x=950, y = 10)

### MENU PRINCIPAL
menu_principal = Menu(app)


### SUB MENU
sub_menu = Menu(menu_principal, tearoff=0)

### ARCHIVOS DEL SUB MENU
sub_menu.add_command(label="Cerrar aplicacion", command=app.destroy)

### OPCIONES ARCHIVOS DEL SUB MENU
menu_principal.add_cascade(label="Archivo", menu=sub_menu)

app.config(menu=menu_principal)

#vp = VENTANA PRINCIPAL
vp = Frame(app)
vp.grid(column=1, row=1, padx = (50,50), pady = (10, 10))
vp.columnconfigure(0, weight=5)
vp.rowconfigure(0, weight=5)

### ETIQUETAS DE NOMBRE VALOR

etiqueta = Label(vp, text="        Valor")
etiqueta.grid(column=7, row=1, sticky=(W,E))

etiqueta3 = Label(vp, text="")
etiqueta3.grid(column=4, row=2, sticky=(W,E))

etiqueta4 = Label(vp, text="        Valor")
etiqueta4.grid(column=7, row=3, sticky=(W,E))

etiqueta6= Label(vp, text="")
etiqueta6.grid(column=4, row=4, sticky=(W,E))

etiqueta7 = Label(vp, text="        Valor")
etiqueta7.grid(column=7, row=5, sticky=(W,E))

etiqueta8 = Label(vp, text="")
etiqueta8.grid(column=4, row=6, sticky=(W,E))

etiqueta9 = Label(vp, text="        Valor")
etiqueta9.grid(column=7, row=7, sticky=(W,E))

etiqueta11 = Label(vp, text="        TOTALhhh")
etiqueta11.grid(column=7, row=10, sticky=(W,E))

etiqueta15 = Label(vp, text="Sub Total")
etiqueta15.grid(column=11, row=1, sticky=(W,E))

etiqueta19 = Label(vp, text="   Iva   ")
etiqueta19.grid(column=15, row=1, sticky=(W,E))

etiqueta20 = Label(vp, text="   Total   ")
etiqueta20.grid(column=19, row=1, sticky=(W,E))

###ETIQUETAS DE SEPARACION

etiqueta5 = Label(vp, text="")

etiqueta5.grid(column=2, row=1 )

etiqueta5 = Label(vp, text="")
etiqueta5.grid(column=4, row=1 )

etiqueta5 = Label(vp, text="")
etiqueta5.grid(column=6, row=1 )

etiqueta10 = Label(vp, text="")
etiqueta10.grid(column=8, row=1 )

etiqueta12 = Label(vp, text="")
etiqueta12.grid(column=5, row=9 )

etiqueta13 = Label(vp, text="")
etiqueta13.grid(column=8, row=1 )

etiqueta14 = Label(vp, text="")
etiqueta14.grid(column=10, row=1 )

etiqueta15 = Label(vp, text="")
etiqueta15.grid(column=12, row=1 )

etiqueta16 = Label(vp, text="")
etiqueta16.grid(column=14, row=1 )

etiqueta17 = Label(vp, text="")
etiqueta17.grid(column=16, row=1 )

etiqueta18 = Label(vp, text="")
etiqueta18.grid(column=16, row=1 )


### ETIQUETAS DE INTRODUCION DE TEXTOS

etiqueta2 = Label(vp, text="Introduce el valor")
etiqueta2.grid(column=1, row=1)

etiqueta2 = Label(vp, text="Introduce el valor")
etiqueta2.grid(column=1, row=3)

etiqueta2 = Label(vp, text="Introduce el valor")
etiqueta2.grid(column=1, row=5)

etiqueta2 = Label(vp, text="Introduce el valor")
etiqueta2.grid(column=1, row=7)

etiqueta2 = Label(vp, text="Suma totalizada")
etiqueta2.grid(column=1, row=10)


### BOTENES DE NOMBRE VALOR COMERCIAL

boton = Button(vp, text = "Valor comercial", command= hacer_click)
boton.grid(column=5, row=1)

boton2 = Button(vp, text = "Valor comercial", command= hacer_click2)
boton2.grid(column=5, row=3)

boton3 = Button(vp, text = "Valor comercial", command= hacer_click3)
boton3.grid(column=5, row=5)

boton4 = Button(vp, text = "Valor comercial" , command= hacer_click4)
boton4.grid(column=5, row=7)

boton5 = Button(vp, text = "Valor Total", command= Valor_Total)
boton5.grid(column=5, row=10)


## DECLARACION DEL VALOR TOTAL
boton6 = Button(vp, text = "    IVA   ", command= Valor_Total)
boton6.grid(column=13, row=1)

boton7 = Button(vp, text = "Sub TOTAL", command= Valor_Total)
boton7.grid(column=9, row=1)

boton8 = Button(vp, text = "TOTAL 1", command= Valor_Total)
boton8.grid(column=17, row=1)

## ENTADAS CON TEXTO VARIABLES


valor=("")
entrada_texto =  Entry(vp, width=10, textvariable = valor)
entrada_texto.grid(column=3, row=1)

valor2=("")
entrada_texto2 = Entry(vp, width=10, textvariable = valor2)
entrada_texto2.grid(column=3, row=3)

valor3=("")
entrada_texto3 = Entry(vp, width=10, textvariable = valor3)
entrada_texto3.grid(column=3, row=5)

valor4=("")
entrada_texto4 = Entry(vp, width=10, textvariable = valor4)
entrada_texto4.grid(column=3, row=7)



app.mainloop()



