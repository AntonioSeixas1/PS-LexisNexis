# PS-LexisNexis

Repositório para solução das tarefas referente ao processo seletivo da Lexis Nexis - Risk solutions

## Arquivos utilizados
- precoMedicamentos.csv
- output.csv

## Executando o código

Vá o diretório e firstTask e execute no terminal o comando "python main.py"

O programa irá pedir que insira qual resposta de qual item se deseja visualizar sendo:
- Item 1: O nome dos campos do arquivo
- Item 2: O produto com o maior preço de fábrica sem impostos
- Item 3: Quais os possíveis tipos de produto
- Item 4: O produto e preço do genérico mais barato
- Item 5: Qual o valor total (soma) dos preços finais sem imposto(novo arquivo)
- Item 6: Quantos tipos diferentes de produtos estão presentes?(novo arquivo)
- Item 7: Existe algum produto que possua a mesma “substância” de um outro produto do arquivo original com preço final sem impostos inferior a ‘100’?

### Dependências 
O programa utiliza as bibliotecas pandas e numpy
Caso não tenha instaladas, executar o comando "pip install numpy pandas"

### Interrompendo o programa
Caso queira interromper a execução do programa, aperte Ctrl+c

## Observações

A parte de gerar o novo arquivo csv está comentada, visto que ele já está gerada.
Caso queira testá-la, deve apenas alterar o caminho de destino do arquivo

