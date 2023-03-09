from controle.Conectarbanco import *
from modelo.semana import *

import datetime
from controle.controleGenerico import *

class ControleSemana(ControleGenerico):

    def incluirSemana(self,semana):
        self.incluir(semana)

    def alterarSemana(self, semana):
        self.alterar(semana)

    def deletarSemana(self,id):
        semana = Semana()
        semana.idSemana = id
        self.delete(semana)

    def pesquisaCodigo(self,entrada):
        semana = Semana()
        semana.idSemana = entrada
        semana = self.procuraRegistro(semana)
        retorno = Semana()
        if len(semana) >= 1:
            retorno.idSemana = semana[0][0]
            retorno.nome = semana[0][1]
            retorno.descricao = semana[0][2]
            retorno.inicio = semana[0][3]
            retorno.fim = semana[0][4]
        return retorno

    def listarTodosRegistros(self):
        semana = Semana()
        return self.listarTodos(semana)


