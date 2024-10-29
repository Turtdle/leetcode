def intToRoman(num: int) -> str:
        ma = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        digits = len(str(num))
        def seperate_into_tensthings(num):
            str_number = str(num)
            place_values = []
        
            for i, digit in enumerate(str_number):
                
                place_value = int(digit) * (10 ** (len(str_number) - i - 1))
                
                place_values.append(place_value)
            
            return place_values
        place_values = seperate_into_tensthings(num)
        roman = ""
        for place_value in place_values:
            if place_value in ma:
                roman += ma[place_value]
            elif place_value == 4:
                roman += "IV"
            elif place_value == 9:
                roman += "IX"
            elif place_value == 40:
                roman += "XL"
            elif place_value == 90:
                roman += "XC"
            elif place_value == 400:
                roman += "CD"
            elif place_value == 900:
                roman += "CM"
            else:
                if place_value < 5:
                    roman += ma[1] * (place_value // 1)
                elif place_value < 10:
                    roman += ma[5] + ma[1] * ((place_value - 5) // 1)
                elif place_value < 50:
                    roman += ma[10] * (place_value // 10)
                elif place_value < 100:
                    roman += ma[50] + ma[10] * ((place_value - 50) // 10)
                elif place_value < 500:
                    roman += ma[100] * (place_value // 100)
                elif place_value < 1000:
                    roman += ma[500] + ma[100] * ((place_value - 500) // 100)
                else:
                    roman += ma[1000] * (place_value // 1000)
        return roman