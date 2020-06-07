from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self,node):
        self.num_vertices +=1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex


    def get_vertex(self,n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        return None

    def add_edge(self,frm,to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)

        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to],cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)


    def get_vertices(self):
        return self.vert_dict.keys()

    def delete(self,node):
        if node in self.vert_dict.keys():
            v = self.vert_dict[node]

        for key,value in self.vert_dict.items():
            if value is not v and key is not node:
                if  v in value.adjacent.keys():
                    del value.adjacent[v]

        del self.vert_dict[node]

    def bft(self,node):
        queue=[]
        visited =[]
        if node in self.vert_dict.keys():
            ref = self.vert_dict[node]
            queue.append(ref)
            while queue:
                val = queue[0]
                del queue[0]
                if val not in visited:
                    print(val.id,end =" ")
                    visited.append(val)
                    for n in val.adjacent.keys():
                        if n not in queue:
                            queue.append(n)

    def dft(self):
       for v in g.vert_dict.values():
           print(f'g.vert_dict[{v.get_id()}]={g.vert_dict[v.get_id()]}')