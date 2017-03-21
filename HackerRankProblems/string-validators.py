def output(string):
    print string

def validate(string):

    if string.isalnum():
        print "True"
    else:
        print "False"

    for i in string:
        if i.isalpha():
            print "True"
            break
    else:
        print "False"

    for i in string:
        if i.isdigit():
            print "True"
            break
    else:
        print "False"

    for i in string:
        if i.islower():
            print "True"
            break
    else:
        print "False"

    for i in string:
        if i.isupper():
            print "True"
            break
    else:
        print "False"
        #output("True" if s.isalnum() else "False")
        #output("True" if s.isalpha() else "False")
        #output("True" if s.isdigit() else "False")
        #output("True" if s.islower() else "False")
        #output("True" if s.isupper() else "False")


if __name__ == '__main__':
    s = raw_input().strip()
    validate(s)
