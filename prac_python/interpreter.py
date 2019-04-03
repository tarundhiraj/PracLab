def interpreter(code, tape):
    # Implement your interpreter here
    tape = [ int(x) for x in tape]
    try:
        pos = 0
        for sym in code:
            if sym == '>':
                pos += 1
                print(pos, tape)
                if pos >= len(tape):
                    raise IndexError
            elif sym == '<':
                pos -= 1
                print(pos, tape)
                if pos < 0:
                    raise IndexError
            elif sym == '*':
                tape[pos] = 1 - tape[pos]
                print(pos, tape)
            elif sym == '[':
                if tape[pos] == 0:
                    pos += 1
                    if pos >= len(tape):
                        raise IndexError
                    else:
                        pos = code[pos:].index(']')
                    print(pos, tape)
            elif sym == ']':
                if tape[pos] != 0:
                    pos = code[0:pos].index('[')
                else:
                    pos += 1
                print(pos, tape)
            else:
                print(pos, tape)
    except IndexError as e:
        print(e)

    return ''.join([str(x) for x in tape])

if __name__ == '__main__':
    print(interpreter(">*>*", "00101100"))
