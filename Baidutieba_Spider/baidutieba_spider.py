# coding = utf-8


import requests


class TiebaSpider:
	def __init__(self, tieba_name):
		self.tieba_name = tieba_name
		self.url_temp = 'https://tieba.baidu.com/f?kw='+tieba_name+'&ie=utf-8&pn=0{}'
		self.headers = {"User-Agent": "ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}



	def get_url_list(self):
		url_list = []
		for i in range(1000):
			url_list.append(self.url_temp.format(i*50))
		return url_list


	def parse_url(self, url):  # 发送请求, 获取响应
		print(url)
		response = requests.get(url, headers=self.headers)
		return response.content.decode()


	def save_html(self, html_str, page_num):  # 保存html 字符串
		file_path = '{}-第{}页.html'.format(self.tieba_name, page_num)
		with open(file_path,"w", encoding="utf-8") as f:  # 李毅-第1页.html
			f.write(html_str)
			print(file_path)



	def run(self):  # 实现主要逻辑
		# 1. 构造url 列表
		url_list = self.get_url_list()
		# 2. 遍历发送请求, 获取响应
		for url in url_list:
			html_str = self.parse_url(url)
			# 3. 保存
			page_num = url_list.index(url) + 1  # 页码数
			self.save_html(html_str, page_num)


if __name__ == "__main__":
	tieba_spider = TiebaSpider("李毅")
	tieba_spider.run()