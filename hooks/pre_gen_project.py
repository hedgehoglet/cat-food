import logging
import re
import sys

REPOSITORY_REGEX = r"^[_a-zA-Z][-_a-zA-Z0-9]+$"
MAX_REPOSITORY_NAME_LENGTH = 64
MAX_REPOSITORY_DESCRIPTION_LENGTH = 1024


def validate_repository(
    repository_name: str,
    repository_description: str,
):
    """
    Validate repository name and description based on some certain criteria such as name and description length

    Args:
        repository_name::str
            Repostory name
        repository_description::str
            Repository description

    Returns:
        repository_status::bool
            Is repository information meet the criteria?
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
    repository_name = "{{cookiecutter.repository_name}}"
    repository_description = "{{cookiecutter.repository_description}}"

    logging.basicConfig(level=logging.INFO)

    repository_status = validate_repository(
        repository_name,
        repository_description,
    )

    if repository_status:
        logging.info(f"{repository_name} is successfully created!")
    else:
        logging.info(f"{repository_description} is failed to created!")
        sys.exit(-1)
