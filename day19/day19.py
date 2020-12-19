import sys

class Rule:
    def __init__(self, rule_str):
        rule_str = rule_str.strip()
        self.resolved_letter = None
        if rule_str in ('"a"', '"b"'):
            self.resolved_letter = rule_str.strip('"')
            return

        self.or_parts = []
        or_parts_str = rule_str.split('|')
        for ops in or_parts_str:
            ops.strip()
            ops = [int(i) for i in ops.split()]

            self.or_parts.append(ops)
        
        self.rule_refs = {}

    def print(self):
        s = ''
        for op in self.or_parts:
            for n in op:
                s += str(n) + ' '
            s += '| '
        print(s[:-1])

    def check_rule(self, string):
        # Return a set of possible matches and the chars they take
        if not string:
            return {}
        if self.resolved_letter:
            if string[0] == self.resolved_letter:
                return {1}
            else:
                return {}
        else:
            all_mls = set()
            for o in self.or_parts:
                match_lengths = {0}

                for n in o:
                    r = self.rule_refs[n]
                    new_match_lengths = set()
                    for pm in match_lengths:
                        sub_mls = r.check_rule(string[pm:])
                        if sub_mls:
                            for s in sub_mls:
                                new_match_lengths.add(pm + s)
                    match_lengths = new_match_lengths
                all_mls = all_mls.union(match_lengths)
            return all_mls

    def add_needed_rules(self, rules):
        if self.resolved_letter:
            return
        for o in self.or_parts:
            for n in o:
                self.rule_refs[n] = rules[n]

ans = 0
rules_dict = {}
section = 0
for line in sys.stdin:
    line = line.rstrip('\n')
    if not line:
        section += 1
        for r in rules_dict:
            rules_dict[r].add_needed_rules(rules_dict)
        continue

    if section == 0:
        rule_no, rule_str = line.split(':')
        rules_dict[int(rule_no)] = Rule(rule_str)
    if section == 1:
        rule = rules_dict[0]
        if len(line) in rule.check_rule(line):
            ans += 1
        pass

print(ans)
