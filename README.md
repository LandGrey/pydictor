# pydictor
[![build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://www.github.com/landgrey/pydictor) [![Python 2.7|3.4](https://img.shields.io/badge/python-2.7|3.4-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](http://www.gnu.de/documents/gpl-3.0.en.html)

**README.md in [English](https://github.com/LandGrey/pydictor/blob/master/README_EN.md)**

##### pydictor —— 一个小巧实用的黑客暴力破解字典建立工具

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
A: 理由太多了，不管你是使用的python 2.7版本还是python 3.x版本，pydictor都可以在Windows、Linux 或者是Mac上运行；
   你可以用pydictor生成普通爆破字典、基于网站内容的自定义字典、社会工程学字典等等一系列高级字典，
   几乎渗透测试中一切和生成密码有关的工作，它都能帮到你。

Q: pydictor的目标是什么?
A: 一个实用、帮助大量渗透测试人员更好的工作的更好的密码字典生成器。
```

## 开始:
```
git clone https://www.github.com/landgrey/pydictor.git
cd pydictor/
chmod 755 pydictor.py
./pydictor.py
```

## 预览：
#### 终端显示  
```
pydictor.py [options]
           -o        output_path
           -base     type
           -char     custom_char
           -chunk    <chunk1> <chunk2> ...
           -plug     [pid6,pid8,extend,passcraper]
           -tool     [shredder,uniqifer,counter,combiner,uniqbiner] <arguments ...>
           --len     minlen maxlen
           --sex     [m, f, all]
           --head    prefix_string
           --tail    suffix_string
           --encode  [none,b64,md5,md516,sha1,url,sha256,sha512]
           --conf    config_file_path
           --sedb

*[+] A Useful Hacker Dictionary  Builder. [+]*
 [+] Build by LandGrey    email:LandGrey@qq.com

optional arguments:
  -h, --help            show this help message and exit
  -base Type
                        Choose from  (d, L, c, dL, dc, Lc, dLc)
                            d     digital             [0 - 9]
                            L     lowercase letters   [a - z]
                            c     capital letters     [A - Z]
                            dL    Mix d and L         [0-9 a-z]
                            dc    Mix d and c         [0-9 A-Z]
                            Lc    Mix L and c         [a-z A-Z]
                            dLc   Mix d, L and dL     [0-9 a-z A-Z]
  -char Character       Use Custom Character build the dictionary
  -chunk Chunk [Chunk ...]
                        Use the string [Chunk Multiplication] build the dictionary
  -plug Plug [Plug ...]

                        Choose from    (pid6, pid8, extend, passcraper)
                            pid6       [id_card_post_6_number]     default sex:all
                            pid8       [id_card_post_8_number]     default sex:all
                            extend     [file_path]
                            passcraper [url_or_file_path]
  -o Output
                        Set the directory output path
                            default: pydictor\results
  -tool Tool [Tool ...]

                        Choose from    (shredder, uniqifer, counter, combiner, uniqbiner)
                            shredder   [file_or_dir]
                            uniqifer   [file_path]
                            counter    ['v','s','vs'] [file_path] [view_num]
                            combiner   [dir]
                            uniqbiner  [dir]
  --sex Sex
                        Choose from  (m, f, all)
                            m: Male        f: Female   all: Male and Female
  --len Minlen Maxlen
                        [Minimun_Length]  [Maximun_Length]
                                            Default: min=2  max=4
  --head Prefix         Add string head for the items
  --tail Suffix         Add string tail for the items
  --encode Encode
                        Choose from [none, b64, md5, md516, sha1, url, sha256, sha512]
  --conf [Conf_file_path]

                        Use the configuration file build the dictionary
                            Default: pydictor\build.conf
  --sedb                Enter the Social Engineering Dictionary Builder
```
#### 运行图  
![passcraper](https://github.com/LandGrey/pydictor/raw/master/screenshots/passcraper.png "passcraper")  
![social engineering dictionary builder](https://github.com/LandGrey/pydictor/raw/master/screenshots/sedb.png "sedb")

## 功能和用法:
### 一. 基础字典
##### 命令: -base
##### 示例1: 使用纯数字、纯小写字母或纯大写字母生成任意位数的爆破字典
    python pydictor -base d --len 6 6			生成6位纯数字字典

##### 示例2: 使用数字、小写字母与大写字母两两组合生成任意位数的爆破字典
    python pydictor -base dL --len 1 3

##### 示例3: 使用数字、小写字母与大写字母3者组合的任意位数的爆破字典生成
    python pydictor -base dLc					默认字典长度:最小2，最大4

### 二. 自定义字符字典
##### 命令: -char   
##### 示例4: 使用自定义字符(包括特殊字符)作为字符集生成任意位数的爆破字典
	python pydictor -char abcABC123456._@ --len 6 8
  
**注**:  当需要空格等特殊字符时,请加双引号包围所有自定义字符,如:"abc ABC123."

### 三. 块乘法字典
##### 命令: -chunk
	python pydictor -chunk abc ABC 666 . _ @			生成由'abc'、'ABC'、'666' 、'.'、'_'、'@'6个块组成的所有可能性的排列组合字典
  
**注**:  当需要空格等特殊字符时,请加双引号单独包围特殊字符,如:abc " " 123 asdf

### 四. 为字典条目添加前缀与后缀:
##### 命令: --head,--tail
	python pydictor.py -base L --len 1 4 --head a --tail 123
**注**:  指定的头和尾并不包括在指定的长度(--len参数)中,而是在原来的长度基础上额外增加的。
  
### 五. 将字典条目进行编码或加密
##### 命令: --encode
    python pydictor.py -chunk abc ABC 123 123456 . @ _ --encode b64

### 六. 指定字典输出目录
##### 命令: -o
    python pydictor.py -base d -o D:\output

### 七. 特殊功能字典插件
##### 命令: -plug
##### 示例4: 使用pid6插件生成中国公民身份证后6位爆破字典
	python pydictor -plug pid6

##### 示例5: 使用pid8插件生成中国公民身份证后8位爆破字典
	python pydictor -plug pid8 --sex m

**注**:  默认的--sex参数为全体'all','m'指男性,'f'指女性

##### 示例6: 使用extend插件将原始单词按内置规则扩展成爆破字典
	python pydictor -plug extend D:\word.txt

##### 示例7: 使用passcraper插件爬行网站指定页面并基于获得的文本词组生成密码字典
    python pydictor -plug passcraper								使用默认scraper.site作为多个输入
	python pydictor -plug passcraper http://www.example.com

### 八. 字典处理工具
##### 命令: -tool
##### 示例8: 安全删除字典工具shredder
	python pydictor.py -tool shredder 			删除当前指定的字典输出目录(默认为results)及其所有字典文件
    python pydictor.py -tool shredder base 		删除当前指定的字典输出目录下,以"BASE"开头的所有字典文件

支持的前缀(不区分大小写)有12种:base,char, chunk, conf,sedb,idcard,extend,uniqifer,counter,combiner,uniqbiner,passcraper

  另外,还可以像下面这样，将传入的任意位置的一个文件或目录，整个的安全删除

    python pydictor.py -tool shredder /data/mess
    python pydictor.py -tool shredder D:\mess\1.zip

  为提高安全删除速度，默认使用1遍擦除重写，可修改lib\data.py中的file_rewrite_count和dir_rewrite_count，提高擦除次数；

##### 示例9: 字典去重工具uniqifer
	python pydictor.py -tool uniqifer /tmp/my.dic				

##### 示例10: 词频统计工具counter
	python pydictor.py -tool counter vs /tmp/mess.txt 100		选取/tmp/mess.txt文件中出现次数最多的100个词输出到终端并保存到文件中

  **注**: 默认选取前10条打印或保存；默认分隔符号为换行符"\n",可修改lib\data.py中counter_split变量来更改分隔符

##### 示例11: 文本合并工具combiner
	python pydictor.py -tool combiner /my/messdir

##### 示例12: 文本合并去重工具uniqbiner
	python pydictor.py -tool uniqbiner /my/messdir

### 九. 用配置文件生成字典
##### 命令: --conf
   此功能可以完成"-base"和"-char"的所有功能，并在此基础上有更精细化的字典控制力

    python pydictor.py --conf				    		使用默认位置的build.conf 配置文件建立字典
    python pydictor.py --conf /my/other/awesome.conf	使用/my/other/awesome.conf文件建立字典

**注**: 具体解析规则如下，另可参考build.conf文件示例；

#### 配置文件解析规则:
```
  1. 解析的基本单位称为一个解析元，一个解析元包括五个解析元素，分别是:头、字符集、长度范围、编码方式、尾，其中的头与尾均可省略不写；
一个标准解析元的写法:head[characters]{minlength:maxlength}<encode-type>tail，一个示例解析元，如：a[0-9]{4:6}<none>_
其意义为生成以"a"为开头，以0到9共10个字符为字符集的，字符集生成长度为4到6位，不做任何编码的，并以"_"结尾的字典集合；
  2. 暂时只支持一行解析，生成一个字典，一个生成好的字典中的一行为一条解析的一种可能；
  3. 一条解析可包含一至十个解析元；
如:[4-6,a-c,A,C,admin]{3:3}<none>_[a,s,d,f]{2:2}<none>[789,!@#]{1:2}<none>,就包含了三个解析元；
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

### 十. 社会工程学字典
##### 命令: --sedb
    python pydictor.py --sedb
#
             _______                __   _          _
            |_   __ \              |  ] (_)        / |_
              | |__) |_   __   .--.| |  __   .---.`| |-' .--.   _ .--.
              |  ___/[ \ [  ]/ /'`' | [  | / /'`\]| | / .'`\ \[ `/'`\]
             _| |_    \ '/ / | \__/  |  | | | \__. | |,| \__. | | |
            |_____| [\_:  /   '.__.;__][___]'.___.'\__/ '.__.' [___]
                     \__.'


                       Social Engineering Dictionary Builder
                                                                Build by LandGrey
    ----------------------------------[ command ]------------------------------------
    [+]help desc     (View the description) |  [+]show name     (Show current settings)
    [+]cls/clear     (Clean the screen)     |  [+]quit/exit     (Quit the progress)
    [+]run           (Build the dictionary) |
                                            |
    Usage Exp :show  (Show all of settings) |  help desc   (view all of descriptions)

    -------------------------------[ setting options ]--------------------------------
    [+]cname      [+]ename      [+]sname    |  [+]birth      [+]usedpwd    [+]phone
    [+]uphone     [+]hphone     [+]email    |  [+]postcode   [+]nickname   [+]idcard
    [+]jobnum     [+]otherdate  [+]usedchar |
                                            |
    Usage Exp :sname zhang wei zw zwell     |  * Each setting supports multiple values
    pydictor SEDB>>

##### 命令:
    help				重新显示界面
	help desc			查看每项数据的意义描述
	show				查看每项数据的当前设置情况
	run					建立字典
	cls/clear			清除当前屏幕
	quit/exit			退出

##### 终点即起点，到你一展身手的时候了。