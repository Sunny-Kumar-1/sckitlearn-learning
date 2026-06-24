import numpy as np
def gd(x,y):
    m_curr = b_curr = 0
    iter =10000
    n = len(x)
    lr = 0.001

    for i in range(iter):
        y_pred = m_curr * x + b_curr
        cost = (1/n)*sum((y-y_pred))**2
        md = -(2/n)* sum(x*(y-y_pred))
        bd = -(2/n)* sum(y-y_pred)
        m_curr = m_curr - lr * md
        b_curr = b_curr - lr * bd
        print("m{},b{},iteration {}, cost {}".format(m_curr,b_curr,i,cost))

x = np.array([1,2,3,4,5,6])
y = np.array([8,16,24,32,40,48])

gd(x,y)
