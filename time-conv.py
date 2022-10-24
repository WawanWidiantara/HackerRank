def timeConversion(s):
    if 'PM' in s and s[:2] != '12':
        s = str(12+int(s[:2])) + s[2:]
    elif 'AM' in s and s[:2] == '12':
        s = '00' + s[2:]
    return s[:-2]

s = '12:00:00AM'
print(timeConversion(s))