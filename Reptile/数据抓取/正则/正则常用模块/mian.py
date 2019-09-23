# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/16 0016 12:12'

import re

# 1、find_all()：匹配所有符合条件的字符，返回列表
text = "a1 price is $99，a2 price is $79"
ret = re.findall('\$\d+', text)
print(ret)  # ['$99', '$79']

# 2、sub：替换字符
# 2.1、替换价格
text = "a1 price is $99，a2 price is $79"
ret = re.sub('\$\d+', '0', text)  # sub（待替换，替换成，执行字符串）
print(ret)  # a1 price is 0，a2 price is 0
print('='*30)

# 2.2、将标签替换为空

html = """
<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
        <p>职位职责：</p>
<p>1、负责公司客服智能化项目的设计和开发维护；</p>
<p>2、负责业务需求分析，将业务需求拆分成独立的业务功能，并负责相关的开发等工作；</p>
<p>3、负责部分核心技术问题的攻关，架构设计，系统优化，协助解决项目开发过程中的技术难题。</p>
<p>要求:</p>
<p>1、3年以上Python经验，熟悉Django, Tornado, Flask框架中的至少一种，熟悉Web后端架构；</p>
<p>2、熟悉Linux平台环境的开发，掌握Linux常用命令 ；</p>
<p>3、熟悉python网络编程，能够设计和维护基于TCP/IP协议的高性能事件驱动框架程序；</p>
<p>4、熟悉mysql、mongodb、redis等数据库使用。</p>
<p>5、拥有强烈的求知欲，优秀的学习和沟通能力。</p>
<p>6、有机器学习实际操作经验、参加过相关竞赛者优先。</p>
<p>7、对数据分析有兴趣者优先。</p>
        </div>
    </dd>
"""
# 正则白话：<.+?> 获取小<>，而不是大<>
ret = re.sub('<.+?>', '', html).strip()  # +(1至多) *（0至多） ?（0至1）
print(ret)

#  split()：对指定分隔符，对字符串进行切片

