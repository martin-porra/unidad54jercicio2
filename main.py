from tkinter import *
from tkinter import ttk, messagebox
from  pagina import cotizador


class Aplicacion():
    __ventana = None
    __dolares = None
    __pesos = None
    __cotizador = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('300x100')
        self.__ventana.title('Conversor de moneda')
        self.__ventana.resizable(0, 0)

        self.__dolares = StringVar()
        self.__pesos = StringVar()
        self.__cotizador = cotizador()

        self.frame = ttk.Frame(self.__ventana, borderwidth=2, relief='groove', padding=(15,15))
        self.frame.grid(column=0, row=0)
        self.label1 = ttk.Label(self.frame, text='dólares').grid(column=2, row=0)
        self.label2 = ttk.Label(self.frame, text='pesos').grid(column=2, row=1)
        self.label3 = ttk.Label(self.frame, text='es equivalente a').grid(column=0, row=1)
        self.label4 = ttk.Label(self.frame, textvariable=self.__pesos).grid(column=1, row=1)
        self.__dolaresen = ttk.Entry(self.frame, textvariable=self.__dolares, width=18)
        self.boton = ttk.Button(self.frame, text="Salir", command=self.__ventana.destroy).grid(column=2, row=2)
        self.__dolaresen.grid(column=1, row=0)
        self.__dolares.trace('w', self.calcular)
        self.__dolaresen.focus()
        self.__ventana.mainloop()

    def calcular(self, *args):
        if self.__dolaresen.get() != '':
            try:
                ventaofi = self.__cotizador.Cotizacion()
                dolares = float(self.__dolaresen.get())
                pesos = ventaofi * dolares
                self.__pesos.set(pesos)
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')


if __name__ == '__main__':
 miapp = Aplicacion()
