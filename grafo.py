class  Vértice :
	def  __init__ ( self , vertices ):
		self .name = vértice
		self .vizihos = []
		
	def  adcVizinho ( self , vizinho ):
		if  isinstance (vizinho, vertices):
			if vizinho.name not in  self .vizinhos:
				self .vizinhos.append (vizinho.name)
				vizinho.vizinhos.append ( self .name)
				self .vizinhos =  classificado ( self .vizinhos)
				vizinho.vizinhos =  classificado (vizinho.vizinhos)
		else :
			return  False
		
	def  adcVizinhos ( self , neighbours ):
		for vizinho in vizinhos:
			if  isinstance (vizinho, vertices):
				if vizinho.name not in  self .vizinhos:
					self .vizinhos.append (vizinho.name)
					vizinho.vizinhos.append ( self .name)
					self .vizinhos =  classificado ( self .vizinhos)
					vizinho.vizinhos =  classificado (vizinho.vizinhos)
			else :
				return  False
		
	def  __repr__ ( self ):
		return  str ( self.vizinhos)


class  grafo :
	def  __init__ ( self ):
		self .vertices = {}
	
	def  add_vertex ( self , vertices ):
		if  existir (vértice, vértice):
			self .vertices [vertices.name] = vertices.vizinhos

			
	def  add_vertices ( self , vertices ):
		for vértice in vértices:
			if  isinstance (vertices, vertices):
				self .vertices [vertices.name] = vértice.neijos

			
	def  add_edge ( self , verticeFrom , vertex_to ):
		if  isinstance (verticeFrom, vertices) and  isinstance (verticeTo, Vertex):
			verticeFrom.adcVizinho (verticeTo)
			if  isinstance (verticeFrom, Vertex) and  isinstance (verticeTo, Vertex):
				self .vertices [verticeFrom.name] = verticeFrom.vizinhos
				self .vertices [verticeTo.name] = verticeTo.vizinhos
				
	def  add_edges ( self , edges ):
		for arestas in bordas:
			self .add_edge (edge[ 0 ], edge [ 1 ])          
	
	def  adjacencyList ( self ):
		if  len ( self .vertices >=  1) :
			return [ str (chave) +  " : "  +  str ( self .vertices [key]) for chave in  self .vertices.keys ()]  
		else :
			return  dict ()
		
          
						

def  grafo ( g ):
	"" " Função para imprimir um gráfico como lista de adjacências e matriz de adjacências. " ""
	return  str (g.adjacencyList ()) 

# ################################################# ###############

a = vertice ( ' A ' )
b = vértice ( ' B ' )
c = vértice ( ' C ' )
d = vértice ( ' D ' )
e = vertice ( ' E ' )

a.adcVizinhos ([b, c, e]) 
b.adcVizinhos ([a, c])
c.adcVizinhos ([b, d, a, e])
d.adcVizinho (c)
e.adcVizinhos ([a, c])
		
		
g = grafo ()
print (gráfico (g))
print ( " \ n " )
g.add_vertices ([a, b, c, d, e])
g.add_edge (b, d)
print ( " \ n " )
print (gráfico (g))