# Development Log – The Torchbearer

**Student Name:** __Alex Kondan_________________________
**Student ID:** ____817311203_______________________



---

## Entry 1 – 05/12/2026: Initial Plan

My initial plan is to find a way to find the cheapest fuel route through this dungeon while meeting the requirements. I will have to collect relics while starting at node S and ending at node T while also having the lowest cost. I will need the least amount of fuel usage route. My plan is to implement a sorting algorithm that will find the best path. I am using non negative node weights for fuel cost. Therfore my plan is to use greedy optimal sort. I expect implementing this will be quite time consuming and extensive. To test this I will use cases provided in starter file.

---

## Entry 2 – 05/12/2026: Follow up

I wanted to prove out why greedy search will not work first before I began the dijkstra implementation. I need a way to go through all nodes and get best route. I have decided to change my plan. I will implement dijkstra. This will give me the best and cheapest route from source node to end node while collecting relics. I will also use backtracking to explore all possible ways to solve. (lecture notes 04/28/2026) This will be the best option as of right now.

---

## Entry 3 – 05/13/2026: Follow up

Implementation has been a mess. I have had trouble testing and recieved errors. The work has been lengthsome for parts 3 through 6. I plan to finish the remaining functions and test everything together.

---

## Entry 4 – 05/14/2026: Post-Implementation Reflection



Implementation is complete and all tests pass. The parameters and variables for section 5 caused confusion during testing. Adjustments had to be made. Given more time I would test more test cases to see what would pass and would could be improved for further implementations. I had trouble with the parameters ro find_optimal_route that caused a crash because _explore() did not have the parameter I was passing.

---

## Final Entry – 05/14/2026: Time Estimate



| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis |4 |
| Part 2: Precomputation Design | 3.5|
| Part 3: Algorithm Correctness |2.5 |
| Part 4: Search Design |4.5 |
| Part 5: State and Search Space |1.5 |
| Part 6: Pruning |4 |
| Part 7: Implementation |12 |
| README and DEVLOG writing | 1.5|
| **Total** |33.5 |
