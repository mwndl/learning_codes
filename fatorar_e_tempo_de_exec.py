import time

def soma1(n):
    soma = 0

    for i in range(n + 1):
        soma = soma + i
    return soma

def soma2(n):
    return (n * (n + 1)) / 2

print("Qual metodo você deseja utilizar?")
metodo = int(input("Digite 1 ou 2: "))

if metodo == 1:
    met = soma1
elif metodo == 2:
    met = soma2
else:
    print("Ocorreu um erro.")

valor = int(input("Digite o numero para fatorar: "))
print("Processando solicitação, aguarde alguns instantes...")
start_time = time.time()
resultado = met(valor)
end_time = time.time()
exec_time = end_time - start_time
print(f'Resultado: {resultado}')
print(f'Tempo de execução: {exec_time}')

