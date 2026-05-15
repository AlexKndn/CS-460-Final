"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: __Alex Kondan_________________________
Student ID:   ____817311203_______________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return (
        "A single shortest-path run will not accommodate all the possible routes "
        "to save the most fuel and visit all the relics then finding the finish line.\n"
        "What path we should take to visit all the relics.\n"
        "So we can try them all and find the best route to save the minimum fuel."
    )

# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = list(set([spawn] + relics))
    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    dist = {node: float('inf') for node in graph} #creates dictionary with every node set to infinity
    dist[source] = 0 #source node costs 0

    pq = [(0, source)] #initalize priorty queue with source node at cost 0, Heap always pops cheapest item first

    while pq:
        cost, node = heapq.heappop(pq) #keep goes while nodes to process. Pops node with cheapest known cost

        if cost > dist[node]: # if a cheaper path to this node is fund skip it it's outdated
            continue

        for neighbor, weight in graph[node]: # look at every neighbor of current node and calculate cost to reach it through the current node
            new_cost = cost + weight
            if new_cost < dist[neighbor]: #if found a cheaper path to the neighbor update it  and add it to the queue to explore later
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return dist # return dictionary of minimum costs from source to every node



def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    dist_table = {} #store results
    sources = select_sources(spawn, relics, exit_node) #get list of source nodes (spawn + relics)
    for source in sources: # run dijkstra from each source node S and store results. dist_table['S'] gives you all distances from S
        dist_table[source] = run_dijkstra(graph, source)
    return dist_table # returns dictionary of all distances


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return (
        "Once finalized, the node's distance is the true shortest path "
        "from the source node and no shorter paths will be found.\n"
        "Nodes that are not finalized the current distance is the shortest path so far with finalized "
        "nodes, this may still be updated with a shorter path.\n"
        "It holds true because the source node distance is 0 which is true since it "
        "costs nothing to get to itself and all other unexplored nodes are set to infinity.\n"
        "Because when the weights are non negative there will be no other path that can "
        "make it a cheaper cost.\n"
        "It guarantees that the connected nodes will be finalized and the cheapest path "
        "cost will be found from the source.\n"
        "By having the correct distances the route planner is able to find the most optimal path."
    )


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return (
        "Greedy only looks at the next cheapest choices and commits whereas we want one that will "
        "look globally for the cheapest cost path as there could be a better overall route.\n"
        "Counter-example: S can go to R1(cost 1) and R2(cost 25). R1 can go to R2(cost 50) and "
        "T(cost 1). R2 can go to R1(cost 1) and T(cost 1).\n"
        "Greedy picks: S to R1 (cost 1), R1 to R2 (cost 50) and R2 to T (cost 1) for total of 52.\n"
        "Optimal picks: S to R2 (cost 25), R2 to R1 (cost 1) and R1 to T (cost 1) for total of 27.\n"
        "Greedy loses because it picks the locally cheapest edge which forces it to take R1 to R2 "
        "which costs 50 rather than S to R2 which only costs 25.\n"
        "The algorithm must explore all possible orders of nodes and relics to find the most optimal path."
    )


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    best = [float('inf'), []] # container storing the best cost solution found and order found so far. best[0] is the minimum cost, best [1] is the optimal relic order. Starts at infity since nothing found yet.
    _explore(dist_table, spawn, relics, [], 0.0, exit_node, best) # start recursive search from explore from spawn with no relics vistited or fuel spent
    return best[0], best[1] # returns best cost and best relic order found


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    if cost_so_far >= best[0]: #Pruning is safe because all the edge weights are not negative so no future path from this branch can reduce the cost_so_far below best[0]. We will only prune when current cost exceeds best, therefore optimal solution is not discarded
        return #pruning if the current cost already eceeds the best found, stop exploring this branch
    
    if not relics_remaining: # Base case, all relics collected. Add the cost to reach the exit
        final_cost = cost_so_far + dist_table[current_loc][exit_node]
        if final_cost < best[0]: # if this complete route is cheaper than the best found so far, update best. [:] makes a copy of the list
            best[0] = final_cost
            best[1] = relics_visited_order[:]
        return

    for relic in relics_remaining: #tries each remaining relic. Looks up precomputed cost to reach it
        travel_cost = dist_table[current_loc][relic] #cost to reach relic
        new_remaining = [r for r in relics_remaining if r != relic] # creates a list of remaining relics with the current one removed
        relics_visited_order.append(relic) #marks the relic visited by adding it to the order list
        _explore(dist_table, relic, new_remaining, relics_visited_order, cost_so_far + travel_cost, exit_node, best) #recursively explore from this relic with updated cost and remaining relics
        relics_visited_order.pop() #backtrack , undo the choice by removing the last relic from the order list


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node) #run dijkstra from all source nodes to precompute all the shortest distances
    return find_optimal_route(dist_table, spawn, relics, exit_node) # uses the precomputed distances to find the optimal relic collection order


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()


