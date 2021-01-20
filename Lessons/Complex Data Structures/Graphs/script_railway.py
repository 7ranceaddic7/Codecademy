from graph import Graph
from vertex import Vertex

railway = Graph()

callan = Vertex('Callan')
peel = Vertex('Peel')
ulfstead = Vertex('Ulfstead')
harwick = Vertex('Harwick')

railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)
railway.add_vertex(ulfstead)

railway.add_edge(peel, harwick)
railway.add_edge(harwick, callan)
railway.add_edge(callan, peel)

peel_to_ulfstead_path_exists = railway.find_path('Peel', 'Ulfstead')
harwick_to_peel_path_exists = railway.find_path('Harwick', 'Peel')

print("\n\nA path exists between Peel and Ulfstead:")
print(peel_to_ulfstead_path_exists)
print("\n\nA path exists between Harwick and Peel:")
print(harwick_to_peel_path_exists)

