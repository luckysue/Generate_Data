from sklearn.datasets import load_iris

from sklearn import tree

iris = load_iris()

clf = tree.DecisionTreeClassifier()

clf = clf.fit(iris.data, iris.target)

with open("iris.dot", 'w') as f:

    f = tree.export_graphviz(clf, out_file=f)

import os

os.unlink('iris.dot')

#import pydotplus
#
#dot_data = tree.export_graphviz(clf, out_file=None)
#
#graph = pydotplus.graph_from_dot_data(dot_data)
#
#graph.write_pdf("iris.pdf")

# from IPython.display import Image
# 
# dot_data = tree.export_graphviz(clf, out_file=None,feature_names=iris.feature_names,
#                                 class_names=iris.target_names,filled=True, rounded=True,special_characters=True)
# 
# graph = pydotplus.graph_from_dot_data(dot_data)
# 
# Image(graph.create_png())

print(clf.predict(iris.data[:1, :]))

print(clf.predict_proba(iris.data[:1, :]))
