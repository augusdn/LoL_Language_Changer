import os
from shutil import copyfile
from constants import *


def search(path):
    path = path + '/RADS/projects/league_client/releases/'
    folder_list = os.listdir(path)
    try:
        folder_list.remove('installer')
    except ValueError:
        pass
    folder_list.sort(key=lambda s: list(map(int, s.split('.'))), reverse=True)
    newest_folder = folder_list[0]
    return path + newest_folder


def backup(path):
    yaml_path = path + 'system.yaml'
    backup_path = path + 'system.yaml.bak'
    if os.path.isfile(yaml_path):
        copyfile(yaml_path, backup_path)


def update_yaml(src, dest):
    yaml_path = src + '/system.yaml'
    replace_path = dest + 'system.yaml'
    if os.path.isfile(yaml_path):
        copyfile(yaml_path, replace_path)
