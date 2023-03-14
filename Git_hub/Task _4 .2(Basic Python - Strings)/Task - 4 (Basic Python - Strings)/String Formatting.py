def print_formatted(number):
    padding_length = len(bin(number)[2:])

    for num in range(1, number + 1):
        dec_num = str(num)
        oct_num = oct(num)[2:]
        hex_num = hex(num)[2:].upper()
        bin_num = bin(num)[2:]
        print(f'{dec_num.rjust(padding_length)} {oct_num.rjust(padding_length)} {hex_num.rjust(padding_length)} {bin_num.rjust(padding_length)}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
