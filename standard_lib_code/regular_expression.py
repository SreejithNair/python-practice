import re

pattern='this'

text = 'Does this text contain this pattern somewhere?'

match= re.search(pattern,text)

print(f'Pattern:{match.re.pattern}, Text:{match.string}, to:{match.start()}, to:{match.end()} ')