# 此脚本，用于将 conda 格式的 requirements.txt 文件转换为 pip 格式

# 读取文件内容
with open("requirements.txt", "r") as f:
    lines = f.readlines()
res=""
# 每行的字符串修改
def convert_str(s:str):
    # 判断是否为注释行
    if s.startswith("#"):
        return None
    parts=s.split("=")
    return f"{parts[0]}=={parts[1]}" if parts[2].startswith("pypi") else None

for i in range(len(lines)):
    tmp = convert_str(lines[i])
    if tmp != None:
        res+=tmp+"\n"

# 写入文件
with open("requirements.txt", "w") as f:
    f.write(res)

