import sklearn
import pickle
import numpy as np


label_path = 'data/label_entitypair.pkl'
pred_path = 'result/best_pred_entitypair.pkl'

with open(label_path, 'rb') as input:
    label_entitypair = pickle.load(input)
with open(pred_path, 'rb') as input:
    pred_entitypair = pickle.load(input)
list_pred = []
for key in pred_entitypair.keys():
    tmp_prob = pred_entitypair[key][0]
    tmp_relation = pred_entitypair[key][1]
    tmp_entitypair = key
    list_pred.append((tmp_prob, tmp_entitypair, tmp_relation))
list_pred = sorted(list_pred, key=lambda x: x[0], reverse=True)
print('Len:', len(list_pred))
true_positive = 0
Precision = []
Recall = []
for i, item in enumerate(list_pred):
    tmp_entitypair = item[1]
    tmp_relation = item[2]
    label_relations = label_entitypair[tmp_entitypair]
    if tmp_relation in label_relations:
        true_positive += 1
        print(label_relations)
        if true_positive > 10:
            break
