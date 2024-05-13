import math as m
from pyscript import document
tp=[0,0,0,1.32,1.20,1.14,1.11,1.09,1.08,1.07,1.06,1.06,1.05,1.04,1.03,1.02,1.00]
def mean(data):
    _sum=0
    for x in data:
        _sum+=float(x)

    return _sum/len(data)
class dataset:

    def __init__(self,org):
        self.distribution='uniform'
        self.trust_level=0.683
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
#use pyscript to retrieve the data from the sheet
def master(event):
    class prop:
        def __init__(self,form):
            self.form=form
            self.dist=0
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
        return  str(data).split(';')




    exp_prop.org_data=splitdata(exp_prop.org_data)

    org_data=exp_prop.org_data
    l=len(org_data)
    global data_set
    data_set=dataset(org_data)
    data_set.checkBadValue(org_data)
    data_set.removeBadValue(org_data)
    #write the result into the html with pyscript
    def post_process():
        res_average=mean(org_data)
        res_deviation=data_set.avgDeviation(org_data)
        res_standardError=data_set.standardError()
        A=data_set.UncertaintyA()
        B=data_set.UncertaintyB()
        combined=m.sqrt(A**2+B**2)
        global p
        p=f'Average{res_average}\nDeviation偏离度{res_deviation}\nStandard Error标准误差 :{res_standardError}\nAuncertaintyA类不确定度:{A}\nBUncertaintyB类不确定度{B}\nCombined uncertainty结合不确定度:{combined}'

            
    post_process()

    document.querySelector("#output").innerText=p
    ################################################################