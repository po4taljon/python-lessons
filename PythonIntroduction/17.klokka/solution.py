n = int(input())
sekInHour = 60 * 60
sekInMin = 60
print((n // sekInHour % 60), ":", n // sekInMin % 60, ":", n % 60, sep="")
