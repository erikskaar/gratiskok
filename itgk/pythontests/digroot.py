def digital_root(n):
    return (n-1) % 9 + 1 if n else 0

print(digital_root(502312321))