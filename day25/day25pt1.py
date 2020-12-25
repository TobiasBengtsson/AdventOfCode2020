import sys

INITIAL_VALUE = 1
PUBLIC_KEY_SUBJECT_NUMBER = 7
LOOP_MODULO = 20201227

card_pk = int(sys.stdin.readline().rstrip('\n'))
door_pk = int(sys.stdin.readline().rstrip('\n'))

def perform_loop(s_n, val):
    val *= s_n
    val = val % LOOP_MODULO
    return val

def find_loop_size(pk):
    s_n = PUBLIC_KEY_SUBJECT_NUMBER
    val = INITIAL_VALUE
    loops = 0
    while val != pk:
        val = perform_loop(s_n, val)
        loops += 1
    return loops

def transform(pk, loop_size):
    s_n = pk
    val = INITIAL_VALUE
    for _ in range(loop_size):
        val = perform_loop(s_n, val)
    return val

card_loop_size = find_loop_size(card_pk)
door_loop_size = find_loop_size(door_pk)
card_key = transform(door_pk, card_loop_size)
door_key = transform(card_pk, door_loop_size)
assert card_key == door_key
print(card_key)
