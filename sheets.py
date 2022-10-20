
from __future__ import print_function
import re
from auth import spreadsheet_service
from auth import drive_service
import json

id = '1PDCHp9Dq_84n7o5kWX1iuazyGceu5Op9jTl3gAeGMAA'

def create():
    spreadsheet_details = {
    'properties': {
        'title': 'Python-google-sheets-demo'
        }
    }
    sheet = spreadsheet_service.spreadsheets().create(body=spreadsheet_details,
                                    fields='spreadsheetId').execute()
    sheetId = sheet.get('spreadsheetId')
    print('Spreadsheet ID: {0}'.format(sheetId))
    permission1 = {
    'type': 'user',
    'role': 'writer',
    'emailAddress': 'ccriollo@enersinc.com'
    }
    drive_service.permissions().create(fileId=sheetId, body=permission1).execute()
    return sheetId

def read_range():
    range_name = 'Sheet1!A1:H1'
    spreadsheet_id = '1PDCHp9Dq_84n7o5kWX1iuazyGceu5Op9jTl3gAeGMAA'
    result = spreadsheet_service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    print((rows[0]))


def write_range():
    spreadsheet_id = id
    range_name = 'Sheet1!A4:B4'
    values = [[
        'termoflorez', 'Actualizar graficas del mercado',
    ]]
    value_input_option = 'USER_ENTERED'
    body = {
        'values': values
    }
    result = spreadsheet_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))

