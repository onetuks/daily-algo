from collections import deque

def dijstra(graph, gates, summits) : 
	distance = {node : float('inf') for node in graph}

	queue = deque([])
	for gate in gates : 
		distance[gate] = 0
		queue.append([distance[gate], gate])

	while queue :
		curr_dist, curr_dest = queue.popleft()

		# 기존 거리보다 더 큰 값은 볼 필요가 없음
		if curr_dist > distance[curr_dest] : 
			continue

		for next_dest, next_dist in graph[curr_dest].items() :
			# 다음 경로까지 거리
			dist = max(next_dist, curr_dist)
			# 다음 경로까지 거리가 기존에 구한 다음 노드로의 거리보다 작으면 갱신 및 큐에 추가
			if dist < distance[next_dest] : 
				distance[next_dest] = dist
				if next_dest not in summits : 
					queue.append([dist, next_dest])

	return distance

def solution(n, paths, gates, summits):
	graph = {i : dict() for i in range(1, n+1)}
	for x, y, c in paths :
		graph[x][y] = c
		graph[y][x] = c

	answer = [float('inf'), float('inf')]
	distance = dijstra(graph, gates, set(summits))
	# print(distance)
	for dest in distance.keys() : 
		if dest in summits and distance[dest] < answer[1] :
			answer = [dest, distance[dest]]

	return answer

def main() :
	testcase = [
		[6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1, 3],[5],[5, 3]],
		
		[7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],[1],[2, 3, 4],[3, 4]],
		
		[7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],[3, 7],[1, 5],[5, 1]],
		
		[5,[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],[1, 2],[5],[5, 6]]
	]

	for n, paths, gates, summits, result in testcase :
		print("내가 만든 솔루션 : ", solution(n, paths, gates, summits))
		print("정답 : ", result)
		print()

main()