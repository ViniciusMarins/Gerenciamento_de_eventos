from datetime import date, datetime

class Semana:

    def __init__(self):

        self.__idSemana=""
        self.__nome=""
        self.__descricao=""
        self.__inicio=""
        self.__fim=""
        self.__lista='nome,descricao,inicio,fim'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'semana'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}','{}'".format(self.nome, self.descricao,self.inicio,self.fim)
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = "nome='{}',descricao='{}',inicio='{},fim ='{}' where idSemana={}".format(self.nome, self.descricao,self.inicio,self.fim,self.idSemana)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idSemana={}".format(self.idSemana)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from semana where idSemana={}".format(self.idSemana)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idSemana(self):
        return self.__idSemana

    @idSemana.setter
    def idSemana(self, entrada):
        self.__idSemana = entrada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,entrada):
        self.__nome=entrada

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, entrada):
        self.__descricao = entrada

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, entrada):
        self.__inicio = entrada

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, entrada):
        self.__fim = entrada

    def __repr__(self):
        return  self.nome

