import datetime
import string

# January 20th 2023, 18:10 
start_time = datetime.datetime(2023, 1, 20, 18, 10, 0)

current_time = datetime.datetime.now()

minutes_since_start = int(((current_time - start_time).total_seconds() // 60))

# 0-9, A-V
valid_chars = [str(i) for i in range(10)] + [chr(i) for i in range(65,87)]
num_valid_chars = len(valid_chars)

# Result string
res = ''

quotient, remainder = divmod(minutes_since_start, num_valid_chars)

# Repeatedly divide for each character (if we even get there)
while quotient != 0:
    print(remainder)
    res += valid_chars[remainder]
    quotient, remainder = divmod(quotient, num_valid_chars)

res += valid_chars[remainder]
res = res[::-1]
print(remainder)
print(res)
# @1M2DR0S4A7QRV7
# 0S4A
# A + 13  = 
# 4 + 1   = 5
