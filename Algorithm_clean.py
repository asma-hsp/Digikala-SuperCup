#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np


# In[21]:


def get_input():
    shape = input()
    a = [int(x) for x in shape.split()]
    r, c = a[0], a[1]
    matrix = np.zeros((r,c))
    
    for i in range(r):
        row = input()
        a = [int(x) for x in row.split()]
        for j in range(len(a)):
            matrix[i][j] = a[j]
            
    return r, c, matrix


# In[22]:


def find_max(matrix, r, c):
    max_row = list()
    max_col = list()
    max_row_idx = list()
    max_col_idx = list()

    for i in range(r):
        max_row.append(matrix[i].max())
        max_row_idx.append((i, matrix[i].argmax()))

    for j in range(c):
        max_col.append(matrix[:,j].max())
        max_col_idx.append((matrix[:,j].argmax(), j))
    
    return max_row, max_col, max_row_idx, max_col_idx


# In[23]:


def make_graph(matrix, r, c, max_row, max_col):
    graph = np.zeros((r,c))
    for i in range(r):
        for j in range(c):
            if (max_row[i]==max_col[j]) &  (matrix[i][j]>0):
                graph[i][j]=1
                
    return  graph


# In[24]:


# Python program to find
# maximal Bipartite matching.
 
class GFG:
    def __init__(self,graph):
         
        # residual graph
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])
        self.matching = []
 
    # A DFS based recursive function
    # that returns true if a matching
    # for vertex u is possible
    def bpm(self, u, matchR, seen):
 
        # Try every job one by one
        for v in range(self.jobs):
 
            # If applicant u is interested
            # in job v and v is not seen
            if self.graph[u][v] and seen[v] == False:
                 
                # Mark v as visited
                seen[v] = True
                self.matching.append((u,v))

 
                '''If job 'v' is not assigned to
                   an applicant OR previously assigned
                   applicant for job v (which is matchR[v])
                   has an alternate job available.
                   Since v is marked as visited in the
                   above line, matchR[v]  in the following
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],  matchR, seen):
                    matchR[v] = u                
                    return True

        return False
 
    # Returns maximum number of matching
    def maxBPM(self):
        '''An array to keep track of the
           applicants assigned to jobs.
           The value of matchR[i] is the
           applicant number assigned to job i,
           the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs
         
        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):
             
            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs
             
            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1
        return result, matchR
 
 


# In[25]:


def matrix_change(matrix, r, c , max_row, max_col, max_row_idx, max_col_idx, matching,  matched_rows, matched_columns):
    changed_matrix = matrix.copy()
    flag = np.zeros((r,c))


    for i in range(r):
        if i not in matched_rows:
            flag[max_row_idx[i][0]][max_row_idx[i][1]] = 1

        for j in range(c):

            if j not in matched_columns:
                flag[max_col_idx[j][0]][max_col_idx[j][1]] = 1

            if (i, j) in matching:
                flag[i][j]=1

                if (changed_matrix[i][j]!=max_row[i]) & (changed_matrix[i][j]>0):
                    #print(i,j)
                    cnt = changed_matrix[i][j] 
                    changed_matrix[i][j] = max_row[i]
                    #print(max_row_idx[i][0], max_row_idx[i][1], (max_row[i]-cnt))

                    if (changed_matrix[max_row_idx[i][0]][max_row_idx[i][1]]>0):
                         changed_matrix[max_row_idx[i][0]][max_row_idx[i][1]] = changed_matrix[max_row_idx[i][0]][max_row_idx[i][1]]-                                                                             (max_row[i]-cnt)
                    elif (changed_matrix[max_col_idx[j][0]][max_col_idx[j][1]]>0):
                         changed_matrix[max_col_idx[j][0]][max_col_idx[j][1]] =  changed_matrix[max_col_idx[j][0]][max_col_idx[j][1]]-                                                                             (max_col[j]-cnt)

                            
    return changed_matrix, flag


# In[26]:


def count_solution (matrix, flag, r, c):
    #print(matrix)
    
    #print('\n', flag)
    cnt = 0
    for i in range(r):
        for j in range(c):
            if (flag[i][j]==0) & (matrix[i][j]>0):
                cnt+= matrix[i][j]-1
    
    return cnt


# In[27]:


def main():
    
    r, c, matrix = get_input()
    max_row, max_col, max_row_idx, max_col_idx = find_max(matrix, r, c)
    graph = make_graph(matrix, r, c, max_row, max_col)


    #print(graph)
    g = GFG(graph)
    
    matching = g.maxBPM()[1]
    list_matching = []
    
    #print(matching)
    
    for j in range(c):
        if (matching[j]>-1):
            list_matching.append((matching[j], j))
    
    
    matched_rows = [match[0] for match in list_matching]
    matched_columns = [match[1] for match in list_matching]
    
    
#    print(matching)
    
    changed_matrix, flags = matrix_change(matrix, r, c , max_row, max_col, max_row_idx, max_col_idx,                                          list_matching,  matched_rows, matched_columns)
    
    ret = count_solution(changed_matrix, flags, r, c)
    
    print(int(ret))


# In[28]:


main()


# In[ ]:




