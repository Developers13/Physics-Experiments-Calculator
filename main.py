import re,sympy
from math import sqrt
#import numba 
def seperate_alpha(string):
    _l=re.split("",string)
    l=[]
    for x in _l:
        if x.isalpha():
            l.append(x)
        else:
            pass
    return l

def partial_derivative(formula):
    global _vars
    _vars = seperate_alpha(formula)
    grad=[]
    vars=[]
    for i in range(len(_vars)):
        vars.append(sympy.symbols(_vars[i]))
        #Calculate partial dif
        
        #append into gradient matrix
        grad.append(sympy.diff(formula,vars[i]))
    return grad

#@jit(nopython=True)
def back_substitution(formula,var_value,d):
    global res
    res=[]
    str_grad=[]
    grad=partial_derivative(formula)
    for i in range(len(_vars)):
        str_grad.append(str(grad[i]))
        for j in range(len(_vars)):
            str_grad[i]=str_grad[i].replace(_vars[j],var_value[j])
            
        res.append(eval(str_grad[i]))
    for k in range(len(res)):
        res[k]=float(res[k])
        res[k]=res[k]*float(d[k])
    return res
    
a=input("Input formula, for example x**2+y**2 \n")
li=seperate_alpha(a)
v=[]
v_d=[]
for i in range(len(li)):
    v.append(input(f"input the {i}th variable value\n"))
    v_d.append(input(f"input the {i}th variable's uncertainty\n "))
final=back_substitution(a,v,v_d)
print(final)
_final=0
#Calculate sqrt of square sum of list final
for i in range(len(final)):
    _final+=final[i]**2
print(sqrt(_final))



