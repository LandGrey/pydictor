# pydictor  

		一个实用的黑客字典建立工具
		A useful hacker dictionary  builder
##### Build by LandGrey
###### Email: LandGrey@qq.com
-

##### 快速使用:
```
git clone https://www.github.com/landgrey/pydictor.git
cd pydictor/
chmod 755 pydictor.py
./pydictor.py
```

```


                     _______                __   _          _
                    |_   __ \              |  ] (_)        / |_
                      | |__) |_   __   .--.| |  __   .---.`| |-' .--.   _ .--.
                      |  ___/[ \ [  ]/ /'`' | [  | / /'`\]| | / .'`\ \[ `/'`\]
                     _| |_    \ '/ / | \__/  |  | | | \__. | |,| \__. | | |
                    |_____| [\_:  /   '.__.;__][___]'.___.'\__/ '.__.' [___]
                             \__.'

usage:
pydictor.py [options]
               -base     type
               -char     customchar
               -chunk    <chunk1> <chunk2> ...
               -plug     <pid6, pid8, extend>
               -o        output path
               --sex     <m, f, all>
               --len     minlen maxlen
               --head    prefix
               --tail    suffix
               --encode  <b64,md5,md516,sha1,url,sha256,sha512>
               --conf    conf file
               --sedb
               --shred   prefix or file or directory

*[+] A Useful Hacker Dictionary  Builder. [+]*
 [+] Build by LandGrey    email:LandGrey@qq.com

optional arguments:
  -h, --help            show this help message and exit
  -base Type
                        Choose from  [d L c dL dc Lc dLc]
                        d     digital             [0 - 9]
                        L     lowercase letters   [a - z]
                        c     capital letters     [A - Z]
                        dL    Mix d and L         [0-9 a-z]
                        dc    Mix d and c         [0-9 A-Z]
                        Lc    Mix L and c         [a-z A-Z]
                        dLc   Mix d, L and c      [0-9 a-z A-Z]
  -char Character       Use   [Custom Character]  build the dictionary
  -chunk Chunk [Chunk ...]
                        Use the string [Chunk Multiplication] build the dictionary
  -plug Plug [Plug ...]

                        Choose plug from  [pid6 pid8 extend]
                            pid6 [Id Card post 6 number]     default sex:all
                            pid8 [Id Card post 8 number]     default sex:all
                            extend [file path]
  -o Output
                        Set the directory output path
                            default: pydictor\results
  --sex Sex
                        Choose sex from    [m f all]
                            m: Male        f: Female   all: Male and Female
                            Provided for   [pid6 | pid8]
  --len Minlen Maxlen
                        Minimun Length  Maximun Length (excluded head | tail | encode)
                                        Default: min=2  max=4
  --head Prefix         Add string head for the dictionary
  --tail Suffix         Add string tail for the dictionary
  --encode Encode
                        Choose encode or encrytion from:
                            b64     base64 encode
                            md5     md5 encryption (32)
                            md516   md5 encryption (16)
                            sha1    sha1 encryption
                            url     urlencode
                            sha256  sha256 encrytion
                            sha512  sha512 encrytion
  --conf [Conf file]
                        Use the configuration file build the dictionary
                            Default: pydictor\build.conf
  --sedb                Enter   the Social Engineering Dictionary Builder
  --shred [target]
                        Safe shredded the [target]:
                                                    [!!! Warning !!!]
                            Once this function is enabled, the data will be shredded
                            default              pydictor\results
                            common file          specified the complete file path
                            prefix file          <prefix> choice from 6 types as follow:
                                                 [base | chunk | conf | sedb | idcard | extend]
                            directory            specified the complete directory

```

#### 功能速览:
  总览:

    1. 在本程序的参数命令中，凡是以一个"-"开头的命令，如"-base"，其后至少要有1个参数；
    2. 在本程序的参数命令中，凡是以两个"--"开头的命令，如"--conf"，其后若无参数，将使用程序默认数值，否则使用用户指定的一个参数；
    3. 用户可以控制的程序的所有默认设置，如最大长度限制，字典的最大行数等，都在lib\data.py中；
    如果受到限制，请先明确它们的意义后更改，否则不要轻易修改，以避免使程序异常；

##### 1. 支持使用纯数字、纯小写字母或纯大写字母的任意位数爆破字典生成
  例:
    `python pydictor -base d --len 6 6`				生成6位纯数字字典

##### 2. 支持使用数字、小写字母与大写字母两两组合的任意位数爆破字典生成
  例：
    `python pydictor -base dL --len 2 4`			生成数字和小写字母组成的所有2-4位长度字典

##### 3. 支持使用数字、小写字母与大写字母3者组合的任意位数爆破字典生成
  例：
    `python pydictor -base dLc --len 4 6`		生成数字、小写字母和大写字母组成的所有4-6位字典
	   	   
##### 4. 支持使用自定义字符(包括特殊字符)的任意位数爆破字典生成
  例:
	`python pydictor -char aAbBcC123. --len 6 8`			生成由'aAbBcC123.' 10个字符组成的所有6位到8位字典
  
**注**:  当需要空格等特殊字符时,请加双引号包围所有自定义字符,如:"abcAB C123."
	   
##### 5. 支持使用自定义字符串、字符生成所有排列可能性组合的字典
  例:
	`python pydictor -chunk abc ABC 123 .`			生成由'abc'、'ABC'、'123' 和'.'4个块组成的所有排列的可能性组合字典
  
**注**:  当需要空格等特殊字符时,请加双引号单独包围特殊字符,如:abc " " 123 asdf;此类字典的生成长度为块数的阶乘.

##### 6. 支持使用特殊功能的字典生成插件
    6.1 pid6插件
        中国公民身份证后6位爆破字典生成
  例:
	`python pydictor -plug pid6 --sex m`			生成中国男性公民的身份证后6位所有可能性组合字典

    6.2 pid8插件
        中国公民身份证后8位爆破字典生成
  例:
	`python pydictor -plug pid8`			        生成所有中国公民的身份证后8位所有可能性组合字典

**注**:  不支持指定生成此类字典的长度，默认的--sex参数为全体("all")公民

    6.3 extend插件
        将收集到的目标元词组按内置规则扩展成爆破字典
  例:
	`python pydictor -plug extend D:\1.txt`			将'D:\\1.txt'文件中的每一行进行扩展生成扩展字典
  
	   
	   
##### 7. 支持指定生成的字典前缀(头)与后缀(尾)
  例:
	`python pydictor.py -base L --len 1 4 --head a --tail 123`
  
**注**:  指定的头和尾并不包括在指定的长度(--len参数)中,而是在原来的长度基础上额外增加的。
  
  
##### 8. 支持将生成的字典进行编码或加密
  例:
    `python pydictor.py -base d --encode b64`
  
**注**:  支持 base64 urlencode编码, md5(32位) md516(16位) sha1 sha256 sha512加密


##### 9. 支持指定输出目录
  例:
    `python pydictor.py -base d --len 4 4 -o D:\output`
  
**注**: 如指定的目录不存在, 则会尝试创建；如果创建失败，则使用或创建默认的results目录；


##### 10. 配置文件解析功能
  此功能可以完成"-base"和"-char"的所有功能，并在此基础上有更精细化的提升；

    python pydictor.py --conf				    使用默认位置的build.conf 配置文件建立字典
    python pydictor.py --conf D:\conf\my.conf	使用指定位置的配置文件建立字典
  
**注**: 具体解析规则如下，另可参考build.conf文件示例；

##### 配置文件解析规则:
```
  1. 解析的基本单位称为一个解析元，一个解析元包括五个解析元素，分别是:头、字符集、长度范围、编码方式、尾，其中的头与尾均可省略不写；
一个标准解析元的写法:head[characters]{minlength:maxlength}<encode-type>tail，一个示例解析元，如：a[0-9]{4:6}<none>_
其意义为生成以"a"为开头，以0到9共10个字符为字符集的，字符集生成长度为4到6位，不做任何编码的，并以"_"结尾的字典集合；
  2. 暂时只支持一行解析，生成一个字典，一个生成好的字典中的一行为一条解析的一种可能；
  3. 每一行当作一条解析，一条解析可包含一至十个解析元，以提供粒度更小的字典生成方式；
如:[4-6,a-c,A,C,admin]{3:3}<none>_[a,s,d,f]{2:2}<none>[789,!@#]{1:2}<none>,就包含了三个解析元；
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
  4. 从控制范围上看解析元素，长度范围的控制范围仅为字符集中的生成长度，不包括头、尾以及编码后的长度，而编码方式的控制范围为一个解析元；
  5. 配置文件的一行中的第一个字符为"#"字符的，代表注释，程序将不再解析本行；
  6. 用配置文件方式可产生精确至一位的高度可控字典，推荐有需求的人员使用；

  另附字符的大小顺序(从小到大，处在[]中间的):
  [ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~]

```

##### 11. 安全删除指定文件或目录功能	
	python pydictor.py --shred 			删除默认的 results 目录及其所有字典文件
    python pydictor.py --shred base 	删除当前输出目录(默认为results)下，以"BASE"开头的所有字典文件

因为输出时前缀固定，所以可以用这种方式删除某一类字典文件

当前支持的前缀(不区分大小写)有5种:base、chunk、conf、sedb、idcard

   另外,--shred选项还支持将传入的任意位置的一个目录、文件，整个的安全删除，程序会自动判断待删除的是目录还是文件，从而自动工作

    python pydictor.py --shred D:\mess			删除整个D:\mess目录
    python pydictor.py --shred D:\mess\1.zip	删除D:\mess\1.zip 文件

  为提高安全删除速度，默认使用1遍擦除重写，如有更高安全需要，可修改lib\data.py中的file_rewrite_count和dir_rewrite_count，提高擦除次数；建议最高修改次数为3次；

  **注**: 安全删除功能请谨慎使用，造成重要数据不可恢复与本程序开发者无任何关系!

##### 12. 支持建立社会工程学字典
  例:
     `python pydictor.py --sedb ` 进入社工字典生成界面

-
#### 社会工程学字典生成功能介绍:

##### 1. 内置15项收集数据
	[+]cname        Chinese name's phonetic          中文名拼音全拼
	[+]ename        English name                     英文名 
	[+]sname        Simple spellings phonetic        姓名简拼 
	[+]birth        Birthday [YYYYMMDD]              生日
	[+]usedpwd      Used password                    曾用密码
	[+]phone        Cell phone number                手机号
	[+]uphone       Used phone                       曾用手机号
	[+]hphone       Homephone number                 老家座机号
	[+]email        E-mail accounts                  电子邮箱账号
	[+]postcode     Postcode                         老家邮政编码
	[+]nickname     Commonly used nickname           常用昵称
	[+]idcard       Identity card number             身份证号
	[+]jobnum       Job or student number            学号或工号或其简写等
	[+]otherdate    Others date [YYYYMMDD] 			 其他亲人生日等特殊日期
	[+]usedchar     Commonly used characters         其他常用字符串数字等

##### 2. 命令速通
	进入 Social Engineering Dictionary Builder 界面后,可以使用
	[项目名] [v1] [...]	设置某项数据的值 
	help disc			查看15项数据的意义描述;
	help [具体项]		查看某项数据的意义描述;
	show				查看15项数据的当前设置情况;
	show [具体项]		查看某项数据的当前设置情况;
	run					建立字典
	cls					清除命令行文字
	clear				清除命令行文字
	quit				退出
	exit				退出

##### 3. 15项数据说明
		(1) 以上15项,每一项都支持用空格隔开输入多个数据,不清楚的可以不填;
		    命令: nickname Tomcat Zwell zer0
		(2) 其他的一些目标信息可以在otherid和usedchar项目输入;
            比如宠物名、个人图腾、特殊意义字符、爱人亲人生日等等各种相关的信息
		(3) 准确的社工字典不仅需要大量的目标信息,而且还需要结合目标的性格特征，比如:懒惰、完美主义、身份特征、目标平台等;
		    然而,由于缺少人物画像,对目标的性格和爆破平台密码策略不详,所以生成字典难免可能有累赘,不准确,请谅解。
		(4) 为了解决(3)的问题,可以自己在rules中修改/增加规则,修改相应代码来定制相关的生成策略。