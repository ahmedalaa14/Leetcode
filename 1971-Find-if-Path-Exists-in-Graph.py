class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True
        if [source, destination] in edges:
            return True

        graph = defaultdict(set)
        for edge in edges:
            if (edge[0] == source and edge[1] == destination) or (
                edge[0] == source and edge[1] == destination
            ):
                return True
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        des_list = [graph[source]]
        visits = [False] * n
        while des_list:
            new_list = []
            for des in des_list:
                if destination in des:
                    return True
                for node in des:
                    if visits[node]:
                        continue
                    visits[node] = True
                    new_list.append(graph[node])
            des_list = new_list

        return False