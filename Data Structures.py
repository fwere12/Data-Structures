#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List
import sys

def parse_network(input_network: str) -> List[List[int]]:
    rows = input_network.strip().split('\n')
    network = []
    for row in rows:
        row_values = []
        for cost in row.split(','):
            if cost == '-':
                row_values.append(sys.maxsize)
            elif cost.strip():
                row_values.append(int(cost))
        network.append(row_values)
    return network

def minimum_spanning_tree(network: List[List[int]]) -> int:
    num_nodes = len(network)
    visited = [False] * num_nodes
    min_cost = [sys.maxsize] * num_nodes
    min_cost[0] = 0
    total_cost = 0

    for _ in range(num_nodes):
        min_node = -1
        for node in range(num_nodes):
            if not visited[node] and (min_node == -1 or min_cost[node] < min_cost[min_node]):
                min_node = node
        
        visited[min_node] = True
        total_cost += min_cost[min_node]

        for node in range(num_nodes):
            if not visited[node] and node < len(network[min_node]) and network[min_node][node] < min_cost[node]:
                min_cost[node] = network[min_node][node]
    
    return total_cost

def maximum_saving(input_network: str) -> int:
    network = parse_network(input_network)
    total_cost = sum(sum(cost for cost in row if cost != sys.maxsize) for row in network) // 2
    minimum_spanning = minimum_spanning_tree(network)
    return total_cost - minimum_spanning

# Usage example
if __name__ == "__main__":
    input_network = '''-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,,29,-
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
-,-,-,21,9,25,-
'''
    max_saving = maximum_saving(input_network)
    print(max_saving)


# In[ ]:




