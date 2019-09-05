from graph import Graph

def main():
  graph = Graph()

  print("O grafo gerado foi: ")
  print("\n")
  graph.DFS()
  print("\n")
  
  print('-' * 80)
  
  first = input('Digite o primeiro nome de usuário: ')
  second = input('Digite o segundo nome de usuário: ')
  
  print('-' * 80)

  print("\n")
  print("Distância entre {} e {}: ".format(first, second), end=" ")
  print(graph.distance(first, second))
  print("\n")

main()