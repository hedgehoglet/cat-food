import logging
import re
import sys

REPOSITORY_REGEX = r"^[_a-zA-Z][-_a-zA-Z0-9]+$"
MAX_REPOSITORY_NAME_LENGTH = 64
MAX_REPOSITORY_DESCRIPTION_LENGTH = 1024

repository_name = "{{cookiecutter.repository_name}}"
repository_description = "{{cookiecutter.repository_description}}"


def validate_repository():
    """
    Validate repository name and description based on some constraints

    :return: repository status as boolean
    """

    if not re.match(REPOSITORY_REGEX, repository_name):
        logging.error(f"{repository_name} is not a valid repository name!")
        return False

    if len(repository_name) > MAX_REPOSITORY_NAME_LENGTH:
        logging.error(f"{repository_name} is too long to be valid repository name!")
        return False

    if len(repository_description) > MAX_REPOSITORY_DESCRIPTION_LENGTH:
        logging.error(f"{repository_name} have too long description!")
        return False

    return True


if __name__ == "__main__":
    repository_status = validate_repository()

    if not repository_status:
        sys.exit(-1)
