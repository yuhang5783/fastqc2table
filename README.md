# fastqc2table
 此脚本用于从fastqc软件运行产生的“fastqc_data.txt”文件中提取并整理信息，信息包括文件名，总reads数，GC含量，Q20百分率，Q30百分率

```
File_Name	Total_Reads	GC_Content	Q20(%)	Q30(%)
Y25_2.fq.gz	95453868	45	99.14114952	86.74958882
```



 在Unix或者Win命令行执行：
```shell
python3 fastqc2table.py fastqc_data.txt > result.xls
```

在你的Unix系统中，可以使用以下命令整理多个fastqc结果文件：

```shell
# 解压所有fastqc结果压缩包
for i in *.zip; do unzip $i; done
# 对所有文件夹中的“fastqc_data.txt”文件执行操作并将结果
ls -l | grep ^d | while read id; do python3 fastqc2table.py ${id##* }/fastqc_data.txt >> fastqc_table.xls; done
```



---

Date: 2018-09-28
E-mail: yuhang5783@163.com

