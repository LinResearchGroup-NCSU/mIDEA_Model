import os
import sys

# 切换工作目录到脚本所在的子文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())

# 现在可以使用相对路径访问文件
if not os.path.exists('../for_bindingE/1hlo/tms/native.tm'):
    print("Error: ../for_bindingE/1hlo/tms/native.tm not found")
    sys.exit(1)
else:
    print("ture")
