# -*- coding: utf-8 -*-
'''
此脚本用于从fastqc软件运行产生的“fastqc_data.txt”文件中提取并整理信息，
信息包括文件名，总reads数，GC含量，Q20百分率，Q30百分率

在Unix或者Win命令行执行：
python3 fastqc2table.py fastqc_data.txt > result.xls

Date: 2018-09-28
E-mail: yuhang5783@163.com
'''
import sys
import re
fastqc_data = sys.argv[1]
# 读取文件名，总reads数，GC含量
for line in open(fastqc_data):
    if line.startswith("Filename"):
        filename = line.split("\t")[1].strip()
    if line.startswith("Total Sequences"):
        total_reads = line.split("\t")[1].strip()
    if line.startswith("%GC"):
        GC_content = line.split("\t")[1].strip()

# 读入所有行，正则匹配“#Quality”和“>>END_MODULE”之间的行
all_data = open(fastqc_data).read()
pattern = r'#Quality[\s\S]*?>>END_MODULE'
quality_data = re.findall(pattern, all_data)
# 匹配返回的是一个字符串元素的列表，将其分隔成为多个字符串的列表
quality_data = quality_data[0].split("\n")

# 将结果保存为质量值为键，reads数量为值得字典
q_dict = {}
for line in quality_data:
    if not (re.findall('#Quality', line) or re.findall('>>END_MODULE', line)):
        quality = line.split()[0]
        count = line.split()[1]
        q_dict[quality] = count

# 提取并计算比值
all_count = 0
q20 = 0
q30 = 0
for quality in q_dict.keys():
    all_count += float(q_dict[quality])
    if int(quality) >= 20:
        q20 += float(q_dict[quality])
    if int(quality) >= 30:
        q30 += float(q_dict[quality])

# 打印结果
print("File_Name", "Total_Reads", "GC_Content", "Q20(%)", "Q30(%)", sep="\t")
print(filename, total_reads, GC_content, q20/all_count * 100, q30/all_count * 100, sep="\t")
