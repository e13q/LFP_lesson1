from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
import collections
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
from dotenv import load_dotenv

CREATION_DATE_OF_WINERY = 1920


def get_years_sub_title(years: str) -> str:
    return f"Уже {years} {get_years_additional_word(years)} с вами"


def get_years_additional_word(years: str) -> str:
    words_years_type = {
        'one': 'год',
        'some': 'года',
        'many': 'лет'
    }
    exeptions = [
        '11',
        '12',
        '13',
        '14'
    ]
    if len(years) > 1:
        years_last_two_char = years[-2::]
        if years_last_two_char in exeptions:
            return words_years_type['many']
    years_last_digit = int(years[-1::])
    if years_last_digit == 0:
        return words_years_type['many']
    if years_last_digit == 1:
        return words_years_type['one']
    if years_last_digit > 1 and years_last_digit < 5:
        return words_years_type['some']
    return words_years_type['many']


def get_beverages(xsl_filepath_beverages):
    excel_data_df = pandas.read_excel(
        xsl_filepath_beverages,
        sheet_name='Лист1',
        names=[
            'category',
            'title',
            'variety',
            'price',
            'image',
            'promotion'
        ],
        na_values='nan',
        keep_default_na=False
    ).to_dict(orient='records')
    beverages = collections.defaultdict(list)
    for excel_row in excel_data_df:
        beverages[excel_row['category']].append(excel_row)
    return beverages


if __name__ == '__main__':
    load_dotenv()
    xsl_filepath_beverages = os.getenv(
        'XSL_FILEPATH_BEVERAGES',
        default='wine.xlsx'
    )
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    winery_age = str(datetime.datetime.now().year - CREATION_DATE_OF_WINERY)
    try:
        rendered_page = template.render(
            sub_title=get_years_sub_title(winery_age),
            beverages=get_beverages(xsl_filepath_beverages)
        )
    except (FileNotFoundError):
        print(f'Файл {xsl_filepath_beverages} не найден')
        exit()
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
