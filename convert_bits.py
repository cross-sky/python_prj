#writecom(0x01)  //aa
#to
#writecom(0x80)  //writecom(0x01)  //aa

'''
string str="路摊 (456)";
int left = str.find('(');
int right = str.find(')');
str.substr(left+1,right-left-1);
'''

import re

def convert_bits(txts):
    #pattern = re.compile(r'[(](.*)[)]', re.S)
    pattern = re.compile(r'(?<=\()\s+(?=\))')
    out = re.sub(pattern, '0x00', txts)
    #print(re.findall(pattern, txts))
    print(out)

txts = 'writecom(0x01)  //aa'
convert_bits(txts)

'''
(?<=\()\S+(?=\))
(?<=exp)是以exp开头的字符串, 但不包含本身.
(?=exp)就匹配惟exp结尾的字符串, 但不包含本身.
(?<=\()    也就是以括号开头, 但不包含括号.
(?=\)) 就是以括号结尾
\S 匹配任何非空白字符。等价于[^ \f\n\r\t\v]。
+表示至少有一个字符.
(?<=\()\S+(?=\))  就是匹配以 (开头, )结尾的括号里面最少有一个非空白字符的串, 但不包括开头的(和结尾的) 
'''