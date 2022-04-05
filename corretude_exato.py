import subprocess, sys

def main():
    text_file = sys.argv[1]
    with open('./dataset/patterns_exato.txt', 'r') as f:
        lines = f.readlines()
        errors = []
        for line in lines:
            line = line.replace('\n', "")
            if "*" not in line:
                grep = "grep -o \'" + line + "\' " + text_file + " | wc -l"
                p = subprocess.run(grep, capture_output=True, text=True, shell=True)
                for algo in ['sliding_window', 'kmp', 'aho_corasick', 'shift_or']:
                    pmt = "./utils/pmt -a " + algo + " -c " + line + " " + text_file
                    p1 = subprocess.run(pmt, capture_output=True, text=True, shell=True)
                    if p.stdout != p1.stdout:
                        errors.append([algo, line, p.stdout.replace('\n', ''), p1.stdout.replace('\n', '')])
    
    if len(errors) == 0:
        print("Nenhum erro de corretude foi encontrado")
    else:
        print("Os seguintes erros foram achados:")
        for error in errors:
            print("No seguinte padrão", error[1], "o algoritmo", error[0], "produziu", error[3], "quando o esperado era", error[2])

if __name__ == '__main__':
    main()