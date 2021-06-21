import requests


class cotizador:
    __url = None
    __cargar = None
    __cotizacion = None

    def __init__(self):
        self.__url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        self.__cargar = requests.get(self.__url)
        self.__cotizacion = self.__cargar.json()

    def Cotizacion(self):
        cotizacion = self.__cotizacion[0]['casa']['venta']
        cotizacion = cotizacion.replace(',', '.')
        cotizacion = float(cotizacion)
        return cotizacion
