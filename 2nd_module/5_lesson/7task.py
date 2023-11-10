ip = input("Введите IP: ")
ipNumbers = ip.split(".")
if len(ipNumbers) != 4:
    print("Адрес — это четыре числа, разделённые точками.")
else:
    ip = [x for x in ipNumbers if x.isdigit()]
    if len(ip) != 4:
        for i in ipNumbers:
            if i.isalnum() and (not(i.isdigit())):
                print("{} - это не целое число.".format(i))
    else:
        ipNumbers = []
        for numbers in ip:
            if int(numbers) > 255:
                print("{} превышает 255.".format(numbers))

            else:
                ipNumbers.append(numbers)
        if len(ipNumbers) == 4:
            print("IP-адрес корректен.")