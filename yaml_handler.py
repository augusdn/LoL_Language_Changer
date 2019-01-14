import yaml


def read_yaml(file_path):
    with open(file_path, "rt") as stream:
        try:
            content = yaml.load(stream)
            return content
        except yaml.YAMLError as exc:
            print(exc)


def write_yaml(data):
    with open('system_new.yaml', 'w') as output:
        output.write("---\n")
        yaml.dump(data, output, default_flow_style=False)


def change_locale(target, src):
    src_yaml = read_yaml("system_kr.yaml")
    target_yaml = read_yaml("system_global.yaml")

    src_regions = src_yaml.get("region_data")
    target_regions = target_yaml.get("region_data")

    src_region = src_regions.get(src)
    target_region = target_regions.get(target)

    temp_locale = target_region
    temp_locale["available_locales"] = src_region["available_locales"]

    src_yaml["region_data"][src] = temp_locale
    write_yaml(src_yaml)


if __name__ == '__main__':
    change_locale('NA', 'KR')
