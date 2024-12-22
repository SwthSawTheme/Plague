from pymem.process import *
from pymem.exception import *
from pymem import *
import json

with __builtins__.open("settings.json","r") as arquivo:
    data = json.load(arquivo)
    name = data["module"]

pm = Pymem("PlagueIncEvolved.exe")
module = module_from_name(pm.process_handle,name).lpBaseOfDll

def getPointer(base, offsets):
    # Lê o endereço base na memória do processo
    addr = pm.read_ulonglong(base)
    # Itera sobre os offsets fornecidos para calcular o endereço final
    for offset in offsets:
        if offset != offsets[-1]:  # Se não for o último offset, continua o cálculo
            addr = pm.read_ulonglong(addr + offset)
    # Adiciona o último offset para obter o endereço final
    addr += offsets[-1]
    return addr  # Retorna o endereço final calc

def addDNA():
    endereco = data["endereco"]
    offsets = [int(f"0x{offset}",16) for offset in data["offsets"]]
    return pm.write_int(getPointer(module+endereco,offsets))