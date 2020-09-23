import docx
from docx.api import Document
import re
from transliterate import translit


class ImportDoc:
    filename = 'source/КСи Д/Д-115.docx'
    group = 'bi-15'
    grouplist = []
    text = ''

    def __init__(self, filename):
        self.filename = filename
        self.group = self.normalise_group(self.get_text(filename))
        self.grouplist = self.get_grouplist(filename)

    def get_text(self, filename):
        doc = docx.Document(filename)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)

        return ''.join(full_text)

    def normalise_group(self, p):
        group_pattern = r'\w+\-([0-9])([0-9])([0-9])$'
        match = re.search(group_pattern, p)

        group_ru = match.group()

        group = (translit(group_ru, 'ru', reversed=True)).lower()
        group = group[0:2] + group[1 - 3:]
        return group

    def get_grouplist(self, filename):
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