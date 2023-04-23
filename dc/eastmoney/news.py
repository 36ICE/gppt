import json

import requests

from db.mongo_utils import MongoDB

url = 'https://search-api-web.eastmoney.com/search/jsonp'


mongo = MongoDB("mongodb://localhost:27017/")
db_name = "my_database"
collection_name = "my_collection"

for i in range(1,50):
    params = {
        'cb': 'jQuery3510019881728984392444_1682256137205',
        'param': '{"uid":"","keyword":"医疗","type":["cmsArticleWebOld"],"client":"web","clientType":"web","clientVersion":"curr","param":{"cmsArticleWebOld":{"searchScope":"default","sort":"default","pageIndex":'+str(i)+',"pageSize":50,"preTag":"<em>","postTag":"</em>"}}}',
        '_': '1682256137216'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:

        # Process the response here
        json_str = response.content.decode('utf-8')
        jsonp_prefix = params['cb'] + '('
        if json_str.startswith(jsonp_prefix) and json_str.endswith(')'):
            # 删除前后括号并解析JSON数据
            json_data = json.loads(json_str[len(jsonp_prefix):-1])
            # 在此处处理解析后的JSON数据
            list = json_data['result']['cmsArticleWebOld']
            mongo.insert_many(db_name,collection_name,list)
            print(list)
    else:
        # Handle errors here
        print('Error: status code', response.status_code)