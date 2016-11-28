# pydictor  
=	
		一个实用的黑客字典建立工具
		A useful hacker dictionary  builder
##### Build by LandGrey
-
##### 前言：
第一次自己独立写一个github工程,完全是出于兴趣和想要提高自己的心.
email:LandGrey@qq.com.

-

#### 功能简介:

##### 1. 支持使用纯数字、纯小写字母或纯大写字母的任意位数爆破字典生成
  例:
       `python pydictor -t d --len 6 6`
生成6位纯数字字典

##### 2. 支持使用数字、小写字母与大写字母两两组合或3者组合的任意位数爆破字典生成
  例：
       `python pydictor -t dL --len 4 4	`			生成数字和小写字母组成的所有4位字典
	   
##### 3. 支持使用自定义字符(包括特殊字符)的任意位数爆破字典生成
  例:
	   `python pydictor -cc aAbBcC123. --len 6 8`			生成由'aAbBcC123.' 10个字符组成的所有6位到8位字典
	   
##### 4. 支持使用自定义字符串、字符生成所有可能性组合的字典
  例:
	   `python pydictor -cm abc ABC 123 .`			生成由'abc'、'ABC'、'123' 和'.'生成的所有可能性组合字典
	   
  注:  不支持指定生成此类字典的长度 

##### 5. 支持中国公民身份证后6/8位爆破字典生成
  例:
	   `python pydictor -p pid6 --sex m`			生成中国男性公民的身份证后6位所有可能性组合字典
	
  注:  不支持指定生成此类字典的长度 
	   

##### 6. 支持指定生成的字典前缀(头)与后缀(尾)
  例:
	   `python pydictor.py -t L --len 1 4 --head a --tail 123`
	   
  注:  指定的头和尾并不包括在指定的长度(--len参数)中,而是在原来的长度基础上额外增加的。
  
##### 7. 支持将生成的字典进行编码或加密
  例:
       `python pydictor.py -t d --encode b64`
	   
  **注**:  支持 base64 urlencode编码, md5(32位) md516(16位) sha1 sha256 sha512加密

##### 8. 支持建立社会工程学字典
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
	help all			查看15项数据的意思;
	help [具体项]		查看某项数据的意思;
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