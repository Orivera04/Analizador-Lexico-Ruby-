import sys
import re
from tkinter import *
#from tkinter import tkFileDialog

from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QFileDialog
from PyQt5 import uic
from Resaltador import *
from Operaciones import *




def AbrirArchivo(self,textEdit):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self, "Abra un archivo", "","Archivo de texto (*.txt);;Ruby Files (*.rb)", options=options)
    try:
        Cadena = ""
        Archivo = open(fileName,'r')
        Datos = list(Archivo.read().split("\n"))
        for i in Datos:
            Cadena = Cadena+"\n" + i
    except Exception as r:
        print("Error: ",r)
    finally:
        Archivo.close()

    textEdit.textEdit.setPlainText(Cadena + "\n")
    """
        try:
            Archivo = open(Nombre,'r')
            Datos = Archivo.read().split("\n")
            for i in Datos:
                Texto.insert(END,i + "\n")
        except:
            print("Error: ")
        finally:
            Archivo.close()
        """

def TextoCambio(Texto,TablaTokens,EtiquetaIdenti,EtiquetaOpera,EtiquetaReser,EtiquetaDelim,EtiquetaErr):

                TablaTokens.setRowCount(0)                
                Instancia = Tabla()                                                                                                   
                Cadenas = Texto.toPlainText().split("\n")

                Contador = 0
                ContadorColumnas = 0
                Tokens={"Identificadores":0,"Operadores":0,"Reservadas":0,'Delimitadores':0,"Errores":0}

                for I in Cadenas:
                        Contador = Contador + 1                                
                        if (I!= "") :
                            if (I.find("#") == -1):
                                if  (Instancia.GenerarToken("Identificador",I,0) == 1):
                                    ContadorColumnas = -1
                                    Objeto = Instancia.GenerarToken("Identificador",I,1)
                                    for Coincidencias in  Objeto["Identificador"]:
                                        ContadorColumnas = ContadorColumnas + 1
                                        Expresion1 = len(re.findall("\\balias\\b|\\band\\b|\\bbreak\\b|\\bcase\\b|\\bclass\\b|\\bdef\\b|\\bdefined\\b|\\bdo\\b|\\belse\\b|\\belsif\\b|\\bend\\b|\\bensure\\b|\\bfalse\\b|\\btrue\\b|\\bfor\\b|\\bif\\b|\\bin\\b|\\bmodule\\b|\\bnext\\b|\\bnil\\b|\\bnot\\b|\\bor\\b|\\bredo\\b|\\brescue\\b|\\bretry\\b|\\breturn\\b|\\bself\\b|\\bsuper\\b|\\bthen\\b|\\bundef\\b|\\bunless\\b|\\buntil\\b|\\bwhile\\b|\\bwhen\\b|\\byield\\b|\\b_FILE_\\b|\\b_LINE_\\b", Coincidencias))
                                        Expresion3 = len(re.findall("#[^\n]+",Coincidencias))
                                        CadenaEvaluar = ("\"\s{0,10}"+Coincidencias+"\s{0,10}\"")
                                        Expresion2 = len(re.findall(CadenaEvaluar,I))
                                        if(Expresion1 == 0  and Expresion3 == 0  and Expresion2 == 0):
                                                FilaContador = TablaTokens.rowCount()
                                                TablaTokens.insertRow(FilaContador)
                                                TablaTokens.setItem(FilaContador , 0,QTableWidgetItem("Identificador"))
                                                TablaTokens.setItem(FilaContador , 1,QTableWidgetItem(Coincidencias))
                                                TablaTokens.setItem(FilaContador , 2,QTableWidgetItem(str(Contador)))
                                                TablaTokens.setItem(FilaContador , 3,QTableWidgetItem(str(Objeto['Columnas'][ContadorColumnas]+1)))
                                                TablaTokens.setItem(FilaContador , 4,QTableWidgetItem(str(Objeto['Informacion'])))
                                                Tokens['Identificadores'] = Tokens['Identificadores'] +1
                                        elif(Expresion2 >= 1):
                                                FilaContador = TablaTokens.rowCount()
                                                TablaTokens.insertRow(FilaContador)
                                                TablaTokens.setItem(FilaContador, 0, QTableWidgetItem("Otros (Cadena)"))
                                                TablaTokens.setItem(FilaContador, 1, QTableWidgetItem(Coincidencias))
                                                TablaTokens.setItem(FilaContador, 2, QTableWidgetItem(str(Contador)))
                                                TablaTokens.setItem(FilaContador, 3, QTableWidgetItem(str(Objeto['Columnas'][ContadorColumnas] + 1)))
                                                TablaTokens.setItem(FilaContador, 4, QTableWidgetItem("Cadena de Texto"))
                            else:
                                FilaContador = TablaTokens.rowCount()
                                TablaTokens.insertRow(FilaContador)
                                TablaTokens.setItem(FilaContador, 0, QTableWidgetItem("Otros"))
                                TablaTokens.setItem(FilaContador, 1, QTableWidgetItem(I))
                                TablaTokens.setItem(FilaContador, 2, QTableWidgetItem(str(Contador)))
                                TablaTokens.setItem(FilaContador, 3,QTableWidgetItem(str(I.index('#')+1)))
                                TablaTokens.setItem(FilaContador, 4, QTableWidgetItem("Comentarios o Cadenas de Texto"))


                            if  (Instancia.GenerarToken("Operador",I,0) == 1):
                                ContadorColumnas = -1
                                Objeto = Instancia.GenerarToken("Operador",I,1)                            
                                for Coincidencias in  Objeto["Operador"]:
                                    ContadorColumnas = ContadorColumnas + 1
                                    FilaContador = TablaTokens.rowCount()                                
                                    TablaTokens.insertRow(FilaContador)                                
                                    TablaTokens.setItem(FilaContador , 0,QTableWidgetItem("Operador"))
                                    TablaTokens.setItem(FilaContador , 1,QTableWidgetItem(Coincidencias))                                    
                                    TablaTokens.setItem(FilaContador , 2,QTableWidgetItem(str(Contador)))                                    
                                    TablaTokens.setItem(FilaContador , 3,QTableWidgetItem(str(Objeto['Columnas'][ContadorColumnas]+1)))
                                    TablaTokens.setItem(FilaContador , 4,QTableWidgetItem(str(Objeto['Informacion'])))
                                    Tokens['Operadores'] = Tokens['Operadores'] +1
                                
                                    
                            if  (Instancia.GenerarToken("Reservada",I,0) == 1):                                
                                ContadorColumnas = -1
                                Objeto = Instancia.GenerarToken("Reservada",I,1)                                                                
                                for Coincidencias in  Objeto["Palabra"]:
                                    ContadorColumnas = ContadorColumnas + 1                                    
                                    FilaContador = TablaTokens.rowCount()                                
                                    TablaTokens.insertRow(FilaContador)                                
                                    TablaTokens.setItem(FilaContador , 0,QTableWidgetItem("Reservada"))
                                    TablaTokens.setItem(FilaContador , 1,QTableWidgetItem(Coincidencias))                                    
                                    TablaTokens.setItem(FilaContador , 2,QTableWidgetItem(str(Contador)))                                    
                                    TablaTokens.setItem(FilaContador , 3,QTableWidgetItem(str(Objeto['Columnas'][ContadorColumnas]+1)))
                                    TablaTokens.setItem(FilaContador , 4,QTableWidgetItem(str(Objeto['Informacion'])))
                                    Tokens['Reservadas'] = Tokens['Reservadas'] +1
                                 

                            if  (Instancia.GenerarToken("Delimitador",I,0) == 1):
                                ContadorColumnas = -1
                                Objeto = Instancia.GenerarToken("Delimitador",I,1)                                                                
                                for Coincidencias in  Objeto["Delimitador"]:
                                    ContadorColumnas = ContadorColumnas + 1                                    
                                    FilaContador = TablaTokens.rowCount()                                
                                    TablaTokens.insertRow(FilaContador)                                
                                    TablaTokens.setItem(FilaContador , 0,QTableWidgetItem("Delimitador"))
                                    TablaTokens.setItem(FilaContador , 1,QTableWidgetItem(Coincidencias))                                    
                                    TablaTokens.setItem(FilaContador , 2,QTableWidgetItem(str(Contador)))                                    
                                    TablaTokens.setItem(FilaContador , 3,QTableWidgetItem(str(Objeto['Columnas'][ContadorColumnas]+1)))
                                    TablaTokens.setItem(FilaContador , 4,QTableWidgetItem(str(Objeto['Informacion'])))
                                    Tokens['Delimitadores'] = Tokens['Delimitadores'] +1
                                    

                            if  (Instancia.GenerarToken("Errores",I,0) == 1):
                                ContadorErroresFila = 0
                                Objeto = Instancia.GenerarToken("Errores",I,1)
                                for Coincidencias in  Objeto["Error"]:
                                    FilaContador = TablaTokens.rowCount()                                
                                    TablaTokens.insertRow(FilaContador)                                
                                    TablaTokens.setItem(FilaContador , 0,QTableWidgetItem("Error"))
                                    TablaTokens.setItem(FilaContador , 1,QTableWidgetItem(Coincidencias))                                    
                                    TablaTokens.setItem(FilaContador , 2,QTableWidgetItem(str(Contador)))                                    
                                    TablaTokens.setItem(FilaContador , 3,QTableWidgetItem(str(Objeto['Columnas'][ContadorErroresFila])))
                                    TablaTokens.setItem(FilaContador , 4,QTableWidgetItem(str(Objeto['Informacion'])))
                                    ContadorErroresFila = ContadorErroresFila +1
                                    Tokens['Errores'] = Tokens['Errores'] + 1
                                    
                            
                            
                EtiquetaIdenti.setText("Identificadores : "+str(Tokens['Identificadores']))
                EtiquetaOpera.setText("Operadores : "+str(Tokens['Operadores']))
                EtiquetaReser.setText("Reservadas : "+str(Tokens['Reservadas']))
                EtiquetaDelim.setText("Delimitadores : "+str(Tokens['Delimitadores']))
                EtiquetaErr .setText("Errores : "+str(Tokens['Errores']))

                          
                                                    
                        
#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
     #Método constructor de la clase
     def __init__(self):
          #Iniciar el objeto QMainWindow
          QMainWindow.__init__(self)
          #Cargar la configuración del archivo .ui en el objeto
          uic.loadUi("Final.ui", self)

          self.mitabla.setColumnCount(5)
          Etiquetas = ['Tipo', 'Token', 'Linea','Columna','Descripcion']  
          self.mitabla.setHorizontalHeaderLabels(Etiquetas)
          header = self.mitabla.horizontalHeader()
          header.setStretchLastSection(True)
          Instancia = Resaltador( self.textEdit)
          self.textEdit.textChanged.connect(lambda: TextoCambio(self.textEdit,self.mitabla,self.label,self.label_4,self.label_5,self.label_6,self.label_7))
          self.pushButton_14.clicked.connect(lambda: AbrirArchivo(self.textEdit,self))

          


  
  
  
  
#Instancia para iniciar una aplicación
app = QApplication(sys.argv)

#Crear un objeto de la clase
_ventana = Ventana()


#Mostra la ventana
_ventana.show()

#Ejecutar la aplicación
app.exec_()


