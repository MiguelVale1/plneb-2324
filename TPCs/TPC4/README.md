# TPC4
## Considerações Iniciais

Neste tpc, foi pedida a criação de uma página web em HTML, CSS e se pretendermos JavaScript sobre um dos nossos passatempos (hobbies). Para tal, decidi inicialmente o display que pretendia e o conteúdo que esta página teria. Visto que, não tenho um passa-tempo específico e visto que, utilizando um único passatempo, simplificaria a estrutura da página web, escolhi combinar um conjunto pequeno de passatempos mais comuns que tenho, podendo assim aproveitar mais as capacidades que o HTML, CSS e JavaScript têm a oferecer.

## Estrutura Inicial

Para a estrutura da página, escolhi utilizar uma zona de escolha dos passatempos apresentados com um subtítulo referrente a cada umm destes por baixo destes. No final da página está descrita o que a pagina é e como utilizá-la. Após a escolha de um dos passatempos, a página por baixo destes alterava da introdução dos passatempos, para um maior desenvolvimento de cada um, o que gosto especificamente sobre cada um, porquê, quando os faço, como e aonde. 

## Estrutura HTML

O html está dividido em duas partes lógicas, a primeira div "corpo" que delimita a primeira página e um conjunto de 4 diferentes divs no final do html representantes às 4 diferentes páginas de escolha, descricao_exercicio, descricao_desporto, descricao_aprender e descricao_artes.

A div corpo contém a div inicio que altera a cor da página, dentro desta o título da página, e a div "slider" que irá conter as escolhas dos hobbies, dentro desta, estão 4 divs sobre cada escolha, exercicio, desporto, aprender e artes, respetivamente. Cada uma destas tem duas outras divs, uma denominada "imagens" para colocar a ilustração do hobby e outra denominada "hooby" que contém o nome do hobby. após estas existe uma div só para a descrição da página.

Cada uma das divs das páginas que poderão aparecer contêm duas divs para a inclusão das imagens, normalmente denominadas pela descrição de cada uma das imagens em si, intercaladas com um header para o título do texto e um parágrafo para o conteúdo do texto.

No final da página html está referenciado o script do javascript.

## Estrutura CSS
### Primeira Página

No inicio do css defino todas as funções pelo box-sizing : border-box para tornar mais fácil o somatório das dimensões das divs dentro da página e margin: 0 para poder ter mais liberdade sobre a posição das divs. Antes de passar as divs também adicionei um scroll-behavior: smooth em html, para tornar a descida da página quando se clica num botão mais suave.

Na div corpo defini os tamanhos máximos da div comom toda a página visível e adicionei a sua cor de fundo. Na div iicio defini a altura como 70% do container corpo e alterei a cor desta área. O título for centrado na página e foram alteradas as caraterísticas da letra e espaço à sua volta.

A área onde os sliders se irão posicionar tem um display de flex, uma largura da página total e uma centralização deste coonteúdo. No conteúdo em si foram definidas as larguras, distância entre os blocos e padding dentro destes e uma largura mínima para as palavras incluídas nestas não ultrapassarem os limites laterais desta. Defini que quando o rato passar por cima desta área a cor alteraria e o mesmo quando se clicar nela.

As divs que contêm as imagens dentro destas divs foram alteradas para preservarem uma proporção de 6/5. as imagens em si ocupam o espaço todo da div anterior e foi usado object-fit para esta não ser menor do que a div em si. Por baixo destas a descrição do exercício sofreu pequenas alterações a nível de formatação.

### Segunda Página

Cada página tem uma div maior que descreve a estrutura da página, devido a estas serem id's foi necessário repetir a informação para todas as páginas. nela é definido a altura e largura da página, o seu dissplay de none para que n se veja esta sem se clicar no botão relativo à página, a cor de fundo e um justify-content: space-between para que as imagens fiquem nas laterais da página cmo o texto no centro.

Foi criada uma div cahamada imagem só para todas as formatações da estrutura da div partilhadas por todas as imagens em todas as páginas, para não se repetir a mesma informação desnecessáriamente. Esta div apresenta o tamanho e largura das divs das imagens, centra-as no meio desta div e diz que não devem ultrapassar os limites inferiores da div, mantendo a sua proporção.

Finalmente para cada imagem foi instanciado o seu id e definida a imagem de fundo como a imagem escolhida.

## JavaScript

No javascript foram definidas 8 variáevis relativas aos id's dos botões da primeira página e as páginas relativas a estes.

Por baixo destas foram criados 4 event listenenrs para o click do botão, quando este acontece a página relativa a esta ganha a caraterística de display: flex, enquanto as outras ficam com a propriedade de display: none. Por último foi criada uma função scrollTo para a página direcionar o utilizador diretamente para a página apresentada. 
