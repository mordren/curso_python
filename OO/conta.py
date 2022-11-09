

class Conta():
    
    def __init__(self, numero, titular, saldo, limite):
        print('construindo objecto...')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite        
        
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor          

    def __pode_sacar(self, valor):
        valor_maximo = self.limite+self.saldo
        if(valor_maximo >= valor):
            return True
        else:
            return False
    
    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):
        self.__limite = valor
    
    @staticmethod
    def codigo_banco():
        return '001'
        
conta = Conta(123, 'João', 120, 1000)
print(conta.codigo_banco)