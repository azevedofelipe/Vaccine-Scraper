import psycopg2

class DBManager():

    def __init__(self,csv_path=""):
        
        self._db = csv_path
        self._conn = None
        self._cursor = None

    def open_connection(self):
        self._conn = psycopg2.connect(database="vacina", user='postgres', password='1', host='127.0.0.1', port='5432')
        self._conn.autocommit = True
        self._cursor = self._conn.cursor()

    def close_connection(self):
        self._conn.close()

    def init_table(self):

        create_table_query = """ CREATE TABLE vacinas_municipios(municipios varchar(80), BCG int, hepatite_b_crianca int, rotavirus_humano int, meningococo_c int,
                                hepatite_b int, penta int, pneumococica int, poliomielite int, poliomielite_4_anos int, febre_amarela int, hepatite_a int, 
                                pneumococica_1a_ref int, meningococo_c_1a_ref int, poliomielite_1a_ref int, triplice_viral_d1 int, triplice_viral_d2 int, tetra_viral int, dtp int,
                                dtp_ref_4_6_anos int, triplice_bacteriana_dtp_1a_ref int, dupla_adulto_e_triplice_acelular_gestante int, dtpa_gestante int, varicela int, total int                                                     
        )"""

        self._cursor.execute("select exists(select * from information_schema.tables where table_name=%s)", ('vacinas_municipios',))

        if(self._cursor.fetchone()[0] != True):
            self._cursor.execute(create_table_query)
        
        copy_query =""" COPY vacinas_municipios FROM stdin WITH CSV HEADER
                        DELIMITER as ';'
                    """
        
        with open(self._db,'r') as f:
            self._cursor.copy_expert(sql=copy_query,file=f)
            self._conn.commit()

    def drop_table(self):
        drop_query = """ DROP TABLE vacinas_municipios"""
        self._cursor.execute(drop_query)
        self._conn.commit()

        print("Table dropped\n")

    def show_table(self):
        sql3 = '''select * from vacinas_municipios'''
        self._cursor.execute(sql3)
        for i in self._cursor.fetchall():
            print(i)

        self._conn.commit()


    