from controle.Conectarbanco import *
from modelo.aluno import *

import datetime
from controle.controleGenerico import *

class ControleAluno(ControleGenerico):

    def incluirAluno(self,aluno):
        self.incluir(aluno)

    def alterarAluno(self, aluno):
        self.alterar(aluno)

    def deletarAluno(self,id):
        aluno = Aluno()
        aluno.idaluno = id
        self.delete(aluno)

    def pesquisaCodigo(self,entrada):
        aluno = Aluno()
        aluno.idaluno = entrada
        aluno = self.procuraRegistro(aluno)
        retorno = Aluno()
        if len(aluno) >= 1:
            retorno.idaluno = aluno[0][0]
            retorno.nome = aluno[0][1]
            retorno.endereco = aluno[0][2]
            retorno.cidade = aluno[0][3]
            retorno.uf = aluno[0][4]
            retorno.cep = aluno[0][5]
            retorno.nascimento = aluno[0][6]
        return retorno

    def listarTodosRegistros(self):
        aluno = Aluno()
        return self.listarTodos(aluno)


