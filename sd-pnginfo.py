# _*_ coding:utf-8 _*_
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def get_pnginfo(file_path):
    print('path:', file_path)
    img = Image.open(file_path)
    parameters_arr = img.info
    print(parameters_arr)
    parameters = parameters_arr.get('parameters', 'No parameters found')
    return parameters

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        parameters = get_pnginfo(file_path)
        update_ui(file_path, parameters)

def update_ui(file_path, parameters):
    # 更新UI，显示缩放后的图片和参数
    img = Image.open(file_path)
    img.thumbnail((200, 200))  # 缩放图片大小
    img = ImageTk.PhotoImage(img)

    # 清空之前的内容
    canvas.delete("all")

    # 显示图片
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    canvas.image = img

    # 显示参数
    parameter_text.config(state=tk.NORMAL)
    parameter_text.delete(1.0, tk.END)
    parameter_text.insert(tk.END, parameters)
    parameter_text.config(state=tk.DISABLED)

# 创建主窗口
root = tk.Tk()
root.title("Image Parameter Viewer")
root.geometry("500x500")

# 创建选择文件按钮
select_file_button = tk.Button(root, text="Select Image", command=open_file_dialog)
select_file_button.pack(pady=10)

# 创建画布用于显示缩放后的图片
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# 创建文本框用于显示参数，可滚动
parameter_text = tk.Text(root, wrap=tk.WORD, width=60, height=10, state=tk.DISABLED)
parameter_text.pack(pady=10)

root.title("stable diffusion PNG绘图参数提取工具 - 爱思考吧")
# 运行主循环
root.mainloop()
