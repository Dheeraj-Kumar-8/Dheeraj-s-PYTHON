def binpow(a, b):
    if b == 0:
        return 1

    ans = binpow(a, b // 2)

    if b % 2 == 0:
        return ans * ans
    else:
        return ans * ans * a


a = int(input("Enter base value: "))
b = int(input("Enter power value: "))

ans = binpow(a, b)
print(ans)


