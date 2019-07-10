class Roman():
    def __init__(self):
        self.values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, num):
        """
        This is the main function of the class that takes a roman numeral as a parameter and
        returns the integer value of the roman numeral
        """
        sum = 0
        i = 0

        while (i < len(num)):
            digit1 = self.values[num[i]]

            if (i+1 < len(num)):
                digit2 = self.values[num[i+1]]

                if (digit1 >= digit2):
                    # Normal case: preceding digit is greater than next digit
                    sum = sum + digit1
                    i += 1
                else:
                    # Special case: preceding digit is less than next digit
                    sum = sum + digit2 - digit1
                    i += 2
            else:
                sum = sum + digit1
                i += 1

        # print(sum)
        return sum

if __name__ == '__main__':
    roman = Roman()
    roman.roman_to_int('XIX') # Change this roman numeral to test edge cases
