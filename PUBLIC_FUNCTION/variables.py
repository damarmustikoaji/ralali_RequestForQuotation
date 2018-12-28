import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Variables:
    SERVER      = "https://www.ralali.com/permintaan-penawaran/form"
    BROWSER     = "Chrome"#Chrome or Firefox
    BROWSER_MODE= "-"#headless or mobile
    a           = id_generator()
    NAME        = "Nathasya Syahidah " + a
    EMAIL       = a + "@mailinator.com"
    COUNTRY     = "62"
    PHONE       = "895444877889"
