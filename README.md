# pydictor		Build by LandGrey
 A useful hacker dictionary  builder
 
 一个实用的黑客字典生成工具
 
功能简介:
  1.支持使用纯数字、纯小写字母或纯大写字母的任意位数爆破字典生成;
  例如:
       python pydictor -t d --len 6 6				生成6位纯数字字典
	   
  2.支持使用数字、小写字母与大写字母两两组合或3者组合的任意位数爆破字典生成;
  例如：
       python pydictor -t dL --len 4 4				生成数字和小写字母组成的所有4位字典
	   
  3.支持使用自定义字符(包括所有键盘字符)的任意位数爆破字典生成;
  例如:
	   python pydictor -cc aAbBcC123. --len 6 8		生成由'aAbBcC123.' 10个字符组成的所有6位到8位字典
	   
  4.支持使用自定义字符串、字符生成所有可能性组合的字典。
  例如:
	   python pydictor -cm abc ABC 123 .			生成由'abc'、'ABC'、'123' 和'.'生成的所有可能性组合字典
	   
  注:  不支持指定生成字典的长度 
	   
  5.支持指定生成的字典前缀(头)与后缀(尾)
  例如:
	   python pydictor.py -t L --len 1 4 --head a --tail 123
	   
  注:  指定的头和尾并不包括在指定的长度(--len参数)中,而是在原来的长度基础上额外增加的。
  
  6.支持将生成的字典进行编码或加密
  例如:
       python pydictor.py -t d --encode b64
	   
  注:  支持 base64 urlencode编码, md5 sha1 sha256 sha512加密

  
 另:准备在完善pydictor v 1.0版本的基础上，增加社会工程学字典生成功能