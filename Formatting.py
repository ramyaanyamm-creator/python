def print_formatted(number):
    
    # your code goes here
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        dec = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(dec.rjust(width),
              octa.rjust(width),
              hexa.rjust(width),
              binary.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
