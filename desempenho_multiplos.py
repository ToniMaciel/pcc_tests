import subprocess, sys

def main():
    text_file = sys.argv[1]
    with open('./dataset/patterns_multi.txt', 'r') as f:
        total = []
        total.append(['grep', 'sliding_window', 'kmp', 'aho_corasick', 'shift_or'])
        lines = f.readlines()
        for line in lines:
            line = line.replace('\n', "")
            if "*" not in line:
                lst = []
                patterns = line.split(' ')
                pattern_flag = ""
                with open('p.txt', 'w') as f1:
                    for pattern in patterns:
                        pattern_flag += " -e " + pattern
                        f1.write(pattern + '\n')
                grep = "/usr/bin/time -f \"%E\" grep -c -o " + pattern_flag + " " + text_file
                p = subprocess.run(grep, capture_output=True, text=True, shell=True)
                #Quando o grep não encontra um match, responderá com com um 'Command exited with non-zero status 1'
                lst.append(p.stderr.replace("Command exited with non-zero status 1\n", "").replace('\n', ''))
                for algo in ['sliding_window', 'kmp', 'aho_corasick', 'shift_or']:
                    pmt = "/usr/bin/time -f \"%E\" ./utils/pmt -p p.txt -a " + algo + " -c " + text_file
                    p1 = subprocess.run(pmt, capture_output=True, text=True, shell=True)
                    lst.append(p1.stderr.replace('\n', ''))
                total.append(lst)
            else:
                total.append(line.replace('*', ''))
    
    with open('desempenho_multiplos.txt', 'w') as f:
        for elemento in total:
            if len(elemento) < 5:
                f.write("Total de padrões " + elemento + ": ")
            else:
                for n in elemento:
                    f.write(n + " ")
            f.write('\n')
    
if __name__ == '__main__':
    main()