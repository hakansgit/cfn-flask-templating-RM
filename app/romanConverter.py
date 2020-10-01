class RomanConvertor:
    ROMANS = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
              100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    @classmethod
    def convert(cls, decimal):
        """
        converts decimal numbers between [1, 4000) to roman numerals
        @args
            decimal_number: number to be converted
        """

        try:
            number = int(decimal)
        except:
            raise ValueError('Not a number')

        if number > 3999 or number < 1:
            raise ValueError('Number out of range')

        result = ''

        for k in cls.ROMANS.keys():
            result += (number // k) * cls.ROMANS[k]
            number %= k

        return result

