# EmailSender
一个邮件发送的工具

##使用
```
from EmailSender import *

if __name__ == "__main__":
    attach1 = os.path.abspath(os.path.join(__file__, "../README.md"))
    sendEmail('smtp.qq.com', '***@qq.com', '***', ['***@qq.com', '***@qq.com'], '**<***@qq.com>, **<***@qq.com>', "测试邮件", "这是一封测试邮件", {attach1: "log1"})
  ```