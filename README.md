🐍 Regex Practice in Python
A collection of small Python exercises using the re module. Each task demonstrates a practical regex use case.

📌 Exercises
Extract numbers
"I have 2 apples, 15 bananas, and 1 orange." → ["2", "15", "1"]

Validate emails
Keep only valid username@domain.tld (2–4 letter TLD).
["alice@example.com", "bob(at)example.com", "carol@example.co.uk", "dave@example"] → ["alice@example.com", "carol@example.co.uk"]

Normalize whitespace
"This is a\t\ttest.\nNew line!" → "This is a test. New line!"

Reformat dates
Convert DD/MM/YYYY or D/M/YY → ISO YYYY-MM-DD.
"01/02/2020, 23/11/1999, 5/6/21" → "2020-02-01, 1999-11-23, 2021-06-05"

Split CSV line (ignore commas in quotes)
'123,"Doe, John",35,"New York, NY"' → ["123", "Doe, John", "35", "New York, NY"]

Extract URLs from HTML
Finds http/https links in href/src.
→ ["http://site.com/page1", "https://cdn.site.com/img.png", "https://example.org"]

Parse Apache log line
Extracts (IP, user, datetime, method, path, protocol, status, size).

Remove Python comments

x = 5  # init
# comment
y = x * 2

→

x = 5
y = x * 2

(to be continued)

🚀 Run
python regex_practice.py

🎯 Purpose
For regex practice in Python with clear, practical examples. Will be updated upon completion of new tasks.
