import os, sys, subprocess, time
fs = {}
def hio():
    try:
        io(open('.tmp', 'r').read())
    except:
        print('error.')
def io(file):
    x = open(file, 'r').read().split('\n')
    for item in x:
        ion(item)
def partition(alist, indices):
    return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]
def ion(c):
    cc = c.split('  ')
    for item in cc:
        if item == '||':
            if cc[cc.index(item) - 1] == 'print':
                tmp = cc[cc.index(item) + 1:]
                exec('print(' + ''.join(tmp) + ')')
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
                    if eval(args[0]) == eval(args[1]):
                        exec('ion("' + eval('  '.join(args[2:])) + '")')
                except:
                    pass
                return ''
            elif cc[cc.index(item) - 1] == 'in':
                args = cc[cc.index(item) + 1]
                x = input(args)
                return x
            elif cc[cc.index(item) - 1] == 'exio':
                args = cc[cc.index(item) + 1:]
                try:
                    exec('ion("' + eval('  '.join(args[0:])) + '")')
                except:
                    pass
            elif cc[cc.index(item) - 1] == 'define':
                args = cc[cc.index(item) + 1:]
                fs[args[0]] = '  '.join(args[1:])
            else:
                if c.split('  ')[0] in fs:
                    return ion(eval(fs[c.split('  ')[0]]))
                else:
                    return ''.join(list(c)[:-3])
        elif item == '=':
            tmp = ion('  '.join(cc[cc.index(item) + 1:]) + '  ~')
            exec('global ' + cc[cc.index(item) - 1] + '; ' + cc[cc.index(item) - 1] + ' = tmp')
            vars()
            return ''
