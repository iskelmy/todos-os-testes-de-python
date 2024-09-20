class CalculadoraTarifas:
    @staticmethod
    def calcular_tarifa_base():
        return 5  # Tarifa base de R$ 5 para todas as contas

    @staticmethod
    def calcular_tarifa_transacao(numero_transacoes):
        if numero_transacoes > 10:
            return (numero_transacoes - 10) * 1.5  # R$ 1,50 por transação adicional
        else:
            return 0

    @staticmethod
    def calcular_tarifa_saldo(saldo):
        if saldo < 1000:
            return 10  # Tarifa de R$ 10 para saldos abaixo de R$ 1000
        else:
            return 0

class ContaBancaria:
    def __init__(self, numero_conta, saldo=0, numero_transacoes=0):
        self.__numero_conta = numero_conta
        self.__saldo = saldo
        self.__numero_transacoes = numero_transacoes

    def depositar(self, valor):
        self.__saldo += valor
        self.__numero_transacoes += 1

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            self.__numero_transacoes += 1
            return True
        else:
            return False

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        else:
            return False

    def consultar_saldo(self):
        return self.__saldo

    def calcular_tarifa(self):
        tarifa_base = CalculadoraTarifas.calcular_tarifa_base()
        tarifa_transacao = CalculadoraTarifas.calcular_tarifa_transacao(self.__numero_transacoes)
        tarifa_saldo = CalculadoraTarifas.calcular_tarifa_saldo(self.__saldo)
        return tarifa_base + tarifa_transacao + tarifa_saldo

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, saldo=0, numero_transacoes=0):
        super().__init__(numero_conta, saldo, numero_transacoes)

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, saldo=0, numero_transacoes=0):
        super().__init__(numero_conta, saldo, numero_transacoes)

class ContaUniversitaria(ContaBancaria):
    def __init__(self, numero_conta, saldo=0, numero_transacoes=0):
        super().__init__(numero_conta, saldo, numero_transacoes)

    def calcular_tarifa(self):
        return 0  # Conta universitária não possui tarifas


# Exemplo de uso
conta_corrente1 = ContaCorrente("12345")
conta_corrente1.depositar(1000)

conta_corrente2 = ContaCorrente("54321")
conta_corrente2.depositar(500)

conta_corrente1.transferir(conta_corrente2, 200)

print("Saldo da conta corrente 1:", conta_corrente1.consultar_saldo())
print("Saldo da conta corrente 2:", conta_corrente2.consultar_saldo())
