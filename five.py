import random
def ordenar_numeros(numbers):
  num_a = random.randint(1,100)
  numb_b = random.randint(1,100)
  numb_c = random.randint(1,100)
print(f"Valores aleatórios gerados: A={num_a}, B={num_b}, C={num_c}")
  resultado_ordenado = ordenar_numeros(num_a, num_b, num_c)

print(f"Valores ordenados em ordem crescente: {resultado_ordenado}")
