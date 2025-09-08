# 1. Extract all numbers from the string
# "I have 2 apples, 15 bananas, and 1 orange."
# use a regex to find all integer numbers.

# Expected output:
# ["2", "15", "1"]

import re

print("\n")
text = "I have 2 apples, 15 bananas, and 1 orange."
print(re.findall(r'\d+', text))

# 2. Given the list
# ["alice@example.com", "bob(at)example.com", "carol@example.co.uk", "dave@example"]
# Filter to only those strings that look like valid email addresses of the form username@domain.tld (where the TLD is 2–4 letters).

# Expected output:
# ["alice@example.com", "carol@example.co.uk"]

print("\n")
text2 = ["alice@example.com", "bob(at)example.com", "carol@example.co.uk", "dave@example"]
print(re.findall(r'\w+@\w+\.\w+\.*\w*'," ".join(text2)))

# 3. Normalize whitespace: 
# Collapse any sequence of whitespace (spaces, tabs, newlines) in the string
# "This   is a\t\ttest.\nNew   line!"
# down to single spaces, and strip leading/trailing whitespace.

# Expected output:
# "This is a test. New line!"

print("\n")
text3 = "This   is a\t\ttest.\nNew   line!"
print(re.sub(r'\s+', ' ', text3))

# 4. Reformat dates: In the text
# "Important dates: 01/02/2020, 23/11/1999 and 5/6/21."
# replace all dates in DD/MM/YYYY or D/M/YY format with ISO YYYY-MM-DD, zero-padding day and month as needed.

# Expected output:
# "Important dates: 2020-02-01, 1999-11-23 and 2021-06-05."

text4 = "Important dates: 01/02/2020, 23/11/1999 and 5/6/21."
days = re.findall(r'\b(\d{1,2})/\d{1,2}/\d{2,4}\b', text4)

for i in range(len(days)):
    if len(days[i]) == 1:
        days[i] = '0' + days[i]          

# print("days:",days)

month = re.findall(r'\b\d{1,2}/(\d{1,2})/\d{2,4}\b', text4)

for i in range(len(month)):
    if len(month[i]) == 1:
        month[i] = '0' + month[i]

# print("months:",month)

year = re.findall(r'\b\d{1,2}/\d{1,2}/(\d{2,4})\b', text4)

for i in range(len(year)):
    if len(year[i]) == 2:
        year[i] = '20' + year[i]

# print("years:",year)

pattern = r'\b\d{1,2}/\d{1,2}/\d{2,4}\b'
original = re.findall(pattern, text4)

for i in range(len(original)):
    iso = f"{year[i]}-{month[i]}-{days[i]}"
    text4 = text4.replace(original[i], iso, 1)

print("\n")
print(text4)


# 5. Split CSV line but ignore commas in quotes
# Task: Split the line
# '123,"Doe, John",35,"New York, NY"'
# into its four fields without splitting on the commas inside quotes.

# Expected output:
# ["123", "Doe, John", "35", "New York, NY"]

print("\n")
text5 = '123,"Doe, John",35,"New York, NY"'
text5 = re.sub(r'\b(\d+)\b', r'"\1"', text5)
text5 = re.sub(r',\s*', ', ', text5)
print(text5)

# 6. Extract URLs from HTML
# Task: From the HTML snippet ...
# <a href="http://site.com/page1">Link</a>
# <img src='https://cdn.site.com/img.png' alt=''>
# <a href=https://example.org>Example</a>
# ... extract all URLs (both in href and src), handling single, double, or no quotes.

# Expected output:
# ["http://site.com/page1", "https://cdn.site.com/img.png", "https://example.org"]

text6 = '''
<a href="http://site.com/page1">Link</a>
# <img src='https://cdn.site.com/img.png' alt=''>
# <a href=https://example.org>Example</a>

'''
print("\n")
print(re.findall(r'https?://[^"\'<>]+', text6))

# 7. Parse Apache-style log lines
# Task: Given a log line
# 127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache.gif HTTP/1.0" 200 2326
# extract the client IP, username, datetime, request method, path, protocol, status code, and response size into a tuple.

# Expected output:

# (
#   "127.0.0.1",
#   "frank",
#   "10/Oct/2000:13:55:36 -0700",
#   "GET",
#   "/apache.gif",
#   "HTTP/1.0",
#   "200",
#   "2326"
# )

print("\n")

text7 = '''127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache.gif HTTP/1.0" 200 2326'''
text77 = re.match(r'(\d{1,3}(?:\.\d{1,3}){3}) - (\S+) \[([^\]]+)\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+)', text7)
print(text77.groups())

# 8. Remove Python comments
# Task: Strip out both single-line (# ...) and inline (code # comment) comments from the code snippet

# x = 5  # initialize x
# # this is a full-line comment
# y = x * 2  # double
# leaving only the code.

# Expected output:
# "x = 5\ny = x * 2"

print("\n")
text8 = '''
x = 5  # initialize x
# this is a full-line comment
y = x * 2  # double
'''

print(re.sub(r'(?m)^[ \t]*#.*$|#.*$', '', text8).strip().replace('\n\n', '\n'))


print("\n")
