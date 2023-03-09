from datetime import date, datetime

class Palestrante:

    def __init__(self):

        self.__idPalestrante=""
        self.__nome=""
        self.__email=""
        self.__cpf=""
        self.__lista='nome,email,cpf'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'palestrante'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}'".format(self.nome, self.email,self.cpf)
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = "nome='{}',email='{}',cpf='{}' where idPalestrante={}".format(self.nome, self.email,self.cpf,self.idPalestrante)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idPalestrante={}".format(self.idPalestrante)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from palestrante where idPalestrante={}".format(self.idPalestrante)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idPalestrante(self):
        return self.__idPalestrante

    @idPalestrante.setter
    def idPalestrante(self, entrada):
        self.__idPalestrante = entrada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,entrada):
        self.__nome=entrada

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, entrada):
        self.__email = entrada

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, entrada):
        self.__cpf = entrada

    def __repr__(self):
        return  self.nome

