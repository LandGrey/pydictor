# pydictor
[![build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://www.github.com/landgrey/pydictor)  [![Python 2.7|3.4](https://img.shields.io/badge/python-2.7|3.4-yellow.svg)](https://www.python.org/)  ![release](https://img.shields.io/badge/version-2.0.1-orange.svg) ![License](https://img.shields.io/badge/license-GPLv3-red.svg)

**README.md [English](README.md)**

##### pydictor —— 一个强大实用的黑客暴力破解字典建立工具
                          _ _      _
          _ __  _   _  __| (_) ___| |_ ___  _ __
         | '_ \| | | |/ _` | |/ __| __/ _ \| '__|
         | |_) | |_| | (_| | | (__| || (_) | |
         | .__/ \__, |\__,_|_|\___|\__\___/|_|
         |_|    |___/                         


#### Email: LandGrey@qq.com

-
## 前言：
```
Q: 为什么要使用pydictor ?
A: 1.生成密码它总会帮到你
      你可以用pydictor生成普通爆破字典、基于网站内容的自定义字典、社会工程学字典等等一系列高级字典；
      你可以使用pydictor的内置工具，对字典进行安全删除、合并、去重、合并并去重、高频词筛选等操作；

   2.可定制性强
      你可以通过修改多个配置文件、加入自己的字典、选用leet mode 模式、长度选择等方式生成独一无二的高度定制和复杂字典，生成密码字典的好坏和你的自定义规则有很大关系；

   3.强大灵活的配置解析功能
      无需多言,熟练运用后自己体会；
   
   4.兼容性强
     不管你是使用的python 2.7版本还是python 3.4 以上版本，pydictor都可以在Windows、Linux 或者是Mac上运行；
```


## 开始:
```
git clone --depth=1 --branch=master https://www.github.com/landgrey/pydictor.git
cd pydictor/
chmod 755 pydictor.py
python pydictor.py
```

-
## 预览：
 
![extend](/screenshots/extend.png "extend")

![social engineering dictionary builder](/screenshots/sedb.png "sedb")


## 快速上手:

#### 可以生成的字典类型（14种）及其说明

|     类型      |  编号  |      说明         |
|: ----------- :| :----:| :---------------: |
| base          | 1     | 基础字典          |
| char          | 2     | 自定义字符集字典  |
| chunk         | 3     | 排列组合字典      |
| conf          | 4     | 配置文件生成字典  |
| sedb          | 5     | 社会工程学字典    | 
| idcard        | 6     | 身份证后6/8位字典 |
| extend        | 7     | 扩展字典          |
| scratch       | 8     | 网页原始关键词字典| 
| passcraper    | 9     | 网页爆破针对字典  |
| handle        | 10    | 筛选处理字典      |
| uniqifer      | 11    | 去重字典          |
| counter       | 12    | 词频统计字典      |
| combiner      | 13    | 合并字典          |
| uniqbiner     | 14    | 先合并后去重字典  |

#### 字典类型与功能适用范围对照表  

| 功能       | 适用范围(编号)                 | 说明                             |
|: -------- :| :-------------------------- :| :------------------------------ :|
| len        | 1 2 3 4 5 6 7 9 10 11 12 14  | 定义长度范围                      |
| head       | 1 2 3 4 5 6 7 9 10 11 12 14  | 添加字典条目前缀                  | 
| tail       | 1 2 3 4 5 6 7 9 10 11 12 14  | 添加字典条目后缀                  | 
| encode     | 1 2 3 4 5 6 7 9 10 11 12 14  | 对字典条目进行编码                 |
| occur      | 3 4 5 7 9 10 11 12 14        | 字母、数字、特殊字符出现次数范围筛选 |
| types      | 3 4 5 7 9 10 11 12 14        | 字母、数字、特殊字符各种类数范围筛选 |
| regex      | 3 4 5 7 9 10 11 12 14        | 正则筛选                          |
| level      | 5 7 9                        | 字典级别筛选                       |
| leet       | 5 7 9                        | 1337 模式                         |


## 使用实例
#### 1: 生成4位纯数字爆破字典, 并保存到'D:\exits\or\not\dict.txt'文件中
```
python pydictor.py -base d --len 4 4 --output D:\exits\or\not\dict.txt
```

### 2: 生成1-3位小写字母——名字首字母拼音缩写爆破字典, 并用base64编码
```
python pydictor.py -base c --len 1 3 --encode b64
```

#### 示例3: 生成包含数字、小写与大写字母的1-4位(默认)爆破字典,保存到'/awesome/pwd' 目录
```
python pydictor.py -base dLc -o /awesome/pwd
```

### 示例4: 生成由【a b c 1 2 3 . _ @ 空格】字符集组成的1—3位爆破字典, 并在每项后面添加额外的'@site'字符串
```
python pydictor.py -char "abc123._@ " --len 1 3 --tail @site
```

#### 示例5: 生成词组【abc ABC 666 . _ @ '】的所有排列组合爆破字典,并为每项添加额外的前缀'a'和后缀'123',最后用md5进行进行加密
```
python pydictor.py -chunk abc ABC 666 . _ @ "'" --head a --tail 123 --encode md5
```

#### 示例6: 用extend插件生成针对用户或web管理员的密码爆破字典

1.  extend功能主要针对web应用管理员生成密码字典
2.  将自己的弱口令字典放在 wordlist/Web 目录下, 程序会自动去重，把它们加入生成的字典中
3.  你可以修改 funcfg目录下的extend.conf文件，设定扩展时加入的前缀、后缀、前后缀组合、双写中间词等
4.  extend 支持leet 模式、level筛选、长度筛选、不同字符个数筛选、不同字符种类筛选、正则表达式筛选

将以下4个收集到的信息写入 /names.txt 文件中
```
liwell
shelly
bianji
webzhang
```

生成针对以上四个信息,启用代码为 0 1 2 11 21 的leet模式来生成更多密码,选用可生成最多密码的level 1模式,   
并规定生成的字典长度范围为4——16,规定生成的字典的每个项目中出现的字母个数要小于等于10个、至少出现一个数字并且  
出现的特殊字符不能超过2个，最后输出到'/possbile/wordlist.lst' 文件中

```
python pydictor.py -extend /names.txt --leet 0 1 2 11 21 --level 1 --len 4 16 --occur "<=10" ">0" "<=2" -o /possbile/wordlist.lst
```

#### 示例7: 身份证后6/8位生成插件
##### 使用pid6插件生成中国公民身份证后6位爆破字典, 并规定至少要出现4种不同的数字，并用base64编码
```
pydictor.py -plug pid6 --types ">=0" ">=4" ">=0" --encode b64
```

**注**:  默认的性别为全体'all'，它由 lib/data/data.py文件default_sex参数指定，'m'指男性,'f'指女性

#### 示例8: 使用passcraper插件爬行网站指定页面并基于获得的文本词组生成密码字典

1.  passcraper 规则和extend完全一致
2.  passcraper 插件会生成两个字典，SCRATCH开头的是从网站内容获得的原始词组列表，如果感觉SCRATCH字典中有许多无关词，可以自己去除后，重新使用extend功能指定文件生成字典
3.  你可以修改 funcfg/passcraper_blacklist.conf 文件，选择需要过滤掉的无用单词，也可以修改lib/data/data.py 中的passcraper_filter，更改过滤正则表达式
4.  和extend一样，你可以将自己的弱密码字典放在 /wordlist/Web 目录下，生成的字典会包含它们

```
python pydictor.py -plug passcraper			                使用默认funcfg/scraper.sites作为多个目标的输入文件
python pydictor.py -plug passcraper http://www.example.com
```

#### 示例9: 用配置文件生成字典

1.  此功能可以完成"-base"和"-char"的所有功能，并在此基础上有更精细化的字典控制力；
2.  extend.conf 文件支持此功能，具体参考funcfg/extend.conf文件；
3.  可以生成固定模式的字典,比如 lisa【两位到四位数字】@【qq.com, 163.com, some.net 中的一个】，在配置文件中写入  
    'lisa[0-9]{2,4}<none>@[qq.com,163.com,some.net]{1,1}<none>' ，然后指定运行即可

```
python pydictor.py --conf --encode b64			    使用默认位置的funcfg/build.conf 配置文件建立字典,并用base64编码
python pydictor.py --conf /my/other/awesome.conf    使用/my/other/awesome.conf文件建立字典
```

**注**: 具体解析规则如下，另可参考build.conf文件示例；

##### 配置文件解析规则:
```
  1. 解析的基本单位称为一个解析元，一个解析元包括五个解析元素，分别是:头、字符集、长度范围、编码方式、尾，其中的头与尾均可省略不写；
一个标准解析元的写法:head[characters]{minlength,maxlength}<encode-type>tail，一个示例解析元，如：a[0-9]{4,6}<none>_
其意义为生成以"a"为开头，以0到9共10个字符为字符集的，字符集生成长度为4到6位，不做任何编码的，并以"_"结尾的字典集合；
  2. 暂时只支持一行解析，生成一个字典，一个生成好的字典中的一行为一条解析的一种可能；
  3. 一条解析可包含一至十个解析元；
如:[4-6,a-c,A,C,admin]{3,3}<none>_[a,s,d,f]{2,2}<none>[789,!@#]{1,2}<none>,就包含了三个解析元；
  4. 配置文件的一行中的第一个字符为"#"字符的，代表注释，程序将不再解析本行；
  5. 用配置文件方式可产生精确至一位的高度可控字典；

值得注意的是字符集：
				   既可以按照字符的大小顺序，以"-"来连接，表示用多个单个字符做为元素组成的字符集；
				   又可以用","来分隔多个字符集，或单个字符，或单个字符串，来作为字符集中的一个元素；
支持的编码方式:
			   none    不进行任何编码
			   b64     base64 编码
			   md5     md5 摘要输出32位
			   md516   md5 摘要输出16位
			   sha1    sha1 摘要
			   url     urlencode
			   sha256  sha256 摘要算法
			   sha512  sha512 摘要算法

```

#### 示例10: 字典处理工具
##### 字典筛选处理工具 handler
  指定输入文件, 然后用pydictor处理后输出
```
python pydictor.py -tool handler /wordlist/raw.txt --len 6 16 --occur "" "=6" "<0" --encode b64 -o /wordlist/ok.txt
```

##### 安全删除字典工具shredder
```
python pydictor.py -tool shredder           删除当前指定的字典输出目录(默认为results)及其所有字典文件
python pydictor.py -tool shredder base      删除当前指定的字典输出目录下,以"BASE"开头的所有字典文件
```

  支持的前缀(不区分大小写)有14种:base,char, chunk, conf,sedb,idcard,extend,handle,uniqifer,counter,combiner,uniqbiner,scratch,passcraper

  另外,还可以像下面这样，将传入的任意位置的一个文件或目录，整个的安全删除
```
python pydictor.py -tool shredder /data/mess
python pydictor.py -tool shredder /mess/1.zip
```

  为提高安全删除速度，默认使用1遍擦除重写，可修改lib/data/data.py中的file_rewrite_count和dir_rewrite_count，提高擦除次数；

##### 字典去重工具uniqifer
```
python pydictor.py -tool uniqifer /tmp/my.dic				
```

##### 词频统计工具counter
```
python pydictor.py -tool counter vs /tmp/mess.txt 100	选取/tmp/mess.txt文件中出现次数最多的100个词输出到终端并保存到文件中
```

  **注**: 默认选取前100条打印或保存；默认分隔符号为换行符"\n",可修改lib/data/data.py中counter_split变量来更改分隔符

##### 文本合并工具combiner
```
python pydictor.py -tool combiner /my/messdir
```

##### 文本合并去重工具uniqbiner
```
python pydictor.py -tool uniqbiner /my/messdir
```

#### 示例11: 字典筛选
##### 级数筛选

1.  此功能目前只支持extend功能，passcraper插件，社会工程学字典功能SEDB
2.  默认level 3, level越小，代表可能性越低，生成的字典项目越多；用level 5生成最小的字典，level范围1—5
3.  可修改相应funcfg/extend.conf文件，自定义level规则

```
python pydictor.py -extend bob adam sarah --level 5
```

##### leet模式

1.  此功能目前只支持extend功能，passcraper插件，社会工程学字典功能SEDB
2.  默认全部不启用，启用后可选择多个模式代码一起使用
3.  sedb可以在进入sedb界面时单独启用leet mode并选择模式代码
4.  使用leet mode不会使正常字典减少，而是在不使用leet mode字典基础上增加

##### 默认置换表
```
leet字符 = 替换字符
```
```
a = 4
b = 6
e = 3
l = 1
i = 1
o = 0
s = 5
```

##### 模式代码
```
0               默认模式，全部替换
1               从左至右, 将第一个遇到的leet字符全部替换
2               从右至左, 将第一个遇到的leet字符全部替换
11-19           从左至右, 将第一个遇到的leet字符最多替换 code-10 个
21-29           从右至左, 将第一个遇到的leet字符最多替换 code-20 个
```

##### 代码作用表

| code| old string         | new string        |
|:---:| :----------------: |:----------------: |
| 0   | as a airs trees    | 45 4 41r5 tr335   |
| 1   | as a airs trees    | 4s 4 4irs trees   |
| 2   | as a airs trees    | a5 a air5 tree5   |
| 11  | as a airs trees    | 4s a airs trees   |
| 12  | as a airs trees    | 4s 4 airs trees   |
| 13  | as a airs trees    | 4s 4 4irs trees   |
| 14  | as a airs trees    | 4s 4 4irs trees   |
| ... | as a airs trees    | 4s 4 4irs trees   |
| 21  | as a airs trees    | as a airs tree5   |
| 22  | as a airs trees    | as a air5 tree5   |
| 23  | as a airs trees    | a5 a air5 tree5   |
| 24  | as a airs trees    | a5 a air5 tree5   |
| ... | as a airs trees    | a5 a air5 tree5   |


你可以:   

```
修改 /funcfg/leet_mode.conf 文件,更换字符置换表;   
修改 /lib/lib/data.py extend_leet、passcraper_leet、sedb_leet参数, 选择某个功能默认是否启用leet模式;
修改 /lib/data/data.py leet_mode_code 选择默认使用的模式代码;
```

##### 字母、数字、特殊字符分别出现个数筛选

```
--occur [字母出现个数范围] [数字出现个数范围] [特殊字符出现个数范围]
```

默认  
```
--occur "<=99" "<=99" "<=99"
```

##### 字母、数字、特殊字符分别出现字符种类数筛选
```
 --types [出现的字母种类数范围] [出现的数字种类数范围] [出现的特殊字符种类数范围]
```

默认
```
 --types ">=0" ">=0" ">=0"
```

#### 示例12: 字典筛选社会工程学字典

```
                                  _ _      _
                  _ __  _   _  __| (_) ___| |_ ___  _ __
                 | '_ \| | | |/ _` | |/ __| __/ _ \| '__|
                 | |_) | |_| | (_| | | (__| || (_) | |
                 | .__/ \__, |\__,_|_|\___|\__\___/|_|
                 |_|    |___/                         

                   Social Engineering Dictionary Builder
                                            Build by LandGrey
    ----------------------------[ command ]----------------------------
    [+]help desc             [+]exit/quit            [+]clear/cls
    [+]show option           [+]set option arguments [+]rm option
    [+]len minlen maxlen     [+]head prefix          [+]tail suffix
    [+]encode type           [+]occur L d s          [+]types L d s
    [+]regex string          [+]level code           [+]leet code
    [+]output directory      [+]run

    ----------------------------[ option ]----------------------------
    [+]cname                 [+]ename                [+]sname
    [+]birth                 [+]usedpwd              [+]phone
    [+]uphone                [+]hphone               [+]email
    [+]postcode              [+]nickname             [+]idcard
    [+]jobnum                [+]otherdate            [+]usedchar

pydictor SEDB>>
```

##### 命令:
```
help                重新载入界面
help desc           查看每项数据的意义描述
exit or quit        退出
clear or cls        清除当前屏幕
show                查看每项数据的当前设置情况
set                 设置选项值
rm                  删除选项值
len                 选择每个字典项目的长度范围
head                为每个条目添加前缀
tail                为每个条目添加后缀
encode              设置每个条目的编码方式
occur               分别规定字母、数字、特殊字符的出现次数范围
types               分别规定字母、数字、特殊字符的各种类数范围
regex               使用正则表达式筛选结果
level               选择扩展level值
leet                开启并选择使用leet模式的指定模式
output              设置字典输出目录或输出文件位置
run                 建立字典
```

如果你有关于一个人的类似以下相关信息(如有雷同，呃……那是不可能的)    


|    信息项          |        值             |
|: ----------------- | :-------------------- |
| 中文名             | 李伟                  |
| 名字拼音           | liwei                 | 
| 名字简拼           | lw                    | 
| 名字简拼           | Lwei                  |
| 英文名             | zwell                 | 
| 生日               | 19880916              | 
| 曾用密码           | liwei123456.          | 
| 曾用密码           | liwei@19880916        | 
| 曾用密码           | lw19880916_123        | 
| 曾用密码           | abc123456             |
| 手机号             | 18852006666           | 
| 曾用手机号         | 15500998080           | 
| 家庭座机号         | 76500100              |
| 公司座机号         | 010-61599000          | 
| 电子邮件帐户       | 33125500@qq.com       |
| 电子邮件帐户       | 13561207878@163.com   |
| 电子邮件帐户       | weiweili@gmail.com    | 
| 电子邮件帐户       | wei010wei@hotmail.com | 
| 家乡邮编           | 663321                | 
| 现居地邮编         | 962210                |
| 常用昵称           | zlili                 |
| 身份证号           | 152726198809160571    | 
| 学号               | 20051230              | 
| 工号               | 100563                |
| 父亲生日           | 152726195910042816    | 
| 母亲生日           | 15222419621012476X    | 
| 女朋友生日         | 152726198709063846    |
| 好朋友生日         | 152726198802083166    | 
| 宠物名             | tiger                 | 
| 狂热的剧           | games of thrones      |
| 具有特殊意义的数字 | 176003                | 
| 具有特殊意义的字符 | m0n5ter               | 
| 具有特殊意义的字符 | ppdog                 |


可以这样使用 pydictor 社会工程学字典建立功能

```
python pydictor.py --sedb
set cname liwei
set sname lw Lwei
set ename zwell
set birth 19880916
set usedpwd liwei123456. liwei@19880916 lw19880916_123
set phone 18852006666
set uphone 15500998080
set hphone 76500100 61599000 01061599000
set email 33125500@qq.com
set email 13561207878@163.com
set email weiweili@gmail.com
set email wei010wei@hotmail.com
set postcode 663321 962210
set nickname zlili
set idcard 152726198809160571
set jobnum 20051230 100563
set otherdate 19591004 19621012
set otherdate 19870906 19880208
set usedchar tiger gof gamesthrones 176003 m0n5ter ppdog
```

到这里, 就可以查看以下配置，初步生成字典了  
```
show
run
```

但是, 你希望生成一个更大的字典  
```
level 1
```

另外, 你可能还想筛选下结果, 去掉对方不太可能用的密码,比如   

密码长度 1—16   

```
len 1 16
```

每条密码里最少要有一个字母，特殊字符最多有3个  
```
occur ">0" "" "<=3"
```

并且每条密码里的特殊字符不超过2种  
```
types "" "" "<=2"
```

最后, 指定输出路径, 再次生成字典  
```
output D:\awesome\dict\liwei_pass.txt
run
```


注:  
1. 可以修改 funcfg/sedb_tricks.conf 文件，可以选择单词变换时加的前缀、后缀、前后缀等规则  
2. 可以将你收集的个人弱密码字典放入 wordlist/SEDB 目录中，生成的字典中将包括它们  
3. sedb 规则中有一小部分完全使用了extend插件规则

##### 终点即起点，到你一展身手的时候了。
