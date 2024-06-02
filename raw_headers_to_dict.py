r = dict()
raw = open('raw_http_headers')
lines = dict(list(map(lambda e: [e[0].strip(' '), e[1].strip(' ')], map(lambda e : e.strip('\n').split(':', 1),raw.readlines()))))
print(lines)
