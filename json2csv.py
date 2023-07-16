import csv
import json
rows = json.load(open('maretu.json'))
with open('maretu.csv','w') as f:
    csv_write = csv.writer(f)
    csv_write.writerow(['曲名','日期','歌姬','作曲','作词','视频制作','链接'])
    for x,y in rows.items():
        csv_write.writerow([x]+list(y.values()))
