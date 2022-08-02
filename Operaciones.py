import re
class Tabla:                           
      def GenerarToken(self,Tipo,Cadena,Parametro):
              
              if(Tipo == "Operador"):                                           
                      return(self.EvaluarOperadores(Cadena,Parametro))
              elif(Tipo == "Reservada"):                      
                      return(self.EvaluarReservadas(Cadena,Parametro))
              elif(Tipo == "Delimitador"):                      
                      return(self.EvaluarDelimitadores(Cadena,Parametro)) 
              elif(Tipo == "Identificador"):                      
                      return(self.EvaluarIdentificadores(Cadena,Parametro))
              elif(Tipo == "Especial"):                      
                      return(self.EvaluarCaracteresEspeciales(Cadena,Parametro))
              elif (Tipo == "Errores"):
                  return (self.EvaluarErrores(Cadena, Parametro))

      def EvaluarOperadores(self,Control,Parametro): 
            informacion = "Comparador o Delimitador"
            if(Parametro == 0):
                                  
                if (re.search("<=|>=|[*]{1,2}|[/]|[%]|[+]|[-]|[=]{1,2}|!=|[<]|[>]|[&&][|][!]",Control)):                                           
                      return 1
                else:                                            
                      return 0
            else:            
                      
                      return {'Operador':  re.findall("<=|>=|[*]{1,2}|[/]|[%]|[+]|[-]|[=]{1,2}|!=|[<]|[>]|[&&][|][!]", Control),'Descripcion':"En pruebas",'Conteo':1,'Columnas': [Iteracion.start() for Iteracion in re.finditer('<=|>=|[*]{1,2}|[/]|[%]|[+]|[-]|[=]{1,2}|!=|[<]|[>]|[&&][|][!]', Control)],'Informacion':informacion}

      def EvaluarReservadas(self,Control,Parametro): 
            informacion = "Delimitadores, P. Reservadas,Bucles"
            if(Parametro == 0):
                                  
                if (re.search("\\balias\\b|\\band\\b|\\bbreak\\b|\\bcase\\b|\\bclass\\b|\\bdef\\b|\\bdefined\\b|\\bdo\\b|\\belse\\b|\\belsif\\b|\\bend\\b|\\bensure\\b|\\bfalse\\b|\\btrue\\b|\\bfor\\b|\\bif\\b|\\bin\\b|\\bmodule\\b|\\bnext\\b|\\bnil\\b|\\bnot\\b|\\bor\\b|\\bredo\\b|\\brescue\\b|\\bretry\\b|\\breturn\\b|\\bself\\b|\\bsuper\\b|\\bthen\\b|\\bundef\\b|\\bunless\\b|\\buntil\\b|\\bwhile\\b|\\bwhen\\b|\\byield\\b|\\b_FILE_\\b|\\b_LINE_\\b",Control)):                                           
                      return 1
                else:                                            
                      return 0
            else:                                  
                      return {'Palabra':  re.findall("\\balias\\b|\\band\\b|\\bbreak\\b|\\bcase\\b|\\bclass\\b|\\bdef\\b|\\bdefined\\b|\\bdo\\b|\\belse\\b|\\belsif\\b|\\bend\\b|\\bensure\\b|\\bfalse\\b|\\btrue\\b|\\bfor\\b|\\bif\\b|\\bin\\b|\\bmodule\\b|\\bnext\\b|\\bnil\\b|\\bnot\\b|\\bor\\b|\\bredo\\b|\\brescue\\b|\\bretry\\b|\\breturn\\b|\\bself\\b|\\bsuper\\b|\\bthen\\b|\\bundef\\b|\\bunless\\b|\\buntil\\b|\\bwhile\\b|\\bwhen\\b|\\byield\\b|\\b_FILE_\\b|\\b_LINE_\\b", Control),'Descripcion':"En pruebas",'Conteo':1,'Columnas': [Iteracion.start() for Iteracion in re.finditer('\\balias\\b|\\band\\b|\\bbreak\\b|\\bcase\\b|\\bclass\\b|\\bdef\\b|\\bdefined\\b|\\bdo\\b|\\belse\\b|\\belsif\\b|\\bend\\b|\\bensure\\b|\\bfalse\\b|\\btrue\\b|\\bfor\\b|\\bif\\b|\\bin\\b|\\bmodule\\b|\\bnext\\b|\\bnil\\b|\\bnot\\b|\\bor\\b|\\bredo\\b|\\brescue\\b|\\bretry\\b|\\breturn\\b|\\bself\\b|\\bsuper\\b|\\bthen\\b|\\bundef\\b|\\bunless\\b|\\buntil\\b|\\bwhile\\b|\\bwhen\\b|\\byield\\b|\\b_FILE_\\b|\\b_LINE_\\b', Control)],'Informacion':informacion}
      
      def EvaluarDelimitadores(self,Control,Parametro): 
            informacion = "Delimitador de Sintaxis"
            if(Parametro == 0):
                                  
                if (re.search("[\(\),\"\'']",Control)):                                           
                      return 1
                else:                                            
                      return 0
            else:                                  
                      return {'Delimitador':  re.findall("[\(\),\"\']", Control),'Descripcion':"En pruebas",'Conteo':1,'Columnas': [Iteracion.start() for Iteracion in re.finditer('[\(\),\"\']', Control)],'Informacion':informacion}
      
      def EvaluarIdentificadores(self,Control,Parametro): 
            informacion = "Variable o Metodo"
            if(Parametro == 0):              

                Expresion1 = len(re.findall("\\b[_a-zA-Z][\w\s]*\\b",Control))
                if (Expresion1 >= 1):                      
                      return 1
                else:                                            
                      return 0                      

            else:                                                        
                      return {'Identificador':  re.findall("\\b[_a-zA-Z][\w\s]*\\b", Control),'Descripcion':"En pruebas",'Conteo':1,'Columnas': [Iteracion.start() for Iteracion in re.finditer("\\b[_a-zA-Z][\w]*\\b", Control)],"Devolver": re.findall("\"[\w\s]+\"",Control),'Informacion':informacion}
      
      def EvaluarErrores(self,Control,Parametro):
            informacion = "Errores de sintaxis"
            if(Parametro == 0):
                if (re.search("[°]|[¡]|[?]|[¿]",Control)):
                          return 1
                else:                                            
                          return 0
            else:                                  
                      return {'Error':  re.findall("[°]|[¡]|[?]|[¿]", Control),'Descripcion':"En pruebas",'Conteo':1,'Columnas': [Iteracion.start() for Iteracion in re.finditer('[°]|[¡]|[?]|[¿]', Control)],'Informacion':informacion}
           

              
