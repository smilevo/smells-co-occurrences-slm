# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Replace this line with the value of the cell from the column "Multiple Co-occurrences as One Python String Array"
# in the tab "RQ5" of the Google Spreadsheet "Systematic Mapping Data"
codeSmellCooccurrencesArray = ["Assertion Roulette and Eager Test","Assertion Roulette and Indirect Testing","Assertion Roulette and Mystery Guest","Assertion Roulette and Resource Optimism","Assertion Roulette and Sensitive Equality","Assertion Roulette and Test Code Duplication","Blob Class and Blob Operation","Blob Class and Schizophrenic Class","Blob Class and Tradition Breaker","Blob Operation and Data Clump","Blob Operation and God Class","Blob Operation and Internal Duplication","Blob Operation and Shotgun Surgery","Blob and Spaghetti Code","Complex Class and Feature Envy","Complex Class and Member Ignoring Method","Complex Class and Message Chain","Data Class and External Duplication","Data Class and Feature Envy","Data Class and Interface Segregation Principle Violation","Data Class and Message Chain","Data Class and Schizophrenic Class","Data Class and Shotgun Surgery","Data Clump and External Duplication","Data Clump and Feature Envy","Data Clump and God Class","Data Clump and Interface Segregation Principle Violation","Data Clump and Internal Duplication","Data Clump and Refused Parent Bequest","Data Clump and Shotgun Surgery","Dispersed Coupling and Feature Envy","Dispersed Coupling and God Class","Dispersed Coupling and Long Method","Duplicate Code and Complex Class","Duplicate Code and Large Class","Eager Test and Indirect Testing","Eager Test and Resource Optimism","Excessive Class Length and Excessive Method Length","Excessive Class Length and Too Many Methods","Excessive Class Length and Too Many Public Methods","Excessive Method Length and Too Many Public Methods","Excessive Parameter List and High Coupling","Excessive Parameter List and High NPath Complexity","Excessive Parameter List and Too Many Methods","External Duplication and Blob Operation","External Duplication and God Class","Fear of the Unknown and Anti-Singleton","Fear of the Unknown and Complex Class","Fear of the Unknown and Long Method","Fear of the Unknown and Long Parameter List","Feature Envy and Blob Operation","Feature Envy and Data Class","Feature Envy and Data Clump","Feature Envy and Duplicate Code in Conditional Branches","Feature Envy and God Class","Feature Envy and Intensive Coupling","Feature Envy and Interface Segregation Principle Violation","Feature Envy and Internal Duplication","Feature Envy and Long Method","Feature Envy and Message Chain","Feature Envy and Refused Parent Bequest","Feature Envy and Schizophrenic Class","Feature Envy and Shotgun Surgery","Feature Envy and Temporary Variable Used for Several Purposes","God Class and Brain Method","God Class and Data Class","God Class and Data Clump","God Class and Duplicate Code in Conditional Branches","God Class and Intensive Coupling","God Class and Interface Segregation Principle Violation","God Class and Internal Duplication","God Class and Long Method","God Class and Message Chain","God Class and Schizophrenic Class","God Class and Shotgun Surgery","God Class and Temporary Variable Used for Several Purposes","God Method and Data Class","God Method and Data Clump","God Method and Duplicate Code in Conditional Branches","God Method and Interface Segregation Principle Violation","God Method and Shotgun Surgery","God Method and Temporary Variable Used for Several Purposes","High Method Complexity and Empty Catch Block","High Method Complexity and Excessive Class Length","High Method Complexity and Excessive Method Length","High Method Complexity and Excessive Number of Children","High Method Complexity and Excessive Parameter List","High Method Complexity and Goto Statement","High Method Complexity and High Coupling","High Method Complexity and High NPath Complexity","High Method Complexity and Too Many Methods","High Method Complexity and Too Many Public Methods","High NPath Complexity and Goto Statement","High NPath Complexity and Too Many Methods","Implicit Columns and Anti-Singleton","Implicit Columns and Complex Class","Implicit Columns and Long Parameter List","Inappropriate Intimacy and Feature Envy","Intensive Coupling and Blob Operation","Intensive Coupling and Data Clump","Intensive Coupling and Long Method","Internal Duplication and Blob Class","Internal Duplication and Data Class","Internal Duplication and External Duplication","Internal Duplication and Intensive Coupling","Internal Duplication and Schizophrenic Class","Internal Duplication and Sibling Duplication","Large Class and Complex Class","Leaking Inner Class and Member Ignoring Method","Long Method and Feature Envy","Long Method and Long Parameter List","Long Method and Member Ignoring Method","Long Method and Spaghetti Code","Long Parameter List and Class Data Should Be Private","Long Parameter List and Feature Envy","Long Parameter List and Member Ignoring Method","Message Chain and Blob","Message Chain and Complex Class","Message Chain and External Duplication","Message Chain and Internal Duplication","Message Chain and Member Ignoring Method","Message Chain and Refused Parent Bequest","Message Chain and Schizophrenic Class","Message Chain and Sibling Duplication","Message Chain and Spaghetti Code","Mystery Guest and Eager Test","Mystery Guest and Indirect Testing","Mystery Guest and Resource Optimism","No Low Memory Resolver and Member Ignoring Method","Refused Parent Bequest and God Class","Schizophrenic Class and Blob Operation","Schizophrenic Class and Data Clump","Schizophrenic Class and Intensive Coupling","Shotgun Surgery and Internal Duplication","Sibling Duplication and Data Class","Sibling Duplication and External Duplication","Slow Loop and Member Ignoring Method","Speculative Generality and Swiss Army Knife","Test Code Duplication and Eager Test","Test Code Duplication and Indirect Testing","Test Code Duplication and Mystery Guest","Test Code Duplication and Sensitive Equality","Too Many Public Methods and Too Many Methods","Tradition Breaker and Blob Operation","Tradition Breaker and Internal Duplication","Tradition Breaker and Schizophrenic Class"]

fromArray = []
toArray = []

# Convert the "Code Smell 1 and Code Smell 2" co-occurrences into two arrays for
# the Networkx Graph: the first array is the from array where an edge starts, and
# the second array is the to array where an edge ends
for coocurrence in codeSmellCooccurrencesArray:
    codeSmellsArray = coocurrence.split(" and ")
    fromArray.append(codeSmellsArray[0])
    toArray.append(codeSmellsArray[1])

# Build the Networkx Graph by adding nodes and edges. Also calculate the number of times
# each code smell co-occurrence appears, starting at 1.
df = pd.DataFrame({'from': fromArray, 'to': toArray})
G = nx.Graph()
for row in df.itertuples(index=False, name=None):
    if G.has_edge(row[0], row[1]):
        G[row[0]][row[1]]['weight'] += 1
    else:
        G.add_edge(row[0], row[1], weight=1)

# Print the code smell co-occurrences and the number of times they appear throughout all the studies.
for a, b, data in sorted(G.edges(data=True), key=lambda x: x[2]['weight']):
    print('{a} and {b}, appears {w} time(s)'.format(a=a, b=b, w=data['weight']))

# Set up how the graph will look.
pos = nx.spring_layout(G)

# Plot the graph, using the weight attribute for the edge labels to represent the number of times
# each code smell co-occurrence appears.
nx.draw(G, pos, with_labels=True)
labels = {e: G.edges[e]['weight'] for e in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()