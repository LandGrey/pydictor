# pydictor
[![build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://www.github.com/landgrey/pydictor)  [![Python 2.7|3.4](https://img.shields.io/badge/python-2.7|3.4-yellow.svg)](https://www.python.org/)  ![release](https://img.shields.io/badge/version-2.0.4-orange.svg) ![License](https://img.shields.io/badge/license-GPLv3-red.svg)

**README.md [中文版](README_CN.md)**

##### pydictor —— A powerful and useful hacker dictionary builder for a brute-force attack
                          _ _      _
          _ __  _   _  __| (_) ___| |_ ___  _ __
         | '_ \| | | |/ _` | |/ __| __/ _ \| '__|
         | |_) | |_| | (_| | | (__| || (_) | |
         | .__/ \__, |\__,_|_|\___|\__\___/|_|
         |_|    |___/                         
    

##### Email: LandGrey@qq.com

-
## Preface：
```
Q: Why I need to use pydictor ?
A: 1.it always can help you
      You can use pydictor to generate a general blast wordlist, a custom wordlist based on Web content, a social engineering wordlist, and so on;
      You can use the pydictor built-in tool to safe delete, merge, unique, merge and unique,  count word frequency to filter the wordlist, 
      besides, you also can specify your wordlist and use '-tool handler' to filter your wordlist;

   2.highly customized
      You can generate highly customized and complex wordlist by modify multiple configuration files, 
      add your own dictionary, using leet mode, filter by length、char occur times、types of different char、regex,
      even customized own encryption function by modify /lib/fun/encode.py test_encode function.
      its very relevant to generate good or bad password wordlist with your customized rules and skilled use of pydictor;

   3.powerful and flexible configuration file parsing
      nothing to say,skilled use and you will love it

   4.great compatibility
     whether you are using Python 2.7 version or Python 3.x version , pydictor can be run on Windows, Linux or Mac;
```

## Start:
```
git clone --depth=1 --branch=master https://www.github.com/landgrey/pydictor.git
cd pydictor/
chmod 755 pydictor.py
python pydictor.py
```

## Overview：

![extend](/screenshots/extend.png "extend")

![social engineering dictionary builder](/screenshots/sedb.png "sedb")

## Quick to use:
#### types of generate wordlist（14 types）and descriptions

| wordlist type | number| description                                         |
|:------------- | :---- |:--------------------------------------------------- |
| base          | 1     | basic wordlist                                      |
| char          | 2     | custom character wordlist                           |
| chunk         | 3     | permutation and combination wordlist                |
| conf          | 4     | based on configuration file wordlist                |
| sedb          | 5     | social engineering wordlist                         | 
| idcard        | 6     | id card last 6/8 char wordlist                      |
| extend        | 7     | extend wordlist based on rules                      |
| scratch       | 8     | wordlist based on web pages keywords                | 
| passcraper    | 9     | wordlist against to web admin and users             |
| handler       | 10    | handle the input file generate wordlist             |
| uniqifer      | 11    | unique the input file and generate wordlist         |
| counter       | 12    | word frequency count wordlist                       |
| combiner      | 13    | combine the input file generate wordlist            |
| uniqbiner     | 14    | combine and unique the input file generate wordlist |

#### function and scope of support wordlist number

| function   | number (wordlist)            | description                                              |
|:---------- | :--------------------------- |:-------------------------------------------------------- |
| len        | 1 2 3 4 5 6 7 9 10 11 12 14  | lenght scope                                             |
| head       | 1 2 3 4 5 6 7 9 10 11 12 14  | add items prefix                                         | 
| tail       | 1 2 3 4 5 6 7 9 10 11 12 14  | add items suffix                                         | 
| encode     | 1 2 3 4 5 6 7 9 10 11 12 14  | encode the items                                         |
| occur      | 3 4 5 7 9 10 11 12 14        | filter by occur times of letter、digital、special chars  |
| types      | 3 4 5 7 9 10 11 12 14        | filter by types of letter、digital、special chars        |
| regex      | 3 4 5 7 9 10 11 12 14        | filter by regex                                          |
| level      | 5 7 9                        | set the wordlist level                                   |
| leet       | 5 7 9                        | 1337 mode                                                |


## usage examples

#### 1:  generate the basic wordlsit based on digital lenght of 4
```
python pydictor.py -base d --len 4 4 --output D:\exists\or\not\dict.txt
```

### 2:  encode the wordlist
```
python pydictor.py -base L --len 1 3 --encode b64
```

#### 3: use d(digital) L(lowercase letter) c(capital letter) generating wordlist
```
python pydictor.py -base dLc -o /awesome/pwd
```

### 4: use customized characters generating wordlist
```
python pydictor.py -char "abc123._@ " --len 1 3 --tail @site
```

#### 5: generate permutation and combination wordlist
```
python pydictor.py -chunk abc ABC 666 . _ @ "'" --head a --tail 123 --encode md5
```

#### 6. extend wordlist based on rules

1.  extend function mainly directed against web application administrator to generate password
2.  You can put your own weak password wordlist in wordlist/Web,extend function will auto unique them,new wordlist will contains them
3.  You can modify funcfg/extend.conf,set prefix, suffix, prefix + suffix and middle word when extended
4.  extend function support leet mode,pick by level and pick by lenght function，you can learn more in the following   

write the following information to '/names.txt'
```
liwell
shelly
bianji
webzhang
```

run command
```
python pydictor.py -extend /names.txt --leet 0 1 2 11 21 --level 1 --len 4 16 --occur "<=10" ">0" "<=2" -o /possbile/wordlist.lst
```


#### 7: id card last 6/8 char wordlist

```
pydictor.py -plug pid6 --types ">=0" ">=4" ">=0" --encode b64
```

**note**:   default sex ='all', it decided by lib/data/data.py default_sex, and 'm' is Male, 'f' is Female

#### 8: using passcraper plugin crawl website generating password wordlist based on plain text found and extend rules

1.  the rules of passcraper plug and extend function are the same
2.  passcraper plug will generate two wordlist，preffix with SCRATCH is raw wordlist by website plain text，
    and if you feel that there are a lot of unrelated words in the SCRATCH wordlist, 
    you can remove them, and then use the extend function to specify the new file to generate dictionary again.
3.  you can modify the funcfg/passcraper_blacklist.conf file，add or delete useless words that need to be filtered out，
    and also can modify lib/data/data.py file passcraper_filter argument，change the filter regular expressions
4.  with same extend function，you can put your weak password in /wordlist/Web，new wordlist will contains them

```
python pydictor.py -plug passcraper				using default file scraper.sites as multi-input file
python pydictor.py -plug passcraper http://www.example.com
```


#### 9. using configuration file build dictionary
##### this function contains all of "-base" and "-char" capacities，and more precise control

```
python pydictor.py --conf                           using default file funcfg/build.conf build the dictionary
python pydictor.py --conf /my/other/awesome.conf    using /my/other/awesome.conf build the dictionary
```

**note**: parsing rules details as following，besides referred to build.conf file

#### configuration parsing rules details:
```
 1. the basic unit of parsing is called an parsing element, an parsing element includes five elements, namely: head, character set, length range, encoding, tail, which can be omitted both head and tail;
A standard parsing element:head[characters]{minlength,maxlength}<encode-type>tail，a example parsing element：a[0-9]{4,6}<none>_
Its meaning build a dictionary that  prefix is "a" , character set is 0—9, don't encode,length range is 4—6 and  suffix is "_"
 2. current is support parsing one line
 3. one line can contains 10 parsing elements
such as:[4-6,a-c,A,C,admin]{3,3}<none>_[a,s,d,f]{2,2}<none>[789,!@#]{1,2}<none>,it contains three parsing elements
 4. if annotator "#" in first place, program won't parse this line
 5. conf function can build more precise dictionary up to single char

about character sets：
				   You can add the "-" in the middle of character sets beginning and ending to  join them
				   and can also use "," to separate multiple character sets, or a single character, or a single string, as an element of the character set;

supported encoding:
			   none    don't encode
			   b64     base64
			   md5     md5 digest algorithm output 32 char
			   md516   md5 digest algorithm output 16 char
			   sha1    sha1 digest algorithm
			   url     urlencode
			   sha256  sha256 digest algorithm
			   sha512  sha512 digest algorithm
               test    interface for customized encode function
```


#### 10. handle wordlist's tools
##### filter tool handler
  specify the input file, and output the handled file
```
python pydictor.py -tool handler /wordlist/raw.txt --len 6 16 --occur "" "=6" "<0" --encode b64 -o /wordlist/ok.txt
```

##### safe delete tool shredder
```
python pydictor.py -tool shredder 		delete the currently specified output path(default:results) files and all its dictionary files
python pydictor.py -tool shredder base 		delete the files of it's prefix is "BASE" in currently specified output path
```

prefix(case insensitive) range in 14 items: base,char,chunk,conf,sedb,idcard,extend,handler,uniqifer,counter,combiner,uniqbiner,scratch,passcraper

besides，you can safe shred files or whole directory as following:
```
python pydictor.py -tool shredder /data/mess
python pydictor.py -tool shredder D:\mess\1.zip
```
  for improving the security delete speed, the default uses 1 times to erase and rewrite，you can modify lib/data/data.py file's file_rewrite_count and dir_rewrite_count value

##### remove duplicates tool uniqifer
```
python pydictor.py -tool uniqifer /tmp/my.dic
```

##### word frequency statistics tool counter
```
python pydictor.py -tool counter vs /tmp/mess.txt 100		select 100 words in /tmp/mess.txt file that appear in the most times and output to the terminal and saved to file
```

  **note**: default choose 100 items to print or save；default separator is:"\n",you can modify counter_split value in lib/data/data.py file

##### merge dictionary tool combiner
```
python pydictor.py -tool combiner /my/messdir
```

##### remove duplicates after merging tool uniqbiner
```
python pydictor.py -tool uniqbiner /my/messdir
```

#### 11: wordlist filter
##### filter by level function

1.  this function is currently only support extend function, passcraper plug, Social Engineering Dictionary Builder
2.  default level is 3, the lower level, the lower possibility, the more items
3.  modify funcfg/extend.conf file，customized your awesome level rules

```
python pydictor.py -extend bob adam sarah --level 5
```


##### use leet mode

1.  this function is currently only support extend, passcraper, Social Engineering Dictionary Builder
2.  all default unable to use leet mode, when enable, you can use multiple code at one time
3.  SEDB can enable leet mode and set code in SEDB interface
4.  enable leet mode cannot make wordlist decrease，it will increase wordlist on the basis of unable to use the leet mode


##### default leet table
```
leet char = replace char
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

##### code
```
0			default，replace all
1			left-to-right, replace all the first encountered leet char
2               	right-to-left, replace all the first encountered leet char
11-19			left-to-right, replace the first encountered leet char to maximum code-10 chars   
21-29			right-to-left, replace the first encountered leet char to maximum code-20 chars
```


##### code effection table

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


besides,you also can:   

```
modify /funcfg/leet_mode.conf, add or delete leet table items;   
modify /lib/lib/data.py, extend_leet、passcraper_leet、sedb_leet arguments, choose some functions whether default use leet mode;
modify /lib/data/data.py,leet_mode_code argument, choose default mode code;
```

##### filter by occur times of letter、digital、special chars

```
--occur [scope of occur letter times] [scope of occur digital times] [scope of occur special chars times]
```

default occur times  

```
"<=99" "<=99" "<=99"
```

##### filter by types of letter、digital、special chars
```
 --types [scope of letter types] [scope of digital types] [scope of special types]
```

default types  

```
">=0" ">=0" ">=0"
```

#### 12. social engineering dictionary
```
python pydictor.py --sedb
```
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

##### command:
```
help                reload interface
help desc           view the meaning for each items
exit or quit        exit the program
clear or cls        clear screen
show                view the current settings
set                 set option value
rm                  remove option value
len                 select the length range
head                add prefix
tail                add suffix
encode              encode items
occur               set occur times of letter、digital、special chars
types               set types of letter、digital、special chars
regex               filter by regex
level               select the extend level value
leet                enable leet mode and choose code
output              set output dictionary or file path
run                 build wordlist
```

if you have some information about someone   


| information items  |        value          |
|:------------------ | :-------------------- |
| chinese name       | 李伟                  |
| pinyin name        | liwei                 | 
| simple name        | lw                    | 
| simple name        | Lwei                  |
| english name       | zwell                 | 
| birthday           | 19880916              | 
| used password      | liwei123456.          | 
| used password      | liwei@19880916        | 
| used password      | lw19880916_123        | 
| used password      | abc123456             |
| phone number       | 18852006666           |
| used phone number  | 15500998080           | 
| home phone         | 76500100              |
| company phone      | 010-61599000          | 
| email account      | 33125500@qq.com       |
| email account      | 13561207878@163.com   |
| email account      | weiweili@gmail.com    | 
| email account      | wei010wei@hotmail.com | 
| home postcode      | 663321                | 
| now place postcode | 962210                |
| common nickname    | zlili                 |
| id card number     | 152726198809160571    | 
| student id         | 20051230              | 
| job number         | 100563                |
| father birthday    | 152726195910042816    | 
| mother birthday    | 15222419621012476X    | 
| boy/girl friend brithday | 152726198709063846 |
| friend brithday    | 152726198802083166    | 
| pet name           | tiger                 | 
| crazy something    | games of thrones      |
| special meaning numbers | 176003           | 
| special meaning chars | m0n5ter            | 
| special meaning chars | ppdog              |


now, use follwing command:

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

view the configuration, and build the wordlist  
```
show
run
```

if you want more items wordlist, use  
```
level 1
```

and, you want to filter some impossible password,   

set the password lenght   

```
len 1 16
```

at least one letter and at most three special char,   

```
occur ">0" "" "<=3"
```

and at most two types of special char in one item,  

```
types "" "" "<=2"
```

finaly, specify the output path, build wordlist again  

```
output D:\awesome\dict\liwei_pass.txt
run
```

note:  
1. you can modify funcfg/sedb_tricks.conf file，change the word transform prefix, suffix and prefix+suffix rules
2. you can put your own individual weak password wordlist in wordlist/SEDB, 
3. SEDB some little rules contains extend function

##### Destination is just a point of departure，It's your show time.
