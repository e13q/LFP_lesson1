from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
import collections

from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas


def get_years_sub_title(years: str) -> str:
    return f"Уже {years} {get_years_additional_word(years)} с вами"


def get_years_additional_word(years: str) -> str:
    if years is not str:
        try:
            years = int(years)
            years = str(years)
        except Exception:
            print('Года указаны некорректно')
            return 'None'
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


def get_beverages():
    try:
        excel_data_df = pandas.read_excel(
            'wine3.xlsx',
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
    except (FileNotFoundError):
        print('Файл wine3.xlsx не найден')
        exit()
    beverages = collections.defaultdict(list)
    for item in excel_data_df:
        beverages[item['category']].append(item)
    return beverages


if __name__ == '__main__':
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    years_of_winery = datetime.datetime.now().year - 1920
    rendered_page = template.render(
        sub_title=get_years_sub_title(years_of_winery),
        beverages=get_beverages()
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
