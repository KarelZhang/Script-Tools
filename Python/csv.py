import os

#读取数据
with open('./city1.csv') as file_object:
    lines_1=file_object.readlines()

with open('./city2.csv') as file_object:
    lines_2=file_object.readlines()

#存储年份
years_1 = []
years_2 = []

#存储城市群内部城市的GTFP
GTPFs_1 = []
GTPFs_2 = []

#处理数据
##剔除回车符
for i in range(len(lines_1)):
    lines_1[i] = lines_1[i].replace('\n','')

for i in range(len(lines_2)):
    lines_2[i] = lines_2[i].replace('\n','')

##剔除城市名称
lines_1 = lines_1[1:]
lines_2 = lines_2[1:]

##分割数据
if '\t' in lines_1[0]:
    for i in range(len(lines_1)):
        lines_1[i] = lines_1[i].split('\t')
elif ',' in lines_1[0]:
    for i in range(len(lines_1)):
        lines_1[i] = lines_1[i].split(',')

if '\t' in lines_2[0]:
    for i in range(len(lines_2)):
        lines_2[i] = lines_2[i].split('\t')
elif ',' in lines_2[0]:
    for i in range(len(lines_2)):
        lines_2[i] = lines_2[i].split(',')

##提取年份
for i in range(len(lines_1)):
    years_1.append(int(lines_1[i][0]))
    lines_1[i] = lines_1[i][1:]

for i in range(len(lines_2)):
    years_2.append(int(lines_2[i][0]))
    lines_2[i] = lines_2[i][1:]

##提取GTFP
for line in lines_1:
    tmp = []
    for element in line:
        tmp.append(float(element))
    GTPFs_1.append(tmp)

for line in lines_2:
    tmp = []
    for element in line:
        tmp.append(float(element))
    GTPFs_2.append(tmp)

##输出数据
print('**************************************************')
print('读取到的城市群1的GTFP结果为：')
for i in range(len(years_1)):
    string = str(years_1[i]) + ': '
    for element in GTPFs_1[i]:
        string = string + str(element) + '\t'
    print(string)
print('**************************************************')
print('读取到的城市群2的GTFP结果为：')
for i in range(len(years_2)):
    string = str(years_2[i]) + ': '
    for element in GTPFs_2[i]:
        string = string + str(element) + '\t'
    print(string)

#处理数据
##城市群1的城市个数
n_1 = len(GTPFs_1[0])
##城市群2的城市个数
n_2 = len(GTPFs_2[0])

##计算城市群的GTFP均值
mu_1 = []
mu_2 = []

for i in range(len(years_1)):
    tmp = 0
    for element in GTPFs_1[i]:
        tmp = tmp + element
    mu_1.append(tmp / n_1)

for i in range(len(years_2)):
    tmp = 0
    for element in GTPFs_2[i]:
        tmp = tmp + element
    mu_2.append(tmp / n_2)

##计算城市群1自己的基尼系数
G_1_1 = []
for i in range(len(years_1)):
    tem = 0
    for yi in GTPFs_1[i]:
        for yr in GTPFs_1[i]:
            tmp = tmp + abs(yi - yr)
    tmp = tmp / (2 * n_1 * n_1 * mu_1[i])
    G_1_1.append(tmp)

##计算城市群2自己的基尼系数
G_2_2 = []
for i in range(len(years_2)):
    tem = 0
    for yi in GTPFs_2[i]:
        for yr in GTPFs_2[i]:
            tmp = tmp + abs(yi - yr)
    tmp = tmp / (2 * n_2 * n_2 * mu_2[i])
    G_2_2.append(tmp)

##计算城市群1和城市群2之间的基尼系数
G_1_2 = []
for i in range(len(years_1)):
    tem = 0
    for yi in GTPFs_1[i]:
        for yr in GTPFs_2[i]:
            tmp = tmp + abs(yi - yr)
    tmp = tmp / (n_1 * n_2 * (mu_1[i] + mu_2[i]))
    G_1_2.append(tmp)

##输出结果
print('\n**************************************************')
print('城市群1的城市个数: ' + str(n_1))
print('城市群2的城市个数: ' + str(n_2))
print('城市群1的GTFP均值:')
for i in range(len(years_1)):
    string = str(years_1[i]) + ': ' + str(mu_1[i]) + '\t'
    print(string)
print('城市群2的GTFP均值:')
for i in range(len(years_2)):
    string = str(years_2[i]) + ': ' + str(mu_2[i]) + '\t'
    print(string)

print('\n**************************************************')
print('城市群1的自己的基尼系数:')
for i in range(len(years_1)):
    string = str(years_1[i]) + ': ' + str(G_1_1[i]) + '\t'
    print(string)
print('城市群2的自己的基尼系数:')
for i in range(len(years_2)):
    string = str(years_2[i]) + ': ' + str(G_2_2[i]) + '\t'
    print(string)
print('城市群1和城市群2之间的基尼系数:')
for i in range(len(years_1)):
    string = str(years_1[i]) + ': ' + str(G_1_2[i]) + '\t'
    print(string)
