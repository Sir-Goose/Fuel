while True:
    text = input("Fraction: ")
    text = text.split("/")
    numerator = text[0]
    denominator = text[1]

    exception = 0

    if denominator == "0":
        exception = exception + 1
    elif "." in denominator:
        exception = exception + 1

    elif "." in numerator:
        exception = exception + 1
    elif exception == 0:
        break

level = (float(numerator) / float(denominator)) * 100

if level <= 1:
    print("E")
elif level >= 99:
    print("F")
else:
    level = round(level, )
    print(str(int(level)) + "%")
