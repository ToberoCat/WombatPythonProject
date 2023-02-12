import yaml
import os

RESOURCE_PATH = "res" # Default resource path
HYPERPARAMS_PATH = os.path.join(RESOURCE_PATH, "hyperparams")


class HyperParams:
    def __init__(self, file: str):
        self.file = file
        self.__yml = self.__read_yml()

    def get_int(self, param: str) -> int:
        return self.get(param)

    def get_int_default(self, param: str, default: int) -> int:
        return self.get_default(param, default)

    def get_string(self, param: str) -> str:
        return self.get(param)

    def get_string_default(self, param: str, default: str) -> str:
        return self.get_default(param, default)

    def get(self, param: str):
        return self.get_default(param, None)

    def get_default(self, param: str, default):
        return self.__yml.get(param, default)

    def __read_yml(self):
        with open(self.file, "r+") as stream:
           try:
               return yaml.safe_load(stream)
           except yaml.YAMLError as exc:
               print(exc)
               return {}

def initialise(resource_path):
    RESOURCE_PATH = resource_path

def get_hyperparameters(name: str) -> HyperParams:
    return HyperParams(os.path.join(HYPERPARAMS_PATH, name + ".yml"))