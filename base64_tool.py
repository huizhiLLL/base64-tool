import base64
import random

base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#输入 预处理
steString = input("请输入要隐写的字符串：")
ordString = [format(ord(char), '08b') for char in steString]#隐写的二进制字符串
letterarray = ["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","vv","ww","xx","yy","zz"]
plainText = random.choices(letterarray,k=len(ordString)*4)#随机选择单词作为明文（均为2个字母）

base64_stringarray = [base64.b64encode(text.encode('utf-8')).decode('utf-8') for text in plainText]#明文base64编码
splitString = [
    bin_string[i:i+2]
    for bin_string in ordString
    for i in range(0,8,2)
]
#分割隐写二进制串为2位一组

thirdString = [format(base64_chars.index(letter[2]),'08b') for letter in base64_stringarray]
new1String = [string[0:6] for string in thirdString]
for i in range(len(new1String)):
    new1String[i] = new1String[i] + splitString[i]
new2String = [base64_chars[int(string,2)] for string in new1String]
split1String = [string[0:2] for string in base64_stringarray]

resultString = "".join([split1String[i] + new2String[i] + "=" for i in range(len(new2String))])
print("隐写后base64编码：")
print(resultString)
