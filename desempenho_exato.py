import subprocess, sys

def main():
    pattern_file = sys.argv[1]
    text_file = sys.argv[2]
    with open(pattern_file, 'r') as f:
        lines = f.readlines()
        total = []
        total.append(['grep','sliding_window', 'kmp', 'aho_corasick', 'shift_or'])
        for line in lines:
            line = line.replace('\n', "")
            if "*" not in line:
                lst = []
                grep = "/usr/bin/time -f \"%E\" grep -c -o '" + line + "' " + text_file
                p = subprocess.run(grep, capture_output=True, text=True, shell=True)
                #Quando o grep não encontra um match, responderá com com um 'Command exited with non-zero status 1'
                lst.append(p.stderr.replace("Command exited with non-zero status 1\n", "").replace('\n', ''))
                for algo in ['sliding_window', 'kmp', 'aho_corasick', 'shift_or']:
                    if(len(line) > 64 and algo == 'shift_or'):
                            lst.append("inf")
                            continue
                    pmt = "/usr/bin/time -f \"%E\" ./utils/pmt -a " + algo + " -c " + line + " " + text_file
                    p1 = subprocess.run(pmt, capture_output=True, text=True, shell=True)
                    lst.append(p1.stderr.replace('\n', ''))
                total.append(lst)
            else:
                total.append(line.replace('*', ''))
    
    with open('desempenho_exato.txt', 'w') as f:
        for elemento in total:
            if len(elemento) < 5:
                f.write("Padrões de tamanho " + elemento + ": ")
            else:
                for n in elemento:
                    f.write(n + " ")
            f.write('\n')

if __name__ == '__main__':
    main()