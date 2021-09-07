#
from _pytest.compat import safe_isclass

class Conta:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo
        self.__limite = 50

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            self.__saldo += 0
        
        elif valor == 0:
            self.__saldo += 0
            return None
    
        else:
            self.__saldo += valor
        
    def sacar(self, valor):     
        # if (self.saldo + self.limite) > 0:
        if (self.saldo + self.limite) > valor:
            self.__saldo -= valor
            return True

        else:
            return False
    
    def conta_teste_dois(self):
        return '000123-02'

    def transferir(self, numero, valor):
        if numero == self.conta_teste_dois():
            if valor <= (self.saldo + self.limite):
                self.sacar(valor)
                return True 
            else:
                return False
        else:
            return False
    
    def extrato(self, validate):
        if validate == 0:
            return False
        else:
            return f'''============================
            \033[1;36mEXTRATO\033[m
    ----------------------------
    Número: \033[1;32m{self.numero}\033[m
    Nome: \033[1;32m{self.titular}\033[m
    Saldo: \033[1;32m{self.saldo}\033[m
    ============================'''
