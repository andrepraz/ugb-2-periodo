class MyCrud:
    def __init__(self, banco):
        import sqlite3
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def fecharDB(self):
        self.conexao.close()

    def criar_tabela(self):
        sql = """
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT
            );
        """
        self.cursor.execute(sql)
        print('Tabela criada')

    def selecionar(self):
        sql = """
            SELECT * FROM clientes;
        """
        resultados = self.cursor.execute(sql)
        return resultados.fetchall()

    def inserir(self, dados):
        campos = '('
        valores = '('
        for i in dados['campos']:
            campos += f'{i}, '
            valores += '?, '
        campos = f'{campos[:-2]})'
        valores = f'{valores[:-2]})'

        sql = f"""
            INSERT INTO {dados['tabela']} {campos}
            VALUES {valores};
        """

        self.cursor.execute(sql, dados['valores'])
        self.conexao.commit()
        print('salvo com sucesso...')

    def alterar(self, a_nome, a_cpf, a_id):
        sql = """
            UPDATE clientes
            SET nome = ?, cpf = ?
            WHERE id = ?;
        """
        self.cursor.execute(sql, [a_nome, a_cpf, a_id])
        self.conexao.commit()
        print('alterado com sucesso...')

    def deletar(self, d_id):
        sql = """
            DELETE FROM clientes
            WHERE id = ?;
        """
        self.cursor.execute(sql, [d_id])
        self.conexao.commit()
        print('deletado com sucesso...')