# coding=utf-8
# ����ѡȡ�����

from copy import copy
from tmall import *


def generateFeature(classify, data):
    F = {}

    item = {
        'click': 0,
        'buy': 0,
        'fav': 0,
        'cart': 0,
        'diff_day': 1000,

    }


    feature_name = ['click', 'buy', 'fav', 'cart', 'diff_day']

    for uid, bid, action_type, month, day in data:

        if classify != getClassify(month, day):
            continue

        F.setdefault(uid, {})
        F[uid].setdefault(bid, copy(item))

        e = F[uid][bid]

        if action_type == 0:
            e['click'] += 1
        elif action_type == 1:
            e['buy'] += 1
        elif action_type == 2:
            e['fav'] += 1
        elif action_type == 3:
            e['cart'] += 1

        diff_day = getDiffDayByClass(classify, (month, day))
        if diff_day < e['diff_day']:
            e['diff_day'] = diff_day

    return F, feature_name
