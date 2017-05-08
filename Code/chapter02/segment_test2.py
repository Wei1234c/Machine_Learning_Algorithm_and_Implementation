# -*- coding: utf-8 -*-

import sys  
import os
import jieba
import imp

# 设置utf-8 unicode环境
imp.reload(sys)
sys.setdefaultencoding('utf-8')

seg_list = jieba.cut("小明终于在1995年从北京清华大学毕业了。")
print("  ".join(seg_list))

