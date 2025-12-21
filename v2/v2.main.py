import re,sympy
from math import *
from pyscript import document
illegal_vars_list=('a','c','o','s','t','n','e','h','p','i')
#global varibles:_vars(list of varibles in the expr)

#local varibles:str_grad(list of gradient, in which every element is a string)
#import numba 
def splitVars(string:str) -> list[str]:
    if ',' in string:
        l=string.split(",")
    else:
        l=string.split()
    return l
def initVars(defvarslist):
    return 0 #I ain't know what this fn for..
def partial_derivative(expr,string):
    global _vars
    _vars = splitVars(string)
    grad=[]
    vars=[]
    for i in range(len(_vars)):
        vars.append(sympy.symbols(_vars[i]))
        #Calculate partial dif
    for j in range(len(_vars)):
        #append into gradient vector
        grad.append(sympy.diff(expr,vars[j]))
    return grad

#@jit(nopython=True)
def back_substitution(expr,varsString,var_value,d):
    global res
    res=[]
    str_grad=[]
    grad=partial_derivative(expr,varsString)
    for i in range(len(_vars)):
        str_grad.append(str(grad[i]))
        for j in range(len(_vars)):
            str_grad[i]=str_grad[i].replace(_vars[j],var_value[j])#replace the characters into numbers
            
        res.append(eval(str_grad[i]))#cannot calcuate sin cos..
    for k in range(len(res)):
        res[k]=float(res[k])
        res[k]=res[k]*float(d[k])
    return res

##################################################

def master(event):
    
    #retrieve and organize input data
    
    output=document.querySelector("#output2")
    data=document.querySelector("#data").value
    uncertainty=document.querySelector("#uncertainty").value
    defvars=document.querySelector("#defvars").value
    _expr=sympy.simplify(str(document.querySelector("#input").value))
    #pre-process data
    data=splitVars(str(data).strip())
    uncertainty=splitVars(uncertainty)
    #backsubstitution
    result=back_substitution(_expr,defvars,data,uncertainty)
    _result=0
    for i in range(len(result)):
        _result+=result[i]**2
    output.innerText=f"Result:{sqrt(_result)}"#the final output is the square root of square sum
def getOrder(event):
    _expr=sympy.simplify(str(document.querySelector("#input").value))
    output=document.querySelector("#output1")
    originalDefinedVars=document.querySelector("#defvars").value
    for x in illegal_vars_list:
        if (x in str(originalDefinedVars)):
            output.innerHTML="<p style='background-color:red'>ERR:</p>Contains illegal characters.<br />Confused?<a href='https://github.com/Developers13/Physics-Experiments-Calculator/issues/4'> Look at the issue and help us deal with this=></a>"
        else:
            continue
    else:
        output.innerText=f"Gradient:{partial_derivative(_expr,originalDefinedVars)}"


        

        