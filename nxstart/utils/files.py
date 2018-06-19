from os.path import join, dirname

PROJECT_ROOT = dirname(dirname(__file__))


def get_full_path(*path):
    """
    Get full path within project directory.

    :param path: Path to join with PROJECT_ROOT
    """
    return join(PROJECT_ROOT, *path)


def replace_in_file(file, replacements):
    """
    Replace strings with the replacements in the given file.

    :param file: File to replace strings in
    :param replacements: {string to replace: replacement, }
    """
    lines = []
    with open(file) as infile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            lines.append(line)
    with open(file, 'w') as outfile:
        for line in lines:
            outfile.write(line)
