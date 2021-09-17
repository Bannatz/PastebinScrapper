class format:
    
    def combo(combo):
        s = combo
        if " " in s:
            s = s.split(" ")
            for i in s:
                if ":" in i and "@" in i:
                    s = i
                    s = "".join(s)
        return str(s)
