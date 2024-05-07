import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pandastable import Table

def import_excel():
    # 打开文件对话框选择Excel文件
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    if file_path:
        try:
            # 使用pandas读取Excel文件
            df = pd.read_excel(file_path)
            # 填充表格的数据
            for i in range(min(len(df), 3)):
                for j in range(min(len(df.columns), 2)):
                    table.model.df.at[i, j] = df.iat[i, j]
        except Exception as e:
            print("Failed to import Excel:", e)

# 创建主窗口
root = tk.Tk()
root.title("Excel Viewer")

# 创建一个Frame用于放置按钮
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# 创建按钮，点击按钮导入Excel文件
import_button = tk.Button(button_frame, text="Import Excel", command=import_excel)
import_button.pack()

# 创建一个Frame用于放置表格
frame = tk.Frame(root)
frame.pack(pady=20)

# 创建一个空的3行2列的表格
df = pd.DataFrame(index=range(3), columns=range(2))
table = Table(frame, dataframe=df)
table.show()

# 启动主循环
root.mainloop()
