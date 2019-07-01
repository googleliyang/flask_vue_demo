import random

from flask import jsonify, request, current_app

from info import db
from info.models import Chart1, Chart2
from info.utils.response_code import RET
from . import chart_print


@chart_print.route('/chart', methods=['GET', 'POST'])
def chart():
    if request.method == 'GET':
        # generate data to
        year = random.randint(2000, 2020)
        value = random.randint(12, 20)
        data = Chart1.query.first()
        if data:
            data.year = year
            data.value = value
            db.session.add(data)
            try:
                db.session.commit()
                print(data)
            except Exception as e:
                current_app.logger.error(e)
                return jsonify(errno=RET.DBERR, errmsg='Save chart data error')
        else:
            _chart = Chart1()
            _chart.year = year
            _chart.value = value
            db.session.add(_chart)
            db.session.commit()
        _l = []
        charts = Chart1.query.all()
        for i in charts:
            _l.append(i.to_dict())
        res_data = dict(charts=_l)
        return jsonify(errno=RET.OK, errmsg='OK', data=res_data)
    if request.method == 'POST':
        year = request.json.get('name')
        value = str(request.json.get('value'))
        print(year, value)
        if not year and not value:
            return jsonify(errno=RET.DATAERR, errmsg='ERROR')
        chart = Chart2()
        chart.year = year
        chart.value = value
        db.session.add(chart)
        try:
            db.session.commit()
            return jsonify(errno=RET.OK, errmsg='OK')
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='Save chart data error')


@chart_print.route('/chart2', methods=['GET'])
def chart2():
    _l = []
    charts = Chart2.query.all()
    for i in charts:
        _l.append(i.to_dict())
    res_data = dict(charts=_l)
    return jsonify(errno=RET.OK, errmsg='OK', data=res_data)
