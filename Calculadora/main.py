
from tkinter import *
from tkinter import ttk


#cores
cor1 = "#050505" #preta
cor2 = "#f6f5f7" #branca
cor3 = "#4b078f" #roxa
cor4 = "#495eeb" #azul claro
cor5 = "#f79102" #laranja

janela = Tk()

janela.title("Calculadora")
janela.geometry("235x320")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=60, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width= 235, height=258)
frame_corpo.grid(row=1, column=0)

#variavel que recebe toos os valores 
todos_valores = ""

#Criando label 
valor_texto = StringVar()

#funcação para entrada de valores

def entar_varlores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    #pasando os valores para tela
    valor_texto.set(todos_valores)


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)
    

def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")


app_label= Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 16'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# cirando botoes
botao_clear = Button(frame_corpo, command=limpar_tela,text="C", width=9, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_clear.place(x=0, y=0)
botao_porcem = Button(frame_corpo, command= lambda: entar_varlores('%'), text="%", width=3, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_porcem.place(x=126, y=0)
botao_divi = Button(frame_corpo, command= lambda: entar_varlores('/'),text="/", width=3, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_divi.place(x=180, y=0)

botao7 = Button(frame_corpo, command= lambda: entar_varlores('7') ,text="7", width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao7.place(x=0, y=52)
botao8= Button(frame_corpo, command= lambda: entar_varlores('8'),text="8", width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao8.place(x=65, y=52)
botao9= Button(frame_corpo, command= lambda: entar_varlores('9'),text="9", width=3, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao9.place(x=128, y=52)
botao_multiplicar= Button(frame_corpo, command= lambda: entar_varlores('*'),text="*", width=3, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_multiplicar.place(x=180, y=52)

botao7 = Button(frame_corpo, command= lambda: entar_varlores('4'),text="4", width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao7.place(x=0, y=104)
botao8= Button(frame_corpo, command= lambda: entar_varlores('5'),text="5", width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao8.place(x=65, y=104)
botao9= Button(frame_corpo, command= lambda: entar_varlores('6'),text="6", width=3, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao9.place(x=128, y=104)
botao_multiplicar= Button(frame_corpo, command= lambda: entar_varlores('-'),text="-", width=3, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_multiplicar.place(x=180, y=104)

botao7 = Button(frame_corpo, command= lambda: entar_varlores('1'),text="1", width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao7.place(x=0, y=156)
botao8= Button(frame_corpo, command= lambda: entar_varlores('2'),text="2", width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao8.place(x=65, y=156)
botao9= Button(frame_corpo, command= lambda: entar_varlores('3'),text="3", width=3, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao9.place(x=128, y=156)
botao_multiplicar= Button(frame_corpo, command= lambda: entar_varlores('+'),text="+", width=3, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_multiplicar.place(x=180, y=155)

botao0= Button(frame_corpo, command= lambda: entar_varlores('0'), text="0", width=9, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao0.place(x=0, y=208)
botao_ponto= Button(frame_corpo, command= lambda: entar_varlores('.'),text=".", width=3, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_ponto.place(x=128, y=208)
botao_igual = Button(frame_corpo, command=calcular,text="=", width=3, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botao_igual.place(x=180, y=208)

janela.mainloop()