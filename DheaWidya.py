while True:
    try:
        input1 = int(input("input 1: "))
        input2 = int(input("input 2: "))
        input3 = input("input 3: ")

    except:
        print("Input yang anda masukan salah!")

    else:
        if input3.lower() == "tambah":
            print("outputnya adalah:", (input1 + input2))
        elif input3.lower() == "kurang":
            print("outputnya adalah:", (input1 - input2))
        elif input3.lower() == "bagi":
            print("outputnya adalah:", (input1 * input2))
        elif input3.lower() == "kali":
            print("outputnya adalah:", (input1 / input2))
        else:
            print("output tidak sesusai!")
    