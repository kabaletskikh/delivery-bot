class Formater():
    def __init__(self, sv):
        self.sv = sv
        self.sv.trace("Модуль успешно подключен", "Formater")

    def sting_to_list(self, string):
        res = string.replace(',', "").split()
        self.sv.trace("string [" + string + "] to list [" + res + "]", "Formater")
        return res

    
    def list_to_string(self, l):
        for i in l:
            res += str(i) + ", "
        res = res[:-2]
        
        self.sv.trace("list [" + l + "] to string [" + res + "]", "Formater")
        return res