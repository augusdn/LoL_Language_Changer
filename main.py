from yaml_handler import *
from yaml_updater import *
from constants import *


def change_language(folderPath, server):
    target = server_dict.get(server)
    src = server_dict.get('Korea')
    change_locale(target, src, folderPath)

    path = folderPath
    latest_folder = search(path)
    target_folder = latest_folder + '/deploy/'
    backup(target_folder)
    update_yaml(path, target_folder)

    return 0


if __name__ == '__main__':
    change_language()
