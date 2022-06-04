from tkinter import *
from tkinter import ttk




#lista de cores
cor1 = '#3b3b3b' #preto
cor2 = '#feffff' #branco
cor3 = '#38576b' #Azul
cor4 = '#ECEFF1' #Cinza
cor5 = '#FFAB40' #Laranja

#dimensão da janela
dimx = 256
dimy = 384

main_menu = Tk() #Inicio da aplicação

ultima_operacao = ''
lista_valores_display = ''
valor_exibido_display = StringVar()

#funções
def exibir_valores(click): 

    global lista_valores_display 

    if len(lista_valores_display) == 13:
        valor_exibido_display.set(lista_valores_display)
        return

    lista_valores_display += str(click)
    #passar para variável e ser exibido.
    valor_exibido_display.set(lista_valores_display)

def exibir_operacoes(click): 
    global ultima_operacao
    global lista_valores_display

    if len(lista_valores_display) == 13:
        valor_exibido_display.set(lista_valores_display)
        return

    if ultima_operacao != str(click):
        lista_valores_display += str(click)
        ultima_operacao = str(click)
        #passar para variável e ser exibido.
        valor_exibido_display.set(lista_valores_display)

    else: 
        valor_exibido_display.set(lista_valores_display)

def calcular():
    global lista_valores_display
    global ultima_operacao

    ultima_operacao = ''

    if not lista_valores_display:
        valor_exibido_display.set(lista_valores_display)
        return

    try:
        resultado = eval(lista_valores_display)
    except SyntaxError:
        valor_exibido_display.set('ERROR')
        lista_valores_display = ''
    else: 
        valor_exibido_display.set(resultado)
        lista_valores_display = str(resultado)
    

def limpar_display():
    global lista_valores_display
    lista_valores_display = ''
    valor_exibido_display.set(lista_valores_display)




#Centralizando a aplicação ao inciar.
largura_tela = main_menu.winfo_screenwidth()
altura_tela = main_menu.winfo_screenheight()
#Cálculo da centralização
centralizarx = largura_tela/2 - dimx/2
centralizary = altura_tela/2 - dimy/2
main_menu.geometry('%dx%d+%d+%d' % (dimx, dimy, centralizarx, centralizary))


#configurações de estilo
main_menu.title('Calculadora')
main_menu.iconbitmap('calculator_icon-icons.com_72046.ico')
main_menu.config(bg=cor1)

#Conteúdo da calculadora
#Grid
frame_display = Frame(main_menu, width=dimx, height=64, bg=cor3)
frame_display.grid(row=0, column=0)

frame_botao = Frame(main_menu, width=dimx, height=320)
frame_botao.grid(row=1, column=0)

#Label
display_label = Label(frame_display, textvariable=valor_exibido_display, bg=cor3, fg=cor2, font='Alarm 25 bold', relief=SOLID, bd=2, anchor=E, justify=RIGHT, padx=8).place(x=0, y=0, width=dimx, height=64)

#botões fileira 1
botao1 = Button(frame_botao, command=limpar_display, text='C', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=0, y=0, width=128, height=64)
botao2 = Button(frame_botao, command=lambda: exibir_operacoes('%'), text='%', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=128, y=0, width=64, height=64)
botao3 = Button(frame_botao, command=lambda: exibir_operacoes('/'), text='/', bg=cor5, fg=cor2, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=192, y=0, width=64, height=64)
#botões fileira 2
botao4 = Button(frame_botao, command=lambda: exibir_valores('7'), text='7', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=0, y=64, width=64, height=64)
botao5 = Button(frame_botao, command=lambda: exibir_valores('8'), text='8', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=64, y=64, width=64, height=64)
botao6 = Button(frame_botao, command=lambda: exibir_valores('9'), text='9', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=128, y=64, width=64, height=64)
botao7 = Button(frame_botao, command=lambda: exibir_operacoes('*'), text='*', bg=cor5, fg=cor2, font='Ivy 30 bold', relief=RAISED, overrelief=RIDGE).place(x=192, y=64, width=64, height=64)
#botões fileira 3
botao4 = Button(frame_botao, command=lambda: exibir_valores('4'), text='4', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=0, y=128, width=64, height=64)
botao5 = Button(frame_botao, command=lambda: exibir_valores('5'), text='5', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=64, y=128, width=64, height=64)
botao6 = Button(frame_botao, command=lambda: exibir_valores('6'), text='6', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=128, y=128, width=64, height=64)
botao7 = Button(frame_botao, command=lambda: exibir_operacoes('-'), text='-', bg=cor5, fg=cor2, font='Ivy 30 bold', relief=RAISED, overrelief=RIDGE).place(x=192, y=128, width=64, height=64)
#botões fileira 4
botao4 = Button(frame_botao, command=lambda: exibir_valores('1'), text='1', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=0, y=192, width=64, height=64)
botao5 = Button(frame_botao, command=lambda: exibir_valores('2'), text='2', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=64, y=192, width=64, height=64)
botao6 = Button(frame_botao, command=lambda: exibir_valores('3'), text='3', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=128, y=192, width=64, height=64)
botao7 = Button(frame_botao, command=lambda: exibir_operacoes('+'), text='+', bg=cor5, fg=cor2, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=192, y=192, width=64, height=64)
#botões fileira 5
botao1 = Button(frame_botao, command=lambda: exibir_valores('0'), text='0', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=0, y=256, width=128, height=64)
botao2 = Button(frame_botao, command=lambda: exibir_operacoes('.'), text='.', bg=cor4, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=128, y=256, width=64, height=64)
botao3 = Button(frame_botao, command=calcular, text='=', bg=cor5, fg=cor2, font='Ivy 20 bold', relief=RAISED, overrelief=RIDGE).place(x=192, y=256, width=64, height=64)


main_menu.mainloop() #Fim da aplicação