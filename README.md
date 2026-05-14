# The Torchbearer

**Student Name:** ___Alex Kondan________________________
**Student ID:** ______817311203_____________________
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis


- **Why a single shortest-path run from S is not enough:**
  A single shortest-path run will not accommadate all the possible routes to save the most fuel and visit all the relics then finding the finish line

- **What decision remains after all inter-location costs are known:**
  What path we should take to visit all the relics

- **Why this requires a search over orders (one sentence):**
  So we can try them all and find the best route to save the minimum fuel 

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
| What the values represent |minimum fuel cost |
| Lookup time complexity | O(1)|
| Why O(1) lookup is possible |because hash map can look up constant time key |

### Part 2c: Precomputation Complexity



- **Number of Dijkstra runs:** k+1 (one from source, one from each relic to end)
- **Cost per run:** O(m log n)
- **Total complexity:** O((k+1) x m log n)
- **Justification (one line):** dijkstra runs one per source node, while visiting each node with priorty queue

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  once finalized, the node's distance is the true shortest path from the source node and no shorter paths will be found

- **For nodes not yet finalized (not in S):**
  nodes that are not finalized the current distance is the shortest path so far with finalized nodes, this may still be updated with a shorter path

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  It holds true because the source node distance is 0 which is true since its costs nothing to get to itself and all other unexplored nodes are set to infinity

- **Maintenance : why finalizing the min-dist node is always correct:**
  Because when the weights are non negative there will be no other path that can make it a cheaper cost

- **Termination : what the invariant guarantees when the algorithm ends:**
  It guarantees that the connected nodes will be finalized and the cheapest path cost will be found from the source

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

By having the correct distances the route planner is able to find the most optimal path

---

## Part 4: Search Design

### Why Greedy Fails



- **The failure mode:** Greedy only looks at the next cheapest choices and committs where as we want one that will look globally for the cheapest cost path as there could be a better overall route 
- **Counter-example setup:** S can go to R1(cost 1) and R2(cost 25). R1 can go to R2(cost 50) and T(cost 1). R2 can go to R1(cost 1) and T(cost 1).
- **What greedy picks:** S to R1 (cost 1), R1 to R2 (cost 50) and R2 to T (cost 1) for total of 52.
- **What optimal picks:** S to R2 (cost 25), R2 to R1 (cost 1) and R1 to T (cost 1) for total of 27.
- **Why greedy loses:** greedy loses because it picks the closest cheapest cost edge which forces it to take R1 to R2 which costs 50 rather than S to R2 which only costs it 25.

### What the Algorithm Must Explore


- The algorithm must explore all the possible orders of nodes and relics to find the most optimal path

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location |current_loc |node   |current node of torchbearer |
| Relics already collected |relics_collected  |set | set of relics already collected |
| Fuel cost so far |fuel_cost |float |total amount of fuel spent so far |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen |set |
| Operation: check if relic already collected | Time complexity: O(1)|
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1)|
| Why this structure fits |set stores collection of nodes while having good time complexity O(1) for operations |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** k!
- **Why:** because there are k relics and we need to try all orders, k x (k-1) x (k-2)...

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
