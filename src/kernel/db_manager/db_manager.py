from models import DbModels
from sql_translator import SqlTranslator
from formater import Formater
from supervisor import Supervisor

# TODO: отчеты супервизору
# TODO: правильно заполнить returning data в виде DTO и SQL requests в соответствии с БД в мини скриптах


class DbManager:
    sql
    models
    form

    def __init__(self):
        self.sv     = Supervisor("db_manager")
        self.sv.trace("Модуль успешно подключен", "Main DB Manager")
        self.sql    = SqlTranslator(self.sv)
        self.form   = Formater(self.sv)
        self.models = DbModels(self.sql, self.form, self.sv)