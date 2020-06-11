#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


file=open("CollegeMsg.txt")
score_lines=file.readlines()
adj_list={}
all_nodes=[]
edges=0
for l in score_lines:
    ip=l.split(" ")
   
    all_nodes.append(int(ip[0]))
    all_nodes.append(int(ip[1]))
    if int(ip[0])  in adj_list:
        if int(ip[1]) not in adj_list[int(ip[0])]:
            adj_list[int(ip[0])].append(int(ip[1]))
            edges+=1
    else:
        adj_list[int(ip[0])]=[]
        adj_list[int(ip[0])].append(int(ip[1]))
        edges+=1
    

#print(len(adj_list))
#print(len(all_nodes))
Total_nodes=list(set(all_nodes))
print("Total nodes ........",len(Total_nodes))
print("Total edges ........",edges)


# In[3]:


print(adj_list)


# In[4]:


largestNode=max(all_nodes)
smallestNode=min(all_nodes)
print(largestNode,smallestNode)
adj_matrix=[[0 for j in  range(largestNode)]for j in range(largestNode)]
for pos in  adj_list:
    for  vert in adj_list[pos]:
        adj_matrix[pos-1][ vert-1]=1
        
print(len(adj_matrix))      


# In[5]:


indeg_dic={}
outdeg_dic={}
indeg_count={}
outdeg_count={}
avg_indeg=0
avg_outdeg=0
adj_matrix_np =np.array(adj_matrix)      
adj_matrix_t=adj_matrix_np.transpose().tolist()
adj_matrix_new=adj_matrix_np.tolist()

# for  pos in range(0,length(adj_matrix_t)):
t=0
max_in=0
Max_in_node=0
for x in adj_matrix_t:
    indeg_dic[t]=x.count(1)
    count1=x.count(1)
    if count1 in indeg_count:
        indeg_count[count1]+=1/len(Total_nodes)
    else:
        indeg_count[count1]=1/len(Total_nodes)
    avg_indeg+=indeg_dic[t]
    if(indeg_dic[t]> max_in):
        max_in=indeg_dic[t]
        Max_in_node=t
    t+=1
#print(avg_indeg)
avg_indeg=avg_indeg/len(Total_nodes)
print("AVG_indegree.........",avg_indeg) 
print("Max Indeg node....",Max_in_node+1,"...... with degree",indeg_dic[Max_in_node])
h=0
max_out=0
Max_out_node=0
for y in adj_matrix_new:
    outdeg_dic[h]=y.count(1)
    count2=y.count(1)
    if count2 in outdeg_count:
        outdeg_count[count2]+=1/len(Total_nodes)
    else:
        outdeg_count[count2]=1/len(Total_nodes)
    
    avg_outdeg+=outdeg_dic[h]
    if(outdeg_dic[h]> max_out):
        max_out=outdeg_dic[h]
        Max_out_node=h
    h+=1
#print(avg_outdeg)
avg_outdeg=avg_outdeg/len(Total_nodes)
print("AVG_outdegree.........",avg_outdeg)        
print("Max Outdeg node....",Max_out_node+1,"...... with degree",outdeg_dic[Max_out_node])
Density_net=0
Density_net=edges/((len(Total_nodes)*(len(Total_nodes)-1)))
print("Density_network....",Density_net)


# In[6]:


list_node=[]
for j in range(1,1900):
    list_node.append(j)


# In[7]:


# print((adj_matrix_new[0]))
#print(indeg_count)
indeg_list=[]
indeg_count_list=[]
for i in sorted (indeg_count) : 
    indeg_list.append(i)
    indeg_count_list.append(indeg_count[i])
print(indeg_list)
print(indeg_count_list)


# In[8]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.title('Indegree_Distribution ')
ax.bar(indeg_list,indeg_count_list)
plt.show()


# In[9]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23,17,35,29,12]
ax.bar(indeg_list[0:25],indeg_count_list[0:25])
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.title('Indegree_Distribution Till 25 degree')
plt.show()


# In[10]:


