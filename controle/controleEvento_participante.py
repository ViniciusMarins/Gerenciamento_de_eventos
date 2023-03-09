from controle.Conectarbanco import *
from modelo.evento_participante import *

import datetime
from controle.controleGenerico import *

class ControleEvento_participante(ControleGenerico):

    def incluirEvento_participante(self,evento_participante):
        self.incluir(evento_participante)

    def alterarEvento_participante(self, evento_participante):
        self.alterar(evento_participante)

    def deletarEvento_participante(self,idE,idP):
        evento_participante = Evento_participante()
        evento_participante.idParticipante = idP
        evento_participante.idEvento = idE
        self.delete(evento_participante)

    def pesquisaCodigo(self,entrada):
        evento_participante = Evento_participante()
        evento_participante.idParticipante = entrada
        evento_participante = self.procuraRegistro(evento_participante)
        retorno = Evento_participante()
        if len(evento_participante) >= 1:
            retorno.idEvento = evento_participante[0][0]
            retorno.idSemana = evento_participante[0][1]
            retorno.idParticipante = evento_participante[0][2]
        return retorno

    def listarTodosRegistros(self):
        evento_participante = Evento_participante()
        return self.listarTodos(evento_participante)


