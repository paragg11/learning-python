def square(number):
    """Calculate the number of grains of wheat on a chessboard square.

    :param number: int - Square number in [0..63]
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Calculate the number of grains on the chessboard."""
    return 2 ** 64 - 1