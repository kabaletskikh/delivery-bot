import executor


class SqlTranslator():
    def __init__(self, sv):
        self.sv = sv
        self.sv.trace("Модуль успешно подключен", "SQL Translator")
        self.executor = executor.Executor(sv)


    def get_real_table_name(self, table):
        res = "database_" + table
        self.sv.trace("Real table name is " + res, "SQL Translator")


    def delete_by_sign(self, table, sign, content):
        command = "DELETE FROM " + self.get_real_table_name(table) + " WHERE " + str(sign) + "='" + str(content) + "';"
        res = self.executor.execute(command)
        self.sv.trace("SQL instruction [" + command + "] executed with status [" + str(res) + "]", "SQL Translator")


    def fetch(self, table, amount=1):
        command = "SELECT * FROM " + self.get_real_table_name(table) + ";"
        res = self.executor.execute(command, amount_to_fetch=amount)
        self.sv.trace("SQL instruction [" + command + "] executed with status [" + str(res) + "]", "SQL Translator")


    def fetch_max_id(self, table, idname):
        command = "SELECT MAX(`" + idname + "`) FROM `" + self.get_real_table_name(table) + "`;"
        res = (self.executor.execute(command, amount_to_fetch=1))[0]
        self.sv.trace("SQL instruction [" + command + "] executed with status [" + str(res) + "]", "SQL Translator")


    def fetch_by_sign(self, table, sign, content, amount=1):
        command = "SELECT * FROM " + self.get_real_table_name(table) + " WHERE " + str(sign) + "='" + str(content) + "';"
        res = self.executor.execute(command, amount_to_fetch=amount)
        self.sv.trace("SQL instruction [" + command + "] executed with status [" + str(res) + "]", "SQL Translator")


    def update_row(self, table, sign, value, param, newContent):
        command = "UPDATE " + self.get_real_table_name(table) + " SET " + str(param) + " = '" + str(newContent) + "' WHERE " + str(sign) + " = '" + str(value) + "';"
        res = self.executor.execute(command)
        self.sv.trace("SQL instruction [" + command + "] executed with status [" + str(res) + "]", "SQL Translator")


    def insert(self, table, dataCortege):
        questionMarks = "?"
        for i in range(0, len(dataCortege)-1):
            questionMarks += ",?"

        command = "INSERT INTO " + self.get_real_table_name(table) + " VALUES(" + questionMarks + ");"
        res = self.executor.execute(command, dataCortege)
        self.sv.trace("SQL instruction [" + command + "] executed with status [" + str(res) + "]", "SQL Translator")


    def create_new(self, table, data):
        newData = []
        newData.append(data[0])
        newData.append(data[0])

        for i in range(1, len(data)):
            newData.append(data[i])

        res = self.insert(table, newData)
        self.sv.trace("Cteating new [" + table + "] with [" + str(data) + "]", "SQL Translator")