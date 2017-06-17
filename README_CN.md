# pydictor
[![build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://www.github.com/landgrey/pydictor) [![Python 2.7|3.4](https://img.shields.io/badge/python-2.7|3.4-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](http://www.gnu.de/documents/gpl-3.0.en.html)

**README.md in [English](README.md)**

##### pydictor —— 一个强大实用的黑客暴力破解字典建立工具

         _______                __   _          _
        |_   __ \              |  ] (_)        / |_
          | |__) |_   __   .--.| |  __   .---.`| |-' .--.   _ .--.
          |  ___/[ \ [  ]/ /'`' | [  | / /'`\]| | / .'`\ \[ `/'`\]
         _| |_    \ '/ / | \__/  |  | | | \__. | |,| \__. | | |
        |_____| [\_:  /   '.__.;__][___]'.___.'\__/ '.__.' [___]
                 \__.'


##### Email: LandGrey@qq.com
-
## 前言：
```
Q: 为什么会有pydictor ? 
A: 写出一个极好的关于密码生成的安全工具，方便大量渗透测试研究人员日常使用。

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

Q: pydictor的目标是什么?
A: 一个实用、帮助大量渗透测试人员更好的工作的更好的密码字典生成器，拥有生成破解 99% 的人的密码的能力
```

## 开始:
```
git clone --depth=1 --branch=master https://www.github.com/landgrey/pydictor.git
cd pydictor/
chmod 755 pydictor.py
python pydictor.py
```

## 预览：
#### 运行图  
![extend](/screenshots/extend.png "extend")

![social engineering dictionary builder](/screenshots/sedb.png "sedb")

## 功能和用法:
### 一. 基础字典
##### 命令: -base
##### 示例1: 使用纯数字、纯小写字母或纯大写字母生成任意位数的爆破字典
```
python pydictor.py -base d --len 6 6            生成6位纯数字字典
```

##### 示例2: 使用数字、小写字母与大写字母两两组合生成任意位数的爆破字典
```
python pydictor.py -base dL --len 1 3
```

##### 示例3: 使用数字、小写字母与大写字母3者组合的任意位数的爆破字典生成
```
python pydictor.py -base dLc                    默认字典长度:最小0，最大4
```


### 二. 自定义字符字典
##### 命令: -char
##### 示例4: 使用自定义字符(包括特殊字符)作为字符集生成任意位数的爆破字典
```
python pydictor.py -char abc123._@ --len 1 3
```

**注**:  当需要空格等特殊字符时,请加双引号包围所有自定义字符,如:"abc ABC123."


### 三. 块乘法字典
##### 命令: -chunk
```
python pydictor.py -chunk abc ABC 666 . _ @     生成由'abc'、'ABC'、'666' 、'.'、'_'、'@'6个块组成的所有可能性的排列组合字典
```

**注**:  当需要空格等特殊字符时,请加双引号单独包围特殊字符,如:abc " " 123 asdf


### 四. 扩展字典
##### 命令: -extend

1.  extend功能主要针对web应用管理员生成密码字典
2.  你可以将自己的弱密码字典放在 wordlist/Web 目录下，extend插件会自动去重，生成的字典将会包含它们
3.  你可以修改 funcfg目录下的extend.conf文件，设定扩展时加入的前缀、后缀、前后缀组合、双写中间词等
4.  extend 支持leet 模式、level筛选和长度筛选功能，你可以在下文看到关于它们的描述

```
python pydictor.py -plug extend /target.txt --leet 0 1 2 11 21 --level 1 --len 4 15 -o /awesome/wordlist
```


### 五. 特殊功能字典插件
##### 命令: -plug
##### 示例5: 使用pid6插件生成中国公民身份证后6位爆破字典
```
python pydictor.py -plug pid6
```


##### 示例6: 使用pid8插件生成中国公民身份证后8位爆破字典
```
python pydictor.py -plug pid8
```

**注**:  默认的性别为全体'all'，它由 lib/data/data.py文件 default_sex参数指定，'m'指男性,'f'指女性


##### 示例7: 使用passcraper插件爬行网站指定页面并基于获得的文本词组生成密码字典

1.  passcraper 规则和extend完全一致
2.  passcraper 插件会生成两个字典，SCRATCH开头的是从网站内容获得的原始词组列表，如果感觉SCRATCH字典中有许多无关词，可以自己去除后，重新使用extend功能指定文件生成字典
3.  你可以修改 funcfg/passcraper_blacklist.conf 文件，选择需要过滤掉的无用单词，也可以修改lib/data/data.py 中的passcraper_filter，更改过滤正则表达式
4.  和extend一样，你可以将自己的弱密码字典放在 /wordlist/Web 目录下，生成的字典会包含它们

```
python pydictor.py -plug passcraper			            使用默认funcfg/scraper.sites作为多个目标的输入文件
python pydictor.py -plug passcraper http://www.example.com
```


### 六. 用配置文件生成字典
##### 命令: --conf

1.  此功能可以完成"-base"和"-char"的所有功能，并在此基础上有更精细化的字典控制力；
2.  extend.conf 文件支持此功能，具体参考funcfg/extend.conf文件；

```
python pydictor.py --conf				            使用默认位置的funcfg/build.conf 配置文件建立字典
python pydictor.py --conf /my/other/awesome.conf    使用/my/other/awesome.conf文件建立字典
```

**注**: 具体解析规则如下，另可参考build.conf文件示例；

#### 配置文件解析规则:
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


### 七. 字典处理工具
##### 命令: -tool
##### 示例8: 安全删除字典工具shredder
```
python pydictor.py -tool shredder           删除当前指定的字典输出目录(默认为results)及其所有字典文件
python pydictor.py -tool shredder base      删除当前指定的字典输出目录下,以"BASE"开头的所有字典文件
```

  支持的前缀(不区分大小写)有13种:base,char, chunk, conf,sedb,idcard,extend,uniqifer,counter,combiner,uniqbiner,scratch,passcraper

  另外,还可以像下面这样，将传入的任意位置的一个文件或目录，整个的安全删除
```
python pydictor.py -tool shredder /data/mess
python pydictor.py -tool shredder /mess/1.zip
```

  为提高安全删除速度，默认使用1遍擦除重写，可修改lib/data/data.py中的file_rewrite_count和dir_rewrite_count，提高擦除次数；

##### 示例9: 字典去重工具uniqifer
```
python pydictor.py -tool uniqifer /tmp/my.dic				
```

##### 示例10: 词频统计工具counter
```
python pydictor.py -tool counter vs /tmp/mess.txt 100	选取/tmp/mess.txt文件中出现次数最多的100个词输出到终端并保存到文件中
```

  **注**: 默认选取前100条打印或保存；默认分隔符号为换行符"\n",可修改lib/data/data.py中counter_split变量来更改分隔符

##### 示例11: 文本合并工具combiner
```
python pydictor.py -tool combiner /my/messdir
```

##### 示例12: 文本合并去重工具uniqbiner
```
python pydictor.py -tool uniqbiner /my/messdir
```


### 八. 长度筛选功能
##### 命令: --len
1.  接受由--len选项参数值限定的长度，sedb可以在进入sedb界面时单独设置

##### 示例13: 只选取长度在4-15位之间的密码
```
python pydictor.py -plug extend /awesome/ext.txt --len 4 15
```


### 九. 为字典条目添加前缀与后缀:
##### 命令: --head，--tail
```
python pydictor.py -base L --len 1 4 --head a --tail 123
```

**注**:  指定的头和尾并不包括在指定的长度(--len参数)中,而是在原来的长度基础上额外增加的。
  

### 十. 将字典条目进行编码或加密
##### 命令: --encode
```
python pydictor.py -chunk abc ABC 123 123456 . @ _ --encode b64
```


### 十一. 级数筛选
##### 命令: --level

1.  此功能目前只支持extend功能，passcraper插件，社会工程学字典功能SEDB
2.  默认level 3, level越小，代表可能性越低，生成的字典项目越多
3.  可修改相应funcfg/extend.conf文件，自定义level规则

```
python pydictor.py -extend bob adam sarah --level 5
```


### 十二. 使用leet模式
##### 命令: --leet

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
0			默认模式，全部替换
1			从左至右, 将第一个遇到的leet字符全部替换
2              		从右至左, 将第一个遇到的leet字符全部替换
11-19			从左至右, 将第一个遇到的leet字符最多替换 code-10 个
21-29			从右至左, 将第一个遇到的leet字符最多替换 code-20 个
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


### 十三. 社会工程学字典
##### 命令: --sedb
```
python pydictor.py --sedb
```
```
         _______                __   _          _
        |_   __ \              |  ] (_)        / |_
          | |__) |_   __   .--.| |  __   .---.`| |-' .--.   _ .--.
          |  ___/[ \ [  ]/ /'`' | [  | / /'`\]| | / .'`\ \[ `/'`\]
         _| |_    \ '/ / | \__/  |  | | | \__. | |,| \__. | | |
        |_____| [\_:  /   '.__.;__][___]'.___.'\__/ '.__.' [___]
                 \__.'

                   Social Engineering Dictionary Builder
                                            Build by LandGrey
    --------------------------[ command ]--------------------------
    [+]help desc             [+]show option
    [+]set option arguments  [+]rm option
    [+]len minlen maxlen     [+]level code           [+]leet code
    [+]run                   [+]exit/quit            [+]clear/cls

    --------------------------[ option ]---------------------------
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
show                查看每项数据的当前设置情况
clear 或 cls        清除当前屏幕
exit 或 quit	        退出
set                 设置选项值
rm                  删除选项值
len                 选择每个字典项目的长度范围
level               选择扩展level值
leet                开启并选择使用leet模式的指定模式
run                 建立字典
```

注:  
1. 修改 funcfg/sedb_tricks.conf 文件，可以选择单词变换时加的前缀、后缀、前后缀等规则  
2. 可以将你收集的个人弱密码字典放入 wordlist/SEDB 目录中，生成的字典中将包括它们  
3. sedb 规则中有一小部分完全使用了extend插件规则

##### 终点即起点，到你一展身手的时候了。
