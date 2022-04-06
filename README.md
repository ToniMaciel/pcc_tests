# Scripts para experimentos do projeto

Aqui disponibilizamos os scripts para reprodução dos experimentos detalhados no relatório do primeiro projeto da disciplina de processamento de cadeias de caracteres, de forma que aqui estarão as isntruções para executar os experimentos, os detalhes de como eles funcionam estarão no relatório mencionado.

No seguinte [link](http://pizzachili.dcc.uchile.cl/texts/nlang/) é possível encontrar os arquivos usados nos quais realizamos as buscas dos padrões.

---

## Aviso

Um necessário adendo é que a rodagem dos scripts pode tomar algum tempo. Tendo isso em vista, optamos por construir um dataset reduzido e um completo. Para os resultados mostrados no relatório, os dataset usados foram os completos, mas dentro do script estão sinalizados os dataset reduzidos, para proporcionar mais rapidez na execução.

Caso deseje realizar a troca para o dataset completo (ou criar uma adaptação à sua preferência, apenas se atentando ao estilo de escrita dos dataset) é possível fazer a troca seguindo o exemplo a seguir:

Suponha que você vá mudar o dataset do script **corretude_aproximado.py**, então você deve ir até o arquivo e modificar todas as ocorrências de **patterns_aproximados.txt** para **patterns_aproximados_full.txt**.

De forma semelhante pode ser possível mudar o dataset de cada script de acordo com as adaptações necessárias.

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
  python3 clean_text.py <nome_do_arquivo>
  ```
---

## Experimentos de corretude

Para executar os testes para os alogritmos de match exato:
```bash
  python3 corretude_exato.py <nome_do_arquivo>
  ```

Já para os algortimos de match aproximado:
```bash
  python3 corretude_aproximado.py <nome_do_arquivo>
  ```
 
Ao final de cada execução, haverá uma sinalização para cada erro de corretude encontrado na nossa ferramenta. Se nenhum output for sinalizado, então não houve nenhum tipo de erro detectado.

---

## Experimentos de desempenho

Para executar o experimento de desempenho para os alogritmos de match exato:
```bash
  python3 desempenho_exato.py <nome_do_arquivo>
  ```

Para o experimento de desempenho dos algortimos de match aproximado:
```bash
  python3 desempenho_aproximado.py <nome_do_arquivo>
  ```

Para o experimento de desempenho dos algortimos match exato com múltiplos padrões:
```bash
  python3 desempenho_multiplos.py <nome_do_arquivo>
  ```
Para cada uma dessas execuções, será produzido um txt (de mesmo nome que o script executado) que vai detalhar o tempo necessário para cada tamanho de padrão ou quantidade de padrões, no caso de múltiplos padrões. Na primeira linha de cada outpút produzido está a ordem na qual os algoritmos foram executados, e portanto,
todos os resultados daquela coluna dizem respeito a execução daquele algoritmo.

Infelizmente, por limitações de tempo, não conseguimos refinar os resultados de forma automatizada, de modo esses são expostos de forma bruta. Uma visão detalhada
desses resultados pode ser encontrada no relatório do projeto, onde nós compilamos e trabalhamos melhor o significado de cada execução. Reconhecemos essa limitação e sentimos muito que a reprodução do experimento não acontecerá da forma facilitada como desejávamos.
