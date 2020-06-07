from Graph import Graph
g = Graph()
a="""
1. Insert Vertex
2. Insert Edge
3. Print Graph
4. Get Neighbour
5. Delete Node
6. BFT
8. DFT"""

while True:
    print(a)
    choice = int(input('Enter choice: '))
    if choice == 1:
        node = input('Enter the node to insert in the graph: ')
        g.add_vertex(node)
    elif choice == 2:
        frm = input('Enter the beginning vertex: ')
        to = input('Enter the to index: ')
        wght = int(input('Ennter the weight(default is 0)'))
        g.add_edge(frm,to,wght)
    elif choice == 3:
        print('Nodes in the graph: ')
        """for v in g.vert_dict.values():
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print(f'{vid}  {wid} {v.get_weight(w)}')"""
        for i,j in g.vert_dict.items():
            print(i,j)
    elif choice == 4:
        node = input('Enter the node to get its neighbours: ')
        if node in g.vert_dict.keys():
            print(g.vert_dict[node])
    elif choice == 5:
        node = input('Enter the node to delete: ')
        if node in g.vert_dict.keys():
            g.delete(node)
        else:
            print(f'There is no node {node} in the graph')
        if node in g.vert_dict.keys():
            print(g.vert_dict[node])