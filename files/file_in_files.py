with open("input.txt", "r") as inp:
    with open("output.txt", "w") as out:

        # Get all files in input
        files = dict()
        data = inp.readlines()
        for i in data:
            name, sizeN, sizeL = i.split()
            nm, re = name.split('.')
            if re in files.keys():
                files[re].append((nm, int(sizeN), sizeL))
            else:
                files[re] = [(nm, int(sizeN), sizeL)]
        for key, value in files.items():
            files[key] = sorted(value)
        print(files)


        # Creating list with sorted files
        sorted_files = []
        for i in sorted(list(files.keys())):
            sorted_files.append(files[i])

        print(sorted_files)
        print("<<<<<<<<<<<<<<<<<<<")

        for i in sorted_files:
            sizes = {"B": 1,
                     "KB": 1000,
                     "MB": 1000000,
                     "GB": 1000000000,
                     "TB": 1000000000000}

            summary = 0 # B
            for file in i:
                summary += file[1]*sizes[file[2]]
            print(i)
            print(summary)
            print("----------")
            