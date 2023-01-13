#!/usr/bin/env python3
def main():
    count = int(input('How many bottles of beer are you counting down? '))
    #count = 99
    if count <= 100:
        for x in range(count):
            print(str(count) + ' bottles of beer on the wall!')
            print(str(count) + ' bottles of beer on the wall! ' + str(count) + ' bottles of beer! You take one down, pass it around!')
            count = count - 1
    else:
        print('You can not count down from more than 100!')

main()
