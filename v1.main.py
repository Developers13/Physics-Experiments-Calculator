import math as m
from pyscript import document

# import statistical helpers from the new module
from stats import mean, Dataset

def recalculate(data):
    # recompute bad-value keys and return a cleaned copy
    data_set.checkBadValue(data)
    if data_set.bvkey:
        return data_set.removeBadValue(data)
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
        def __init__(self, form):
            # form: DOM form element (from pyscript/document)
            self.form = form
            self.dist = ''
            # confidence and uncertainty
            self.conf = 0
            self.uncer = 0.0
            # org_data can be the raw input string or a parsed list of floats
            self.org_data = ''
    exp_prop=prop(document.querySelector('#dataform'))
    
    #event.preventDefault()
    exp_prop.dist=(document.querySelector('#distribution').value)
    exp_prop.conf=float(document.querySelector('#confidence').value)
    exp_prop.uncer=float(document.querySelector('#uncertainty').value)
    exp_prop.org_data=str(document.querySelector('#input').value)
        

    def  splitdata(data):
        _data=str(data).strip().split(' ')
        _data=[float(x) for x in _data] 
        return _data




    exp_prop.org_data=splitdata(exp_prop.org_data)

    org_data=exp_prop.org_data
    l=len(org_data)
    global data_set
    data_set = Dataset(org_data)
    if exp_prop.dist=='normal':
        data_set.distribution='Gaussian'
    data_set.confidence=exp_prop.conf
    data_set.inherientError=exp_prop.uncer
    # iterate: detect bad values and remove them until none remain
    data_set.checkBadValue(org_data)
    while data_set.bvkey:
        org_data = data_set.removeBadValue(org_data)
        data_set = Dataset(org_data)
        data_set.checkBadValue(org_data)

    
    #write the result into the html with pyscript
    def post_process():
        res_average=mean(org_data)
        res_deviation=data_set.avgDeviation(org_data)
        res_standardError=data_set.standardError()
        A=data_set.UncertaintyA()
        B=data_set.UncertaintyB()
        combined=m.sqrt(A**2+B**2)
        relative=combined/res_average
        global p
        p=f'Average{res_average}\nDeviation偏离度{res_deviation}\nStandard Error标准误差 :{res_standardError}\nAuncertaintyA类不确定度:{A}\nBUncertaintyB类不确定度{B}\nCombined uncertainty结合不确定度:{combined}\nRelative Error相对误差{relative}'

            
    post_process()
    
        
    document.querySelector("#part1").innerText=p
    ################################################################
