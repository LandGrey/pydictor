## 用法示例:
 [旧版用法参考文档](https://github.com/LandGrey/pydictor/blob/3c855fecd0274205edef461096db6cdc4c008777/README_CN.md)

 [old document for English usage reference](https://github.com/LandGrey/pydictor/blob/3c855fecd0274205edef461096db6cdc4c008777/README.md)

### 核心功能字典

#### 1. 基础字典
```
python pydictor.py -base L --len 2 3 --encode b64
python pydictor.py -base dLc --len 1 3 -o /awesome/pwd
python pydictor.py -base d --len 4 4 --head Pa5sw0rd --output D:\exists\or\not\dict.txt
```

#### 2. 自定义字符集字典
`python pydictor.py -char "asdf123._@ " --len 1 3 --tail @site.com`

#### 3. 排列组合字典
`python pydictor.py -chunk abc 123 "!@#" @ . _ " " --head a --tail @pass --encode md5`

#### 4. 语法引擎解析字典
```
python pydictor.py --conf                                  用默认的"/funcfg/build.conf"文件建立字典
python pydictor.py --conf /my/other/awesome.conf
python pydictor.py --conf "[0-9]{6,6}<none>[a-f,abc,123,!@#]{1,1}<none>" --encode md5 --output parsing.txt
```

#### 5. 模式字典快速生成

```
# note that: 
# 1. using python3 is fast than python2
# 2. one element only support single character, like: [***]{1,1}<***>

# generate pattern: abc[%d][%d][%l][%d][%d][%l][%d][%d]
python3 pydictor.py --head abc --pattern "[0-9]{1,1}<none>[0-9]{1,1}<none>[a-z]{1,1}<none>[0-9]{1,1}<none>[0-9]{1,1}<none>[a-z]{1,1}<none>[0-9]{1,1}<none>[0-9]{1,1}<none>" -o output.txt
```

#### 6. 规则扩展字典

```
python pydictor.py -extend bob --level 4 --len 4 12
python pydictor.py -extend liwei zwell.com --more --leet 0 1 2 11 21 --level 2 --len 6 16 --occur "<=10" ">0" "<=2" -o /possbile/wordlist.lst
```

#### 7. 社会工程学字典
`python pydictor.py --sedb`

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
根据以下信息：

| information items        | value                 |
| :----------------------- | :-------------------- |
| chinese name             | 李伟                    |
| pinyin name              | liwei                 |
| simple name              | lw                    |
| simple name              | Lwei                  |
| english name             | zwell                 |
| birthday                 | 19880916              |
| used password            | liwei123456.          |
| used password            | liwei@19880916        |
| used password            | lw19880916_123        |
| used password            | abc123456             |
| phone number             | 18852006666           |
| used phone number        | 15500998080           |
| home phone               | 76500100              |
| company phone            | 010-61599000          |
| email account            | 33125500@qq.com       |
| email account            | 13561207878@163.com   |
| email account            | weiweili@gmail.com    |
| email account            | wei010wei@hotmail.com |
| home postcode            | 663321                |
| now place postcode       | 962210                |
| common nickname          | zlili                 |
| id card number           | 152726198809160571    |
| student id               | 20051230              |
| job number               | 100563                |
| father birthday          | 152726195910042816    |
| mother birthday          | 15222419621012476X    |
| boy/girl friend brithday | 152726198709063846    |
| friend brithday          | 152726198802083166    |
| pet name                 | tiger                 |
| crazy something          | games of thrones      |
| special meaning numbers  | 176003                |
| special meaning chars    | m0n5ter               |
| special meaning chars    | ppdog                 |

使用命令
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
查看当前配置然后生成字典
```
show
run
```


### 插件型字典(可自己根据API文档开发)
#### 1. 一段时间内生日字典
`python pydictor.py -plug birthday 19800101 20001231 --len 6 8`

#### 2. 身份证后4/6/8位字典
```
python pydictor.py -plug pid4
python pydictor.py -plug pid6 --encode b64
python pydictor.py -plug pid8 --encode sha1 -o pid8.txt
```

#### 3. 网页原始关键词字典
```
python pydictor.py -plug scratch                             用/funcfg/scratch.sites 文件中的多行 url 作为输入
python pydictor.py -plug scratch http://www.example.com
```


### 内置工具(可自己根据API文档开发)
#### 1. 字典合并工具
`python pydictor.py -tool combiner /my/mess/dir`

#### 2. 字典比较工具
`python pydictor.py -tool comparer big.txt small.txt`

#### 3. 词频统计工具
```
python pydictor.py -tool counter s huge.txt 1000
python pydictor.py -tool counter v /tmp/mess.txt 100
python pydictor.py -tool counter vs huge.txt 100 --encode url -o fre.txt
```

#### 4. 字典处理工具
```
python pydictor.py -tool handler raw.txt --tail @awesome.com --encode md5
python pydictor.py -tool handler raw.txt --len 6 16 --occur "" "=6" "<0" --encode b64 -o ok.txt
```

#### 5. 安全擦除字典工具
```
python pydictor.py -tool shredder                    擦除当前输出目录下所有字典文件
python pydictor.py -tool shredder base 		         擦除当前输出目录下所有以"base"开头的字典文件
python pydictor.py -tool shredder /data/mess
python pydictor.py -tool shredder D:\mess\1.zip
```

#### 6. 合并去重工具
`python pydictor.py -tool uniqbiner /my/all/dict/`

#### 7. 字典去重工具
```
python pydictor.py -tool uniqifer /tmp/dicts.txt --output /tmp/uniq.txt
```

#### 8. 多字典文件组合工具

```
python pydictor.py -tool hybrider heads.txt some_others.txt tails.txt
```

