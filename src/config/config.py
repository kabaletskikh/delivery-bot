import json
import sys


class Config:
    def __init__(self):
        with open(sys.path[0] + '/config/config.json') as f:
            self.info = json.load(f)


    def get(self, module_name, param_name=False):
        if not param_name:
            return self.info[module_name]

        return self.info[module_name][param_name]