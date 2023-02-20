with open('lines.txt') as f:
    print(
        max(
            filter(
                str.isalpha,
                *map(str.split, [f.read()])
            ),
            key=len
        )
    )