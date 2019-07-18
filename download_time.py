L=[["kb","kB","Mb","MB","Gb","GB","Tb","TB"],
   [2 ** 10,2 ** 10 * 8,2 ** 20,2 ** 20 * 8,2 ** 30,2 ** 30 * 8,2 ** 40,2 ** 40 * 8]]
   
def unit(a):
    i=0
    while i<len(L[0]):
        if a==L[0][i]:
            a=L[1][i]
            return a
        else:
            i=i+1
    return "Please key in the correct unit"

def download_time(x,y,z,w):
    L=[]
    assert unit(y)==int(unit(y)), "Please key in the correct unit"
    assert unit(w)==int(unit(w)), "Please key in the correct unit"
    total=(float(x)*unit(y))/(z*unit(w))
    a=total//3600
    b=(total-(a*3600))//60
    c=total-(a*3600)-b*60
    
    if a==float(a) and b==float(b):
        a=int(a)
        b=int(b)
    
    A=str(a)+" hours"
    B=str(b)+" minutes"
    C=str(c)+" seconds"
    
    if a==1:
        A="1 hour"
    if b==1:
        B="1 minute"
    if c==1:
        C="1 second"   
    
    L.append(A)
    L.append(B)
    L.append(C)
    
    return L[0]+", "+L[1]+", "+L[2]

print download_time(1024,'kB', 1, 'MB')

print download_time(1024,'kB', 1, 'Mb')

print download_time(13,'GB', 5.6, 'MB')

print download_time(13,'GB', 5.6, 'Mb')

print download_time(10,'MB', 2, 'kB')

print download_time(10,'MB', 2, 'kb')

print download_time(1,'kB', 1, 'MB')
