import os
from concurrent.futures import ThreadPoolExecutor

def processar_arquivo(caminho_arquivo):
    formandos = []
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            matricula, nome, curso, flag = linha.strip().split(',')
            if flag.strip().upper() == 'CONCLUIDO':
                formandos.append((matricula.strip(), nome.strip(), curso.strip()))
    return formandos

def encontrar_formandos(diretorio):
    formandos = []
    arquivos = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith('.txt')]
    
    with ThreadPoolExecutor() as executor:
        resultados = executor.map(processar_arquivo, arquivos)
        
    for resultado in resultados:
        formandos.extend(resultado)
    
    return formandos

if __name__ == "__main__":
    diretorio_dos_arquivos = r"C:\Users\Roberto Bastos\Downloads\Trabalho Moreno"  # Substitua pelo caminho real do diretório onde os arquivos estão
    formandos = encontrar_formandos(diretorio_dos_arquivos)
    
    for matricula, nome, curso in formandos:
        print(f"Matrícula: {matricula}, Nome: {nome}, Curso: {curso}")
