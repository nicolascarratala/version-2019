class coche():           #establecemos las propiedades clase coche, su estado,propiedades y comportamiento

    def __init__(self):    #estado inicial o punto de partida de las propiedades, se denomina metodo constructor

      self.largochasis=250
      self.anchochasis=120
      self.__ruedas=4       ##utilizamos __ para encapsular la propiedad y asi no puede ser modificada desde afuera      
      self.enmarcha=False
    ###tiene 4 propiedades####
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        if (self.enmarcha):
            return "el coche esta en marcha"        #usamos def method ya que cuando usamos la clase tenemos q emplear defs y no def defuncion
        else:
            return "el coche esta parado"                   #comportamiento, tiene 2 comportamientos
    def estado(self):
       print("el coche tiene ", self.__ruedas,"ruedas.Un ancho de ", self.anchochasis,"y un largo de ",self.largochasis)
        
micoche=coche()                  #creamos el objeto, instaciamos o ejemplarizamos la clase

print(micoche.arrancar(True))
micoche.estado()
print(".....a continuacion creamos el segudo objeto.....")

micoche2=coche() #creamos segundo objeto
print(micoche2.arrancar(False))
micoche2.ruedas=2
micoche2.estado()
