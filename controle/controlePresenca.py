from controle.Conectarbanco import *
from modelo.presenca import *

import datetime
from controle.controleGenerico import *

class ControlePresenca(ControleGenerico):

    def incluirPresenca(self,presenca):
        return self.incluir(presenca)

    def alterarPresenca(self, presenca):
        self.alterar(presenca)

    def deletarPresenca(self,idE,idP):
        presenca = Presenca()
        presenca.id_Evento = idE
        presenca.id_Participante = idP
        self.delete(presenca)

    def pesquisaCodigo(self,idE,idP):
        presenca = Presenca()
        presenca.id_Evento = idE
        presenca.id_Participante = idP
        presenca = self.procuraRegistro(presenca)
        retorno = Presenca()
        if len(presenca) >= 1:
            retorno.id_Evento = presenca[0][0]
            retorno.id_Participante = presenca[0][1]
            retorno.Presente = presenca[0][2]
        return retorno

    def listarTodosRegistros(self):
        presenca = Presenca()
        return self.listarTodos(presenca)


