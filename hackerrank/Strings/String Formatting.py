def print_formatted(number):
    # your code goes here
    # foe len tha last no.out the fiven output is binary so,we have taken binary as the len 
    # 
    w=len(str(bin(number))[2:])
    for i in range(1, number+1):
        # rjust takes two argument :len and the operation like here we wanted equal space and e have used splice[2:]as  the output without splice contains 2 extra zero's

        print(str(i).rjust(w,' '),oct(i)[2:].rjust(w, ' '),hex(i)[2:].upper().rjust(w,' '),bin(i)[2:].rjust(w,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
