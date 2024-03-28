import numpy as npy
import math as m
tp=[0,0,0,1.32,1.20,1.14,1.11,1.09,1.08,1.07,1.06,1.06,1.05,1.04,1.03,1.02,1.00]
class dataset_prop:
    def __init__(self):
        self.distribution='uniform'
        self.accuracy=2
        self.trust_level=0.683
class standardize:
    def __init__(self):
        self.iserror=False
    def standard(self,org):
        if type(org)==list:
            for i in range(len(org)):
                org[i]=round(org[i],dataset_prop().accuracy)#2 digits for float
            return org
        else:
            org=round(org,dataset_prop().accuracy)
            return list(org)
class avg_minus:
    def __init__(self):
        self.iserror=False
    def avg(self,org):
        avg_data=npy.mean(org)
        return avg_data
    def diff(self,org):
        diff_data=[]
        for i in range(len(org)):
            
            diff_data.append(org[i]-npy.mean(org))
        return diff_data
#some codes here...
class standard_error:
    def __init__(self):
        self.iserror=False
    def standard_error(self,times,difference):
        square_sum=0
        for i in range(len(difference)):
            square_sum+=difference[i]**2
        #here might be wrong....
        result=tp[times-1]*m.sqrt(square_sum/(times-1))
        #
        return result
class remove_bad_value:
    def __init__(self):
        self.isbad=False
    def chkbv(self,org):
        self.bvkey=[]
        for i in range(len(org)):
            d=dif.diff(org)
            if abs(d[i])>3*sig.standard_error(len(org),org):
                self.isbad=True
                self.bvkey.append(i)
                
            elif i<len(org):
                continue
            else:
                self.isbad=False
    def rmbv(self,org):
        if self.isbad:
            for j in range(len(self.bvkey)):
                print('Removed bad value:Number %d Value %d in original list' %(self.bvkey[j],org[self.bvkey[j]]))
                org.pop(self.bvkey[j])
            else:
                org=recalculate(org)
        else:
            pass
bv=remove_bad_value()
def recalculate(data):
    bv.chkbv(data)
    if bv.isbad:
        bv.rmbv(data)
        return data
    else:
        return data
        
        
            
        

        

    


#main
sta=standardize()
dif=avg_minus()
sig=standard_error()
prop=dataset_prop()
print('input the experiment properties:')
print('Distribution:\n1.Uniform Distribution\n2.Gaussian Distribution')
d=int(input())
if d==2:
    prop.distribution='Gaussian'
else:
    print('Uniform by default')
print('input trust level')
tl=int(input('1. 0.683 2. 0.95'))
if tl==2:
    prop.trust_level='0.95'
else:
    print('0.683 by default')
print('input accuracy')
acc=int(input())
prop.accuracy=acc


l=int(input('input lenth'))
org_data=[]
for x in range(l):
    t=float(input('number %d' %(x+1)))
    org_data.append(t)
bv.chkbv(org_data)
bv.rmbv(org_data)
a=dif.diff(org_data)
print(a)
a1=sta.standard(a)
print(a1)
print(sig.standard_error(l,a1))



       
