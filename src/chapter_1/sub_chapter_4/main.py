import math


class Solution:
    def __init__(self) -> None:
        print("Solutions class!")
        print()

    def count_digits(self, number: int) -> int:
        """
        This function counts the number of digits in the number

        :param number: Integer used to count number of digits

        :return int: The number of digits in the number
        """
        
        if number == 0:
            return 1

        return int(math.log10(number)) + 1

    def reverse(self, number: int) -> int:
        """
        This function reverses the number

        :param number: Integer to be reversed

        :return int: The revered number 
        """

        return int(str(number)[::-1])

    def is_palindrome(self, number: int) -> bool:
        """
        This function checks if the number is a palindrome

        :param number: Integer to be checked

        :return bool: True if the number is a palindrome
        """

        return str(number) == str(number)[::-1]

    def find_gcd(self, number_one: int, number_two: int) -> None:
        """
        This function finds the GCD of two numbers

        :param number_one: The first number
        :param number_two: The second number

        :return int: The GCD of the two numbers
        """

        while number_one > 0 and number_two > 0:
            if number_one > number_two:
                number_one = number_one % number_two
            else:
                number_two = number_two % number_one

        if number_one == 0:
            return number_two

        return number_one

    def is_armstrong_number(self, number: int) -> None:
        """
        This function check if a number is an armstrong number
        153 = 1^3 + 5^3 + 3^3

        :param number: The number to check if armstrong

        :return bool: True of the number is armstrong false otherwise
        """

        total = 0

        for digit in str(number):
            total += math.pow(int(digit), 3)

        if total == number:
            return True
        else:
            return False

    def find_divisors(self, number: int) -> list[int]:
        """
        This function finds all the divisors of a given number

        :param number: The number to find all the divisors of

        :return list: All the divisors
        """

        divisors = list()

        for digit in range(1, int(math.sqrt(number))+1):
            if number % digit == 0:
                divisors.append(digit)
                divisors.append(number//digit)

        return divisors

    def is_prime(self, number: int) -> bool:
        """
        This function checks if the number is prime

        :param number: The number to be checked

        :return bool: True if the number is prime false otherwise
        """

        if len(self.find_divisors(number)) == 2:
            return True
        else:
            return False


solutions = Solution()

print(solutions.count_digits(1024))
print(solutions.reverse(12345))
print(solutions.is_palindrome(123211))
print(solutions.find_gcd(235, 12))
print(solutions.is_armstrong_number(153))
print(solutions.find_divisors(13))
print(solutions.is_prime(13))
