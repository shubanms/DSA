class Patterns:
    def __init__(self) -> None:
        self.width = 5
        self.length = 5
        return

    def star_rectangle(self, length: int = None, width: int = None) -> None:
        """
        Prints a rectangle pattern of stars

        If no dimensions are provided, use the default class dimensions

        :param length: The number of rows in the rectangle
        :param width: The number of columns in the rectangle

        """

        length = length if length is not None else self.length
        width = width if width is not None else self.width

        for _ in range(length):
            print("*"*width)

        print()

        return

    def left_sided_star_pyramid(self, length: int = None, width: int = None) -> None:
        """
        Prints a left sided pyramid pattern of stars

        If no dimensions are provided, use the default class dimension

        :param length: The number of rows in the pyramid
        :param width: The number of columns in the pyramid
        """

        length = length if length is not None else self.length
        width = width if width is not None else self.width

        for i in range(1, length+1):
            print("*"*i)

        print()

        return

    def left_sided_number_pyramid(self, length: int = None, width: int = None) -> None:
        """
        Prints a left sided pyramid pattern of numbers counting up from 1 on each row

        If no dimensions are provided, use the default class dimension

        :param length: The number of rows in the pyramid
        :param width: The number of columns in the pyramid
        """

        length = length if length is not None else self.length
        width = width if width is not None else self.width

        for i in range(length+1):
            for j in range(1, i+1):
                print(j, end="")
            print()

        print()

        return

    def left_sided_duplicate_number_pyramid(self, length: int = None, width: int = None) -> None:
        """
        Prints a left sided pyramid pattern with same number on one row

        If no dimensions are provided, use the default class dimension

        :param length: The number of rows in the pyramid
        :param width: The number of columns in the pyramid
        """

        length = length if length is not None else self.length
        width = width if width is not None else self.width

        for i in range(1, length+1):
            print(str(i)*i)

        print()

        return


if __name__ == "__main__":
    patterns = Patterns()

    patterns.star_rectangle()
    patterns.left_sided_star_pyramid()
    patterns.left_sided_number_pyramid()
    patterns.left_sided_duplicate_number_pyramid()
