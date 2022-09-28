class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        li=[]
        d=dict()
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                k=i
                li.append(i)
                break
        total=(n*(n+1))//2
        array_sum= sum(arr)-k
        li.append(abs(total-array_sum))
        return(li)
