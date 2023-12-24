from data import Data
from cliente import Cliente


class Conta: 
    def __init__(self,numero_conta, titular, saldo, limite): 
      self.__numero_conta = numero_conta
      self.__titular = titular 
      self.__saldo = saldo 
      self.__limite = limite

    def extrato(self): 
       print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor): 
       self.__saldo += valor 
       

    def __pode_sacar(self,valor_a_sacar): 
         valor_disponivel_a_sacar = self.__saldo + self.__limite
         return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor): 
      if(self.__pode_sacar(valor)):
         self.__saldo -= valor
      else: 
         print(f"O valor {valor} passou o limite")

    def transferir(self, valor, destino):
       self.sacar(valor)
       destino.depositar(valor)

    def get_saldo(self):
       return self.__saldo
    
    def get_titular(self): 
       return self.__titular
    
    @property
    def limite(self): 
       return self.__limite
    
    @limite.setter
    def limite(self, limite): 
       self.__limite = limite 


  

    
   
conta = Conta(123, "Boby", 5000, 5000)
conta2 = Conta(921, "Pedro", 2000, 7000)
data = Data(21,11,2007)
data.formatar()
conta.transferir(2000, conta2)
conta2.extrato()

cliente = Cliente("Boby")

print(cliente.nome)

print(conta.limite)

conta.limite = 7000 

print(conta.limite)


