import sys

n_testes = int(sys.stdin.readline())
trocas = []

for i in range(n_testes):
  num_clientes = int(sys.stdin.readline())
  senhas = []
  senhas_str = list(sys.stdin.readline().split())
  for pos in range(num_clientes):
      senhas.append(int(senhas_str[pos]))

  senhas_ord = sorted(senhas, reverse = True)
  troca_lugar = 0
  for j in range(num_clientes):
    if senhas[j] == senhas_ord[j]:
      troca_lugar += 1
  trocas.append(troca_lugar)

for k in range(len(trocas)):
  print(trocas[k])
