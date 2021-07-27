from Yandex_API import YaUploader

TOKEN = 'AQAAAAAFo08JAADLW4k7LIJX4UU0jEyzpOV26Tk'


class TestCalculatePytest:
    def setup(self):
        print('setup')

    # тест на успешное создание папки
    def test_creating_folder(self):
        assert 201 == YaUploader().create_folder('folder_name')

    # тест для проверки, что папка с таким названием уже не была создана
    def test_creating_existing_folder(self):
        assert 409 != YaUploader().create_folder('folder_name')

    # еще один тест, что папка создана (осуществляется запрос через список файлов)
    def test_is_folder_created(self):
        assert 200 == YaUploader().check_created_folder('folder_name')

    # тест для определения отсутствия папки на Я.Диске
    def test_check_miss_folder(self):
        assert 404 == YaUploader().check_created_folder('folder_name')

    def teardown(self):
        print('teardown')
