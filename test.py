
import requests
import os
import time

#广州14号馆
def download(url):
    # url = "http://192.168.1.149:8081/T28%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/14.1-01.jpg"
	file_name = url.split('/')[-1]
	# 使用流下载大型文件
	r = requests.get(url, stream=True)
	with open(file_name, mode='wb+') as f:
		for chunk in r.iter_content(chunk_size=32):
			f.write(chunk)



#服务器状态检测
website = "http://192.168.1.149:8081/T28%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/14.1-01.jpg"
wait = 3
def ping():
	response = requests.get(website)

	if int(response.status_code) == 200: # OK
		print("start download_14!");
		download('http://192.168.1.149:8081/T28%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/14.1-01.jpg')
		print("ok!");
		print("start download_15!");
		download('http://192.168.1.149:8081/T28%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/15.1-01.jpg')
		print("ok!");
		print("start download_E1!");
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/E1-01.jpg')
		print("ok!");
		print("start download_E2!");
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/E2-01.jpg')
		print("ok!");
		print("start download_E3!");
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/E3-01.jpg')
		print("ok!");
		print("start download_E4!");
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/E4-01.jpg')
		print("ok!");
		print("start download_W1!");
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/W1-01.jpg')
		print("ok!");
		print("start download_W2!");
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/W2-01.jpg')
		print("ok!");
		print("start download_W3!");
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/W3-01.jpg')
		print("ok!");
		print("start download_W4!");
		download('http://192.168.1.149:8081/T29%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/W4-01.jpg')
		print("ok!");
	elif int(response.status_code) == 403: # Internal server error
		print("文件不存在");
	else:
		print("图片服务器关闭");
	time.sleep(wait)

ping()

