import docx
from docx.api import Document
import re
from transliterate import translit


class ImportDoc:
    filename = 'source/КСи Д/Д-115.docx'
    groups = ['bi-15']
    grouplist = []
    text = ''
    pattern = 'n1'

    def __init__(self, filename, pattern):
        self.filename = filename
        self.pattern = pattern

        if pattern == 'n1':
            self.grouplist = self.get_grouplist(filename, pattern)
            self.groups = self.normalise_group(self.get_text(filename), pattern)
        elif pattern == 'n2':
            self.grouplist = self.get_grouplist(filename, pattern)
            self.groups = self.normalise_group(self.get_text(filename), pattern)

    def get_text(self, filename):
        doc = docx.Document(filename)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text.split('\n'))
        return full_text

    def normalise_group(self, p, doc_pattern):
        if doc_pattern == 'n1':
            group_pattern = r'\w+\-([0-9])([0-9])([0-9])$'
            match = re.search(group_pattern, p)
            group_ru = match.group()
            group = (translit(group_ru, 'ru', reversed=True)).lower()
            group = group[0:2] + group[1 - 3:]

        elif doc_pattern == 'n2':
            group_pattern = r'\w+\-([0-9])([0-9])([0-9])*'
            groups = []
            for doc in p:
                for string in doc:
                    if re.match(group_pattern, string):
                        group_ru = re.match(group_pattern, string).group(0)
                        group = (translit(group_ru, 'ru', reversed=True)).lower()
                        if len(group) == 5:         # для групп с 1 буквой. Л Д Э
                            group = group[0:2] + group[1 - 3:]
                            groups.append(group)
                        elif len(group) == 6:       # для групп с 2мя буквами КС Би
                            group = group[0:3] + group[1 - 3:]
                            groups.append(group)
                        elif len(group) == 7:       # заочники с 3мя буквами НЕ ПРОВЕРЕНО
                            group = group[0:4] + group[1 - 3:]
                            groups.append(group)
                        else:
                            print('INCORRECT GROUP NAME')
            return groups

    def get_grouplist(self, filename, pattern):
        # TODO возврат списка списков -- общий формат вывода функций в ImportDoc
        if pattern == 'n1':
            doc = Document(filename)
            table = doc.tables[0]

            # Data will be a list of rows represented as dictionaries
            # containing each row's data.
            data = []

            keys = None
            for i, row in enumerate(table.rows):
                text = (cell.text for cell in row.cells)

                # Establish the mapping based on the first row
                # headers; these will become the keys of our dictionary
                if i == 0:
                    keys = tuple(text)
                    continue

                # Construct a dictionary for this row, mapping
                # keys to values for this row
                row_data = dict(zip(keys, text))
                data.append(row_data)

            grouplist = []

            for dict_ in data:
                fio = dict_.get('Фамилия, имя, отчество ')
                grouplist.append(fio)

            return grouplist

        elif pattern == 'n2':
            tables = Document(filename).tables
            groups_list = []  # list of group lists

            for i in range(len(tables)):
                group_list = []
                for j in range(1, len(tables[i].columns), 2):  # Получаем cells из column ФИО
                    for cell in tables[i].columns[j].cells:
                        for paragraph in cell.paragraphs:
                            group_list.append(paragraph.text.split(','))

                groups_list.append(group_list)

            return groups_list

        else:
            print("WRONG DOC PATTERN")
