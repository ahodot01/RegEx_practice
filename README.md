<h1 align="center">🐍 RegEx Practice in Python</h1>

<p align="center">
A collection of small Python exercises using the <b>re</b> module.  
Each task demonstrates a practical regex use case.
</p>

---

<h2>📌 Exercises</h2>

<ol>
  <li>
    <b>Extract numbers</b><br/>
    <code>"I have 2 apples, 15 bananas, and 1 orange."</code> → <code>["2", "15", "1"]</code>
  </li>
  <li>
    <b>Validate emails</b><br/>
    Keep only valid <code>username@domain.tld</code> (2–4 letter TLD).<br/>
    <code>["alice@example.com", "bob(at)example.com", "carol@example.co.uk", "dave@example"]</code> → <code>["alice@example.com", "carol@example.co.uk"]</code>
  </li>
  <li>
    <b>Normalize whitespace</b><br/>
    <code>"This   is a\t\ttest.\nNew   line!"</code> → <code>"This is a test. New line!"</code>
  </li>
  <li>
    <b>Reformat dates</b><br/>
    Convert <code>DD/MM/YYYY</code> or <code>D/M/YY</code> → ISO <code>YYYY-MM-DD</code>.<br/>
    <code>"01/02/2020, 23/11/1999, 5/6/21"</code> → <code>"2020-02-01, 1999-11-23, 2021-06-05"</code>
  </li>
  <li>
    <b>Split CSV line (ignore commas in quotes)</b><br/>
    <code>'123,"Doe, John",35,"New York, NY"'</code> → <code>["123", "Doe, John", "35", "New York, NY"]</code>
  </li>
  <li>
    <b>Extract URLs from HTML</b><br/>
    Finds <code>http/https</code> links in <code>href</code>/<code>src</code>.<br/>
    → <code>["http://site.com/page1", "https://cdn.site.com/img.png", "https://example.org"]</code>
  </li>
  <li>
    <b>Parse Apache log line</b><br/>
    Extracts tuple: <code>(IP, user, datetime, method, path, protocol, status, size)</code>
  </li>
  <li>
    <b>Remove Python comments</b><br/>
    <pre><code>x = 5  # init
# comment
y = x * 2
    </code></pre>
    → 
    <pre><code>x = 5
y = x * 2
    </code></pre>
  </li>
</ol>

(to be continued)

---

<h2>🚀 Run</h2>

```bash
python regex_practice.py
