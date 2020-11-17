
input_dir = 'input/'    # / в конце нужно
# regex_input_file = r'\w+-\d\d\d\.docx'
regex_input_file = r'.*.csv'  # регулярка входящих файлов
file_pattern = 'csv'  # шаблон согласно примерам n1 -- n1.docx, csv -- new.csv

user_data = {
    'group': 'g-12',                # для группового email
    'group_in_email': False,    # упоминание группы в email
    'domain': 'urtt.ru',
    'password': 'P@ssw0rd',
    'ou': '/wsr',
}
