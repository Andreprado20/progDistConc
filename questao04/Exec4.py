import threading

class SomaThread(threading.Thread):
    """
  Classe que implementa uma thread para calcular a soma de uma parte de um vetor.

  Atributos:
    vetor: O vetor de números inteiros.
    inicio: O índice do início da parte do vetor a ser somada.
    fim: O índice do fim da parte do vetor a ser somada.
    resultado: Pra armazenar o resultado de forma compartilhada.
    lock: Um objeto AtomicInteger para armazenar o resultado parcial da soma.
  """
    
    def __init__(self, vetor, inicio, fim, resultado, lock):
        threading.Thread.__init__(self)
        self.vetor = vetor
        self.inicio = inicio
        self.fim = fim
        self.resultado = resultado
        self.lock = lock

    def run(self):
        soma_parcial = sum(self.vetor[self.inicio:self.fim])
        print(f"Thread calculou soma parcial de {self.inicio} a {self.fim}: {soma_parcial}")
        
        # Adquirir o lock antes de atualizar o resultado total
        with self.lock:
            self.resultado[0] += soma_parcial

def soma_vetor(vetor, num_threads):
    resultado = [0]  # Lista para armazenar o resultado total
    lock = threading.Lock()
    tamanho_subvetor = len(vetor) // num_threads
    threads = []

    for i in range(num_threads):
        inicio = i * tamanho_subvetor
        fim = inicio + tamanho_subvetor if i < num_threads - 1 else len(vetor)
        thread = SomaThread(vetor, inicio, fim, resultado, lock)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return resultado[0]

if __name__ == "__main__":
    vetor = list(range(1, 100000001))  # vetor de 1 milhão de números inteiros (defini 100M, pra demorar mais)
    num_threads = 4  # número de threads para calcular a soma
    resultado = soma_vetor(vetor, num_threads)
    print("A soma do vetor é:", resultado)
