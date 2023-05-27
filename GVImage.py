import graphviz as gv
from PIL import Image, ImageDraw
import json
from jsondiff import diff
import sys
import itertools
import os
# load old and new graphwalker model json files
f1=sys.argv[1]
f2=sys.argv[2]
fn1,ft1=os.path.splitext(f1)
fn1_=fn1.split('//')[-1]
fn1__=fn1_.split('.')[0]
fn2,ft2=os.path.splitext(f2)
with open(sys.argv[1], 'r') as file:
    old_model = json.load(file)
with open(sys.argv[2], 'r') as file:
    new_model = json.load(file)

# compare the models and get the differences
diff_result = diff(old_model['models'], new_model['models'])

# create a new directed graph
graph = gv.Digraph()



# add the new vertices to the graph
old_vertices = old_model['models'][0]['vertices']
new_vertices = new_model['models'][0]['vertices']

old_vertex_map = {v['id']: v['name'] for v in old_vertices}
new_vertex_map = {v['id']: v['name'] for v in new_vertices}

deleted_vertices = set([v['name'] for v in old_vertices]) - set([v['name'] for v in new_vertices])
# add the new vertices to the graph
for vertex in new_vertices:
    if vertex['name'] not in [v['name'] for v in old_vertices]:
        graph.node(vertex['name'], label=vertex['name'], color='blue')

# remove the deleted vertices and edges from the graph
for vertex_name in deleted_vertices:
    graph.node(vertex_name, color='grey', style='dashed')

# add the old vertices to the graph
for vertex in old_vertices:
    if vertex['name'] not in deleted_vertices:
        graph.node(vertex['name'], label=vertex['name'])

#print(old_vertex_map)
#print(new_vertices_dict)

# add the old edges to the graph
# add the old edges to the graph
old_edges = old_model['models'][0]['edges']
#print(old_edges)
new_edges = new_model['models'][0]['edges']
#print(set([(new_vertex_map[e['sourceVertexId']], new_vertex_map[e['targetVertexId']]) for e in new_edges]))
deleted_edges = set([(old_vertex_map[e['sourceVertexId']], old_vertex_map[e['targetVertexId']]) for e in old_edges]) - set([(new_vertex_map[e['sourceVertexId']], new_vertex_map[e['targetVertexId']]) for e in new_edges])


for edge in old_edges:
    if (old_vertex_map[edge['sourceVertexId']], old_vertex_map[edge['targetVertexId']]) in deleted_edges:
        graph.edge(old_vertex_map[edge['sourceVertexId']], old_vertex_map[edge['targetVertexId']], color='red', style='dashed')
    else:
        graph.edge(old_vertex_map[edge['sourceVertexId']], old_vertex_map[edge['targetVertexId']])

# add the new edges to the graph
for edge in new_edges:
    if (new_vertex_map[edge['sourceVertexId']], new_vertex_map[edge['targetVertexId']]) not in [(old_vertex_map[e['sourceVertexId']], old_vertex_map[e['targetVertexId']]) for e in old_edges]:
        graph.edge(new_vertex_map[edge['sourceVertexId']], new_vertex_map[edge['targetVertexId']], color='blue')
        
# create deleted_edges set using vertex name map instead of vertex id
deleted_edges = set([(old_vertex_map[e['sourceVertexId']], old_vertex_map[e['targetVertexId']]) for e in old_edges]) - set([(new_vertex_map[e['sourceVertexId']], new_vertex_map[e['targetVertexId']]) for e in new_edges])
deleted_edges = set([(k1, k2) for k1, v1 in old_vertex_map.items() for k2, v2 in old_vertex_map.items() if (v1, v2) in deleted_edges])


#cut
# create a gif animation to show the changes in both models
frames = []

# add the initial frame
graph.format = 'png'
graph.render(os.getcwd()+'\\Outputs\\'+fn1__, view=False)
img = Image.open(os.getcwd()+'\\Outputs\\'+fn1__+'.png')
frames.append(img)
print("Image Generated")