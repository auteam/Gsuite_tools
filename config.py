

class Config(object):
    """
    Configuration object

    Contain:

    - **ImportConfig** class of import config
    - **UserConfig** class of creating users config
    """

    class ImportConfig(object):
        """
        Import configuration object

        Controls how to import data

        Contain:

        - **dir** (str) where is input (**/** at the end!)
        - **regex_file** (r'str) parameter of incoming filename
        - **pattern** (str) import pattern
        - **split_FIO** (bool) parameter of incoming full_name field
        """

        def __init__(self):
            self.dir = 'input/'         # / в конце нужно
            self.regex_file = r'.*.csv' # регулярка входящих файлов
            self.pattern = 'csv'        # шаблон согласно примерам n1 -- n1.docx, csv -- new.csv
            self.split_FIO = True       # разделенный ФИО в исходном файле или одним полем

    class UserConfig(object):
        """
        User creation configuration object

        Rules of creation GSuite users

        Contain:

        - **group** (str)            group email and email creation
        - **group_in_email** (bool)  email creation
        - **domain** (str)
        - **password** (str)
        - **ou** (str)
        """

        def __init__(self):
            self.group = 'lz-08'         # для группового email
            self.group_in_email = True   # упоминание группы в email
            self.domain = 'urtt.ru'
            self.password = 'P@ssw0rd'
            self.ou = '/students/zaochniki'

    def __init__(self):
        self.import_conf = self.ImportConfig()
        self.user_conf = self.UserConfig()


config = Config()
