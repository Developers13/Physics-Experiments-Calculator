import math as m
from pyscript import document

# import statistical helpers from the new module
from stats import mean, avg_deviation, Dataset
def show(message:str):
    """
    Show message in the #part2 section.
    """
    document.querySelector('#part2').innerText=message

        

    


#main
#use pyscript to retrieve the data from the sheet
def master(event):
    event.preventDefault()
    
    #exp_prop=prop(document.querySelector('#dataform'))
    data_form = document.querySelector('#dataform')

    _data = str(document.querySelector('#input').value).strip().split()
    data_set = Dataset(_data)

    # Initial settings
    data_set.distribution = "Gaussian" if(document.querySelector('#distribution').value) == 'normal' else "uniform"
    data_set.confidence = float(document.querySelector('#confidence').value)
    data_set.inherient_error = float(document.querySelector('#uncertainty').value)

    
    res_average=mean(data_set.ob_data)
    res_deviation=avg_deviation(data_set.ob_data)
    res_standardError=data_set.standard_error()
    data_new = data_set.rm_bad_value()

    
    
    # Format dispose_log (expected shape: {int: {str: str, ...}, ...}) into a readable string
    epochs = sorted(data_set.dispose_log.keys())

    # compute max inner-key width across all epochs for alignment
    max_key_len = 0
    for e in epochs:
        inner = data_set.dispose_log.get(e, {}) or {}
        for k in inner.keys():
            max_key_len = max(max_key_len, len(str(k)))

    dispose_log_lines = []
    for epoch in epochs:
        dispose_log_lines.append(f"Epoch {epoch}:")
        inner = data_set.dispose_log.get(epoch, {}) or {}
        if not inner:
            dispose_log_lines.append('    (no entries)')
        else:
            for k in sorted(inner.keys(), key=lambda x: str(x)):
                v = inner[k]
                # pretty-print inner values (lists/dicts) and align keys using computed width
                def format_value(val):
                    if isinstance(val, (list, tuple)):
                        return ', '.join(str(x) for x in val)
                    if isinstance(val, dict):
                        return '; '.join(f"{kk}={format_value(vv)}" for kk, vv in val.items())
                    return str(val)

                dispose_log_lines.append(f"    {str(k):<{max_key_len}} : {format_value(v)}")
        dispose_log_lines.append('')

    # single string containing the formatted dispose log
    dispose_log_text = "\n".join(dispose_log_lines)

    # If nothing to show, display a friendly message
    if not dispose_log_text.strip():
        dispose_log_text = '(no dispose log entries)'

    # Safely write into the page: check element exists; otherwise fallback to `show()`
    target = document.querySelector("#part1")
    if target is not None:
        target.innerText = dispose_log_text
    else:
        show(dispose_log_text)


    a = data_set.uncertainty_A(data_new)
    b = data_set.uncertainty_B()
    post_text = f"Uncertainty of A:{a}\nUncertainty of B:{b}\nCombined:{m.sqrt(m.pow(a,2)+m.pow(b,2))}"
    show(post_text)



   

    