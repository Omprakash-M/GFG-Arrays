#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, n):
    	p=[True for _ in range(n+1)] 
    	pri=2
    	while(pri*pri<=n):
    	    if p[pri]==True:
    	        for i in range(pri*pri,n+1,pri):
    	            p[i]=False
            pri+=1
    	arr2=[]
        for i in range(2,n+1):
            if p[i]:
               arr2.append(i)
        return arr2
