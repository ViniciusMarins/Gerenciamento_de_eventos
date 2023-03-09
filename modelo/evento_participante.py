from datetime import date, datetime

class Evento_participante:

    def __init__(self):

        self.__idEvento=""
        self.__idSemana=""
        self.__idParticipante=""
        self.__lista='idEvento,idSemana,idParticipante'

        self.__dadosInserir=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'evento_participante'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}'".format(self.idEvento,self.idSemana, self.idParticipante)
        return self.__dadosInserir

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idEvento={} and idParticipante={}".format(self.idEvento,self.idParticipante)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from evento_participante where idEvento={} and idParticipante ={}".format(self.idEvento,self.idParticipante)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idEvento(self):
        return self.__idEvento

    @idEvento.setter
    def idEvento(self, entrada):
        self.__idEvento = entrada

    @property
    def idSemana(self):
        return self.__idSemana

    @idSemana.setter
    def idSemana(self,entrada):
        self.__idSemana=entrada

    @property
    def idParticipante(self):
        return self.__idParticipante

    @idParticipante.setter
    def idParticipante(self, entrada):
        self.__idParticipante = entrada

    def __repr__(self):
        return  self.idSemana

