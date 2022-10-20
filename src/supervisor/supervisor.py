from abc import ABCMeta, abstractmethod
from re import sub
import time


class Eventer():
    __metaclass__ = ABCMeta

    @abstractmethod
    def trace():
        """tracing"""

    @abstractmethod
    def warning():
        """warning"""

    @abstractmethod
    def critical():
        """critical"""

    @abstractmethod
    def fatal():
        """fatality"""

    def get_datetime():
        return time.ctime(0)


    def submodule_mention(submodule):
        if submodule == False:
            return ""
        return "|" + submodule + "| "




class DbEvents(Eventer):
    def trace(self, text, sub):
        print("\n\n<DB Manager> on " + self.get_datetime() + ":\n" + self.submodule_mention(sub) + text)




class Supervisor():
    def __init__(self, requesting_module_name):
        self.module = requesting_module_name


    def trace(self, text, submodule_name=False):
        if self.module == "db_manager":
            DbEvents.trace(text, submodule_name)


    def warning(self, text):
        if self.module == "db_manager":
            DbEvents.warning(text)


    def critical(self, text):
        if self.module == "db_manager":
            DbEvents.critical(text)


    def fatal(self, text):
        if self.module == "db_manager":
            DbEvents.fatal(text)