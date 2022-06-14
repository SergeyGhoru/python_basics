import yaml
import os

FILENAME = "config.yaml"


def load_template(filename: str):
    with open(filename, "r") as stream:
        try:
            parsed_yaml = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return parsed_yaml


def generate_tree(tree_template, path=os.getcwd()):
    for key, value in tree_template.items():
        dir_path = os.path.join(path, key)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        if type(value) == dict:
            generate_tree(value, dir_path)
        elif type(value) == list:

            for item in value:
                if type(item) == dict:
                    generate_tree(item, dir_path)
                else:
                    filename = os.path.join(dir_path, item)
                    if not os.path.exists(filename):
                        os.mknod(filename)


generate_tree(load_template(FILENAME))
