def reverse():
    with open("input.dat","rb") as inp:
        with open("output.dat", 'wb') as out:
            data = []
            dat = inp.read(1)
            while dat:
                data.append(dat)
                dat = inp.read(1)

            for i in data[::-1]:
                out.write(i)
                

reverse()
