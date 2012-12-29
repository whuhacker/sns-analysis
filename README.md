SNS Analysis
============

Social Network Analysis Tool

This tool is based on NetworkX, which is a python library for network analysis.

Introduction
------------
Dataset:
* sigcomm_author.txt
* sigcomm_network.txt 

It is an undirected network, so [ID1, ID2] means [ID2, ID1] also. 

* For sigcomm_network.txt:
  - 1,2 (ID_1 coauthor with ID_2)
  - 3,4 (ID_3 coauthor with ID_4)
  - 4, 216 (ID_4 coauthor with ID_216)....etc 
* For sigcomm_author.txt:
  - 1: Amer El Abbadi (ID_1: name)
  - 2: Thomas Lui (ID_2: name)...etc 

We can determine:
- n: # of nodes
- m: # of edges
- size of the connected components
- clustering coefficient
- network diameter
- degree distribution
- shortest path length distribution
- degree centrality
- eigenvector centrality

More details: [PageRank与社交网络模型评估 (in Chinese)](http://www.lovelucy.info/pagerank-sns-model-3.html)


Environment
-----------
Python 2.6.5 (r265:79063) [GCC 4.4.3] on Linux (Ubuntu 10.04)

```bash
$ sudo apt-get install python-setuptools
$ sudo easy_install networkx
```

Usage
-----

```bash
$ python graph.py
```

First you need to create a network graph from dataset. Type "create", then input the files name: "sigcomm_author.txt" for nodes list, and "sigcomm_network.txt" for edges list. After creating the graph, you can analyze the graph using other commands.

Since the output is large for some properties of the graph, the result will be saved into files.

Enjoy~ :-)

