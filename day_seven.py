'''
九九乘法表
'''
for i in range(1,10):
    for x in range(2,10):
        mut = i*x
        print('%d*%d=%d'%(i,x,mut), end = '\t')