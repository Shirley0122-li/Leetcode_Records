class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        res = float("inf")
        seen = defaultdict(list)

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                p1, p2 = points[i], points[j]
                center_x, center_y = (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
                distance2 = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
                if (center_x, center_y, distance2) in seen:
                    for xx, yy in seen[(center_x, center_y, distance2)]:
                        print(xx, yy)
                        res = min(res, sqrt(((p1[0]-xx)**2+(p1[1]-yy)**2)*((p2[0]-xx)**2+(p2[1]-yy)**2)))
                
                seen[(center_x, center_y, distance2)].append((p1[0], p1[1]))
        
        if res == float("inf"):
            return 0
        
        return res