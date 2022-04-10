import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('##### (.*)', i) is not None:
            i = '<h5>' + i[6:] + '</h5>'
        elif re.match('#### (.*)', i) is not None:
            i = '<h4>' + i[5:] + '</h4>'
        elif re.match('### (.*)', i) is not None:
            i = '<h3>' + i[4:] + '</h3>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list: