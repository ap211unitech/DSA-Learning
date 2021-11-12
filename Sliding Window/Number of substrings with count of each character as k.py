def Issame(freq, k):
    for i in freq.keys():
        if freq[i] != k and freq[i] != 0:
            return False
    return True

def count_substrings(s,k):
    n=len(s)
    dist=len(set([i for i in s]))
    count=0
    
    for i in range(1,dist+1):
        
        
        length=i*k
        start=0
        end=start+length-1
        
        freq={}
        for j in range(start,min(end+1,n)):
            freq[s[j]]=freq.get(s[j],0)+1
        while(end<n):
            if Issame(freq,k):
                count+=1
                
            freq[s[start]]-=1
                
            start+=1
            end+=1
            if end<n:
                freq[s[end]]=freq.get(s[end],0)+1
    return count
                

if __name__ == '__main__':
    s = "ababcd"
    k = 2
    print(count_substrings(s, k))
    s = "aabbc"
    k = 2
    print(count_substrings(s, k))
