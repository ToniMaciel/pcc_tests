import subprocess, sys

def main():
    text_file = sys.argv[1]
    with open('./dataset/patterns_aproximado.txt', 'r') as f:
        lines = f.readlines()
        total = []
        total.append(['agrep','wu_manber', 'sellers'])
        for line in lines:
            line = line.replace('\n', "")
            if "*" not in line:
                for max_error in [2, 4, 5]:
                    lst = []
                    lst.append(max_error)
                    agrep = "/usr/bin/time -f \"%E\" agrep -" + str(max_error) + " -c \'" + line + "\' " + text_file
                    p = subprocess.run(agrep, capture_output=True, text=True, shell=True)
                    #Quando o grep não encontra um match, responderá com com um 'Command exited with non-zero status 1'
                    lst.append(p.stderr.replace("Command exited with non-zero status 1\n", "").replace('\n', ''))
                    for algo in ['wu_manber', 'sellers']:
                        pmt = "/usr/bin/time -f \"%E\" ./utils/pmt -a " + algo + " -e " + str(max_error) + " -c " + line + " " + text_file
                        p1 = subprocess.run(pmt, capture_output=True, text=True, shell=True)
                        lst.append(p1.stderr.replace('\n', ''))
                    total.append(lst)
            else:
                total.append(line.replace('*', ''))
    with open('desempenho_aproximado.txt', 'w') as f:
        for elemento in total:
            if len(elemento) < 3:
                f.write("Padrões de tamanho " + elemento + ": ")
            elif len(elemento) == 3:
                for n in elemento:
                    f.write(n + " ")
            else:
                f.write("Com erro máximo " + str(elemento[0]) + ": ")
                for n in range(1, 4):
                    f.write(elemento[n] + " ")
            f.write('\n')

if __name__ == '__main__':
    main()