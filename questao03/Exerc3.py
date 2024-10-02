import concurrent.futures
import time

def get_pipoca():
    # Simula o tempo de preparo da pipoca
    time.sleep(2)
    return "Pipoca Pronta"

def get_refrigerante():
    # Simula o tempo de preparo do refrigerante
    time.sleep(1.5)
    return "Refrigerante Pronto"

def lanche_pronto():
    return "Lanche Pronto! Bom apetite!"

def main():

    print("Pedido feito ao Balcão!!")
    print("Preparando...")
    # Usamos ThreadPoolExecutor para executar as tarefas de forma concorrente
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Inicia as tarefas de pipoca e refrigerante
        future_pipoca = executor.submit(get_pipoca)
        future_refrigerante = executor.submit(get_refrigerante)

        # Aguarda ambas as tarefas serem concluídas
        pipoca = future_pipoca.result()
        refrigerante = future_refrigerante.result()

        # Exibe as mensagens

        
        print(pipoca)
        print(refrigerante)
        print(lanche_pronto())

if __name__ == "__main__":
    main()
