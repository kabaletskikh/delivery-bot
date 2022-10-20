import sqlite3

from config import config



class Executor:
    def __init__(self, sv):
        self.sv = sv
        self.sv.trace("Модуль успешно подключен", "SQL Executor")
        cfg = config.Config()
        self.db_filename = cfg.get("db_manager", "dbname")
        self.adapter = cfg.get("db_manager", "adapter")
        self.used = False
    

    def execute(self, command, data_cortege=False, amount_to_fetch=0):
        if self.adapter == "sqlite":
            if not used:
                self.conn = sqlite3.connect(self.db_filename)
                self.cur  = conn.cursor()
                used = True
            
            res = self.execute_sqlite(command, self.conn, self.cur, data_cortege, amount_to_fetch)
            self.sv.trace("Команда [" + str(command) + "] с кортежем [" + str(data_cortege) + "] выполнена с результатом [" + str(res) + "]", "SQL Executor")


    def execute_sqlite(self, conn, cur, command, data_cortege=False, amount_to_fetch=0):
        if not data_cortege:
            cur.execute(command, data_cortege)
        else:
            cur.execute(command)
    
        if amount_to_fetch == 0:
            res = conn.commit()
            self.sv.trace("Команда [" + str(command) + "] с кортежем [" + str(data_cortege) + "] и amount " + amount_to_fetch + "] выполнена с результатом [" + str(res) + "]", "SQL Executor")
            return res

        res = cur.fetchmany(amount_to_fetch)
        self.sv.trace("Команда [" + str(command) + "] с кортежем [" + str(data_cortege) + "] и amount " + amount_to_fetch + "] выполнена с результатом [" + str(res) + "]", "SQL Executor")


        if not res:
            return False
        return res[0]