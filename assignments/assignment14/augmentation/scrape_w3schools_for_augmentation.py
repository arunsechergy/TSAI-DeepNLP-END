#Main page

import requests
from lxml import html 
import csv


csv_file = "ouput_file.csv"

headers = {
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
}

response = requests.get('https://www.w3schools.com/python/python_examples.asp', headers=headers)
print("First page response", response)


#get problems blocks
tree = html.fromstring(response.content)
blocks_list = tree.xpath('//div[@class="w3-bar-block"]/a')



with open(csv_file, 'w') as wf:
    csv_headers = ["Url","Question", "Code"]
    csv_writer = csv.DictWriter(wf, fieldnames=csv_headers)
    csv_writer.writeheader()
    for each in blocks_list:
        title = each.text.strip()
        url = "https://www.w3schools.com/python/" + each.attrib.get('href')
        url_resp = requests.get(url, headers=headers)
        print(url)
        print(url_resp)
        
        resp_tree = html.fromstring(url_resp.content)
        code_text = resp_tree.xpath('//textarea[@id="textareaCode"]/text()')[0]
        
        current_dict = dict()
        current_dict['Question'] = title
        current_dict['Url'] = url
        current_dict['Code'] = code_text

        csv_writer.writerow(current_dict)
    
print("complete")
