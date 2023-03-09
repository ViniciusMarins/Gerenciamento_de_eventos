from datetime import date, datetime

class Presenca:

    def __init__(self):

        self.__id_Evento=""
        self.__id_Participante=""
        self.__Presente=""
        self.__lista='id_Evento,id_Participante,Presente'

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
        self.__dadosInserir = "'{}','{}','{}'".format(self.id_Evento, self.id_Participante,self.Presente)
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = "id_Evento='{}',id_Participante='{}',Presente='{}' where id_Evento='{}' and id_Participante='{}'".format(self.id_Evento, self.id_Participante,self.Presente,self.id_Evento,self.id_Participante)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where id_Evento = {} and id_Participante = {}".format(self.id_Evento,self.id_Participante)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from presenca where id_Evento = {} and id_Participante = {}".format(self.id_Evento,self.id_Participante)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

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

    @property
    def Presente(self):
        return self.__Presente

    @Presente.setter
    def Presente(self, entrada):
        self.__Presente = entrada

    def __repr__(self):
        return  self.id_Evento

