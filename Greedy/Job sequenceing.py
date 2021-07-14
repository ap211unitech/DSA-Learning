# jobs is a rray of object
# For Problem , Visit https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

def JobScheduling(jobs,n):
    deadlines=[jobs[i].deadline for i in range(n)]
    
    jobs=[[jobs[i].deadline,jobs[i].profit] for i in range(n)]
    jobs.sort(key=lambda x:(-x[1]))
    
    res=[-1 for i in range(max(deadlines))]
    
    for i in range(n):
        current_deadline=jobs[i][0]
        current_profit=jobs[i][1]
        
        j=current_deadline-1
        while(j>=0):
            if res[j]==-1:
                res[j]=i
                break
            j-=1
            
    total=0
    profit=0
    
    for i in res:
        if i!=-1:
            total+=1
            profit+=jobs[i][1]
    
    return [total,profit]


