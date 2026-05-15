# The Torchbearer

**Student Name:** ___Alex Kondan________________________
**Student ID:** ______817311203_____________________
**Course:** CS 460 – Algorithms | Spring 2026



---

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
  It will not accommadate all the possible routes to save the most fuel, visit all the relics, then reach the finish line because the shortest distances taken in account are from the local perspective of the current node.

- **What decision remains after all inter-location costs are known:**
  What is the least cost path we should take to visit all the relics.

- **Why this requires a search over orders (one sentence):**
  So we can try them all and find the best route to use the minimum amount of fuel.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection



| Source Node Type | Why it is a source |
|---|---|
| node S | we need cost from S to each relic|
| Relics | we need cost from each relic to other relics to T |

### Part 2b: Distance Storage



| Property | Your answer |
|---|---|
| Data structure name | nested hash map|
| What the keys represent | source node(outer), destination node (inner)|
| What the values represent | fuel cost to destination node |
| Lookup time complexity | O(1)|
| Why O(1) lookup is possible |because hash map can look up constant time key |

### Part 2c: Precomputation Complexity



- **Number of Dijkstra runs:** k+1 (one from source, one from each relic to end)
- **Cost per run:** O(m log n)
- **Total complexity:** O((k+1) x m log n) 
- **Justification (one line):** dijkstra runs once per source node, while visiting each node with priorty queue

---

## Part 3: Algorithm Correctness



### Part 3a: What the Invariant Means



- **For nodes already finalized (in S):**
  once finalized, the node's distance is the true shortest path from the source node and no shorter paths will be found

- **For nodes not yet finalized (not in S):**
  nodes that are not finalized the current distance is the shortest path so far with finalized nodes, this may still be updated with a shorter path

### Part 3b: Why Each Phase Holds



- **Initialization : why the invariant holds before iteration 1:**
  It holds true because the source node distance is 0 which is true since its costs nothing to get to itself and all other unexplored nodes are set to infinity

- **Maintenance : why finalizing the min-dist node is always correct:**
  Because when the weights are non negative there will be no other path that can make it a cheaper cost

- **Termination : what the invariant guarantees when the algorithm ends:**
  It guarantees that the connected nodes will be finalized and the cheapest path cost will be found from the source

### Part 3c: Why This Matters for the Route Planner



By having the correct distances the route planner is able to find the most optimal path.

---

## Part 4: Search Design

### Why Greedy Fails



- **The failure mode:** Greedy only looks at the next cheapest choices and committs. Whereas we want one that will look globally for the cheapest cost path as there could be a better overall route. 
- **Counter-example setup:** S can go to R1(cost 1) and R2(cost 25). R1 can go to R2(cost 50) and T(cost 1). R2 can go to R1(cost 1) and T(cost 1).
- **What greedy picks:** S to R1 (cost 1), R1 to R2 (cost 50) and R2 to T (cost 1) for total of 52.
- **What optimal picks:** S to R2 (cost 25), R2 to R1 (cost 1) and R1 to T (cost 1) for total of 27.
- **Why greedy loses:** greedy loses because it picks the closest cheapest cost edge which forces it to take R1 to R2 which costs 50 rather than S to R2 which only costs it 25.

### What the Algorithm Must Explore


- The algorithm must explore all the possible orders of nodes and relics to find the most optimal path.

---

## Part 5: State and Search Space

### Part 5a: State Representation



| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location |current_loc |node   |current node of torchbearer |
| Relics already collected |relics_visited_order  |list | relics already collected in order|
| Fuel cost so far |cost_so_far |float |total amount of fuel spent so far |

### Part 5b: Data Structure for Visited Relics


| Property | Your answer |
|---|---|
| Data structure chosen |list |
| Operation: check if relic already collected | Time complexity: O(n)|
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1)|
| Why this structure fits |list will work for tracking visited relics is good for backtracking |

### Part 5c: Worst-Case Search Space


- **Worst-case number of orders considered:** k!
- **Why:** because there are k relics and we need to try all orders, k x (k-1) x (k-2)...

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking


- **What is tracked:** We track what is the total best so far in terms of route (edge weights)
- **When it is used:** We will compare the current total edge weight with our total best edge weight with each step
- **What it allows the algorithm to skip:** A edge weight that exceedes in cost versus of what we currently have as total best so far

### Part 6b: Lower Bound Estimation


- **What information is available at the current state:** the cost, leftover relics and shortest distances between nodes
- **What the lower bound accounts for:** the leftover minimum cost
- **Why it never overestimates:** because the cost can only be greater than or equal to the shortest path

### Part 6c: Pruning Correctness



- Pruning is safe because if the current cost is more than the best so far the branch will be cut allowing for a optimal solution

---

## References



- Lecture notes Professor Manju Maralidharan Priya, CS 460 Spring 2026
- Skiena, Steven S. The Algorithm Design Manual, 2nd edition. Springer, 2008. (Chapter 6 and 7)
- ByteQuest. "Dijkstra's Shortest Path Algorithm Visually Explained | How it Works | With Examples." Youtube. https://www.youtube.com/watch?v=CmIQ29cUGiE