outdeg_list=[]
outdeg_count_list=[]
for i in sorted (outdeg_count) : 
    outdeg_list.append(i)
    outdeg_count_list.append(outdeg_count[i])
print(outdeg_list)
print(outdeg_count_list)


# In[11]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.title('Outdegree_Distribution ')
ax.bar(outdeg_list,outdeg_count_list)
plt.show()


# In[12]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
# langs = ['C', 'C++', 'Java', 'Python', 'PHP']
# students = [23,17,35,29,12]
ax.bar(outdeg_list[0:25],outdeg_count_list[0:25])
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.title('Outdegree_Distribution Till 25 degree')
plt.show()


# In[13]:


val_indeg=[]
for i in range(0,len(Total_nodes)):
    val_indeg.append(indeg_dic[i])
    print(i,)
    


# In[ ]:





# In[14]:


import matplotlib.pyplot as plt 
  
# x-coordinates of left sides of bars  

  
# labels for bars 
#tick_label = ['one', 'two', 'three', 'four', 'five'] 
  
# plotting a bar chart 
plt.bar(list_node,val_indeg, 
        width = 0.4) 
  
# naming the x-axis 
plt.xlabel('Node number') 
# naming the y-axis 
plt.ylabel('InDegree centrality value') 
# plot title 
plt.title('In Degree Centrality ') 
  
# function to show the plot 
plt.show() 


# In[15]:


neighbour_node_dic={}
for i in range(0,len(Total_nodes)):
    neighbour_node=[]
    for j in range(0,len(Total_nodes)):
        if (adj_matrix[i][j]) ==1:
            neighbour_node.append(j+1)
        if((adj_matrix_t[i][j]) ==1):
            if j+1 not in neighbour_node:
                neighbour_node.append(j+1)
    neighbour_node_dic[i+1]=neighbour_node


# In[16]:


print((neighbour_node_dic))


# In[17]:


print(indeg_dic)


# In[18]:


edge_neighbour_dic={}
for i in range(1,len(Total_nodes)+1):
    edge_neighbour=0
    #print(i,".........of" )
    for f in neighbour_node_dic[i]:
        #print(f)
        for r in neighbour_node_dic[i]:
            #print(" inside........ ",r)
            if adj_matrix[f-1][r-1]==1:
                edge_neighbour+=1
#             if adj_matrix_t[f-1][r-1]==1:
#                 edge_neighbour+=1
    edge_neighbour_dic[i]=edge_neighbour
print(edge_neighbour_dic)            


# In[19]:


clustering_coeff={}

for i in range(1,len(Total_nodes)+1):
    #print("lennnn",len(neighbour_node_dic[i]))
    if((len(neighbour_node_dic[i]))!=0 and (len(neighbour_node_dic[i]))!=1  ):
        
        clustering_coeff[i]=(edge_neighbour_dic[i])/((len(neighbour_node_dic[i]))*(len(neighbour_node_dic[i])-1))
        
    else:
        clustering_coeff[i]=0
        
    #print(clustering_coeff[i])
print(clustering_coeff)


# In[20]:


cc_count=[0,0,0,0,0,0]
for i in range(1,len(Total_nodes)+1):
    if 0<=clustering_coeff[i] <0.2:
        cc_count[0]+=1/(len(Total_nodes))
    elif 0.2<=clustering_coeff[i] <0.4:
        cc_count[1]+=1/(len(Total_nodes))
    elif 0.4<=clustering_coeff[i] <0.6:
        cc_count[2]+=1/(len(Total_nodes))
    elif 0.6<=clustering_coeff[i] <0.8:
        cc_count[3]+=1/len(Total_nodes) 
    elif 0.8<=clustering_coeff[i] <1:
        cc_count[4]+=1/len(Total_nodes)
    else:
        cc_count[5]+=1/len(Total_nodes)
        

print(cc_count)       


# In[ ]:





# In[21]:


import matplotlib.pyplot as plt 
  
# x-coordinates of left sides of bars  
clustering_coeff_=[0,0.2,0.4,0.6,0.8,1]
  
