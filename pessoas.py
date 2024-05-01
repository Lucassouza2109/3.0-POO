
import contas

class Pessoa: # Criacao da classe - Pessoa. 
    def __init__(self, nome: str, idade: int) -> None: # INIT com nome e idade. 
        self.nome = nome
        self.idade = idade

    @property # getter no python é uma Property. Utilizado para acessar um dado. Nesse caso acessar o atributo nome. 
    def nome(self):
        return self._nome

    @nome.setter # Utilizado para armazenar ou modificar um dado. Nesse caso o atributo nome. 
    def nome(self, nome: str):
        self._nome = nome

    @property # getter no python e uma Property. Utilizado para acessar um dado. Nesse caso acessar o atributo idade. 
    def idade(self):
        return self._idade

    @idade.setter # Utilizado para armazenar ou modificar um dado. Nesse caso o atributo idade.
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self): # e uma representacao textual do objeto quando ele e impresso. 
        class_name = type(self).__name__ #nome da classe do Objeto. 
        attrs = f'({self.nome!r}, {self.idade!r})' #string formatada. 
        return f'{class_name}{attrs}' # ira retornar o nome da classe e os atributos formatados, formando um representacao do objeto. 


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None #barra na vertical - OU. 


if __name__ == '__main__':
    c1 = Cliente('Luiz', 30)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Maria', 18)
    c2.conta = contas.ContaPoupanca(112, 223, 100)
    print(c2)
    print(c2.conta)