import hashlib
import tkinter as tk
import tkdnd
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import messagebox, Label, Button, filedialog

dropped_files = []

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def on_drop(event):
    file_paths = root.tk.splitlist(event.data)
    
    for file_path in file_paths:
        file_path = file_path.replace('{', '').replace('}', '')
        add_file(file_path)

def add_file(file_path):
    global dropped_files
    dropped_files.append(file_path)
    if len(dropped_files) == 2:
        file1, file2 = dropped_files
        compare_and_show_result(file1, file2)
        dropped_files = []  # 清空列表以便下次比较
    update_file_list_label()

def update_file_list_label():
    file_list_label.config(text="选择的文件:\n" + "\n".join(dropped_files))

def compare_and_show_result(file1, file2):
    md5_first = calculate_md5(file1)
    md5_second = calculate_md5(file2)
    
    result_text = f'第一个文件的MD5: {md5_first}\n第二个文件的MD5: {md5_second}\n\n'
    result_text += '两个文件的MD5相同。' if md5_first == md5_second else '两个文件的MD5不同。'
    messagebox.showinfo('MD5对比结果', result_text)

def select_files():
    # 只有当已选择的文件少于2个时才允许选择更多文件
    if len(dropped_files) < 2:
        file_path = filedialog.askopenfilename()
        if file_path:
            add_file(file_path)

def clear_file_list():
    global dropped_files
    dropped_files = []
    update_file_list_label()

root = TkinterDnD.Tk()
root.title('MD5文件校验器 ——by.yanhy')
root.geometry('600x400')  # 更大的窗口尺寸

select_button = Button(root, text='选择文件', command=select_files)
select_button.pack(side=tk.TOP, pady=5)

clear_button = Button(root, text='清空文件列表', command=clear_file_list)
clear_button.pack(side=tk.TOP, pady=5)

file_list_label = Label(root, text='选择的文件:')
file_list_label.pack(side=tk.TOP, pady=5)

result_label = Label(root, text='请拖拽文件到这里或使用上方的按钮选择文件', wraplength=560)
result_label.pack(side=tk.TOP, pady=5, fill=tk.BOTH, expand=True)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