# labels for bars 
#tick_label = ['one', 'two', 'three', 'four', 'five'] 
  
# plotting a bar chart 
plt.bar(clustering_coeff_,cc_count, 
        width = 0.2) 
  
# naming the x-axis 
plt.xlabel('Clustering Coeff Values') 
# naming the y-axis 
plt.ylabel('Fraction of Nodes') 
# plot title 
plt.title('Clustering Coefficient  Distribution Graph ') 
  
# function to show the plot 
plt.show() 


# In[22]:


print(adj_list[3])


# In[23]:


list_node=[]
for j in range(1,1900):
    list_node.append(j)
        


# In[24]:


import networkx as nx
G=nx.DiGraph()


# In[25]:


G.add_nodes_from(list_node)


# In[26]:


node_tuple_list=[]
for i in adj_list:
    for j in adj_list[i]:
        node_tuple_list.append((i,j))
    
# tuple_ = adj_list.items()
# node_tuple = list(tuple_)
print(node_tuple_list)


# In[27]:


G.add_edges_from(node_tuple_list)


# In[28]:


h,a=nx.hits(G)
pr = nx.pagerank(G)


# In[29]:


for i in range(1,6):
    print (   i   ," ","authority score ",a[i],"   ","page rank score  ",pr[i],"   Hub Score",h[i],)


# In[30]:


Keymax = max(pr, key=pr.get) 
print(Keymax) 


# In[31]:


pr[9]


# In[32]:


from heapq import nlargest
kHighest = nlargest(50,pr,key = pr.get)
print("page rank score")
    
for val in kHighest: 
    print(val, ":",  pr.get(val))


# In[33]:


indeg_dic[9]


# In[34]:


indeg_dic[400]


# In[35]:


indeg_dic[103]


# In[36]:


indeg_dic[31]


# In[37]:


from heapq import nlargest
kHighest2 = nlargest(50,a,key = a.get)
print("authority score")

    
for val in kHighest2: 
    print(val, ":",  a.get(val))


# In[38]:


from heapq import nlargest
kHighest3 = nlargest(50,h,key = h.get)
print("hubscore")
    
for val in kHighest3: 
    print(val, ":",  h.get(val))


# In[39]:


print(adj_list[12])


# In[40]:


indeg_dic[8]


# In[41]:


hub_l=[]
auth_l=[]
page_rank_l=[]
for i in range(1,1900):
    hub_l.append(h[i])
    auth_l.append(a[i])
    page_rank_l.append(pr[i])


# In[42]:


import matplotlib.pyplot as plt 
  
# line 1 points 
 
# plotting the line 1 points  
plt.plot(list_node[1:50] ,hub_l[1:50], label = "hub score") 
  
# line 2 points 

# plotting the line 2 points  
plt.plot(list_node[1:50],auth_l[1:50], label = "Authority") 
plt.plot(list_node[1:50],page_rank_l[1:50], label = "Page rank ") 
    
# naming the x axis 
plt.xlabel('Node Number') 
# naming the y axis 
plt.ylabel('Score') 
# giving a title to my graph 
plt.title('Comparison of Algorithms') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show()


# In[43]:


# sh=G.neighbors(103)


# In[44]:


# import matplotlib.pyplot as plt 
  
# # line 1 points 
 
# # plotting the line 1 points  
# #plt.plot(list_node[1:50] ,hub_l[1:50], label = "hub score") 
  
# # line 2 points 

# # plotting the line 2 points  
# #plt.plot(list_node[1:50],auth_l[1:50], label = "Authority") 
# #plt.plot(list_node[1:50],page_rank_l[1:50], label = "Page rank ") 
# plt.plot(page_rank_l[1:50],val_indeg[1:50], label = "Indegree ") 
        
# # naming the x axis 
# plt.xlabel('x - axis') 
# # naming the y axis 
# plt.ylabel('y - axis') 
# # giving a title to my graph 
# plt.title('Comparison of Algorithms') 
  
# # show a legend on the plot 
# plt.legend() 
  
# # function to show the plot 
# plt.show()


# In[ ]:




