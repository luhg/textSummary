import json
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/api/getSummary/', methods=['GET', 'POST'])
def getSummary():
	content = dict()
	try:
		content = request.json
	except:
		return "error:-3 请求数据格式错误"

	if not type(content) == dict:
		return "error:-2 请求json格式错误"
	if 'text' not in content:
		return "error:-1 text字段为空"
	if 'title' not in content:
		return "error:-1 title字段为空"
	text = content['text']
	title = content['title']
	from summary import TextSummary
	s = TextSummary()
	s.SetTitle(title)
	s.SetText(text)
	s.GetSummary()
	results = dict()
	results["keywords"] = s.keywords
	results["summary"] = s.summary
	return json.dumps(results)

@app.route('/')
def index():
	# 直接返回静态文件
	return app.send_static_file("index.html")

if __name__ == '__main__':
	port = int(os.environ.get("PORT", "5000"))
	app.run(host='0.0.0.0', port=port,debug=True)
	# app.run()