import copy

from request import NEW_SHEET_NAME, NEW_SHEET_ID

request_add_sheet_template = {
    "requests": [
        {'addSheet': {'properties': {}}}
    ]
}

request_body_template = {
  "requests": [
    {
      "updateCells": {
        "rows": [],
        "range": {
            "sheetId": NEW_SHEET_ID,
        },
        "fields": "*"
      }
    },
  ]
}


def make_requests_body(data) -> tuple:
    """
    Tuning hierarchy to my dataframe
    And making two objects to perform
    adding sheet and updating it
    :param data:
    :return:
    """
    _first_request = copy.copy(request_add_sheet_template)

    _first_request['requests'][0][
        'addSheet']['properties'] = {
          "sheetId": NEW_SHEET_ID,
          "title": NEW_SHEET_NAME,
          "index": 1
    }
    _second_request = copy.copy(request_body_template)

    _second_request['requests'][0]['updateCells']['rows'] = [
        {
            "values": [
                {
                    "userEnteredValue": {
                        "stringValue": str(_)},
                    "userEnteredFormat": {
                        "backgroundColor": {
                            "green": 1}}
                } for _ in item
            ]
        }
        for item in data
    ]

    return _first_request, _second_request
