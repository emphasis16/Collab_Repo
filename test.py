from pwn import *

r = remote("stembactf.space", 5400)

low = 1
high = 5000
trying = 0

while True:
    try:
        mid = (low + high) // 2
        r.sendlineafter(b'Tebakan: ', (str(mid).encode("utf8")))
        result = r.recvline().decode("utf8")
        if "Kelazzzzz" in result:
            trying += 1
            print(f"succsess, try {trying}")
            low = 1
            high = 5000
        elif "Kurang banyak ygy" in result:
            low = mid + 1
        elif "Terlalu besar nih" in result:
            high = mid - 1
        else:
            print("ytta")
            print(result)
            break
    except EOFError:
        print("An error occurred while receiving data")
        break

flag = r.recvregex('STEMBACTF{.*}').decode("utf8")
print(flag)

r.close()