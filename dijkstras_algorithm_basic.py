# 그래프
infinity = float("inf")
graph ={}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph['fin'] = {}

# 비용
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] =infinity

# 부모
parents = {}
parents['a'] = "start"
parents['b'] = "start"
parents['fin'] = None

processed = []
def find_lowest_cost_node(costs=dict()):
    """
    1. 가장 싼 정점 찾기: 비용 중 가장 낮은 비용을 지닌 노드 리턴
    :param costs:
    :return:
    """
    lowest_node = None
    lowest_cost = infinity
    for key, value in costs.items():
        if value < lowest_cost and key not in processed:
            lowest_node = key
            lowest_cost = value
    return lowest_node

# 다익스트라 알고리즘
node = find_lowest_cost_node(costs)        # 1. 가장 싼 정점 찾기
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for neighbor in neighbors.keys():      # 2. 1 에서 얻은 정점 중 이웃 정점에 대해 현재 가격보다 싼 경로가 존재하는지 확인 후, 있다면 가격을 수정합니다.
        new_cost = cost + graph[node][neighbor]
        if new_cost < costs[neighbor]:
            costs[neighbor] = new_cost
            parents[neighbor] = node
    processed.append(node)
    node = find_lowest_cost_node(costs=costs)    # 다시 1를 반복


print("Cost from the start to each node:")
print(costs)
print("Parents from the start to each node:")
print(parents)

