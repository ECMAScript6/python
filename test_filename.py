
import requests
import os
import time
#url 文件链接，path 储存位置

#广州14号馆
def download(url,path):
	file_name = url.split('/')[-1] # 截取文件名
	print("START ---------------------------------------------> %s" %(file_name))
	r = requests.get(url, stream=True) 	# 使用流下载大型文件
	path_dir = path+file_name	#下载目录
	with open(path_dir, mode='wb+') as f: # 打开文件
		for chunk in r.iter_content(chunk_size=32): #分段
			f.write(chunk) #写入
	print("%s => 【THIS IS OK!】" %(file_name))

# 服务器状态检测
website = "http://192.168.1.149:8081/T28%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/14.1-01.jpg"
wait = 3 #等待时间
def ping():
	response = requests.get(website)

	if int(response.status_code) == 200: # OK
		download('http://192.168.1.149:8081/T28%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/14.1-01.jpg','./down/') #广州
		download('http://192.168.1.149:8081/T28%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/15.1-01.jpg','./down/') #广州
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/E1-01.jpg','./down/')
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/E2-01.jpg','./down/')
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/E3-01.jpg','./down/')
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/E4-01.jpg','./down/')
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/W1-01.jpg','./down/')
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/W2-01.jpg','./down/')
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/W3-01.jpg','./down/')
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/W4-01.jpg','./down/')
		print('************************************** \n 文件更新完成.POWER BY LEISHAOJUN')
	elif int(response.status_code) == 403: # Internal server error
		print("文件不存在");
	else:
		print("小凡电脑关机");
	time.sleep(wait)
ping()