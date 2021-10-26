#!/usr/bin/env python3
# -*- Mode: Python; coding: utf-8;

import pwquality
import sys

import gettext
# import locale
LOCALEDIR = "/usr/share/locale"
_ = gettext.gettext

domain = "libpwquality"
gettext.bindtextdomain(domain, LOCALEDIR)
gettext.textdomain(domain)
_ = gettext.gettext

pwsetting = pwquality.PWQSettings()
pwsetting.read_config()

def set_locales():
    # locale.setlocale(locale.LC_ALL, "")
    domain = "libpwquality"
    gettext.bindtextdomain(domain, LOCALEDIR)
    gettext.textdomain(domain)
    # gettext.install(domain, LOCALEDIR)
    # domain = 'libpwquality'
    # locale.bindtextdomain(domain, LOCALEDIR)
    # locale.textdomain(domain)
    # gettext.bindtextdomain(domain, LOCALEDIR)
    # gettext.textdomain(domain)


def read_config():
    print("pwquality settings:")
    print("minlen:", pwsetting.minlen)
    print("minclass:", pwsetting.minclass)
    print("dictcheck:", pwsetting.dictcheck)

def check_pass(passwd):
    try:
        pwsetting.check(passwd)
        return ("ok;")
    except pwquality.PWQError as e:
        return ("error;" +  _(e.args[1]))


