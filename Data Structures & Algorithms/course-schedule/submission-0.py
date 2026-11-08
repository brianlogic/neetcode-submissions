class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adjacencyList[v].append(u)
        
        # 0 unvisited, 1 in current path, 2 done
        state = [0] * numCourses

        def dfs(u):
            if state[u] == 1:
                return True
            if state[u] == 2:
                return False
            state[u] = 1
            for v in adjacencyList[u]:
                if dfs(v):
                    return True
            state[u] = 2
            return False
        
        return not any(dfs(u) for u in range(numCourses))

