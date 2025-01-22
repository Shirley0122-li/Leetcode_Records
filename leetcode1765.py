from collections import deque 
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        water = []
        neighbor = []
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    isWater[i][j] = 'x'
                    water.append((i, j))
                    for nei_i, nei_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0 <= nei_i < len(isWater) and 0 <= nei_j < len(isWater[0]):
                            neighbor.append((nei_i, nei_j))
        
        height = 1
        while neighbor:
            new_neighbor = []
            for nei in neighbor:
                i, j = nei
                if isWater[i][j] == 0:
                    isWater[i][j] = height
                    for nei_i, nei_j in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0 <= nei_i  < len(isWater) and 0 <= nei_j < len(isWater[0]):
                            new_neighbor.append((nei_i, nei_j))
            neighbor = new_neighbor
            height += 1
        
        for w in water:
            isWater[w[0]][w[1]] = 0
        
        return isWater