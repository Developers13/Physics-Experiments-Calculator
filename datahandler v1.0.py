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
        self.trust_level=0.683
        self.org=org
        self.accuracy=2
        self.bvkey=[]
        self.inherientError=0.0

      
    def avg(self):
        avg_data=round(mean(self.org),self.accuracy)
        return avg_data
    @staticmethod
    def avgDeviation(org):
        diff_data=[]
        for i in range(len(org)):
            diff_data.append(org[i]-mean(org))
        return diff_data
    
   
    def standardError(self):
        square_sum=0
        for i in range(len(self.avgDeviation(self.org))):
            square_sum+=self.avgDeviation(self.org)[i]**2
        #here might be wrong....
        result=tp[len(self.org)]*m.sqrt(square_sum/(len(self.org)))
        #--
        return result

#some codes here...

    def checkBadValue(self,org):
        
        d=self.avgDeviation(org)
        for i in range(len(org)):
            
            if abs(d[i])>3*self.standardError():
                self.bvkey.append(i)
                
            elif i<len(org):
                continue
            else:
                pass
    

    def removeBadValue(self,org):
        if len(self.bvkey) != 0:
            for j in range(len(self.bvkey)):
                print('Removed bad value:Number %d Value %d in original list' %(self.bvkey[j],org[self.bvkey[j]]))
                org.pop(self.bvkey[j])
            else:
                org=recalculate(org)
                print('Completed.Recalulate:')
                print('Average:', self.avg())

                print('Deviation \n', self.avgDeviation(org))

                print('Standard Error :', self.standardError())
                print()
        else:
            print('No bad values. Pass')   
    def UncertaintyA(self):
        return self.standardError()/m.sqrt(len(self.org))
    def UncertaintyB(self):
        if self.distribution=='Gaussian':
            return self.inherientError/3*self.standardError()
        else:
            return self.inherientError/1.46
def recalculate(data):
    data_set.checkBadValue(data)
    if len(data_set.bvkey) != 0:
        data_set.removeBadValue(data)
        return data
    else:
        return data
        
####################################
#Part2 the propagation of uncertainty
        
            


        

    


#main



l=int(input('input lenth共有多少组数据？'))
org_data=[]
for x in range(l):
    t=float(input('number %d\n' %(x+1)))
    org_data.append(t)
data_set=dataset(org_data)
print('输入实验属性properties:')
print('数据分布:\n1.Uniform平均分布\n2.Gaussian Distribution正态分布')
d=int(input())
if d==2:
   data_set.distribution='Gaussian'
   pass
else:
    print('默认平均分布')
print('置信区间')
tl=int(input('1. 0.683 2. 0.95'))
if tl==2:
    data_set.trust_level=0.95
    pass
else:
    print('0.683 默认')
data_set.inherientError=round(float(input('The uncertainty of the experiment equipment输入实验仪器的灵敏度:')), data_set.accuracy)

print('Average:', data_set.avg())

print('Deviation偏离度 \n', data_set.avgDeviation(org_data))

print('Standard Error标准误差 :', data_set.standardError())
A=data_set.UncertaintyA()
B=data_set.UncertaintyB()
print('AuncertaintyA类不确定度:', A)

print('BUncertaintyB类不确定度', B)
print('Combined uncertainty结合不确定度:', round(m.sqrt(A**2+B**2), data_set.accuracy))
data_set.checkBadValue(org_data)
data_set.removeBadValue(org_data)







       
