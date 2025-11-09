#!/usr/bin/env python3
"""
distance_vector.py
Simple Distance Vector Routing implementation using an adjacency (cost) matrix.
- Use a large value (INF) for no direct link.
- Program iterates until routing tables converge.
"""

INF = 10**9

def read_cost_matrix():
    nodes = int(input("Enter number of nodes: ").strip())
    print("Enter cost matrix (use -1 for no direct link).")
    mat = []
    for i in range(nodes):
        row = list(map(int, input().strip().split()))
        if len(row) != nodes:
            raise ValueError("Each row must have exactly %d integers" % nodes)
        # convert -1 to INF, ensure diagonal 0
        for j in range(nodes):
            if row[j] < 0:
                row[j] = INF
        row[i] = 0
        mat.append(row)
    return mat

def init_tables(cost):
    n = len(cost)
    dist = [[INF]*n for _ in range(n)]
    next_hop = [[None]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
                next_hop[i][j] = None
            elif cost[i][j] < INF:
                dist[i][j] = cost[i][j]
                next_hop[i][j] = j        # directly reachable: next hop is j
            else:
                # unreachable initially
                dist[i][j] = INF
                next_hop[i][j] = None
    return dist, next_hop

def distance_vector(cost):
    n = len(cost)
    dist, next_hop = init_tables(cost)

    changed = True
    iter_count = 0
    # iterate until no changes (convergence)
    while changed:
        iter_count += 1
        changed = False
        # For every source node i
        for i in range(n):
            # For every intermediate (neighbor or any) k
            for k in range(n):
                if dist[i][k] == INF or k == i:
                    continue
                # Try to use k's vector to improve routes from i
                for j in range(n):
                    if dist[k][j] == INF:
                        continue
                    new_cost = dist[i][k] + dist[k][j]
                    if new_cost < dist[i][j]:
                        dist[i][j] = new_cost
                        # next hop from i to j is next hop from i to k
                        next_hop[i][j] = next_hop[i][k] if next_hop[i][k] is not None else k
                        changed = True
    return dist, next_hop, iter_count

def print_routing_tables(dist, next_hop):
    n = len(dist)
    for i in range(n):
        print(f"\nRouting table for node {i}:")
        print("Destination\tCost\tNext hop")
        for j in range(n):
            if dist[i][j] >= INF:
                cost_display = "INF"
                nh = "-"
            else:
                cost_display = str(dist[i][j])
                nh = "-" if next_hop[i][j] is None else str(next_hop[i][j])
            print(f"{j}\t\t{cost_display}\t{nh}")

def demo_example():
    # Example graph (6 nodes). Use -1 for no direct link in input style.
    # This is the same shape as typical textbook examples.
    cost = [
        [0,   2,  -1,  1,  -1, -1],
        [2,   0,   3, -1,  -1, -1],
        [-1,  3,   0, -1,   2,  3],
        [1,  -1,  -1,  0,   1, -1],
        [-1, -1,   2,  1,   0,  1],
        [-1, -1,   3, -1,   1,  0],
    ]
    # Convert -1 to INF and set diagonal zero explicitly
    for i in range(len(cost)):
        for j in range(len(cost)):
            if cost[i][j] < 0:
                cost[i][j] = INF
    dist, next_hop, iters = distance_vector(cost)
    print(f"\nConverged after {iters} iterations")
    print_routing_tables(dist, next_hop)

if __name__ == "__main__":
    # If you want to use interactive input, uncomment these lines:
    # cost = read_cost_matrix()
    # dist, next_hop, iters = distance_vector(cost)
    # print(f"\nConverged after {iters} iterations")
    # print_routing_tables(dist, next_hop)

    # For convenience, run the demo example:
    demo_example()
