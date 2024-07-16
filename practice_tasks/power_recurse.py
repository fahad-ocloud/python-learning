def power_func(no,pow):
    if pow == 0:
        return 1
    if pow<0:
        return 1/no * power_func(no,pow+1)
    return no * power_func(no,pow-1)
print(power_func(5,-2))