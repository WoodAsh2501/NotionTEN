import requests, json, os

def getData():
    databaseId = os.environ['DATABASEID']
    token = os.environ['TOKEN']
    
    date0 = os.environ['NOTION_DATE'] if os.environ['NOTION_DATE'] else '日期'
    status0 = os.environ['NOTION_STATUS'] if os.environ['NOTION_STATUS'] else '完成状态'

    url = f"https://api.notion.com/v1/databases/{databaseId}/query"

    payload = {"page_size": 100}
    headers = {
        "Authorization": "Bearer " + token,
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json"
    }
    # 获取数据
    response = requests.post(url, json=payload, headers=headers)
    items = json.loads(response.text)['results']

    outputList = []

    for i in items:
        # 获取事项、日期、状态
        try:
            date = i['properties'][date0]['date']['start']
        except TypeError:
            # 用空格进行补齐
            date = ' ' * 10

        status = i['properties'][status0]['checkbox']

        # 判断有无设定事项标题
        if i['properties']['标题']['formula']['string']:
            item = i['properties']['标题']['formula']['string']
        else:
            item = ''
        # 筛选未完成事项
        if not status:
            outputList.append([date, item])
            
    # 按日期进行排序
    outputList = sorted(outputList, key=lambda i: i[0])
    return outputList

