#!/usr/bin/env  python
# --*--coding:utf-8 --*--
'''
需求：
0-10万提成10%
10-20万提成7.5%
20-40万提成5%
40-60万提成3%
60-100万提成1.5%
100万以上1%
思路：
请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
'''
'''
注：如果列表的顺序相反，计算结果不一样
'''
i = int(raw_input('input:'))
m = [1000000,600000,400000,200000,100000,0]
t = [0.01,0.015,0.03,0.05,0.075,0.1]


r = 0
for s in range(0,6):#循环列表元素数
    if i>m[s]:#判断输入的元素
        r+=(i-m[s])*t[s]
        print (i-m[s])*t[s]
        i=m[s]
print r
print r
print r