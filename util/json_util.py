from flask import jsonify


def serialize(model):
    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)


def make_json_rsp(json: dict):
    return jsonify(rspData(json, 0, "")), 200, {"Content-Type": "application/json"}


def make_simple_rsp(code: int, msg: str):
    return jsonify(rspData({}, code, msg))


def rspData(data: dict, code: int, msg: str):
    return {
        "data": data,
        "code": code,
        "msg": msg
    }