import json
import pandas as pd
import sys
from flask import Blueprint
from flask import current_app as app
from flask import request
from utillities.exceptions import ExceptionHelpers

mod = Blueprint('select_rows', __name__)
null = None
@mod.route('by_match/', methods=["POST"])
def by_match():
    try:
        request_dict = request.get_json()
        jsonstr = request_dict['jsonStr']
        column = request_dict['column']
        match_str = request_dict['matchString']

        df = pd.read_json(json.dumps(eval(jsonstr)), orient='split')
        selected_rows = df[df[column].str.match(match_str,na=False)]
        df_json = selected_rows.to_json(orient='split', date_format='iso')
        response = app.response_class(
            response=df_json,
            status=200,
            mimetype='application/json'
        )
    except:
        exception = ExceptionHelpers.format_exception(sys.exc_info())
        response = app.response_class(
            response=exception,
            status=400,
            mimetype='application/json'
        )
    return response

@mod.route('by_contains/', methods=["POST"])
def by_contains():
    try:
        request_dict = request.get_json()
        jsonstr = request_dict['jsonStr']
        column = request_dict['column']
        contains_str = request_dict['containsString']
        df = pd.read_json(json.dumps(eval(jsonstr)), orient='split')
        selected_rows = df[df[column].str.contains(contains_str,na=False)]
        df_json = selected_rows.to_json(orient='split', date_format='iso')
        response = app.response_class(
            response=df_json,
            status=200,
            mimetype='application/json'
        )
    except:
        exception = ExceptionHelpers.format_exception(sys.exc_info())
        response = app.response_class(
            response=exception,
            status=400,
            mimetype='application/json'
        )
    return response

@mod.route('by_index/', methods=["POST"])
def by_index():
    try:
        request_dict = request.get_json()
        jsonstr = request_dict['jsonStr']
        row_index= request_dict['rowIndex']
        df = pd.read_json(json.dumps(eval(jsonstr)), orient='split')
        selected_rows = df.loc[row_index]
        df_json = selected_rows.to_json(orient='split', date_format='iso')
        response = app.response_class(
            response=df_json,
            status=200,
            mimetype='application/json'
        )
    except:
        exception = ExceptionHelpers.format_exception(sys.exc_info())
        response = app.response_class(
            response=exception,
            status=400,
            mimetype='application/json'
        )
    return response

@mod.route('by_label/', methods=["POST"])
def by_label():
    try:
        request_dict = request.get_json()
        jsonstr = request_dict['jsonStr']
        row_label= request_dict['rowLabel']
        column_label = request_dict['columnLabel']
        df = pd.read_json(json.dumps(eval(jsonstr)), orient='split')
        selected_rows = df.loc[row_label,column_label]
        df_json = selected_rows.to_json(orient='split', date_format='iso')
        response = app.response_class(
            response=df_json,
            status=200,
            mimetype='application/json'
        )
    except:
        exception = ExceptionHelpers.format_exception(sys.exc_info())
        response = app.response_class(
            response=exception,
            status=400,
            mimetype='application/json'
        )
    return response

@mod.route('by_bool_expression/', methods=["POST"])
def by_bool_expression():
    try:
        request_dict = request.get_json()
        jsonstr = request_dict['jsonStr']
        expression = request_dict['boolExpression']
        df = pd.read_json(json.dumps(eval(jsonstr)), orient='split')
        selected_rows = eval(expression)
        df_json = selected_rows.to_json(orient='split', date_format='iso')
        response = app.response_class(
            response=df_json,
            status=200,
            mimetype='application/json'
        )
    except:
        exception = ExceptionHelpers.format_exception(sys.exc_info())
        response = app.response_class(
            response=exception,
            status=400,
            mimetype='application/json'
        )
    return response
    