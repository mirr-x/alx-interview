#!/usr/bin/python3
""" test a valid utf-8 """


def validUTF8(data):
    """ function that valid a utf-8 encoding """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8")
        return True
    except Exception:
        return False
