
def achando_proximo(coordenadas, maze,caminho):
    proxima_coordenadas = []
    if coordenadas[0]-1 >= 0 and maze[coordenadas[0]-1][coordenadas[1]] == caminho_livre:
        proxima_coordenadas.append((coordenadas[0]-1,coordenadas[1]))
        caminho.append((coordenadas[0]-1,coordenadas[1]))
        maze[coordenadas[0]-1][coordenadas[1]] = marcado
                
    if coordenadas[0]+1 < len(maze) and maze[coordenadas[0]+1][coordenadas[1]] == caminho_livre:
        proxima_coordenadas.append((coordenadas[0]+1,coordenadas[1]))
        caminho.append((coordenadas[0]+1,coordenadas[1]))
        maze[coordenadas[0]+1][coordenadas[1]] = marcado

    if coordenadas[1]+1 < len(maze[1]) and maze[coordenadas[0]][coordenadas[1]+1] == caminho_livre:
        proxima_coordenadas.append((coordenadas[0],coordenadas[1]+1))
        caminho.append((coordenadas[0],coordenadas[1]+1))
        maze[coordenadas[0]][coordenadas[1]+1] = marcado

    if coordenadas[1]-1 >= 0 and maze[coordenadas[0]][coordenadas[1]-1] == caminho_livre:
        proxima_coordenadas.append((coordenadas[0],coordenadas[1] -1))
        caminho.append((coordenadas[0],coordenadas[1]-1))
        maze[coordenadas[0]][coordenadas[1]-1] = marcado

    return proxima_coordenadas

def busca_profundidade(maze, pilha, visitados,caminho,inicio,fim):    
    pilha.append(inicio)
    while pilha:  
        n = pilha.pop()
        if n == fim:     
            return    
        proximo_passo = achando_proximo(n, maze,caminho)        
        for i in proximo_passo:
            if i in visitados:
                continue
            visitados.add(i)
            pilha.append(i)
            
maze = [
    ['+','#','+','+','+','+','+','+','+'],
    ['+','#','+','+','+','#','#','#','+'],
    ['+','#','#','#','+','#','+','#','+'],
    ['+','+','+','#','+','#','+','#','+'],
    ['+','#','#','#','#','#','#','+','+'],
    ['+','#','+','+','+','+','#','#','+'],
    ['+','#','#','+','+','#','+','#','+'],
    ['+','+','#','#','#','#','+','#','+'],
    ['+','+','+','+','+','+','+','+','+']
    ]


#obstaculo = '+'
caminho_livre = '#'
marcado = '@'

caminho = []
visitados = set()
pilha = []

inicio = (0,1)
fim = (7,7)
print('Sem resolver:')
for i in maze:
    print(i)

busca_profundidade(maze,pilha,visitados,caminho,inicio,fim)

print('')
print('Resolvido:')
for i in maze:
    print(i)
print('')
print('Visitados:')
print(visitados)
print('Caminho:')
print(caminho)