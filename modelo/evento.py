from datetime import date, datetime

class Evento:

    def __init__(self):

        self.__idEvento=""
        self.__nome=""
        self.__descricao=""
        self.__data=""
        self.__horario=""
        self.__idSemana = ""
        self.__idPalestrante = ""
        self.__lista='nome,descricao,data,horario,idSemana,idPalestrante'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'evento'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = "'{}','{}','{}','{}',{},{}".format(self.nome, self.descricao,self.data,self.horario,self.idSemana,self.idPalestrante)
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = "nome='{}',descricao='{}',data='{}',horario='{}',idSemana='{}',idPalestrante='{}' where idEvento={}".format(self.nome, self.descricao,self.data,self.horario,self.idSemana,self.idPalestrante,self.idEvento)
        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where idEvento={}".format(self.idEvento)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from evento where idEvento={}".format(self.idEvento)
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
    def data(self):
        return self.__data

    @data.setter
    def data(self, entrada):
        self.__data = entrada

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, entrada):
        self.__horario = entrada

    @property
    def idSemana(self):
        return self.__idSemana

    @idSemana.setter
    def idSemana(self, entrada):
        self.__idSemana = entrada

    @property
    def idPalestrante(self):
        return self.__idPalestrante

    @idPalestrante.setter
    def idPalestrante(self, entrada):
        self.__idPalestrante = entrada

    def __repr__(self):
        return  self.nome

