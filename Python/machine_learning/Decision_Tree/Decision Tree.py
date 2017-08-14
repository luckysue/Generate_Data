#coding:utf-8

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
import graphviz
import pydot
from IPython.display import Image


allElectronics = open("AllElectronics.csv")
reader = csv.reader(allElectronics)
headers = next(reader)    # 读csv文件头
#print(headers)

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row) - 1])
    rowDict = {}
    for i in range(1,len(row) - 1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)
#print(featureList)

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()

#print("dummyX: " + str(dummyX))
#print(dummyX)
#print(vec.get_feature_names())

#print("labelList: " + str(labelList))
#print(labelList)

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
#print("dummyY: " + str(dummyY))

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX,dummyY)
#print("clf: " + str(clf))


with open("allElectronicInfomationGainOri.dot",'w') as f:
    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)

# dot_data = StringIO()
#
# import pydotplus
#
# dot_data = tree.export_graphviz(clf, out_file=None)
#
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf("ex.pdf")


# from IPython.display import Image
#
# dot_data = tree.export_graphviz(clf, out_file=None,
#
# feature_names=vec.get_feature_names(),
# filled=True, rounded=True,
# )
#
# graph = pydotplus.graph_from_dot_data(dot_data)
#
# Image(graph.create_png())



#oneRowX = dummyX[0, :]
##print("oneRowX: " + str(oneRowX))
#
#newRowX = oneRowX
#
#newRowX[0] = 1
#newRowX[2] = 0
##print("newRowX: " + str(newRowX))
#predictedY = clf.predict(newRowX)
##print("predictedY: " + str(predictedY))

