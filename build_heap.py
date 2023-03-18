# python3
# Anna Kūliņa 14.gr.


def build_heap(data):
    swaps = []
    gar = len(data)
    for i in range(gar//2 - 1, -1, -1):
        a = i
        while 2*a+1 < gar:
            kr = 2*a+1
            if kr+1 < gar and data[kr+1] < data[kr]:
                kr = kr+1
            if data[a] >= data[kr]:
                swaps.append((a, kr))
                data[a], data[kr] = data[kr], data[a]    
                a = kr

    return swaps


def main():

    text = input("Ievadiet F testiem vai I manuālai ievadei: ")
    if 'F' in text:
        fails = input("Ievadiet faila nosaukumu: ").strip()
        if fails:
            try:
                with open("./tests/" + fails) as fails1:
                    n = int(fails1.readlines()[0].strip("\n"))
                    data = list(map(int, fails1.readlines()[1].split()))
                    assert len(data) == n
            except FileNotFoundError:
                print("Fails nav atrasts")
                return
            
    elif 'I' in text:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)

    else:
        print("Nepareiza komanda")
        return


    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
