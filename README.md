# MsohuUrlTest

请设计一个系统，自动完成对于手机搜狐(http://m.sohu.com/ )系统可靠性的检测。  
  
具体要求：  
1. 定时递归检测所有m.sohu.com域名的页面以及这些页面上的链接的可达性，即有没有出现不可访问情况。  
2. m.sohu.com域名页面很多，从各个方面考虑性能优化。  
3. 对于错误的链接记录到日志中，日志包括：连接，时间，错误状态等。  
4. 考虑多线程的方式实现  
  
要求：用Python实现，不使用爬取框架，一周内回复。  
  
【3-24 14：42 ~~ 3-31 14：41】  
  
注意代码质量  
  
**Thread 分支**是我的解答。  
  
实现要求，使用了 threading 模块来实现多线程，Queue模块实现任务队列。底层改写了Queue来实现链接去重。（Queue原使用deque来保证有序，我采用了set与deque双份，多占用空间，但节省时间。并且在这个情形中，我认为占用的空间是可以接受的。）常规做法，应该是布隆过滤器（Bloom Filter），不过布隆过滤器同样不能删除元素。
  
执行时间可见log文件夹。  
  
目前Bug：  
1. 当页面数超过2000左右时，Pycharm运行会在Ubuntu里占很大的内存 4G左右。terminal运行则正常。  
2. 有时会假死。。。并且没什么套路。。概率不大。在 Ubuntu 下碰到过几次， windows 10 下碰到过一次。  