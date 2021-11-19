# Создать `view` функцию выводящую длительность треков сгрупированную по жанрам.
#
# Решить данную задачу средствами Python.

from flask import Flask
from db import execute_query
from formater import list_rec2html_br, milliseconds_conv


app = Flask(__name__)


@app.route('/tracks')
def get_duration():
    sql = 'select g.Name, SUM(t.Milliseconds) ' \
          'from tracks as t ' \
          'join genres as g on t.GenreId = g.GenreId ' \
          'group by g.GenreId;'

    records = execute_query(sql)

    res_lst = []
    for item in records:
        res_lst.append(f'{item[0]}: {milliseconds_conv(item[1])}')

    return list_rec2html_br(res_lst)


app.run(debug=True)
