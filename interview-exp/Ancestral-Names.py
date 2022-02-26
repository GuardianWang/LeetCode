"""
https://leetcode.com/playground/N23j2wJK

In some cultures, children are named after ancestors and there is a number following which represents how many
ancestors have shared that name. They are often shown as Roman Numerals.
In Roman numerals, a value is not repeated more than three times. At that point, a smaller value precedes a larger
value to indicate subtraction. For example, the letter I represents the number 1, and Vrepresents 5. Reason through
the formation of 1 to 70 below, and see how it is applied in the following lines.

I, II, III. IV. V. W. VI. VI, IX and X represent / through 10.
XX XXX XL and L are 20. 30, 40. and 50.
For any other two-digit number < 50, concatenate the Roman numerals) that represent its multiples of ten with the
Roman numerals) for its values < 70. For example, 43is 40 + 3= "XL" + "NT ="XLNW"

Given a list of strings comprised of a name and a Roman numeral, sort the list first by name, then by decimal value of
the Roman numeral.
For example, If you are given the names (Steven XL Steven XVI, David (X, Mary XV. Mary XIN, Mary XX/ the result of the
sort is (David (X, Mary XIll, Mary XV, Mary XX, Steven XVI, Steven XL]. The result with Roman numerals is the expected
return value. Written with the numbers in decimal, they are [David 9, Mary 13, Mary 15, Mary 20, Steven 16, Steven
40%

Function Description
Complete the function sortRoman in the editor below. The function must return the array sorted first by given name.
then by ordinal.
sortRoman has the following parameter:

names[names(0]....namesin-1]: an array of strings
Constraints
1 <= n <= 50
"""
def sortAncestral(names):
    rom2num = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    names = [name.split() for name in names]
    for name in names:
        name[1] = rom_to_num(rom2num, name[1])
    names.sort()
    return names
    
    
def rom_to_num(rom2num, rom):
    num = 0
    for i, c in enumerate(rom):
        if i + 1 < len(rom) and rom2num[c] < rom2num[rom[i + 1]]:
            num -= rom2num[c]
        else:
            num += rom2num[c]
    return num
            

names = ["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"]
print(sortAncestral(names))


"""
Time O(NlogN)
Space O(N)
"""
