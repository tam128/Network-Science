# Repository: 2018-01.project-2.template
# Assignment #2: Network Science 

> Course: **[CS 1656 - Introduction to Data Science](http://cs1656.org)** (CS 2056) -- Spring 2018    
> Instructor: [Alexandros Labrinidis](http://labrinidis.cs.pitt.edu)  
> 
> Assignment: #2. Network Science  
> Released: February 8, 2018  
> **Due:      February 20, 2018**

### Description
This is the **second assignment** for the CS 1656 -- Introduction to Data Science (CS 2056) class, for the Spring 2018 semester.

### Goal
The goal of this assignment is to familiarize you with influnce propagation in network science.

### What to do -- compute_active.py
You are asked to write a Python program, called `compute_active.py`, that will take as input a directed graph and a probability value, and for every node **n** in the graph compute the number of nodes that will become active if node **n** is the source of an influence propagation run, under the (modified) independent cascade model.

You program should be invoked as:
```
python3 compute_active.py graph.csv px results.csv
```
The `graph.csv` file specifies the graph to consider and `px` is used to describe the activation probability. 
 

### Input (graph.csv format)
We assume a directed graph, whose nodes are represented by integer values (nodeIDs). The input file (graph.csv) specifies all the edges of the graph as pairs of (source, destination) nodeIDs. For example, the following is the provided sample input file (graph.csv), consisting of 6 nodes (with nodeIDs from 1 to 6) and 8 edges.
```
1,2
1,4
1,5
1,6
3,1
4,2
5,6
6,4
```

### Modified Independent Cascade Model
In the independent cascade model, an active node **n** will activate its neighbors **N(n)** with probabilities that are provided by the edges connecting **n** to each neighbor. For this assignment, we make two modifications to this original model, which we refer to as the _modified independent cascade model_, as follows:
* For simplicity, all activation probabilities are the same for the entire graph and specified through the `px` parameter at command line.  
* For reproducibility, the activation of a node given a certain probability happens in a deterministic way, as follows. Assume the node of interest is **nodeID** and that the probability of activation is specified as **1/px**. In that case, node nodeID will be **activated if (nodeID % px) == 0** (i.e., if nodeID is a multiple of px, determined using the modulo operator); nodeID will not be activated otherwise.   

### Computation
You program should read its parameters, read in the graph input file (`graph.csv`), and create a graph using the `networkx` library. For every node in the graph you should compute which nodes will be activated if that node is the initial source and we are using the modified independent cascade model. Parameter `px` means that the probability of activation will be 1/px; we use the modulo operator described earlier to determine if a node should become active or not. 


### Output (results.csv)
Once the computation completes for all nodes, the results are written in the specified output file (`results.csv`). Each row should be in the format:
```nodeID, num_activations```
(i.e., you should have one row per nodeID). You should make sure the results are sorted in descending order of activations (i.e., highest first). In case of ties, you should use the nodeID as a tiebreaker: smaller nodeID values are listed earlier in the output. You are asked to overwrite the file if it exists already.

Here's a sample output file from the following execution:
```
python3 compute_active.py graph.csv 1 results1.csv
3,6
1,5
5,4
6,3
4,2
2,1
```

And here's another sample output file from the following execution:
```
python3 compute_active.py graph.csv 2 results2.csv
1,4
5,4
6,3
4,2
2,1
3,1
```


### Important notes about grading
It is absolutely imperative that your python program:  
* runs without any syntax or other errors (using Python 3)  
* strictly adheres to the format specifications for input and output, as explained above.     

Failure in any of the above will result in **severe** point loss. 


### Allowed Python Libraries (Updated)
You are allowed to use the following Python libraries (although a **small** fraction of these will actually be needed):
```
argparse
collections
csv
json
glob
math 
networkx
numpy
os
pandas
re
requests
statistics
string
sys
time
xml
```
If you would like to use any other libraries, you must ask permission by Wednesday, February 14, 2018, using [piazza](http://piazza.cs1656.org).


### About your github account
It is very important that:  
* Your github account can do **private** repositories. If this is not already enabled, you can do it by visiting <https://education.github.com/>  
* You use the same github account for the duration of the course  
* You use the github account that you specified during the test assignment (i.e., this one)  

### How to submit your assignment
For this assignment, you must use the repository that was created for you after visiting the classroom link. You need to update the repository to include file `compute_active.py` as described above, and other files that are needed for running your program. You need to make sure to commit your code to the repository provided. We will clone all repositories shortly after midnight:  
* the day of the deadline **Tuesday, February 20th, 2018 (i.e., at 12:15am, Wednesday, February 21, 2018)**  
* 24 hours later (for submissions that are one day late / -5 points), and  
* 48 hours after the first deadline (for submissions that are two days late / -15 points). 

Our assumption is that everybody will submit on the first deadline. If you want us to consider a late submission, you need to email us at `cs1656-staff@cs.pitt.edu`
