class Solution(object):
    def reverse(self, x):
        
        a=str(x)

        if(a=='0'):
            return '0'
     
        p=a[::-1]
        p=p.lstrip('0')
        l=list(p)
    
        q=''
        for i in range(len(l)):
            if(l[i]=='-'):
                l.remove(l[i])
                r=''.join(l)
                q='-'+r
            else:
                q=p
        b=int(q)
    
        if b < -2**31 or b > 2**31-1:
            return 0
                       
        return q
