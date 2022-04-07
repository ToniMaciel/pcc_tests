import subprocess, sys

def main():
    pattern_file = sys.argv[1]
    text_file = sys.argv[2]
    with open(pattern_file, 'r') as f:
        lines = f.readlines()
        errors = []
        for line in lines:
            line = line.replace('\n', "")
            if "*" not in line:
                for max_error in [2, 4]:
                    for algo in ['sellers', 'wu_manber']:
                        if(len(line) > 64 and algo == 'wu_manber'):
                            continue
                        ground_truth = "python3 ./utils/" + algo + ".py \"" + line + "\" " + text_file + " " + str(max_error)
                        p = subprocess.run(ground_truth, capture_output=True, text=True, shell=True)
                        pmt = "./utils/pmt -a " + algo + " -e " + str(max_error) + " -c " + line + " " + text_file
                        p1 = subprocess.run(pmt, capture_output=True, text=True, shell=True)
                        if p.stdout != p1.stdout:
                            errors.append([algo, line, p.stdout.replace('\n', ''), p1.stdout.replace('\n', ''), str(max_error)])
    
    if len(errors) == 0:
        print("Nenhum erro de corretude foi encontrado")
    else:
        print("Os seguintes erros foram achados:")
        for error in errors:
            print("No seguinte padrão", error[1], "com erro máximo de", error[4], "o algoritmo", error[0], "produziu", error[3], "quando o esperado era", error[2])

if __name__ == '__main__':
    main()