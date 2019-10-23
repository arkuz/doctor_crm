import json

import get_information
import get_page


def main():
    url = 'http://neuroreab.ru/centers/'
    with open('organizations.json', 'a', encoding='utf-8') as export:
        json.dump(get_information.get_data(
            get_page.get_html(url)), export, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
