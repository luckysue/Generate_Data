print(__doc__)

import numpy as np
import pylab as pl
from sklearn import svm

np.random.seed(0)
X = np.r_[np.random.randn(40,2) - [2,2], np.random.randn(40,2) + [2,2]]
Y = [0] * 40 + [1] *40
# print(X)
# print(Y)

clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

w = clf.coef_[0]
# print(w)

a = -w[0] / w[1]
xx = np.linspace(-5, 5)

yy = a * xx - (clf.intercept_[0]) / w[1]

print("clf.intercept_: ",clf.intercept_)

b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a *xx + (b[1] - a * b[0])

print("w: ",w)
print("a: ",a)
print("support vectors: ",clf.support_vectors_)
print("clf.coef_: ",clf.coef_)


pl.plot(xx,yy,'k-')
pl.plot(xx,yy_down,'g--')
pl.plot(xx,yy_up,'r--')

pl.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1],
           s=80,facecolors='y')
pl.scatter(X[:,0],X[:,1],c=Y,cmap=pl.cm.Paired)

pl.axis('tight')
pl.show()



