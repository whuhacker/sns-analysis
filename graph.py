#!/usr/bin/python
#
#  Social Network Analysis
#  Author: Zeng Xi
#  SID:    1010105140
#  Email:  zengxi@cuhk.edu.hk

from __future__ import division
import networkx as nx
#import matplotlib.pyplot as plt

created = 0;

def create():
	import_nodes = raw_input('The file of nodes list:').strip()
	import_edges = raw_input('The file of edges list:').strip()
	try:
		F1 = open(import_nodes)
	except IOError, e:
		print e
		return
	lines = F1.readlines()
	lines = [line.split(': ') for line in lines]
	nodes = [(int(line[0]),{'name':line[1].rstrip()}) for line in lines]
	global G
	G = nx.Graph()
	G.add_nodes_from(nodes)
	#print G.nodes()
	#print G.node[12]['name']
	try:
		F2 = open(import_edges)
	except IOError, e:
		print e
		return
	lines = F2.readlines()
	lines = [line.split(",") for line in lines]
	lines = [(int(line[0]),int(line[1])) for line in lines]
	G.add_edges_from(lines)
	#print G.edges()
	global created
	created = 1
	print "Graph created!"
	F1.close()
	F2.close()

def nodes():
	if created == 0:
		print 'No graph created!'
	elif created == 1:
		print G.number_of_nodes()

def edges():
	if created == 0:
		print 'No graph created!'
	elif created == 1:
		print G.number_of_edges()

def components():
	if created == 0:
		print 'No graph created!'
	elif created == 1:
		print 'There are ' + str(nx.number_connected_components(G)) + ' connected components in the graph.'
		while True:
			choice = raw_input('Do you want to print the size for each connected components?(y/n)').strip().lower()
			choices =  ['y','n']
			if choice not in choices:
				print('Input Error!')
			else:
				if choice == 'n':
					break
				elif choice == 'y':
					f = open('components_size.txt','w')
					for subgraphs in nx.connected_component_subgraphs(G):
						print subgraphs.number_of_nodes()
						print >> f,  subgraphs.number_of_nodes()
					print 'The above output is also saved in file components_size.txt'
					f.close()
					break

def cluster():
	if created == 0:
		print 'No graph created!'
	elif created == 1:
		try:
			print 'The clustering coefficient for the whole graph is %0.4f.'%(nx.transitivity(G))
		except nx.NetworkXError, e:
			print e

def diameter():
	if created == 0:
		print 'No graph created!'
	elif created == 1:
		try:
			print 'The network diameter is ' + str(nx.diameter(G)) + '.'
		except nx.NetworkXError, e:
			print e
			while True:
				choice = raw_input('Do you want to print the diameter of the largest connected component?(y/n)').strip().lower()
				choices =  ['y','n']
				if choice not in choices:
					print('Input Error!')
				else:
					if choice == 'n':
						break
					elif choice == 'y':
						print nx.diameter(nx.connected_component_subgraphs(G)[0])
						break

def degreedist():
	if created == 0:
		print 'No graph created!'
	elif created == 1:
		try:
			dist = [histogram/G.number_of_nodes() for histogram in nx.degree_histogram(G)]
			print dist
			print 'The degree values are the index in the list.'
		except nx.NetworkXError, e:
			print e

def spathdist():
	if created == 0:
		print 'No graph created!'
	elif created == 1:
		try:
			p = nx.all_pairs_shortest_path_length(G)
			dic = {}
			count = 0
			for i in p.values():
				for j in i.values():
					count += 1
					if j in dic:
						dic[j] += 1
					else:
						dic[j] = 1
			dist = []
			for k in dic.values():
				dist.append(k/count)
			print dist
			print 'The shortest path lengths are the index in the list.'
		except nx.NetworkXError, e:
			print e

def degreecentr():
	if created == 0:
		print 'No graph created!'
	elif created == 1:
		try:
			degree = nx.degree_centrality(G)
			f = open('degree_centrality.txt','w')
			for nodes in degree.items():
				print str(nodes[0]) + ': ' + str(int(round(nodes[1]*(G.number_of_nodes()-1))))
				print >> f, str(nodes[0]) + ': ' + str(int(round(nodes[1]*(G.number_of_nodes()-1))))
			f.close()
			print 'The above output is also saved in file degree_centrality.txt'

		except nx.NetworkXError, e:
			print e
		except IOError, d:
			print d

def eigencentr():
	if created == 0:
		print 'No graph created!'
	elif created == 1:
		try:
			centrality = nx.eigenvector_centrality(G)
			f = open('eigenvector_centrality.txt','w')
			for node in centrality:
				print '%s: %0.2f'%(node,centrality[node])
				print >> f, '%s: %0.4f'%(node,centrality[node])
			f.close()
			print 'The above output is also saved in file eigenvector_centrality.txt'

		except nx.NetworkXError, e:
			print e
		except IOError, d:
			print d

def showMenu():
	title = '''
		Social Network Analysis

	create		Create graph of network from file
	nodes		n: # of nodes
	edges		m: # of edges
	components	size of the connected components
	cluster		clustering coefficient
	diameter	network diameter
	degreedist	degree distribution
	spathdist	shortest path length distribution
	degreecentr	degree centrality
	eigencentr	eigenvector centrality
	quit		Quit

Enter choice:'''
	while True:
		choice = raw_input(title).strip().lower()
		choices =  ['create','nodes','edges','components','cluster','diameter','degreedist','spathdist','degreecentr','eigencentr','quit']
		if choice not in choices:
			print('Input Error!')
		else:
			if choice == 'quit':
				break
			elif choice == 'create':
				create()
			elif choice == 'nodes':
				nodes()
			elif choice == 'edges':
				edges()
			elif choice == 'components':
				components()
			elif choice == 'cluster':
				cluster()
			elif choice == 'diameter':
				diameter()
			elif choice == 'degreedist':
				degreedist()
			elif choice == 'spathdist':
				spathdist()
			elif choice == 'degreecentr':
				degreecentr()
			elif choice == 'eigencentr':
				eigencentr()
if __name__ == '__main__':
	showMenu()
