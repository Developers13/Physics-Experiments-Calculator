import math as m
from pyscript import document
tp1=[0,0,0,1.32,1.20,1.14,1.11,1.09,1.08,1.07,1.06,1.05,1.04,1.03,1.02,1.00]
tp2=[0,0,0,4.30,3.18,2.78,2,57,2.45,2.36,2.31,2.26,2.23,2.13,2.09,2.04,1.96]
def mean(data):
    _sum=0
    for x in data:
        _sum+=float(x)

    return _sum/len(data)
class dataset:

    def __init__(self,org):
        self.distribution='uniform'
        self.confidence=0.683
        self.org=org
        self.accuracy=2
        self.bvkey=[]
        self.inherientError=0.0

    @staticmethod
    def avgDeviation(org):
        diff_data=[]
        for i in range(len(org)):
            diff_data.append(float(org[i])-mean(org))
        return diff_data
    
   
    def standardError(self):
        square_sum=0
        for i in range(len(self.avgDeviation(self.org))):
            square_sum+=self.avgDeviation(self.org)[i]**2
        #here might be wrong....
        if len(self.org)<=10:
            if self.confidence==0.683:
                result=tp1[len(self.org)]*m.sqrt(square_sum/(len(self.org)))
            else:
                result=tp2[len(self.org)]*m.sqrt(square_sum/(len(self.org)))
        elif(10<len(self.org)<=15):
            if self.confidence==0.683:
                result=1.05*m.sqrt(square_sum/(len(self.org)))
            else:
                result=2.23*m.sqrt(square_sum/(len(self.org)))
        elif(15<len(self.org)<=20):
            if self.confidence==0.683:
                result=1.04*m.sqrt(square_sum/(len(self.org)))
            else:
                result=2.13*m.sqrt(square_sum/(len(self.org)))
        elif(20<len(self.org)<=30):
            if self.confidence==0.683:
                result=1.03*m.sqrt(square_sum/(len(self.org)))
            else:
                result=2.09*m.sqrt(square_sum/(len(self.org)))
        elif(30<len(self.org)<=50):
            if self.confidence==0.683:
                result=1.02*m.sqrt(square_sum/(len(self.org)))
            else:
                result=2.04*m.sqrt(square_sum/(len(self.org)))
        else:
            if self.confidence==0.683:
                result=1.00*m.sqrt(square_sum/(len(self.org)))
            else:
                result=1.96*m.sqrt(square_sum/(len(self.org)))
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
            for x in self.bvkey:
                show(f'Removed bad value:Number {x+1} Value {org[x]} in original list')
                org.pop(x)
                self.bvkey.remove(x)
            else:
                return org
        else:
            show('No bad values. Pass')
            return 0 
    def UncertaintyA(self):
        return self.standardError()/m.sqrt(len(self.org))
    def UncertaintyB(self):
        if self.distribution=='Gaussian':
            return self.inherientError/3
        else:
            return self.inherientError/1.46
def recalculate(data):
    data_set.checkBadValue(data)
    if len(data_set.bvkey) != 0:
        data_set.removeBadValue(data)
        return data
    else:
        return data
def show(message):
    document.querySelector('#part2').innerText=message
####################################
#Part2 the propagation of uncertainty
        
            


        

    


#main
#use pyscript to retrieve the data from the sheet
def master(event):
    event.preventDefault()
    class prop:
        def __init__(self,form):
            self.form=form
            self.dist=''
            self.conf=0
            self.uncer=0.0
            self.org_data=''
    exp_prop=prop(document.querySelector('#dataform'))
    
    #event.preventDefault()
    exp_prop.dist=(document.querySelector('#distribution').value)
    exp_prop.conf=float(document.querySelector('#confidence').value)
    exp_prop.uncer=float(document.querySelector('#uncertainty').value)
    exp_prop.org_data=str(document.querySelector('#input').value)
        

    def  splitdata(data):
        _data=str(data).split(' ')
        _data=[float(x) for x in _data] 
        return _data




    exp_prop.org_data=splitdata(exp_prop.org_data)

    org_data=exp_prop.org_data
    l=len(org_data)
    global data_set
    data_set=dataset(org_data)
    if exp_prop.dist=='normal':
        data_set.distribution='Gaussian'
    data_set.confidence=exp_prop.conf
    data_set.inherientError=exp_prop.uncer
    while(data_set.removeBadValue(org_data)!=0):
        org_data=data_set.removeBadValue(org_data)
        data_set.checkBadValue(org_data)

    
    #write the result into the html with pyscript
    def post_process():
        res_average=mean(org_data)
        res_deviation=data_set.avgDeviation(org_data)
        res_standardError=data_set.standardError()
        A=data_set.UncertaintyA()
        B=data_set.UncertaintyB()
        combined=m.sqrt(A**2+B**2)
        relative=res_average/combined
        global p
        p=f'Average{res_average}\nDeviation偏离度{res_deviation}\nStandard Error标准误差 :{res_standardError}\nAuncertaintyA类不确定度:{A}\nBUncertaintyB类不确定度{B}\nCombined uncertainty结合不确定度:{combined}\nRelative Error相对误差{relative}'

            
    post_process()
    
        
    document.querySelector("#part1").innerText=p
    ################################################################