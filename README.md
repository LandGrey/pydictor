# pydictor

[![build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://www.github.com/landgrey/pydictor)  [![Python 2.7&3.4](https://img.shields.io/badge/python-2.7&3.4-yellow.svg)](https://www.python.org/)  ![release](https://img.shields.io/badge/version-2.1.5.4-orange.svg) ![License](https://img.shields.io/badge/license-GPLv3-red.svg)


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
      even add customized encode scripts in /lib/encode/ folder, add your own plugin script in /plugins/ folder,
      add your own tool script in /tools/ folder.

   3.powerful and flexible configuration file parsing
      nothing to say,skilled use and you will love it

   4.great compatibility
     whether you are using Python 2.7 version or Python 3.x version , pydictor can be run on Windows, Linux or Mac;
```

#### legal disclaimer
```
1. Usage of pydictor for attacking targets without prior mutual consent is illegal. 
2. It is the end user's responsibility to obey all applicable local, state and federal laws.
3. Developers assume no liability and are not responsible for any misuse or damage caused by this program.
```

## Start:
```
git clone --depth=1 --branch=master https://www.github.com/landgrey/pydictor.git
cd pydictor/
chmod +x pydictor.py
python pydictor.py
```

## Overview：

![extend](/docs/screenshot/extend.png "extend")

![conf](/docs/screenshot/conf.png "conf")

![social engineering dictionary builder](/docs/screenshot/sedb.png "sedb")

## Quick use:
#### [Usage document](/docs/doc/usage.md)

#### [API develop document](/docs/doc/api.md)
#

#### *There's a trick about how to use pydictor: Know what you want type of word list.*
#
#### All of pydictor can generating wordlist

|  type  | wordlist  | identifier | description                                         | supported function |
| :----: | :-------: | :--------: | :-------------------------------------------------- | :----------------- |
|  core  |   base    |     C1     | basic wordlist                                      | F1 F2 F3 F4        |
|  core  |   char    |     C2     | custom character wordlist                           | F1 F2 F3 F4        |
|  core  |   chunk   |     C3     | permutation and combination wordlist                | ALL                |
|  core  |   conf    |     C4     | based on configuration file wordlist                | ALL                |
|  core  |  pattern  |     C5     | fastly generate pattern wordlist                    | F2 F3 F4           |
|  core  |  extend   |     C6     | extend wordlist based on rules                      | ALL                |
|  core  |   sedb    |     C7     | social engineering wordlist                         | ALL                |
|  tool  | combiner  |     T1     | combine the specify directory files tool            |                    |
|  tool  | comparer  |     T2     | compare two file content difference tool            | ALL                |
|  tool  |  counter  |     T3     | word frequency count tool                           | ALL                |
|  tool  |  handler  |     T4     | handle the input file tool                          | ALL                |
|  tool  | uniqbiner |     T5     | combine and unique the directory files tool         | ALL                |
|  tool  | uniqifer  |     T6     | unique the input file tool                          | ALL                |
|  tool  | hybrider  |     T7     | hybrid couples word list tool                       | F1 F2 F3 F4        |
| plugin | birthday  |     P1     | birthday keyword wordlist in specify datetime scope | ALL                |
| plugin |    ftp    |     P2     | against keyword generate ftp password wordlist      | ALL                |
| plugin |   pid4    |     P3     | id card last 4 char wordlist                        | ALL                |
| plugin |   pid6    |     P4     | id card last 6 char wordlist                        | ALL                |
| plugin |   pid8    |     P5     | id card last 8 char wordlist                        | ALL                |
| plugin |  scratch  |     P6     | wordlist based on web pages keywords                | ALL                |


#### function code

| function | code | description                              |
| :------- | :--: | :--------------------------------------- |
| len      |  F1  | the scope of length                      |
| head     |  F2  | add items prefix                         |
| tail     |  F3  | add items suffix                         |
| encode   |  F4  | encode the items                         |
| occur    |  F5  | filter by occur times of letter、digital、special chars |
| types    |  F6  | filter by types of letter、digital、special chars |
| regex    |  F7  | filter by regex                          |
| level    |  F8  | set the word list rule level             |
| leet     |  F9  | enable 1337 mode                         |
| repeat   |  F10 | filter by consecutive repeat times of letter、digital、special chars |

#### encode function supported encodings and encryptions

|  name  | description                              |
| :----: | :--------------------------------------- |
|  none  | default, don't encode                    |
|  b16   | base16 encode                            |
|  b32   | base32 encode                            |
|  b64   | base64 encode                            |
|  des   | des algorithm, need modify code          |
| execjs | execute js function, need modify code    |
|  hmac  | hmac message digest algorithm            |
|  md5   | md5 message digest algorithm output 32 char |
| md516  | md5 message digest algorithm output 16 char |
|  rsa   | rsa algorithm, need modify code          |
|  sha1  | sha-1 message digest algorithm           |
| sha256 | sha-256 message digest algorithm         |
| sha512 | sha-512 message digest algorithm         |
|  url   | url encode                               |
|  test  | a custom encode method example           |


#### occur function
`Usage  : --occur [letters_occur_times_range] [digital_occur_times_range] [special_chars_occur_times_range]`

`Example: --occur ">=4" "<6" "==0"`


#### types function
`Usage  : --types [letters_types_range] [digital_types_range] [special_types_range]`

`Example: --types "<=8" "<=4" "==0"`


#### repeat function
`Usage  : --repeat [letters_repeat_times] [digital_repeat_times] [special_repeat_times]`

`Example: --repeat "<=3" ">=3" "==0"`


#### regex function
`Usage  : --regex [regex]`

`Example: --regex "^z.*?g$"`


#### level function
`Usage  : --level [level]`

`Example: --level 4      level >= 4 will be work in /funcfg/extend.conf`


##### default leet table
`leet char = replace char, and in /funcfg/leet_mode.conf`

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
0            default，replace all
1            left-to-right, replace all the first encountered leet char
2            right-to-left, replace all the first encountered leet char
11-19        left-to-right, replace the first encountered leet char to maximum code-10 chars   
21-29        right-to-left, replace the first encountered leet char to maximum code-20 chars
```

##### leet mode code effection table

| code |   old string    |   new string    |
| :--: | :-------------: | :-------------: |
|  0   | as a airs trees | 45 4 41r5 tr335 |
|  1   | as a airs trees | 4s 4 4irs trees |
|  2   | as a airs trees | a5 a air5 tree5 |
|  11  | as a airs trees | 4s a airs trees |
|  12  | as a airs trees | 4s 4 airs trees |
|  13  | as a airs trees | 4s 4 4irs trees |
|  14  | as a airs trees | 4s 4 4irs trees |
| ...  | as a airs trees | 4s 4 4irs trees |
|  21  | as a airs trees | as a airs tree5 |
|  22  | as a airs trees | as a air5 tree5 |
|  23  | as a airs trees | a5 a air5 tree5 |
|  24  | as a airs trees | a5 a air5 tree5 |
| ...  | as a airs trees | a5 a air5 tree5 |


##### Destination is just a point of departure，It's your show time.
