from datetime import date, datetime

class Presenca:

    def __init__(self):

        self.__idPresenca=""
        self.__id_Evento=""
        self.__id_Participante=""
        self.__lista='id_Evento,id_Participante'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'presenca'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}'".format(self.id_Evento, self.id_Participante)
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = "id_Evento='{}',id_Participante='{}' where idPresenca={}".format(self.id_Evento, self.id_Participante,self.idPresenca)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idPresenca={}".format(self.idPresenca)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from presenca where idPresenca={}".format(self.idPresenca)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idPresenca(self):
        return self.__idPresenca

    @idPresenca.setter
    def idPresenca(self, entrada):
        self.__idPresenca = entrada

    @property
    def id_Evento(self):
        return self.__id_Evento

    @id_Evento.setter
    def id_Evento(self,entrada):
        self.__id_Evento=entrada

    @property
    def id_Participante(self):
        return self.__id_Participante

    @id_Participante.setter
    def id_Participante(self, entrada):
        self.__id_Participante = entrada

    def __repr__(self):
        return  self.id_Evento

