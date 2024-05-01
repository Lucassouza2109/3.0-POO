import contas # importa o modulo contas . 
import pessoas # importa o modulo pessoas . 


class Banco: # criada classe Banco. 
    def __init__(
        self,
        agencias: list[int] | None = None, 
        # tipagem = agencia como uma lista de inteiros, se nao (barra vertical), caso nao seja fornecido valor = None. 
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or [] 
        # Inicializa o atributo agencias da instância do banco com a lista de agências fornecida ou uma lista vazia, se nenhum argumento for fornecido. 
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta): 
        # Define um método interno _checa_agencia que verifica se a agência associada à conta está presente na lista de agências do banco.
        if conta.agencia in self.agencias:
            # Verifica se a agência associada à conta fornecida está presente na lista de agências do banco.
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False
    
    
    def _checa_cliente(self, cliente):
        # def _checa_cliente(self, cliente): ...: Define um método interno _checa_cliente que verifica se o cliente está presente na lista de clientes do banco.
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        # def _checa_conta(self, conta): ...: Define um método interno _checa_conta que verifica se a conta está presente na lista de contas do banco.
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        # def _checa_se_conta_e_do_cliente(self, cliente, conta): ...: Define um método interno _checa_se_conta_e_do_cliente que verifica se a conta pertence ao cliente.
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        # Define um método autenticar que verifica se um cliente pode autenticar usando uma conta específica.
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)
        # Retorna True se todas as condições de autenticação forem atendidas e False caso contrário.

    def __repr__(self):
        # Define um método __repr__ que retorna uma representação de string da instância do banco, mostrando suas agências, clientes e contas.
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    # if __name__ == '__main__': ...: Verifica se o módulo está sendo executado como o programa principal. Se for, ele executa o código abaixo, que cria algumas instâncias de clientes, contas e um banco, adiciona os clientes e contas ao banco e realiza algumas operações bancárias.

    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)