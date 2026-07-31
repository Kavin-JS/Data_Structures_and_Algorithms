class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None
    oldToNew = {}

    def dfs(n):
        if n in oldToNew:
            return oldToNew[n]
        copy = Node(n.val)
        oldToNew[n] = copy
        for neighbor in n.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    return dfs(node)

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n1, n2]
    cloned = cloneGraph(n1)
    print(cloned.val, [n.val for n in cloned.neighbors])
