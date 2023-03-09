from controle.Conectarbanco import *
from modelo.palestrante import *

import datetime
from controle.controleGenerico import *

class ControlePalestrante(ControleGenerico):

    def incluirPalestrante(self,palestrante):
        self.incluir(palestrante)

    def alterarPalestrante(self, palestrante):
        self.alterar(palestrante)

    def deletarPalestrante(self,id):
        palestrante = Palestrante()
        palestrante.idPalestrante = id
        self.delete(palestrante)

    def pesquisaCodigo(self,entrada):
        palestrante = Palestrante()
        palestrante.idPalestrante = entrada
        palestrante = self.procuraRegistro(palestrante)
        retorno = Palestrante()
        if len(palestrante) >= 1:
            retorno.idPalestrante = palestrante[0][0]
            retorno.nome = palestrante[0][1]
            retorno.email = palestrante[0][2]
            retorno.cpf = palestrante[0][3]
        return retorno

    def listarTodosRegistros(self):
        palestrante = Palestrante()
        return self.listarTodos(palestrante)


