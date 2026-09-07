class Solution:
    def intToRoman(self, num: int) -> str:
       
        stri = ""
        while num > 0:
            if num >= 1000:
                stri = stri +"M"
                num -= 1000
            elif num >= 900:
                stri = stri +"CM"
                num -= 900
                
            elif num >= 500:
                stri = stri +"D"
                num -= 500
            elif num >= 400:
                stri = stri +"CD"
                num -= 400
            elif num >= 100:
                stri = stri +"C"
                num -= 100
            elif num >= 90:
                stri = stri +"XC"
                num -= 90
            elif num >= 50:
                stri = stri +"L"
                num -= 50
            elif num >= 40:
                stri = stri +"XL"
                num -= 40
            elif num >= 10:
                stri = stri +"X"
                num -= 10
            elif num >= 9:
                stri = stri +"IX"
                num -= 9
            elif num >= 5:
                stri = stri +"V"
                num -= 5
            elif num >=4:
                stri = stri +"IV"
                num -= 4
            else:
                stri = stri +"I"
                num -= 1
        return stri

        