import MySQLdb
from cpf_tools import cpf_str_validation


class banco_de_dados:

    def __init__(self):
        self.conexao = MySQLdb.connect(db="exemplo_banco", user="root", host="localhost", port=3306)
        self.cursor = self.conexao.cursor()

    def inserir_dados(self,informacoes: dict):
        self.informacoes = informacoes

    def validar_informacoes(self):
        try:
            self.informacoes['nome']=str(self.informacoes['nome'])
            self.informacoes['idade']=int(self.informacoes['idade'])
            self.informacoes['altura']=float(self.informacoes['altura'])
        except:
            return False

        if len(self.informacoes['nome']) < 4 or len(self.informacoes['nome']) > 50:
            return False

        elif cpf_str_validation(self.informacoes['cpf'])==False:
            return False

        elif self.informacoes['idade'] < 1 or self.informacoes['idade'] > 150:
            return False

        elif self.informacoes['altura'] < 0.4 or self.informacoes['altura'] > 2.5:
            return False

        return True

    def insert_banco_de_dados(self):
        if self.validar_informacoes():
            self.cursor.execute("SELECT cpf FROM exemplo_banco_tabela;")
            lista_cpf = [cpf[0] for cpf in self.cursor.fetchall()]
            if self.informacoes['cpf'].replace(".","").replace("-","") not in lista_cpf:
                self.cursor.execute(f"INSERT INTO exemplo_banco_tabela VALUES ('{self.informacoes['nome']}',"
                            f" '{self.informacoes['cpf'].replace('.','').replace('-','')}', "
                                    f"{self.informacoes['idade']}, {self.informacoes['altura']})")
                return True
        return False

    def delete_banco_de_dados(self, lista_cpf=None):
        if lista_cpf==None:
            self.cursor.execute("DELETE FROM exemplo_banco_tabela")
        else:
            self.cursor.execute(f"DELETE FROM exemplo_banco_tabela WHERE cpf in ({''.join(lista_cpf)})")

    def update_banco_de_dados(self, lista_cpf=None):
        if self.validar_informacoes():
            if lista_cpf==None:
                self.cursor.execute(f"UPDATE exemplo_banco_tabela SET nome = '{self.informacoes['nome']}', idade = "
                                    f"'{self.informacoes['idade']}', altura = '{self.informacoes['altura']}'")
            else:
                self.cursor.execute(f"UPDATE exemplo_banco_tabela SET nome = '{self.informacoes['nome']}', idade = "
                                    f"'{self.informacoes['idade']}', altura = '{self.informacoes['altura']}'"
                                    f" WHERE cpf in ({''.join(lista_cpf)}")

    def select_banco_de_dados(self, lista_cpf=None):
        if lista_cpf==None:
            self.cursor.execute("SELECT * FROM exemplo_banco_tabela")
            print([cpf[0] for cpf in self.cursor.fetchall()])
        else:
            self.cursor.execute(f"SELECT * FROM exemplo_banco_tabela WHERE cpf in (({''.join(lista_cpf)})")
            print([cpf[0] for cpf in self.cursor.fetchall()])

    def commit_banco_de_dados(self):
        self.conexao.commit()
        print("ok")


teste = banco_de_dados()
#teste.inserir_dados(dict(nome='Reginaldo Oliveira', cpf='07861218902', idade='22', altura='1.85'))