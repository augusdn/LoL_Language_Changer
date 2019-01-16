import yaml
import sys
from constants import *


def read_yaml(file_path):
    try:
        with open(file_path, "rt") as stream:
            try:
                content = yaml.load(stream)
                return content
            except yaml.YAMLError as exc:
                print(exc)
    except FileNotFoundError as errmsg:
        print(errmsg)
        sys.exit()


def write_yaml(data, file_name):
    with open(file_name, 'w') as output:
        output.write("---\n")
        yaml.dump(data, output, default_flow_style=False)


def change_locale(target, src, path):
    yaml_path = path + '/system.yaml'
    temp_path = path + '/system_global.yaml'
    backup_path = path + '/system.yaml.bak'
    src_yaml = read_yaml(yaml_path)
    target_yaml = read_yaml(temp_path)
    write_yaml(src_yaml, backup_path)

    src_regions = src_yaml.get("region_data")
    target_regions = target_yaml.get("region_data")

    src_region = src_regions.get(src)
    target_region = target_regions.get(target)

    temp_locale = target_region
    temp_locale["available_locales"] = src_region["available_locales"]

    src_yaml["region_data"][src] = temp_locale
    write_yaml(src_yaml, yaml_path)


if __name__ == '__main__':
    destination_yaml = read_yaml("system_global.yaml")
    change_locale(NA, KR, 'E:/leagueTest/leagueofLegends')

