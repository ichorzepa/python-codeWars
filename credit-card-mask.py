# https://www.codewars.com/kata/5412509bd436bd33920011bc
# 7 kyu
# return masked string
def maskify(cc):
    m_cc = list(cc)
    for i in range(0,len(m_cc)-4):
        m_cc[i] = '#'
    return ''.join(m_cc)

cc = "4556364607935616"
cc2 = "45"

print(maskify(cc))
print(maskify(cc2))