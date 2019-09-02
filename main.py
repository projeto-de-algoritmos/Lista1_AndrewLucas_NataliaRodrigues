from graph import Graph

def main():
  print('hey')
  graph = Graph()
  options = graph.graph.keys()
  for user in options:
    print(user, end='\t')
  print('-'*80)
  first = input('Qual nome do primeiro usuário?')
  second = input('Qual nome do segundo usuário?')
  print('-'*80)
  dist = graph.distance(first,second)
  print('A distância entre {} e {} é de {}'.format(first, second, dist))

main()