# Science-simulations-II---SPH
UZH course ESC II computer simulations in science II, writing a smooth particle hydrodynamics program. 

Description partitioning tree exercise:
- Implement a particle class and a cell class
- Implement the partitioning of particles function we introduced in class. 
- The hard part is making sure your partition function is really bomb proof, check all “edge cases” (e.g., no particles in the cell, all   particles on one side or other of the partition, already partitioned data, particles in the inverted order of the partition, etc…).      Write boolean test functions for each of these cases.
- Call all test functions in sequence and check if they all succeed.
- Once you have this, then recursively partition the partitions and build cells linked into a tree as you go. Partition alternately in x   and y dimensions, or simply partition the longest dimension of the given cell.
- Create a random distribution of particles in 2D and build a tree from the particles.
- Plot the particles and tree cells.
