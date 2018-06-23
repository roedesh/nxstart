import os

DIRECTORY_NAME = 'test_project'


def directory_exists():
    return os.path.isdir(DIRECTORY_NAME)


def file_exists(file_path):
    return os.path.isfile(os.path.join(DIRECTORY_NAME, file_path))


def file_has_string(file_path, string):
    if string in open(os.path.join(DIRECTORY_NAME, file_path)).read():
        return True
    return False


def assert_file_contains_strings(file_path, strings):
    with open(os.path.join(DIRECTORY_NAME, file_path), 'r') as file:
        data = file.read().replace('\n', '')
        for s in strings:
            assert s in data


def assert_readme_has_project_and_author_name():
    assert_file_contains_strings('README.md', ['Test project', 'Ruud Schroën'])


def assert_makefile_has_project_and_author_name():
    assert_file_contains_strings('Makefile', ['Test project', 'Ruud Schroën'])
