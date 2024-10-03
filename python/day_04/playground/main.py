"""main file of the project"""


def get_name(name: str) -> str:
    """
    get name from user and return it
    Args:
        name (str): name from user
    Returns:
        a string representing the name
    """
    return name


my_name: str = ""
"""My name is a string variable"""

my_name = get_name(my_name)
