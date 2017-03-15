import copy


request_body_template = {
  "requests": [
    {
      "appendCells": {
        "rows": [],
        "fields": "user.display_name"
      }
    },
  ]
}


def make_request_body(data, sheet_id, sheet_name: str) -> dict:
    """
    Tuning hierarchy to my dataframe
    :param data:
    :param sheet_name:
    :return:
    """
    request_body = copy.copy(request_body_template)
    request_body['requests'][0][
        'appendCells']['sheetId'] = 0
    data.pop(0)
    request_body['requests'][0]['appendCells']['rows'] = [
        {
            "values": [
                {
                    "userEnteredValue": {
                        "stringValue": str(item)},
                    "userEnteredFormat": {
                        "backgroundColor": {
                            "green": 1}}
                }
            ]
        }
        for item in data
    ]

    return request_body_template
