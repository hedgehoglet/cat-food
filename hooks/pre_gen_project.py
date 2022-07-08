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
            Repostory name (64 characters)
        repository_description::str
            Repository description (1024 characters)

    Returns:
        repository_status::bool
            Is repository information meet the criteria?
    """
    repository_name_length = len(repository_name)
    repository_description_length = len(repository_description)

    if not re.match(REPOSITORY_REGEX, repository_name):
        logging.error(f"{repository_name} is not a valid repository name! ({REPOSITORY_REGEX})")
        return False

    if repository_name_length > MAX_REPOSITORY_NAME_LENGTH:
        logging.error(
            f"{repository_name} is too long to be repository name! ({repository_name_length}/{MAX_REPOSITORY_NAME_LENGTH})"
        )
        return False

    if repository_description_length > MAX_REPOSITORY_DESCRIPTION_LENGTH:
        logging.error(
            f"{repository_name} have too long description! ({repository_description_length}/{MAX_REPOSITORY_DESCRIPTION_LENGTH})"
        )
        return False

    return True


if __name__ == "__main__":
    repository_name = "{{cookiecutter.repository_name}}"
    repository_description = "{{cookiecutter.repository_description}}"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s :: 🦔🐈 :: %(levelname)s :: %(message)s",
    )

    repository_status = validate_repository(
        repository_name,
        repository_description,
    )

    if repository_status:
        logging.info(f"{repository_name} is successfully created!")
    else:
        logging.info(f"{repository_description} is failed to created!")
        sys.exit(-1)
