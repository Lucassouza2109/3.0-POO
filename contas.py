
import abc  # modelo para trabalhar com decorador abstrato. 

class Conta(abc.ABC): # CRIACAO DA CONTA - ABSTRATA.
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None: # construtor = init / agencia, conta, saldo --> tipados. 
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ... # metodo sacar

    def depositar(self, valor: float) -> float: # metodo depositar - com tipagem para retornar float . 
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None: # metodo detalhes - com tipagem string.
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')

    def __repr__(self): # e uma representacao textual do objeto quando ele e impresso. 
        class_name = type(self).__name__ #nome da classe do Objeto. 
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})' #string formatada. 
        return f'{class_name}{attrs}' # ira retornar o nome da classe e os atributos formatados, formando um representacao do objeto. 

class ContaPoupanca(Conta): # CRIACAO DA CONTA POUPANCA. 
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor # Verifica o valor: Pos - saque. 

        if valor_pos_saque >= 0: # trava para evitar que apos o saque a conta Poupanca fique zerada. 
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado') # Se o IF nao for atendido, ou seja, se o valor ficar menor que 0, o saque nao sera executado. 
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo

class ContaCorrente(Conta): # CRIACAO DA CONTA CORRENTE. 
    def __init__(
        self, agencia: int, conta: int,
        saldo: float = 0, limite: float = 0
    ): # INIT - semelhante a conta poupanca com o incremento do LIMITE. 
        super().__init__(agencia, conta, saldo) # minha Super-classe é CONTA e eu passo agencia, conta e saldo. 
        self.limite = limite # este atributo fica em conta correte. 

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite # limite maximo de saque = self.limite.

        if valor_pos_saque >= limite_maximo: # se saque for maior ou igual ao limite maximo. Permite seguir com o saque. 
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado') # caso o IF nao seja atingido - nao sera permitido seguir com o saque. 
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo

        def __repr__(self): # e uma representacao textual do objeto quando ele e impresso. 
            class_name = type(self).__name__ #nome da classe do Objeto. 
            attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})' #string formatada. 
            return f'{class_name}{attrs}' # ira retornar o nome da classe e os atributos formatados, formando um representacao do objeto. 

if __name__ == '__main__': # Permite executar o codigo dentro do modulo. E quando o modulo for importado o codigo nao sera executado .  
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(111, 222, 0, 100) # passado limite = 100
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
    print('##')