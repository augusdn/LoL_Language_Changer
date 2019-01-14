import yaml
from constants import *


def read_yaml(file_path):
    with open(file_path, "rt") as stream:
        try:
            content = yaml.load(stream)
            return content
        except yaml.YAMLError as exc:
            print(exc)


def write_yaml(data):
    with open('system_new1.yaml', 'w') as output:
        output.write("---\n")
        yaml.dump(data, output, default_flow_style=False)


def change_locale(orig, target):
    print(orig)
    print(target)


if __name__ == '__main__':
    file_path = "system.yaml"
    org_yaml = read_yaml(file_path)
    # print(yaml.dump(org_yaml, default_flow_style=False))
    write_yaml(org_yaml)
    change_locale(OC1, KR)
