# Создать view функцию выводящую `count` самых продаваемых треков с суммой продаж. `count` - необязательный параметр
# GET запроса. Если он не указан вывести все все продажи отсортированные в порядке убывания сумм.
#
# Задачу решить средствами Python.

from flask import Flask
from db import execute_query
from formater import list_rec2html_br


from webargs import fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.route('/tracks')
@use_kwargs(
    {
        'count': fields.Int(
            required=False,
            missing=None
        )
    },
    location='query'
)
def get_top_tracks(count):
    sql = 'select t.Name, SUM(i.Quantity*i.UnitPrice) as revenue ' \
          'from tracks as t ' \
          'join invoice_items as i on t.TrackId = i.TrackId ' \
          'group by t.TrackId ' \
          'order by revenue desc;'

    records = execute_query(sql)

    res_lst = []
    for item in records:
        res_lst.append(f'{item[0]}: {item[1]}')

    return list_rec2html_br(res_lst[:count])


app.run(debug=True, port=5001)
