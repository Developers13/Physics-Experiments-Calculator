import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
from pyscript import document
import re

def parse_data_string(data_string):
    """解析数据字符串，支持空格和逗号分隔"""
    # 替换逗号为空格，然后分割
    data_string = data_string.replace(',', ' ')
    # 分割字符串并转换为浮点数
    data_list = [float(x.strip()) for x in data_string.split() if x.strip()]
    return data_list

def create_scatter_plot(x_data_str, y_data_str):
    """创建散点图并返回Base64编码的图像"""
    try:
        # 解析数据
        x_data = parse_data_string(x_data_str)
        y_data = parse_data_string(y_data_str)
        
        # 检查数据长度是否匹配
        if len(x_data) != len(y_data):
            return None, f"Data length mismatch: x has {len(x_data)} points, y has {len(y_data)} points"
        
        if len(x_data) == 0:
            return None, "No valid data entered"
        
        # 创建图形
        plt.figure(figsize=(8, 6))
        plt.scatter(x_data, y_data, color='blue', alpha=0.7, s=50)
        plt.grid(True, alpha=0.3)
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title(f'Scatter Plot ({len(x_data)} data points)')
        
        # 添加趋势线（如果数据点足够）
        if len(x_data) > 1:
            z = np.polyfit(x_data, y_data, 1)
            p = np.poly1d(z)
            plt.plot(x_data, p(x_data), "r--", alpha=0.8, label=f'Trend line: y = {z[0]:.2f}x + {z[1]:.2f}')
            plt.legend()
        
        # 转换为Base64
        buffer = BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        img_str = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        return f"data:image/png;base64,{img_str}", None
        
    except Exception as e:
        return None, f"Plotting error: {str(e)}"

def create_function_plot(formula, x_min, x_max):
    """创建函数图像"""
    try:
        # 创建x值范围
        x = np.linspace(float(x_min), float(x_max), 1000)
        
        # 安全地计算y值
        y = []
        for x_val in x:
            # 替换公式中的x为当前值
            expr = formula.replace('x', f'({x_val})')
            # 使用eval计算，但限制在安全范围内
            safe_dict = {
                'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                'exp': np.exp, 'log': np.log, 'sqrt': np.sqrt,
                'pi': np.pi, 'e': np.e
            }
            y_val = eval(expr, {"__builtins__": {}}, safe_dict)
            y.append(y_val)
        
        # 创建图形
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, 'b-', linewidth=2)
        plt.grid(True, alpha=0.3)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'Function Plot: y = {formula}')
        
        # 转换为Base64
        buffer = BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        img_str = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        return f"data:image/png;base64,{img_str}", None
        
    except Exception as e:
        return None, f"Function plotting error: {str(e)}"

def generate_plot(event):
    """生成绘图的主函数"""
    output_div = document.querySelector("#plot-output")
    
    # 检查当前模式
    scatter_inputs = document.querySelector("#scatter-inputs")
    is_scatter_mode = not scatter_inputs.classList.contains("hidden")
    
    if is_scatter_mode:
        # 散点模式
        x_data = document.querySelector("#scatter-x").value
        y_data = document.querySelector("#scatter-y").value
        
        if not x_data.strip() or not y_data.strip():
            output_div.innerHTML = "<span class='text-red-500'>Please enter X and Y data</span>"
            return
        
        image_data, error = create_scatter_plot(x_data, y_data)
        
        if error:
            output_div.innerHTML = f"<span class='text-red-500'>{error}</span>"
        else:
            output_div.innerHTML = f"<img src='{image_data}' class='w-full h-full object-contain' alt='Scatter Plot'>"
    
    else:
        # 函数模式
        formula = document.querySelector("#plot-formula").value
        x_min = document.querySelector("#plot-xmin").value
        x_max = document.querySelector("#plot-xmax").value
        
        if not formula.strip():
            output_div.innerHTML = "<span class='text-red-500'>Please enter function formula</span>"
            return
        
        image_data, error = create_function_plot(formula, x_min, x_max)
        
        if error:
            output_div.innerHTML = f"<span class='text-red-500'>{error}</span>"
        else:
            output_div.innerHTML = f"<img src='{image_data}' class='w-full h-full object-contain' alt='Function Plot'>"









