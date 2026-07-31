from collections import defaultdict

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    for course, pre in prerequisites:
        graph[course].append(pre)

    state = {}

    def dfs(course):
        if state.get(course) == "visiting":
            return False
        if state.get(course) == "done":
            return True
        state[course] = "visiting"
        for pre in graph[course]:
            if not dfs(pre):
                return False
        state[course] = "done"
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True

if __name__ == "__main__":
    print(canFinish(2, [[1,0]]))
    print(canFinish(2, [[1,0],[0,1]]))
