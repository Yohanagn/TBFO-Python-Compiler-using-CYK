from os.path import isfile as isExist
import lexer
import lexer_rules
import cyk

isBlockComment = False
isSkipUntilNextBC = False
isDef = False
isAccepted = True
isIfLevel = []
level = 0

print('>>> PYTHON PARSER 1.0')
print('>>> created by Keep Smile Group K01')
print('>>> Bandung Institute of Technology, 2021.')
print('Diky Restu Maulana\t\t13520017')
print('Hana Fathiyah\t\t\t13520047')
print('Yohana Golkaria Nainggolan\t13520053\n')

inputfile = input('Insert file name (.txt or .py): ')
grammarfile = input('Insert grammar file name: ')
if isExist(inputfile) and isExist(grammarfile):
    lx = lexer.Lexer(lexer_rules.rules, skip_whitespace=True)
    CYK = cyk.Parser(grammarfile)
    with open(inputfile, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        lexered = ''
        lx.input(line)
        try:
            for tok in lx.tokens():
                lexered += f'{tok!r}'
        except lexer.LexerError as err:
            print(f'LexerError at position {err.pos}')

        if "BBCOMMENT" in lexered:
            lexered = lexered.replace("BBCOMMENT ","")
        if "BCOMMENT" in lexered:
            if not isSkipUntilNextBC:
                isBlockComment = True
                posBC = lexered.find("BCOMMENT")
                if posBC == 0:
                    lexered = ''
                else:
                    lexered = lexered[:posBC:]
            else:
                isSkipUntilNextBC = False
                posBC = lexered.find("BCOMMENT")
                lexered = lexered[posBC+9::]

        if isSkipUntilNextBC:
            continue
        if "COMMENT" in lexered:
            lexered = lexered.replace("COMMENT ","")
        if "DEF" in lexered:
            level+=1
            isDef = True
        
        if ("ELIF" or "ELSE") in lexered:
            if level not in isIfLevel:
                isAccepted = False
                break
            elif "ELSE" in lexered:
                isIfLevel.remove(level)
                level-=1
        elif "IF" in lexered:
            level+=1
            isIfLevel.append(level)

        CYK(lexered,parse=True)
        isAccepted = CYK.print_tree(output=False)
        if not isAccepted:
            break
        if isBlockComment:
            isSkipUntilNextBC = True
            isBlockComment = False
    print("\nResult:", end = " ")
    if isAccepted:
        print("Accepted")
    else:
        print(f"\nSyntax Error at line {i+1}:")
        print(f"    >>> {line.strip()}\n")
        print(f"Readed: {lexered}")
else:
    print("There's no such file in directory!")