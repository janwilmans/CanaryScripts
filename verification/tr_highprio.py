#!/usr/bin/env python3
""" re-prioritize rules that have less then 5 issues to top-priority
"""

import traceback, sys, os
from util import *

def read():
    results = []
    for line in sys.stdin:
        results += [readIssuesParts(line)]
    return results

def countRules(lines):
    results = {}
    for parts in lines:
        rule = parts[Column.Rule]
        if rule in results:
            results[rule] = results[rule] + 1
        else:
            results[rule] = 1
    return results


def show_usage():
    eprint("Usage: <input> | " + os.path.basename(__file__))
    eprint("   re-prioritize rules that have less then 5 issues to top-priority")


def main():
    if len(sys.argv) != 1:
        eprint("error: invalid argument(s)\n")
        show_usage()
        sys.exit(1)

    lines = read()
    rules = countRules(lines)
    ruleSet = set()
    for rule in rules:
        count = rules[rule]
        if count <= 5:
            ruleSet.add(rule)

    for line in lines:
        rule = line[Column.Rule]
        if rule in ruleSet:
            line[Column.Prio] = "10"
        reportList(line)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except:
        info = traceback.format_exc()
        eprint(info)
        show_usage()
        sys.exit(1)
