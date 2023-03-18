import re

# 递归下降解析器
class Parser:
    def __init__(self, s):
        self.tokens = re.findall(r"\(\d+\)|\(|\)|AND|OR|\b[A-Z]{2,4}\d{4}[A-Z]?\b", s)
        self.pos = 0

    def parse(self):
        return self.parse_impl()

    def parse_impl(self):
        if self.tokens[self.pos] == "(":
            self.pos += 1
            node = self.parse_impl()
            self.pos += 1
            return node
        elif self.tokens[self.pos] == ")":
            return None
        elif re.match(r'\(\d+\)',self.tokens[self.pos]):
            num = int(re.findall(r'\d+',self.tokens[self.pos])[0])
            self.pos += 1
            if num == 1:
                orlist = []
                while re.match(r'\b[A-Z]{2,4}\d{4}[A-Z]?\b',self.tokens[self.pos]):
                    orlist.append(self.tokens[self.pos])
                    self.pos += 1
                return {"or":orlist}
            else :
                andlist = []
                while re.match(r'\b[A-Z]{2,4}\d{4}[A-Z]?\b',self.tokens[self.pos]):
                    andlist.append(self.tokens[self.pos])
                    self.pos += 1
                return {"and":andlist}
        elif self.tokens[self.pos] == "AND":
            self.pos += 1
            node1 = self.parse_impl()
            self.pos += 1
            node2 = self.parse_impl()
            return {"and": [node1, node2]}
        elif self.tokens[self.pos] == "OR":
            self.pos += 1
            node1 = self.parse_impl()
            self.pos += 1
            node2 = self.parse_impl()
            return {"or": [node1, node2]}
        else:
            token = self.tokens[self.pos]
            self.pos += 1
            return [token]



# 解析prerequisiteRule
prerequisite_rule = "PROGRAM_TYPES IF_IN Undergraduate Degree\nTHEN\n(\n\tCOURSES (1) YSC2232:D,MA2001:D,MA1101R:D,MA1311:D,MA1508E:D,MA1513:D\n\tAND\n\tCOURSES (1) ST1131:D,ST1131A:D,ST1232:D,ST2131:D,MA2116:D,MA2216:D,EE2012A:D,EE2012:D,ST2334:D,YSC2243:D\n\tAND\n\t(\n\t\tCOURSES (1) CS2020:D,CS1020:D,CS1020E:D\n\t\tOR\n\t\t(\n\t\t\tCOURSES (1) CS2030:D,CS2030S:D,CS2113:D,CS2113T:D\n\t\t\tAND\n\t\t\tCOURSES (1) YSC2229:D,CS2040:D,CS2040S:D,CS2040C:D\n\t\t)\n\t)\n\tAND\n\t(\n\t\t(\n\t\t\tCOURSES (1) MA1505:D,MA1507:D,MA1102R:D,YSC1216:D,MA2002:D,MA1521:D\n\t\t)\n\t\tOR\n\t\t(\n\t\t\tCOURSES (2) MA1511:D,MA1512:D\n\t\t)\n\t)\n)"
prerequisite_rule = re.sub(r"\s+", " ", prerequisite_rule)  # 去除多余空格

tree = Parser(prerequisite_rule)
print(tree.tokens)
#tree.parse()
