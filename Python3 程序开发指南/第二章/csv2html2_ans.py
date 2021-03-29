'''
@File    :   csv2html2_ans.py
@Time    :   2021/03/29 10:47:20
@Author  :   mike.wu 
@Version :   0.99
@Contact :   xcwu@whu.edu.cn
'''

#Description: P85 练习题4
import sys 

def main():
    maxwidth, formats = process_options()
    print_start()
    count = 0 
    while True: 
        try:
            line = input()
            if count == 0: 
                color = "lightgreen"
            elif count % 2: 
                color = "white"
            else: 
                color = "lightyellow"
            print_line(line, color, maxwidth, formats)
            count += 1 
        except EOFError:
            break
    print_end()

def print_start():
    print("<table border='1'>")

def print_end():
    print("</table>")

def print_line(line, color, maxwidth, formats):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields: 
        if not field: 
            print("<td></td>")
        else:
            number = field.replace(",","")
            try: 
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(round(x), formats))
            except ValueError:
                field = field.title()
                field = field.replace("And", "and")
                if len(field) <= maxwidth: 
                    field = escape_html(field)
                else: 
                    field = "{0} ...".format(escape_html(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")

def extract_fields(line):
    fields = []
    field = ""
    quote = None 
    for c in line: 
        if c in "\"":
            if quote is None: 
                quote = c 
            elif quote == c:
                quote = None 
            else:
                field += c 
            continue 
        if quote is None and c == ",": 
            fields.append(field)
            field = ""
        else: 
            field += c 
    if field: 
        fields.append(field)
    return fields 


def escape_html(text):
    text = text.replace("&", "&amp")
    text = text.replace("<", "&lt")
    text = text.replace(">", "&gt")
    return text

def process_options():
    maxwidth = 100
    formats = ".0f"
    for arg in sys.argv:
        if '-h' in arg or '--help' in arg:
            print('''
    usage:
    csv2html.py [maxwidth=int][format=str] <infile.csv >outfile.html

    maxwidth is an option integer; if specifiled, it sets the maximum 
    number of characters that can be output for string fields, 
    otherwise a default of 100 is used.

    format is the format to use for numbers; if not specified it 
    defaluts to ".0".
    ''')
            sys.exit(0)
    for arg in sys.argv:
        if '-h' in arg or '--help' in arg:
            print('''
            usage:
            csv2html.py [maxwidth=int][format=str] <infile.csv >outfile.html

            maxwidth is an option integer; if specifiled, it sets the maximum 
            number of characters that can be output for string fields, 
            otherwise a default of 100 is used.

            format is the format to use for numbers; if not specified it 
            defaluts to ".0".
            ''')
        if arg.startswith("maxwidth"):
            maxwidth = int(arg.split('=')[1])
        if arg.startswith("formats"):
            formats = str(arg.split('=')[1])
    return maxwidth, formats

if __name__ == "__main__":
    main()