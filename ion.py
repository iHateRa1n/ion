import os, sys, subprocess, time
def hio():
    try:
        io(open('.tmp', 'r').read())
    except:
        print('error.')
def io(file):
    x = open(file, 'r').read().split('\n')
    for item in x:
        print(ion(item))
def partition(alist, indices):
    return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]
def ion(c):
    cc = c.split('  ')
    for item in cc:
        if item == '||':
            if cc[cc.index(item) - 1] == 'print':
                tmp = cc[cc.index(item) + 1]
                exec('print(' + tmp + ')')
                return ''
        elif item == '~':
            if cc[cc.index(item) - 1] == '+':
                tmp = cc[cc.index(item) + 1]
                tmp = tmp.split(', ')
                x = 0
                for item in tmp:
                    x = x + int(item)
                return float(tmp[0]) + float(tmp[1])
            elif cc[cc.index(item) - 1] == 'exec':
                return subprocess.getoutput(cc[cc.index(item) + 1])
            elif cc[cc.index(item) - 1] == '-':
                tmp = cc[cc.index(item) + 1]
                tmp = tmp.split(', ')
                x = float(tmp[0])
                for item in tmp:
                    x = x - int(item)
                return x
                return float(tmp[0]) - float(tmp[1])
            elif cc[cc.index(item) - 1] == '/':
                tmp = cc[cc.index(item) + 1]
                tmp = tmp.split(', ')
                x = float(tmp[0])
                for item in tmp:
                    x = x / int(item)
                return float(tmp[0]) / float(tmp[1])
            elif cc[cc.index(item) - 1] == '*':
                tmp = cc[cc.index(item) + 1]
                tmp = tmp.split(', ')
                x = float(tmp[0])
                for item in tmp:
                    x = x * int(item)
                return float(tmp[0]) * float(tmp[1])
            elif cc[cc.index(item) - 1] == 'if':
                args = cc[cc.index(item) + 1:]
                try:
                    if eval(args[0]) == args[1]:
                        exec('ion("' + eval('  '.join(args[2:])) + '")')
                except:
                    pass
                return ''
            elif cc[cc.index(item) - 1] == 'in':
                args = cc[cc.index(item) + 1]
                x = input(args)
                return x
            else:
                return ''.join(list(c)[:-3])
        elif item == '=':
            tmp = ion('  '.join(cc[cc.index(item) + 1:]) + '  ~')
            exec('global ' + cc[cc.index(item) - 1] + '; ' + cc[cc.index(item) - 1] + ' = tmp')
            vars()
            return ''
