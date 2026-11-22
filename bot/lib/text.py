import random

unicode_chr = [chr(c) for c in range(0x0300, 0x0370)]

def make_zalgo(text, intensity):
        zalgoed_text = []
        
        for i in text:
            zalgoed_text.append(i)
            zalgoed_text.append("".join(random.choices(unicode_chr, k=random.randint(1, intensity))))
        
        return "".join(zalgoed_text) 