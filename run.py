#!/usr/bin/env python

from insights import rule, make_response, run
from insights.parsers.installed_rpms import InstalledRpm, InstalledRpms


@rule(InstalledRpms)
def bash_installed(rpms):
    rpm = rpms.get_max("bash")
    if rpm:
        return make_response("BASH_INSTALLED", version=rpm.nvr)
    return make_response("BASH_NOT_INSTALLED")


LOWER = InstalledRpm.from_package("bash-4.4.16-1.el7")
UPPER = InstalledRpm.from_package("bash-4.4.22-1.el7")


@rule(InstalledRpms)
def bash_affected(rpms):
    rpm = rpms.get_max("bash")
    if rpm and rpm >= LOWER and rpm < UPPER:
        return make_response("BASH_AFFECTED", version=rpm.nvr)
    elif rpm:
        return make_response("BASH_UNAFFECTED", version=rpm.nvr)
    else:
        return make_response("NO_BASH")


if __name__ == "__main__":
    from sys import argv

    RULE_NAMES = ["bash_installed", "bash_affected"]

    if len(argv) < 2:
        print("Pass a rule name as an argument. Valid rules: {}".format(RULE_NAMES))
        exit(1)

    rule_name = argv[1]

    if rule_name not in RULE_NAMES:
        print("{} is not a valid rule name. Valid rules: {}". format(rule_name, RULE_NAMES))
        exit(2)

    rule_func = globals()[rule_name]
    result = run(rule_func)
    print(result[rule_func])
