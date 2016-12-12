__author__ = 'Josh'
subs = [('M', 1000), ('C', 100), ('X', 10), ('I', 1)]
others = [('D', 500), ('L', 50), ('V', 5)]
roman_values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


class RomanNumber:
    """
    Class that holds a roman number, and it's corresponding int value
    """
    def __init__(self, roman='', number=0):
        """
        Initilazier for the RomanNumber class. If there is both a roman and number, then it will take the roman value
        :param roman: string of value of roman
        :param number: integer of value
        """
        if number > 3888:
            raise NameError("Roman number input is too large. ")
        if not number:
            self.roman = roman.upper()
            self.__number = self.roman_to_number()
        else:
            self.__number = number
            self.roman = self.number_to_roman()

    def __str__(self):
        """
        Overriding the print method of an object
        :return: string containing self.roman and self.__number
        """
        return 'I have a Roman value of: ' + self.roman + ' and a number of: ' + str(self.__number)

    def roman_to_number(self):
        """
        Converts roman number string to number value of the corresponding object
        :return: the integer value of the corresponding self.roman variable
        """
        inp_rom = self.roman
        skip = 0  # Boolean val to skip if it adds a subtracting value
        total = 0  # Total to output
        for i in range(len(inp_rom) - 1):
            if skip:  # Skips if subtracted double value
                skip = 0
                continue
            first_num = roman_values[inp_rom[i]]  # Gets the number value of the letter inp_rom[i]
            second_num = roman_values[inp_rom[i + 1]]  # Gets the next char in string to check if double val
            if first_num < second_num:
                total += second_num - first_num  # Adds the subtracted val to total
                skip = 1  # Skip to avoid using same num-double times
            else:
                total += first_num  # If it wasn't subtracting val, then just add first num
        if not skip:
            total += roman_values[inp_rom[-1]]  # If the last num wasn't used in subtract val, then add the last val
        return total

    def number_to_roman(self):
        """
        Convert number to roman of the current object
        :return: the roman string value which corresponds to the self.__number variable
        """
        inp_num = self.__number
        counter = []  # The counter that contains tuples of letter, times occurred
        for i in range(4):  # For each pair in subs
            letter, num = subs[i]  # Take the letter and the num
            counter += (letter, inp_num / num),  # These are the original additions to the counter
            # if there is a subtraction it is added later
            # This adds the tuple of letter, number of times letter occurs
            inp_num %= num  # This *subtracts* however much was just added into the counter
            for j in range(i + 1, 4):  # Adds the subtraction tuples, loops through smaller numbers in subs
                s_let, s_num = subs[j]  # smaller letter/number in sub
                if inp_num >= (num - s_num):  # If the current value is greater than the big value - the sub value
                    # The big value is the original num, from subs[i]
                    # sub value is the smaller value to subtract
                    counter += (s_let, 1), (letter, 1)  # Adds the subtraction tuple
                    inp_num -= num - s_num  # subtract the tuple that was just added
                    break  # Breaks out of the for loop, cant have multiple subtracts on same subs[i]
            try:  # This is to prevent it from trying to check for others[4] when i = 4
                other, other_num = others[i]  # gets other/other_num from 5's array
                if inp_num >= other_num:  # If the other_num fits in inp_num then put it in counter
                    counter += (other, 1),  # Adds other_num to counter
                    inp_num -= other_num  # subtracts other num from inp
                for sub, sub_num in subs:  # checks for subtractions from mult of 5
                    if inp_num >= (other_num - sub_num) and other_num > sub_num:  # other num is mult of 5
                        counter += (sub, 1), (other, 1)
                        inp_num -= other_num - sub_num
            except IndexError:  # This is to prevent it from trying to check for others[4] when i = 4
                pass
        out = ''  # Default value for the below not reduce, but should be reduce
        for letter, number in counter:  # Basically reducing the list of tuples to a string
            out += letter * number
        return out

    def to_int(self):
        """
        Returns the private __number variable
        :return: the value of the private __number variable
        """
        return self.__number