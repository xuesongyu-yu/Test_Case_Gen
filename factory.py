import random

from constraints import *

# 生成一个简单值参数（整数）
def gen_element(des):
    items = des.split(":")

    if len(items) == 1:
        f = open(r"clean_text.txt", "r")
        # readlines() 方法返回一个列表，其中包含文件中的每一行作为列表项。
        words = f.readlines()
        f.close()
        # 筛选出长度大于等于4的单词
        words = list(filter(lambda x: True if len(x) >= 4 else False, words))
        # 随机返回一个word
        word=words[random.randint(0, len(words) - 1)]
        word=word.rstrip('\n')
        return word

    #无限制性条件，例如i:-10:10
    if len(items) == 3:
        #items[1]为下限,item[2]为上限
        return random.randint(int(items[1]), int(items[2]))

    #有限制性条件，例如i:-10:10:even|positive
    conditions = items[3].split("|")
    while True:
        x = random.randint(int(items[1]), int(items[2]))
        rt = True

        #逐个条件过滤
        for con in conditions:
            #eval() 函数用来执行一个字符串表达式，并返回表达式的值。con的值被constrains.py中定义为函数
            if not eval(con + "(" + str(x) +")"):
                rt = False
                break

        #满足条件
        if rt:
            return x

# 生成一个构造类型参数（列表之类的）
def gen_structure(des):

    items = des.split("#")

    #使元素个数处于合法范围内
    a, b = int(items[2]), int(items[3])
    if a > b:
        a, b = b, a
    a = 1 if a < 0 else a
    b = 1 if b < 0 else b

    #num为生成元素个数
    num = random.randint(a, b)

    # 生成等比数列
    if items[0] == "r":
        par = []
        start = random.randint(2, 10)
        step  = random.randint(2, 5)
        for i in range(num):
            par.append(start * (step **i))
        #del par[random.randint(1, num -2)]
        #random.shuffle(par)#打乱列表
        #set 创建一个无序不重复元素集
        return str(set(par))

    # 生成其他列表
    par = []
    #判断对列表有无限制，如l#i:10:100:prime#0#3#exclusive|dec
    conditions = ([]  if len(items) <= 4 else items[4].split("|"))

    while len(par) < num:
        par.append(gen_element(items[1]))

    #去除重复元素
    if "exclusive" in conditions:
        par = list(set(par))
    #整体向前偏移
    if "progression" in conditions:
        dif = random.randint(1, 5)
        for i in range(num - 1):
            par.append(par[i] + dif)
            break
    #升序
    if "inc" in conditions:
        par.sort()
    #降序
    elif "dec" in conditions:
        par.sort(reverse=True)

    else:
        #shuffle() 方法将序列的所有元素随机排序。
        random.shuffle(par)

    return str(par) if items[0] == "l" else str(tuple(par)) if items[0] == "t" else str(set(par))


# 生成一个用例文件
#gn是用例个数，gw是总测试样例文件名，fn是生成测试用例文件，description是生成用例要求描述

def gen(gn, gw, fn, description):

    # 分解description
    des = str(description).split(",")

    # 打开单个用例文件。此文件仅包含测试数据，供阅卷系统使用。
    lw = open(fn, "w", encoding="utf-8")

    #按要求生成 gn 个测试用例
    for i in range(gn):
        gw.write("    print(" + fn[:-4:] +"(")
        par = ""
        for item in des:
            if item[0] in {"l", "t", "r", "d"}:
                par = par + ", " + gen_structure(item)
            else:
                par = par + ", " + str(gen_element(item))


        #par=par.rstrip("\n")
        par = par if par[0] != "," else par[2::]

        lw.write(par)#写local文件
        gw.write(par)#写global文件

        # 如参数只有一个，用例文件每行须用逗号结尾
        if len(description) == 1:
            lw.write(",")

        lw.write("\n")
        gw.write("))\n")

    lw.close()
    print("生成文件%s" % fn)

    gw.write("    print(\"-\" * 70)\n")
    gw.write("#" + "-"*70 + "\n")
    return
