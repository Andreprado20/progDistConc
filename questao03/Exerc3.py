import concurrent.futures
import time

def get_pipoca():
    time.sleep(2)
    return "Pipoca Pronta"

def get_refrigerante():
    time.sleep(1.5)
    return "Refrigerante Pronto"

def lanche_pronto():
    return "Lanche Pronto! Bom apetite!"

def main():

    print("Pedido feito ao Balcão!!")
    print("Preparando...")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_pipoca = executor.submit(get_pipoca)
        future_refrigerante = executor.submit(get_refrigerante)

        pipoca = future_pipoca.result()
        refrigerante = future_refrigerante.result()

        print(pipoca)
        print(refrigerante)
        print(lanche_pronto())

if __name__ == "__main__":
    main()
