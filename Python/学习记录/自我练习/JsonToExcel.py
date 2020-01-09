import json

import tablib

with open('test.txt', 'r+', encoding='utf-8') as jsx:
    rows = json.load(jsx, strict=False)
    # rows = jsx.readlines()
    print(rows)

header = tuple([i for i in rows[0].items()])
data = []
for row in rows:
    body = []
    for v in row.values():
        body.append(v)
    data.append(tuple(body))

data = tablib.Dataset(*data, headers=header)
open('data.xls', 'wb').write(data.xls)
