import urllib.request as ur
import urllib.parse as up

response = ur.urlopen('http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule')
data = {}

data['i'] = 'I love you'
data['from'] = ' AUTO'
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 1527512542625
sign: df97b867d575034363db698fc86287f8
data['doctype']= 'json'
data['version'] = '2.1'
data['keyfrom']= 'fanyi.web'
data['action'] = 'FY_BY_REALTIME'
data['typoResult'] = 'false'