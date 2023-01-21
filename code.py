import datetime
import string

# January 20th 2023, 18:10 
start_time = datetime.datetime(2023, 1, 20, 18, 10, 0)

# The four digits that change in a regular pattern
starting_code = '0S4A'

current_time = datetime.datetime.now()

minutes_since_start = int(((current_time - start_time).total_seconds() // 60))

# 0-9, A-V
valid_chars = [str(i) for i in range(10)] + [chr(i) for i in range(65,87)]
num_valid_chars = len(valid_chars)

# Result string, as a list so we can change the characters as we go
# (this makes it so that untouched characters remain the same)
res = list(starting_code)

# Calculate how many characters ahead the rightmost character should
# be, based on the number of minutes since our "starting string."
quotient, remainder = divmod(minutes_since_start, num_valid_chars)

# Since the characters "increment" from right to left, loop through the
# string in reverse order.
for index, char in reversed(list(enumerate(starting_code))):
    # Based on the character we're looking at and the remainder from the 
    # above calculation, calculate which character SHOULD be there. Use
    # modulus to "loop back around" to the start of the characters if
    # the number is too large.
    char_idx = valid_chars.index(char)
    new_char = valid_chars[(char_idx + remainder) % num_valid_chars]
    res[index] = new_char
    
    if quotient == 0:
        break

    # Get our remainder/quotient ready for the next iteration
    quotient, remainder = divmod(quotient, num_valid_chars)

res = ''.join(res)    
print(res)
