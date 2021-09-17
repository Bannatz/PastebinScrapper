class format:
    
    def combo(combo):
        s = combo.replace(";", ":")
        s = combo.replace("\n", "")
        s = s.split(" ")
        for i in s:
            if ":" in i and "@" in i:
                s = i
        return s
