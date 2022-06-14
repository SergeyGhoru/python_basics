import os
import shutil


PROJECT = "my_project"
TEMPLATES_DIR = "templates"
PROTECTED_DIRS = [TEMPLATES_DIR, "settings"]


def create_templates_dir(proj: str, t_dir: str):
    templates_dir = os.path.join(proj, t_dir)
    if not os.path.exists(templates_dir):
        os.mkdir(templates_dir)


def copy_templates_in_root(proj: str, t_dir: str):
    for item in os.listdir(proj):
        try:
            if item in PROTECTED_DIRS:
                pass
            else:
                app_items = os.listdir(os.path.join(proj, item))
                if t_dir in app_items:
                    original = os.path.join(proj, item, t_dir, item)
                    target = os.path.join(proj, t_dir, item)
                    if not os.path.exists(target):
                        shutil.copytree(original, target)
        except NotADirectoryError:
            pass


create_templates_dir(PROJECT, TEMPLATES_DIR)
copy_templates_in_root(PROJECT, TEMPLATES_DIR)
