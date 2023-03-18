import os
# 导入时间处理库
from datetime import datetime
# 导入邮件发送库
import yagmail
# 导入数据获取函数以及变量
from getData import getData

sender = os.environ['sender']
receiver = os.environ['receiver']
SMTPserver = os.environ['SMTPserver']
password = os.environ['password']
port = os.environ['port']

def sendEMail():
    # 获取当前八位日期
    date = datetime.date.today()

    # 对数据进行html格式化
    items = ''.join(
        ["<pre><p>{} | {}</p></pre>".format(*i)
        for i in getData()])

    # 制作html格式信息
    mailMessage = """
    <h1 align="center">NotionTEN:%s</h1>
    <p align="center">以下是你的待办事项：</p>
    %s
    """% (date, items)

    # 发送邮件
    yag = yagmail.SMTP(sender, password, host=SMTPserver, port=port)
    yag.send(to = receiver, subject = "今日的NotionTEN", contents = mailMessage)