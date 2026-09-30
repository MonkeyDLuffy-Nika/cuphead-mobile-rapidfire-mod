import re
import json

with open('extracted/assets/www/data.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Let's search for "t18" and "t481" in the events section of data.js
# The events section usually comes after the layouts.
# Let's find occurrences of '"t18"' and '"t481"'
print('Occurrences of "t18":')
for m in re.finditer(r'"t18"', content):
    pos = m.start()
    start = max(0, pos - 150)
    end = min(len(content), pos + 150)
    print(f'-- offset {pos} --')
    print(content[start:end])

print('\nOccurrences of "t481":')
for m in re.finditer(r'"t481"', content):
    pos = m.start()
    start = max(0, pos - 150)
    end = min(len(content), pos + 150)
    print(f'-- offset {pos} --')
    print(content[start:end])
