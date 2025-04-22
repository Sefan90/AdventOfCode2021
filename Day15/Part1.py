map = [[int(j) for j in i.strip()]for i in open('testinput.txt').readlines()]
graph = {}
for x in range(len(map)):
    for y in range(len(map[0])):
        if x == 0 and y == 0:
            graph[str(x)+","+str(y)] = [str(x+1)+","+str(y),str(x)+","+str(y+1)]
        elif x == 0:
            graph[str(x)+","+str(y)] = [str(x+1)+","+str(y),str(x)+","+str(y+1),str(x)+","+str(y-1)]
        elif y == 0:
            graph[str(x)+","+str(y)] = [str(x+1)+","+str(y),str(x-1)+","+str(y),str(x)+","+str(y+1)]
        else:
            graph[str(x)+","+str(y)] = [str(x+1)+","+str(y),str(x-1)+","+str(y),str(x)+","+str(y+1),str(x)+","+str(y-1)]
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0) 
        print (m, end = " ") 
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)   

def part1():
    bfs(visited,graph,"0,0")


part1()
#531 high