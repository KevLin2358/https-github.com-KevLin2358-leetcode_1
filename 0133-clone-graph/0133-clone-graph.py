"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        
        node_map, visited, stack = dict(), set(), deque([node])
        
        while stack:
            current_node = stack.pop()
            
            if current_node in visited:
                continue
                
            visited.add(current_node)
            
            if current_node not in node_map:                
                node_map[current_node] = Node(current_node.val)
                #key is originial node, value is the clone
                
            for neigh in current_node.neighbors:
                
                if neigh not in node_map:
                    node_map[neigh] = Node(neigh.val)
                    
                node_map[current_node].neighbors.append(node_map[neigh])
                stack.append(neigh)
                
        return node_map[node]