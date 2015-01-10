import re

def controllaData(data):

    # lettere nella data?
    if re.match("^[\w]*$", data):
        return False

    # barre in posto giusto?
    if data[2] != '/' or data[5] != '/':
        return False

    return True


# =========

data = "32/12/15"

if int(data[0:1]) > 31:
    print "Error"