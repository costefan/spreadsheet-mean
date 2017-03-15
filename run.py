import argparse
import httplib2
import os
import pandas as pd
import json

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from validators.file_validation import FileValidator
from calc import Calculator

try:
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument('key')
    flags = parser.parse_args()
except ImportError:
    flags = None


# Default params
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Calculating average'


def _get_service_n_spreadsheet():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discovery_url = ('https://sheets.googleapis.com/'
                     '$discovery/rest?version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discovery_url)
    spreadsheet_id = flags.key

    return service, spreadsheet_id


def parse_file(df: pd.DataFrame):

    validator = FileValidator(df)
    df = validator()
    df = Calculator.rolling_mean(df)
    inserted_df = [list(df.columns)]
    for _, row in df.iterrows():
        inserted_df.append(
            [item if not isinstance(item, pd.tslib.Timestamp)
             else str(item.date()) for item in row]
        )
    service, spreadsheet_id = _get_service_n_spreadsheet()

    service.spreadsheets().batchUpdate(
        {
            "addSheet": {
                "properties": {
                  "sheetId": spreadsheet_id,
                  "title": "Title",

                }
        }
        }
    ).execute()


def get_credentials():
    """Gets valid user credentials from storage.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    """Shows basic usage of the Sheets API.
    """
    service, spreadsheet_id = _get_service_n_spreadsheet()
    range_name = 'First'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        majorDimension='ROWS'
    ).execute()

    data = pd.DataFrame(
        result.get('values'), columns=result.get('values').pop(0)
    )
    parse_file(data)


if __name__ == '__main__':
    main()
