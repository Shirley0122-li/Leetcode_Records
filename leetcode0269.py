class Solution:
    def alienOrder(self, words: List[str]) -> str:
        ## step 1: build the graph
        order_dict = defaultdict(set)
        in_degree = {c:0 for word in words for c in word}

        for i in range(len(words) - 1):
            prev, cur = words[i], words[i+1]
            min_len = min(len(prev), len(cur))
            if prev[:min_len] == cur[:min_len] and len(prev) > len(cur):
                return ""
            
            for c1, c2 in zip(prev[:min_len], cur[:min_len]):
                if c1 != c2:
                    if c2 not in order_dict[c1]:
                        order_dict[c1].add(c2)
                        in_degree[c2] += 1
                    break
        
        ## step 2: assemble the word
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for nei in order_dict[char]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        if len(result) < len(in_degree):
            return ""
        
        return "".join(result)