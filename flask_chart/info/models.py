# -*- coding:utf-8 -*-

from datetime import datetime

from . import db


class BaseModel(object):

    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now)


class Chart1(BaseModel, db.Model):

    __tablename__ = "demo_chart1"

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(10), unique=True, nullable=False)
    value = db.Column(db.String(32), nullable=False)

    def to_dict(self):
        resp_dict = {
            "name":
                self.year,
            "value":
                int(self.value)
        }
        return resp_dict


class Chart2(BaseModel, db.Model):

    __tablename__ = "demo_chart2"
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(10),  nullable=False)
    value = db.Column(db.String(32), nullable=False)

    def to_dict(self):
        resp_dict = {
            "name":
                self.year,
            "value":
                int(self.value)
        }
        return resp_dict