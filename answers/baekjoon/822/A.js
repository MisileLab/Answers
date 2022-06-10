/*
a = []

def return_number(n: float, n2: float):
    if n < 140.1:
        return 6
    elif n < 146.0:
        return 5
    elif n < 159.0:
        return 4
    elif n < 161.0:
        if n2 >= 16.0 and n2 < 35.0:
            return 3
        else:
            return 2
    elif n < 204.0:
        if n2 < 25.0 and n2 >= 20.0:
            return 1
        elif (n2 >= 18.5 and n2 < 20.0) or (n2 >= 25.0 and n2 < 30.0):
            return 2
        elif (n2 >= 16.0 and n2 < 18.5) or (n2 >= 30.0 and n2 < 35.0):
            return 3
        else:
            return 4
    else:
        return 4

for _ in range(int(input())):
    b, c = map(int, input().split(" "))
    d = b / 100
    a.append(return_number(b, round(c/(d*d), 2)))

for i in a:
    print(i)
*/

a = []

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

function return_number(n, n2) {
    if (n < 140.1) {
        return 6
    } else if (n < 146.0) {
        return 5
    } else if (n < 159.0) {
        return 4
    } else if (n < 161.0) {
        if (n2 >= 16.0 && n2 < 35.0) { return 3 } else { return 4 }
    } else if (n < 204.0) {
        if (n2 < 25.0 && n2 >= 20.0) {
            return 1
        } else if ((n2 >= 18.5 && n2 < 20.0) || (n2 >= 25.0 && n2 < 30.0)) {
            return 2
        } else if ((n2 >= 16.0 && n2 < 18.5) || (n2 >= 30.0 && n2 < 35.0)) {
            return 3
        } else { return 4 }
    } else { return 4 }
}

readline.question('', aa => {
    ba = Number(aa)
    for (s = 0; s < ba; step++) {
        readline.question('', ac => {
            var aaa = ac.split(' ')
            
            for (var i = 0; i < aaa.length; i++) {
                aaa[i] = +aaa[i];
            }
            
            a.push(return_number(aaa[0], aaa[1]/((aaa[0] / 100)*(aaa[0] / 100), 2)))
        })
    }
    readline.close();
});

for (const e of aaa) {
    console.log(e);
}