# ### Intro to Graphs in Python

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict: ", self.graph_dict)
    
    def get_path(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = [] # List to store all paths from start to end

        for node in self.graph_dict[start]:  #for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths
    def get_shortest_path(self, start, end, path = []):
        path = path + [start]
        if start not in self.graph_dict:
            return None
        if start == end:
            return path
        
        shortest_path = None
        
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

routes = [
    ("Kigali", "Paris"),
    ("Kigali", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto")
]

route_graph = Graph(routes)



start = "Kigali"
end   = "Kigali"
print(f"Path between {start} and {end}: {route_graph.get_path(start, end)}")


# When start is end-node only # Currently there is no flight starting from Kigali, in that case, the path should be blank
start = "Toronto"
end   = "Kigali"
print(f"Path between {start} and {end}: {route_graph.get_path(start, end)}")


# true path
start = "Kigali"
end   = "New York"
print(f"Path between {start} and {end}: {route_graph.get_path(start, end)}")

print(f"Shortest Path between {start} and {end}: {route_graph.get_shortest_path(start, end)}")

# true path
start = "Paris"
end   = "New York"
print(f"Shortest Path between {start} and {end}: {route_graph.get_shortest_path(start, end)}")


