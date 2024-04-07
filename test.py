with open("./succ_private.txt", "a+") as f:
    f.seek(0)  # 移动文件指针到开头
    lines = f.readlines()  # 读取所有行
    line_count = len(lines)  # 统计行数
    print("行数为", line_count)
