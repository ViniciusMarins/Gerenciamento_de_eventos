from controle.Conectarbanco import *
from modelo.evento import *

import datetime
from controle.controleGenerico import *

class ControleEvento(ControleGenerico):

    def incluirEvento(self,evento):
        self.incluir(evento)

    def alterarEvento(self, evento):
        self.alterar(evento)

    def deletarEvento(self,id):
        evento = Evento()
        evento.idEvento = id
        self.delete(evento)

    def pesquisaCodigo(self,entrada):
        evento = Evento()
        evento.idEvento = entrada
        evento = self.procuraRegistro(evento)
        retorno = Evento()
        if len(evento) >= 1:
            retorno.idEvento = evento[0][0]
            retorno.nome = evento[0][1]
            retorno.descricao = evento[0][2]
            retorno.data = evento[0][3]
            retorno.horario = evento[0][4]
            retorno.idSemana = evento[0][5]
            retorno.idPalestrante = evento[0][6]
        return retorno

    def listarTodosRegistros(self):
        evento = Evento()
        return self.listarTodos(evento)


