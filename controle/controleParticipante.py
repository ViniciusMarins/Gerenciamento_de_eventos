from controle.Conectarbanco import *
from modelo.participante import *

import datetime
from controle.controleGenerico import *

class ControleParticipante(ControleGenerico):

    def incluirParticipante(self,participante):
        self.incluir(participante)

    def alterarParticipante(self, participante):
        self.alterar(participante)

    def deletarParticipante(self,id):
        participante = Participante()
        participante.idParticipante = id
        self.delete(participante)

    def pesquisaCodigo(self,entrada):
        participante = Participante()
        participante.idParticipante = entrada
        participante = self.procuraRegistro(participante)
        retorno = Participante()
        if len(participante) >= 1:
            retorno.idParticipante = participante[0][0]
            retorno.nome = participante[0][1]
            retorno.email = participante[0][2]
            retorno.cpf = participante[0][3]
        return retorno

    def listarTodosRegistros(self):
        participante = Participante()
        return self.listarTodos(participante)


