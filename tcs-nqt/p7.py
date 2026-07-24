a=[1,2,4,5,8,12,15,18,20,25]
b=[29,26,25,22,12,11,9,7,5,3]

def act(a,b):
    result=[]
    i=0
    j=len(b)-1
    while i<len(a) and j>=0:
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
                    
        else:
            result.append(b[j])
            j-=1
    while j>=0:
        result.append(b[j])
        j-=1
    while i<len(a):
        result.append(a[i])
        i+=1
    # remove duplicates optimal code
    result=list(dict.fromkeys(result))

    return result
print(act(a,b))