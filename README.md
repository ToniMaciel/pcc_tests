# Scripts para experimentos do projeto

Aqui disponibilizamos os scripts para reprodução dos experimentos detalhados no relatório do primeiro projeto da disciplina de processamento de cadeias de caracteres, de forma que aqui estarão as isntruções para executar os experimentos, os detalhes de como eles funcionam estarão no relatório mencionado.

No seguinte [link](http://pizzachili.dcc.uchile.cl/texts/nlang/) é possível encontrar os arquivos usados nos quais realizamos as buscas dos padrões.

---

## Ajustes no texto

Os textos possuem alguns caracteres fora do limite ASCII, de modo que foi necessário o uso de um script que eliminará cada linha que possui esses caracteres. Não processar esse texto, levará a respostas distintas em relação à corretude, visto que ferramentas cocmo grep não irão contabilizar matchs do padrão em linhas que possuem caracteres fora do ASCII.

Dessa forma, para os ajustes no texto, siga os seguintes passos:

1. Baixe o texto que você deseja analizar e coloque-o nesse repositório.
2. Em seguida, execute o seguinte comando para descompactar o arquivo: 
```bash 
  gzip -d <nome_do_arquivo> 
  ```
3. Para ajustar o texto conforme discutido, execute o seguinte script:
```bash
  python3 <nome_script>.py <nome_do_arquivo>
  ```
---

## Experimentos de corretude

Para executar os testes para os alogritmos de match exato:
```bash
  python3 <nome_script>.py <nome_do_arquivo>
  ```

Já para os algortimos de match aproximado:
```bash
  python3 <nome_script>.py <nome_do_arquivo>
  ```
 
Ao final de cada execução, haverá uma sinalização para cada erro de corretude encontrado na nossa ferramenta. Se nenhum output for sinalizado, então não houve nenhum tipo de erro detectado.

---

## Experimentos de desempenho

Para executar o experimento de desempenho para os alogritmos de match exato:
```bash
  python3 <nome_script>.py <nome_do_arquivo>
  ```

Para o experimento de desempenho dos algortimos de match aproximado:
```bash
  python3 <nome_script>.py <nome_do_arquivo>
  ```

Para o experimento de desempenho dos algortimos match exato com múltiplos padrões:
```bash
  python3 <nome_script>.py <nome_do_arquivo>
  ```
Para cada uma dessas execuções, será produzido um txt que vai detalhar o tempo necessário para cada tamanho de padrão ou quantidade de padrões para o caso de múltiplos padrões. Infelizmente, por limitações de tempo, os dados são expostos de forma bruta, de modo que só são apresentados de forma compilada no relatório da disciplina, Reconhecemos essa limitação e sentimos muito que a reprodução do experimento não acontecerá da forma facilitada como desejávamos.
