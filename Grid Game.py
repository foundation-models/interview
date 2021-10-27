from unittest import TestCase, main
import collections


def find_neighbors(grid, node_index):
    i, j = node_index
    if i ==len(grid) or j == len(grid[0]):
        return None
    result =  []
    direction = [[0,1],[1,0]]   
    for di, dj in direction:  
        if i + di <  len(grid) and j + dj < len(grid[0]):
            result.append( (i + di, j + dj) )
    return result

def calculate_point(graph, path):
    result = 0
    for i, j in path:
        result += graph[i][j]
    print(result)
    return result

def BFS(graph):
    
    queue = [[(0,0)]]
    optimizer = {}
    
    while len(queue) > 0:
        path = queue.pop(0)
        neighbors = find_neighbors(graph, path[-1])
        if neighbors is None or not neighbors:
            optimizer[calculate_point(graph,  path)] = path
        for neighbor in neighbors:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
            
    return collections.OrderedDict(sorted(optimizer.items()))
    

def DFS(graph):
    
    path = [(0,0)]
    optimizer = {}
    
    def dfs(graph, path, optimizer):
        neighbors = find_neighbors(graph, path[-1])
        if neighbors is None or not neighbors:
            optimizer[calculate_point(graph,  path)] = path
            return
        for neighbor in neighbors:
            new_path = list(path)
            new_path.append(neighbor)
            dfs(graph, new_path, optimizer)
            
    dfs(graph, path, optimizer)
    return collections.OrderedDict(sorted(optimizer.items()))
    

def grid_game(grid):
    direction = [[0,1],[1,0]]
    def next_move(grid, i = 0, j = 0):
        if i ==2 or j == len(grid[0]):
            return None, None
        if i == 1 and j == len(grid[0]) - 1:
            print("final")
            return grid[i][j], [(i,j)]
        points = 0
        path = []
        for di, dj in direction:
            next_point, new_path = next_move(grid, i + di, j + dj)
            if new_path is not None:
                path = new_path
            if next_point is not None:            
                if next_point + grid[i][j] > points:
                    path.append((i,j))
                    print(path)
                    points = next_point + grid[i][j]
                    print(points)
        return points, path
    
    # points, path = next_move(grid)
    # print(path)
    # points = BFS(grid)
    points = DFS(grid)
    max = list(points.keys())[-1]
    for i, j in points[max]:
        grid[i][j] = 0
    print(grid)
    # points = BFS(grid)
    points = DFS(grid)
    max = list(points.keys())[-1]    
    return max

class TestSoltuin(TestCase):
    
    def test_solution(self):
        self.assertEqual(grid_game([[2,5,4],[1,5,1]]), 4)
        self.assertEqual(grid_game([[3,3,1],[8,5,2]]), 4)
        self.assertEqual(grid_game([[1,3,1,15],[1,3,3,1]]), 7)
        self.assertEqual(grid_game([[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]), 63)


if __name__ == "__main__":
    main()