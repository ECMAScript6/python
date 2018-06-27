
import requests
import os
import time

#广州14号馆
def download_14():
    url_14 = "http://192.168.1.149:8081/T28%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/14.1-01.jpg"
    file_name = url_14.split('/')[-1]
    # 使用流下载大型文件
    r = requests.get(url_14, stream=True)
    with open(file_name, mode='wb+') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)

#广州15号馆
def download_15():
    url_15 = "http://192.168.1.149:8081/T28%E5%B1%95%E4%BD%8D%E5%9B%BE/%E5%86%85%E9%83%A8%E5%9B%BE/15.1-01.jpg"
    file_name = url_15.split('/')[-1]
    # 使用流下载大型文件
    r = requests.get(url_15, stream=True)
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
        download_14()
        print("ok!");
        print("start download_15!");
        download_15()
        print("ok!");
    elif int(response.status_code) == 403: # Internal server error
        print("文件不存在");
    else:
        print("图片服务器关闭");
    time.sleep(wait)

ping()

