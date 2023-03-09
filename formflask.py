from flask import Flask, render_template, request,redirect,url_for
#Modelos
from modelo.aluno import *
from modelo.evento import *
from modelo.evento_participante import *
from modelo.palestrante import *
from modelo.participante import *
from modelo.presenca import *
from modelo.semana import *

#Controles
from controle.controleAluno import *
from controle.controleSemana import *
from controle.controleParticipante import *
from controle.controlePalestrante import *
from controle.controleEvento import *
from controle.controleEvento_participante import *

import sys
import subprocess as sp

app = Flask(__name__)


@app.route('/')
def index():
    daoSemana = ControleSemana()
    dados = daoSemana.listarTodosRegistros()
    return render_template('homepage.html', result=dados)


@app.route('/editar/<id>')
def editar(id):
    daoAluno = ControleAluno()
    dados = daoAluno.pesquisaCodigo(id)
    return render_template("editaestudante.html",dados = dados)

@app.route('/delete/<id>')
def delete(id):
    daoSemana = ControleSemana()
    daoSemana.deletarSemana(id)
    return redirect(url_for('tabela'))

@app.route('/gravar',methods = ['POST', 'GET'])
def gravar():
    if request.method == 'POST':
       result = request.form
       sem = Semana()
       sem.nome = result['nome']
       sem.descricao = result['descricao']
       sem.inicio = result['inicio']
       sem.fim = result['fim']
       daoSemana = ControleSemana()

       if result['botao']=='Gravar':
           daoSemana.incluirSemana(sem)
       elif result['botao']=='Alterar':  
           sem.idSemana=result['codigo']
           daoSemana.alterarSemana(sem)

    return redirect(url_for('index'))

#-----------------------------------------------------------------------
@app.route('/participantes')
def participantes():
    daoParticipante = ControleParticipante()
    dados = daoParticipante.listarTodosRegistros()
    return render_template('participantes.html', result=dados)

@app.route('/gravarParticipante',methods = ['POST', 'GET'])
def gravarParticipante():
    if request.method == 'POST':
       result = request.form
       par = Participante()
       par.nome = result['nome']
       par.email = result['email']
       par.cpf = result['cpf']
       daoParticipante = ControleParticipante()

       if result['botao']=='Gravar':
           daoParticipante.incluirParticipante(par)
       elif result['botao']=='Alterar':  
           par.idParticipante=result['codigo']
           daoParticipante.alterarParticipante(par)

    return redirect(url_for('participantes'))  

@app.route('/deleteParticipante/<id>')
def deleteParticipante(id):
    daoParticipante = ControleParticipante()
    daoParticipante.deletarParticipante(id)
    return redirect(url_for('participantes'))


#------------------------------------------------------------------------

@app.route('/palestrantes')
def palestrantes():
    daoPalestrante = ControlePalestrante()
    dados = daoPalestrante.listarTodosRegistros()
    return render_template('palestrantes.html', result=dados)

@app.route('/gravarPalestrante',methods = ['POST', 'GET'])
def gravarPalestrante():
    if request.method == 'POST':
       result = request.form
       pal = Palestrante()
       pal.nome = result['nome']
       pal.email = result['email']
       pal.cpf = result['cpf']
       daoPalestrante = ControlePalestrante()

       if result['botao']=='Gravar':
           daoPalestrante.incluirPalestrante(pal)
       elif result['botao']=='Alterar':  
           pal.idPalestrante=result['codigo']
           daoPalestrante.alterarPalestrante(pal)

    return redirect(url_for('palestrantes'))  

@app.route('/deletePalestrante/<id>')
def deletePalestrante(id):
    daoPalestrante = ControlePalestrante()
    daoPalestrante.deletarPalestrante(id)
    return redirect(url_for('palestrantes'))

#--------------------------------------------------------------------

@app.route('/eventos')
def eventos():
    daoEvento = ControleEvento()
    eventos = daoEvento.listarTodosRegistros()
    daoSemana = ControleSemana()
    semanas = daoSemana.listarTodosRegistros()
    daoPalestrantes = ControlePalestrante()
    palestrantes = daoPalestrantes.listarTodosRegistros()
    
    return render_template('eventos.html', semanas=semanas,eventos=eventos,palestrantes=palestrantes)

@app.route('/gravarEvento',methods = ['POST', 'GET'])
def gravarEvento():
    if request.method == 'POST':
       result = request.form
       eve = Evento()
       eve.nome = result['nome']
       eve.descricao = result['descricao']
       eve.data = result['data']
       eve.horario = result['horario']
       eve.idSemana = result['idSemana']
       eve.idPalestrante = result['idPalestrante']
       daoEvento = ControleEvento()

       if result['botao']=='Gravar':
           daoEvento.incluirEvento(eve)
       elif result['botao']=='Alterar':  
           eve.idEvento=result['codigo']
           daoEvento.alterarEvento(eve)

    return redirect(url_for('eventos'))  

@app.route('/deleteEvento/<id>')
def deleteEvento(id):
    daoEvento = ControleEvento()
    daoEvento.deletarEvento(id)
    return redirect(url_for('eventos'))

#---------------------------------------------------------------------

@app.route('/inscricoes')
def inscricoes():
    daoInscricoes = ControleEvento_participante()
    inscricoes = daoInscricoes.listarTodosRegistros()

    daoParticipantes = ControleParticipante()
    participantes = daoParticipantes.listarTodosRegistros()

    daoEvento = ControleEvento()
    eventos = daoEvento.listarTodosRegistros()

    daoSemana = ControleSemana()
    semanas = daoSemana.listarTodosRegistros()

    return render_template('inscricoes.html', inscricoes = inscricoes,participantes = participantes,eventos = eventos,semanas=semanas)


@app.route('/gravarInscricao',methods = ['POST', 'GET'])
def gravarInscricao():
    if request.method == 'POST':
       result = request.form
       ins = Evento_participante()
       ins.idEvento = result['idEvento']
       ins.idParticipante = result['idParticipante']

       daoInscricoes = ControleEvento_participante()
       daoEvento = ControleEvento()
       eve = daoEvento.pesquisaCodigo(ins.idEvento)
       ins.idSemana = eve.idSemana

       if result['botao']=='Gravar':
           daoInscricoes.incluirEvento_participante(ins)

    return redirect(url_for('inscricoes'))  

@app.route('/deleteInscricao/<idE>,<idP>')
def deleteInscricao(idE,idP):
    daoInscricoes = ControleEvento_participante()
    daoInscricoes.deletarEvento_participante(idE,idP)
    return redirect(url_for('inscricoes'))


if __name__ == '__main__':
   app.run(debug = True)