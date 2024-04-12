import math as m
from re import I
tp=[0,0,0,1.32,1.20,1.14,1.11,1.09,1.08,1.07,1.06,1.06,1.05,1.04,1.03,1.02,1.00]
def mean(data):
    average=0
    sum=0
    for i in data:
        sum=sum+i
    average=sum/len(data)
    return average
class dataset:

    def __init__(self,org):
        self.distribution='uniform'
        self.accuracy=2 #2 digits for float
        self.trust_level=0.683
        self.org=org
        
    @staticmethod   
    def avg(org):
        avg_data=mean(org)
        return avg_data
    @staticmethod
    def avgDiviation(org):
        diff_data=[]
        for i in range(len(org)):
            diff_data.append(org[i]-mean(org))
        return diff_data
    
    def standardError(self,org,difference):
        square_sum=0
        for i in range(len(difference)):
            square_sum+=difference[i]**2
        #here might be wrong....
        result=tp[len(org)]*m.sqrt(square_sum/(len(org)))
        #--
        return result

#some codes here...

    def checkBadValue(self,org):
        self.bvkey=[]
        d=self.avgDiviation(org)
        for i in range(len(org)):
            
            if abs(d[i])>3*self.standardError(len(org),org):
                self.isbad=True
                self.bvkey.append(i)
                
            elif i<len(org):
                continue
            else:
                self.isbad=False
    

    def removeBadValue(self,org):
        if self.isbad:
            for j in range(len(self.bvkey)):
                print('Removed bad value:Number %d Value %d in original list' %(self.bvkey[j],org[self.bvkey[j]]))
                org.pop(self.bvkey[j])
            else:
                org=recalculate(org)
        else:
            pass
def recalculate(data):
    data_set.checkBadValue(data)
    if data_set.isbad:
        data_set.removeBadValue(data)
        return data
    else:
        return data
        
        
            
        

        

    


#main



l=int(input('input lenth'))
org_data=[]
for x in range(l):
    t=float(input('number %d' %(x+1)))
    org_data.append(t)
data_set=dataset(org_data)
print('input the experiment properties:')
print('Distribution:\n1.Uniform Distribution\n2.Gaussian Distribution')
d=int(input())
if d==2:
   data_set.distribution='Gaussian'
   pass
else:
    print('Uniform by default')
print('input trust level')
tl=int(input('1. 0.683 2. 0.95'))
if tl==2:
    data_set.trust_level=0.95
    pass
else:
    print('0.683 by default')
print('input accuracy')
acc=int(input())
data_set.accuracy=acc

print(data_set.avgDiviation(org_data))
print(data_set.standardError(org_data,data_set.avgDiviation(org_data)))
raise ValueError




       
