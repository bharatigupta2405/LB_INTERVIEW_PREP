def ReverseWord(s):
    n=s[0:len(s)]
    s=n[len(s)-1::-1] 
    # //using string slicing concept [length of string:step count(after how many you want to print):till where you want to print]
    return s

I= str(input('Enter the String'))
print(f'The Reverse String is -{ReverseWord(I)}')
