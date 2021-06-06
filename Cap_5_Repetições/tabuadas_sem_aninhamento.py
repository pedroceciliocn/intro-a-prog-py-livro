tabuada = 1
número = 1
while tabuada <= 10:
    print(f"{tabuada} x {número} = {tabuada * número}")
    número += 1
    if número == 11:
        número = 1
        tabuada += 1
