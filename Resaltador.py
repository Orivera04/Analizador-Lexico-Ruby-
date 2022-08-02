from PyQt5.QtCore import QFile, QRegExp, Qt
from PyQt5.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat,QColor
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow, QMenu,
        QMessageBox, QTextEdit,QPlainTextEdit)

class Resaltador(QSyntaxHighlighter):
    def __init__(self, parent=None):        
        super(Resaltador, self).__init__(parent)

      
      
        PalabrasReservadas = QTextCharFormat()
        PalabrasReservadas.setForeground(QColor(236,183,85))


        OperadoresExpresion = ['=','==', '!=', '<', '<=', '>', '>=','\+', '-', '\*', '/', '//', '\%', '\*\*','\+=', '-=', '\*=', '/=', '\%=','\^', '\|', '\&', '\~', '>>', '<<','[',']']
        
        self.ReglasDeResaltado = []
        
        MetodosIdentificacion = QTextCharFormat()
        MetodosIdentificacion.setForeground(QColor(137,158,184))
        self.ReglasDeResaltado.append((QRegExp("[_a-zA-Z][_a-zA-Z0-9]{0,30}"),MetodosIdentificacion))

        PalabrasReservadas = QTextCharFormat()
        PalabrasReservadas.setForeground(QColor(236,183,85))

        self.ReglasDeResaltado.append((QRegExp("\\balias\\b|\\band\\b|\\bbreak\\b|\\bcase\\b|\\bclass\\b|\\bdef\\b|\\bdefined\\b|\\bdo\\b|\\belse\\b|\\belsif\\b|\\bend\\b|\\bensure\\b|\\bfalse\\b|\\btrue\\b|\\bfor\\b|\\bif\\b|\\bin\\b|\\bmodule\\b|\\bnext\\b|\\bnil\\b|\\bnot\\b|\\bor\\b|\\bredo\\b|\\brescue\\b|\\bretry\\b|\\breturn\\b|\\bself\\b|\\bsuper\\b|\\bthen\\b|\\bundef\\b|\\bunless\\b|\\buntil\\b|\\bwhile\\b|\\bwhen\\b|\\byield\\b|\\b_FILE_\\b|\\b_LINE_\\b"),PalabrasReservadas))

        

      
        
        
        
        
  
        
        for Iteracion in OperadoresExpresion:
                OperadorExpresion = QTextCharFormat()
                OperadorExpresion.setFontWeight(QFont.Bold)
                OperadorExpresion.setForeground(QColor(116,85,236))
                self.ReglasDeResaltado.append((QRegExp(Iteracion),OperadorExpresion))



        
      

        ParantesisExpresion = QTextCharFormat()
        ParantesisExpresion.setForeground(QColor(247,191,190))
        self.ReglasDeResaltado.append((QRegExp("[\(\),\"\'']"),ParantesisExpresion))

        CorchetesExpresion = QTextCharFormat()
        CorchetesExpresion.setForeground(QColor(116,85,236))
        self.ReglasDeResaltado.append((QRegExp("[\[\];,]"),CorchetesExpresion))

        DelimitadoresExpresionRegular = QTextCharFormat()
        DelimitadoresExpresionRegular.setForeground(Qt.darkGreen)
        self.ReglasDeResaltado.append((QRegExp("#[^\n]*"),DelimitadoresExpresionRegular))

        

        ComillasExpresion = QTextCharFormat()
        ComillasExpresion.setForeground(QColor(247,191,190))
        self.ReglasDeResaltado.append((QRegExp("(\".*\")|('.*')"), ComillasExpresion))

        ErroresExpresion = QTextCharFormat()
        ErroresExpresion.setForeground(QColor(255,0,0))
        self.ReglasDeResaltado.append((QRegExp("[°]|[¡]|[?]|[¿]"), ComillasExpresion))

        self.ComentarioInicio = QRegExp("/\\*")
        self.ComentarioFinal = QRegExp("\\*/")

    def highlightBlock(self, Texto):
        for Regla, format in self.ReglasDeResaltado:
            Expresion = QRegExp(Regla)
            Indice = Expresion.indexIn(Texto)
            while Indice >= 0:
                Longitud = Expresion.matchedLength()
                self.setFormat(Indice, Longitud, format)
                Indice = Expresion.indexIn(Texto, Indice + Longitud)

        self.setCurrentBlockState(0)

        IndiceDeInicio = 0
        if self.previousBlockState() != 1:
             IndiceDeInicio = self.ComentarioInicio.indexIn(Texto)

        while IndiceDeInicio >= 0:
            IndiceFinal = self.ComentarioFinal.indexIn(Texto, IndiceDeInicio)

            if IndiceFinal == -1:
                self.setCurrentBlockState(1)
                LongitudComentario = len(Texto) - IndiceDeInicio
            else:
                LongitudComentario = IndiceFinal - IndiceDeInicio + self.ComentarioFinal.matchedLength()

            self.setFormat(IndiceDeInicio, LongitudComentario,
                    self.ComentarioMultilinea)
            IndiceDeInicio = self.ComentarioInicio.indexIn(Texto,
                    IndiceDeInicio + LongitudComentario);



