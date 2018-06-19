import os


def generate_folder_name_and_path(name, cwd):
    """
    Returns a folder name and path based on the project name and current working directory.

    :param name: Project name
    :param cwd: Current working directory
    :return: New folder name and path
    """
    folder_name = name.lower().replace(" ", "_")
    folder_path = os.path.join(cwd, folder_name)
    return folder_name, folder_path
