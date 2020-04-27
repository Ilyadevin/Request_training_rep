import configparser


def config_file():
    configuration = configparser.ConfigParser()
    configuration.read('config.ini')
    api = configuration['api_key']['yandex_api']
    return api
