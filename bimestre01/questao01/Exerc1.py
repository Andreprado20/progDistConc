import threading
import time


class ContaBancaria:
    def __init__(self, numero: str, titular: str, saldo_inicial=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial
        self.lock = threading.Lock()

    def sacar(self, valor, thread_name):
        with self.lock:
            print(f"{thread_name} tentando sacar R${valor}. Saldo atual: R${self.saldo}")
            if self.saldo >= valor:
                print(f"{thread_name}: Saldo antes do saque: R${self.saldo}")
                self.saldo -= valor
                print(f"{thread_name}: Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
            if self.saldo <= 0:
                print(f"{thread_name}: Saldo insuficiente para sacar R${valor}. Saldo atual: R${self.saldo}")
                if self.saldo < 0:
                    print(f"Alerta: Saldo negativo de R${self.saldo} na conta {self.numero}.")

    def depositar(self, valor, thread_name):
        with self.lock:
            self.saldo += valor
            print(f"{thread_name}: Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")


class ThreadGastadora(threading.Thread):
    def __init__(self, conta):
        threading.Thread.__init__(self)
        self.conta = conta

    def run(self):
        while True:
            time.sleep(3)
            self.conta.sacar(10, self.name)


class ThreadEsperta(threading.Thread):
    def __init__(self, conta):
        threading.Thread.__init__(self)
        self.conta = conta

    def run(self):
        while True:
            time.sleep(6)
            self.conta.sacar(50, self.name)


class ThreadEconomica(threading.Thread):
    def __init__(self, conta):
        threading.Thread.__init__(self)
        self.conta = conta

    def run(self):
        while True:
            time.sleep(12)
            self.conta.sacar(5, self.name)


class ThreadPatrocinadora(threading.Thread):
    def __init__(self, conta):
        threading.Thread.__init__(self)
        self.conta = conta

    def run(self):
        while True:
          if self.conta.saldo <= 0:
            print(f"{self.name}: Conta {self.conta.numero} zerada ou negativa, depositando R$100")
            self.conta.depositar(100, self.name)


if __name__ == '__main__':
    conta = ContaBancaria(numero="123456", titular="Cliente 1", saldo_inicial=100)

    gastadora = ThreadGastadora(conta)
    esperta = ThreadEsperta(conta)
    economica = ThreadEconomica(conta)
    patrocinadora = ThreadPatrocinadora(conta)

    gastadora.start()
    esperta.start()
    economica.start()
    patrocinadora.start()

    gastadora.join()
    esperta.join()
    economica.join()
    patrocinadora.join()
