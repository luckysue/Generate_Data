# coding:utf-8
from collections import Counter
from pytagcloud import create_tag_image, make_tags

counts = {'Python':14,'Mysql':8,'C':6,'Machine Learning':7,'Lunix shell':4,
          'Wireshark':4,'PPT':7,'Viso':6,'Git':6,'Eclipse':6,'Pycharm':5,'RapidMinder':3,
          'Writing':6,'Spider':6,'八爪鱼采集器':4}
counts = counts.items()

tags = make_tags(counts, maxsize=120)
create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='MicrosoftYaHei')

print('done !')