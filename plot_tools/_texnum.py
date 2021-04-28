

def texnum(x, mfmt='{}', show_one=True):
    m, e = "{:e}".format(x).split('e')
    m, e = float(m), int(e)
    mx = mfmt.format(m)
    if float(mx) >= 10.0:
        m /= 10
        e += 1
        mx = mfmt.format(m)
    if e == 0:
        if m == 1:
            return "1" if show_one else ""
        return mx
    ex = r"10^{{{}}}".format(e)
    if m == 1:
        return ex
    return r"{}\;{}".format(mx, ex)
