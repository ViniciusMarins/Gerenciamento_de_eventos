import pymysql

class Banco:

   def __init__(self):
       self.servidor="localhost"
       self.usuario="root"
       self.senha=""
       self.banco="db_proj"
       self.ponteiro =""

   def abrirConexao(self):
      self.con = pymysql.connect(host=self.servidor,db=self.banco, user=self.usuario, passwd=self.senha)
      self.ponteiro=self.con.cursor()

      self.ponteiro.execute("CREATE TABLE IF NOT EXISTS semana (idSemana INT NOT NULL AUTO_INCREMENT,nome VARCHAR(50) NOT NULL,descricao VARCHAR(200) NOT NULL,inicio VARCHAR(100) NOT NULL,fim VARCHAR(100) NOT NULL,PRIMARY KEY (idSemana))ENGINE = InnoDB;")

      self.ponteiro.execute("CREATE TABLE IF NOT EXISTS palestrante (idPalestrante INT NOT NULL AUTO_INCREMENT,nome VARCHAR(100) NOT NULL,email VARCHAR(100) NOT NULL,cpf VARCHAR(45) NOT NULL,PRIMARY KEY (idPalestrante))ENGINE = InnoDB;")

      self.ponteiro.execute("CREATE TABLE IF NOT EXISTS evento (idEvento INT NOT NULL AUTO_INCREMENT,nome VARCHAR(100) NOT NULL,descricao VARCHAR(200) NOT NULL,data VARCHAR(25) NOT NULL,horario VARCHAR(50) NOT NULL,idSemana INT NOT NULL,idPalestrante INT NOT NULL,PRIMARY KEY (idEvento),INDEX idSemana (idSemana ASC) VISIBLE,INDEX idPalestrante (idPalestrante ASC) VISIBLE,CONSTRAINT evento_ibfk_1 FOREIGN KEY (idSemana) REFERENCES semana (idSemana),CONSTRAINT evento_ibfk_2 FOREIGN KEY (idPalestrante) REFERENCES palestrante (idPalestrante)) ENGINE = InnoDB;")

      self.ponteiro.execute("CREATE TABLE IF NOT EXISTS participante (idParticipante INT NOT NULL AUTO_INCREMENT,nome VARCHAR(200) NOT NULL,email VARCHAR(200) NOT NULL,cpf VARCHAR(45) NOT NULL,PRIMARY KEY (idParticipante))ENGINE = InnoDB;")

      self.ponteiro.execute("CREATE TABLE IF NOT EXISTS evento_participante ( idEvento INT NOT NULL, idSemana INT NOT NULL, idParticipante INT NOT NULL, PRIMARY KEY (idParticipante, idSemana, idEvento), INDEX idEvento_idx (idEvento ASC) VISIBLE, INDEX idSemana_idx (idSemana ASC) VISIBLE, CONSTRAINT idEvento FOREIGN KEY (idEvento) REFERENCES evento (idEvento), CONSTRAINT idParticipante FOREIGN KEY (idParticipante) REFERENCES participante (idParticipante), CONSTRAINT idSemana FOREIGN KEY (idSemana) REFERENCES semana (idSemana)) ENGINE = InnoDB;")

      self.ponteiro.execute("CREATE TABLE IF NOT EXISTS presenca (id_Evento INT NOT NULL, id_Participante INT NOT NULL, Presente CHAR(1) NOT NULL, PRIMARY KEY (id_Evento, id_Participante))ENGINE = InnoDB;")

   def selectQuery(self,entrada):
      self.ponteiro.execute(entrada)
      resposta = self.ponteiro.fetchall()
      return resposta

   def executeQuery(self, entrada,dados):
       self.ponteiro.execute(entrada,dados)

   def execute(self, entrada):
       self.ponteiro.execute(entrada)

   def gravar(self):
      self.con.commit()

   def descarte(self):
      self.con.rollback()

   def configura(self,ho,db,se="01112001",us='root'):
       self.servidor = ho
       self.usuario = us
       self.senha = se
       self.banco = db

   def mostraResultado(self,entrada):
       for i in entrada:
           print(i)
