import sys

# Originally solved by Wolfram Alpha by pasting the following:
# -t mod 23 = 0, -t mod 41 = 13, -t mod 733 = 23, -t mod 13 = 10, -t mod 17 = 3, -t mod 19 = 4, -t mod 29 = 23, -t mod 449 = 54, -t mod 37 = 17 

earliest_time = int(sys.stdin.readline().rstrip('\n'))
id_strings = sys.stdin.readline().rstrip('\n').split(',')
operational_ids = []
targets = []
for i, ids in enumerate(id_strings):
    if ids != 'x':
        operational_ids.append(int(ids))
        targets.append(i % int(ids))

def bezout_coeff(a, b):
    prev_r = a
    r = b
    prev_s = 1
    s = 0
    prev_t = 0
    t = 1
    while r != 0:
        q = prev_r // r
        prev_r, r = (r, prev_r - q * r)
        prev_s, s = (s, prev_s - q * s)
        prev_t, t = (t, prev_t - q * t)

    return (prev_s, prev_t)

N = 1 # cumulative product of modulos.
x = 0 # as in "x mod N"
for t, id in zip(targets, operational_ids):
    bi1, bi2 = bezout_coeff(N, id)
    x = x * bi2 * id + (-t) * bi1 * N
    N *= id
    x = x % N

print(x)
