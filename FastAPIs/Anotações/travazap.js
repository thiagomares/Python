async function enviarScript(scriptText){
	const lines = scriptText.split(/[\n\t]+/).map(line => line.trim()).filter(line => line);
	main = document.querySelector("#main"),
	textarea = main.querySelector(`div[contenteditable="true"]`)
	
	if(!textarea) throw new Error("Não há uma conversa aberta")
	
	for(const line of lines){
		console.log(line)
	
		textarea.focus();
		document.execCommand('insertText', false, line);
		textarea.dispatchEvent(new Event('change', {bubbles: true}));
	
		setTimeout(() => {
			(main.querySelector(`[data-testid="send"]`) || main.querySelector(`[data-icon="send"]`)).click();
		}, 100);
		
		if(lines.indexOf(line) !== lines.length - 1) await new Promise(resolve => setTimeout(resolve, 250));
	}
	
	return lines.length;
}

enviarScript(`
O CLONE Capítulo 78
de Glória Perez
Episódio escrito por Alex Spinola
Inspirado na obra "O CLONE", de Glória Perez
CENA 1. CASA DE LEONIDAS. SALA. INTERIOR. DIA
Leônidas e Lucas. Tensão entre eles.
LEONIDAS
O que foi que você disse, Lucas?!
LUCAS
O senhor ouviu: eu vou pro
Marrocos!
Lucas vai saindo, Leônidas o segura. Tom ameaçador.
LEONIDAS
Você não vai pra lugar nenhum,
você tá me ouvindo? Dessa casa
você não sai!
CORTA PARA:
CENA 2. CASA DE DEUSA. SALA. INTERIOR DIA
Toque de campainha. Dona Mocinha por ali. Sorridente,
Deusa corre para antender. Sorriso murcha ao abrir a
porta. Tia Filó entra.
DEUSA
Cadê o Léo, tia?
TIA FILÓ
(sem jeito)
Você sabe como ele é, filha...
Deusa vai perdendo o chão, desaba no sofá.
CORTA PARA:
CENA 3. CASA DE LEONIDAS. SALA. INTERIOR. DIA
Leônidas e Lucas. Continuação.
LUCAS
Solta meu braço, pai!
LEONIDAS
Você não vai jogar tudo o que a
gente conquistou pela janela,
correndo atrás da mulher do Said.
LUCAS
(solta-se do pai, vai
subindo as escadas)
E o que foi que a gente
conquistou, pai? Eu não
conquistei nada.Eu só tô vivendo
uma vida que não é minha.
2.
LEONIDAS
Chega desse papo, chega dessa
conversinha de analista! Pra
fugir dos seus problemas, você
não precisa arrumar outros!
LUCAS
Pelos menos vão ser problemas que
eu procurei. Uma vez na vida eu
vou tá conquistando alguma coisa
pra mim, alguma coisa que eu
quero. E se eu tiver que pagar
por isso, eu vou pagar.
LEONIDAS
(BERRA)
Não vai pagar com as minhas
empresas, seu irresponsável!
Leônidas sente uma forte dor no peito, cai. Lucas corre
até ele.
LUCAS
Pai?! Pai?!
CORTA PARA:
CENA 4. FEZ. EXTERIOR. NOITE
Clipes de Fez, Marrocos.
CENA 5. CASA DE ALI. QUARTO DE JADE. INTERIOR. NOITE.
Jade aflita. Zoraide entra.
JADE
(corre para Zoraide, abraça)
Zoraide, eu tô muito aflita.
ZORAIDE
Mas por que, minha florzinha?
JADE
Eu não sei, Zoraide. Tô sentindo
um aperto aqui no peito. Faz dois
dias que tô aqui, Said lá no
Brasil, ia se encontrar com a
mulher do Lucas, que eu sei, tava
escrito no olho dele que ia se
encotrar com ela. Aquela mulher
vai aprontar alguma coisa...
ZORAIDE
Mas será, Jade? Será que ela vai
botar na mão do Said uma adaga
pra fazer mal pro Lucas, o marido
dela? Uma coisa que pode destruir
a vida da família dela?
3.
JADE
Eu não sei, Zoraide. A Maysa é
uma naja, e a gente sabe o que
uma naja faz: ela cospe no olho
do inimigo... Ela pode cegar o
Said...
ZORAIDE
Calma, Jade, você tá muito
nervosa, tá com medo, e o medo
não é bom conselheiro pra
ninguém. Faz o seguinte: liga pra
Said, sonda o coração dele.
JADE
Será, Zoraide?
ZORAIDE
Não custa tentar, minha
florzinha. Será que ele já se
encontrou com ela?
JADE
Não sei, Zoraide, não sei...
CORTA PARA
CENA 6. RIO DE JANEIRO. EXTERIOR. DIA
Clipes do Rio de Janeiro.
CENA 7. RESTAURANTE.INT.DIA
Maysa e Said acabam de chegar. Garçom se aproxima.
GARÇOM
A senhora bebe alguma coisa?
MAYSA
Um suco de abacaxi com hortelã,
tem?
Garçom faz que sim.
MAYSA
E você, Said?
SAID
O mesmo.
Garçom sai.
MAYSA
E a Jade?
4.
(...cont.)
Foi para o Marrocos. Tive que
ficar, muita coisa pra resolver
por aqui. E o seu marido?
MAYSA
Deve ter muita coisa pra resolver
também.
SAID
(pensa)
O que ela tá tentando me dizer?
CORTA PARA:
CENA 8. HOSPITAL. RECEPÇÃO. INTERIOR. DIA
Lucas e Dalva por ali. Aprensivos. Médico chega.
LUCAS
E então, doutor, como é que meu
pai tá?
Na expressão fechada do médico, CORTA PARA:
CENA 9.RESTAURANTE. INT. DIA
Maysa e Said.
MAYSA
(prova o suco)
Hum, muito bom. Nesse calor vai
bem.
SAID
Calor daqui perto do Marrocos, é
nada.
MAYSA
Verdade. De coisas quentes vocês
devem entender.
SAID
(constrangido)
Como?
MAYSA
Nada. Divaguei.
SAID
(direto)
Mas não foi pra divagar que você
marcou esse encontro comigo, não
é?
5.
MAYSA
(na falsa defensiva)
Nossa, Said, e por que não?
SAID
Porque você não é mulher de
perder tempo com isso.
MAYSA
Pode ser. Ou talvez eu seja
diferente das mulheres do
Marrocos.
SAID
Quanto a isso não tenho a menor
dúvida.
Toca o celular de Said.
SAID
Alô, Jade?
MAYSA
(pensa)
Ela deve estar morrendo de medo.
CORTA PARA:
CENA 10. HOSPITAL. RECEPÇÃO. INTERIOR. DIA
Lucas e Dalva diante do médico.
LUCAS
E então, doutor, como ele está?
MÉDICO
Melhor agora.
DALVA
Graças a Deus!
MÉDICO
Mas inspira cuidados, Lucas. Seu
pai teve um pico de pressão
arterial muito preocupante...
LUCAS
(interrompe)
Eu posso ver ele?
MÉDICO
Primeiro precisamos conversar.
E no clima, CORTA PARA:
CENA 11. CASA DE DEUSA. SALA. INTERIOR. DIA
6.
Deusa desconsolada. Dona Mocinha e Tia Filó procuram
anima-la.
TIA FILÓ
Fica em paz, Deusa. O Léo tá bem,
eu te garanto. Ele só não quis
vir.
DEUSA
Mas no telefone, ele me garantiu
que vinha.
TIA FILÓ
E você não sabe como ele é,
Deusa? Num dia, tá de um jeito,
no outro, muda igual lua.
DONA MOCINHA
Eu tava sentindo, isso, Deusa, eu
te falei.
DEUSA
Eu não me conformo. Onde será que
esse menino se enfiou agora?
CORTA PARA:
CENA 12. SÃO PAULO. EXTERIOR. DIA
Clipes de São Paulo.
CORTA PARA:
CENA 13. AVENIDA PAULISTA. EXTERIOR. DIA
Na profusão de rostos, encontramos Lucas. Aquele jeito
perdido de explorar o mundo.
CORTA PARA:
CENA 14. HOSPITAL. QUARTO DE LEONIDAS. INTERIOR. DIA
Dalva a alisar a cabeleira branca de Leônidas. Lucas
segura a mão do pai.
LEONIDAS
Escuta o que tô te pedindo, meu
filho, não vai atrás daquela
mulher, não bota a sua vida em
risco.
Dalva e Lucas trocam olhares.
CORTA PARA:
CENA. 15.RESTAURANTE.INT. DIA
Toca outro celular de Said. Maysa o observa.
7.
SAID
(ao celular, com Jade)
Jade, um momento, preciso atender
outra ligação, (coloca celular
aberto na mesa, atende o outro,
assunto de negócios, em inglês),
Hey, Mr. Thompson? How are you?
Yes, we can talk.
Said se afasta, Maysa gesticula: "Posso falar com a
Jade?". Said faz que sim.
MAYSA
(pega o celular)
Alô, Jade, tudo bem?
CORTE BRUSCO PARA:
CENA 16. CASA DE ALI. QUARTO DE JADE. INTERIOR. NOITE.
Jade ao celular. Tensa.
JADE
O que você quer com o meu marido,
sua naja?
MAYSA
(OFF)
Logo, logo, você vai saber...
No pânico de Jade, CORTA PARA:
COMERCIAL 1
CENA 17. CASA DE ALI. QUARTO DE JADE. INTERIOR. NOITE
Continuaçao da cena anterior. Jade ao telefone. Zoraide
aflita, ao lado dela.
JADE
Fala, sua naja, o que você quer
com meu marido?
MAYSA
(OFF)O que você acha de uma
mesa redonda. Eu já até
falei com o Lucas...
CORTA PARA:
CENA 18. RESTAURANTE. INTERIOR. DIA
Maysa finge que a ligação caiu. Said termina a ligação de
negócios, volta para a mesa.
8.
MAYSA
Alô, Jade? Alô?, (desliga o
celular, passa para Said), que
pena, caiu.
SAID
(pega o celular, pensa)
Por que a Nazira não apareceu?
MAYSA
O que foi, Said? Você parece
preocupado?
CORTA PARA:
CENA 19. CASA DE ALI. QUARTO DE JADE. INT. NOITE
Jade berrando ao celular. Zoraide apavaorada.
JADE
Alô, Maysa?! Alô?!(atira o
celular longe) Naja! Naja
traiçoeria!
ZORAIDE
O que foi, Jade? O que ela te
falou?
JADE
Não falou nada, Zoraide, só jogou
veneno, aquela víbora!
ZORAIDE
Será que ela falou alguma
malidicência pro Said?
JADE
Não sei... acho que não (respira
fundo, tenta se acalmar), se ela
tivesse falado, Said tinha ligado
de novo...
ZORAIDE
(cabreira)
Ou não...
E na expressão preocupada de Jade, corta para:
CENA 20. RESTAURANTE. INT. DIA
Said chama o garçom. Maysa com aquela cara de esfinge.
SAID
Bom, acho que aconteceu alguma
coisa, Nazira não vem mais...
Melhor fazer o pedido.
CORTA PARA:
9.
CENA 21. CASA DE MOHAMED. SALA INT. DIA
Mohamed e Nazira em pé de guerra. Latiffa tenta apaziguar.
LATIFFA
Por Allah, por favor, se acalmem.
MOHAMED
E tem como se acalamar com a
teimosia da Nazira, tem?
NAZIRA
Não vou! Já falei que não vou e
pronto! Said que se vire lá com a
brasileria...
MOHAMED
Não foi esse o combinada, hein,
Nazira! Não foi esse o combinado!
NAZIRA
Ah, pra isso Nazira serve, né,
pra ficar pajeando Said, servindo
de babá...agora, quando é pra
vocês falarem com o tio Abdul pra
levar o Ed pra conhecer o
Marrocos e pedir a minha mão em
casamento, ninguém se mexe,
ninguém faz nada por Nazira.
MOHAMED
Nazira, desobediência é rarám,
hein, Nazira, é rarám! Você tá
sapateando na palavra do profeta!
NAZIRA
Quem tá sapateando na palavra do
profeta é voce, Mohamed! Jurou
que falava com tio Abdul e não
falou! Mentira é rarám grave.
Voce vai arder no mármore do
inferno!
LATIFFA
Chega! Chega!
O berro de Latiffa faz os dois se calarem.
CORTA PARA:
CENA 22. HOSPITAL. QUARTO DE LEONIDAS. INT. DIA
Lucas, Dalva e Leônidas.
LEONIDAS
Diz, Lucas, me promete que você
nao vai correr atrás da mulher do
Said, meu filho...
10.
Breve silêncio. Dalva olha suplicante para Lucas.
LUCAS
Tudo bem, pai, eu prometo.
E no sorriso débil de Leonidas, corta para:
CENA 23. RIO DE JANEIRO. EXT. NOITE. DIA
STOCK SHOTS marcam passagem para o dia seguinte.
Corta para:
CENA 24. CLINICA DE ALBIERE. LABORATÓRIO. INT. DIA
Albiere diante Julio e Escobar. Os dois cheios de dedos.
ALBIERE
Mas o que foi? Vocês dois com
essas caras. Parecem que viram um
fantasma...
JULIO
Quase isso, Albiere.
ESCOBAR
A gente queria ter conversado com
você ontem mesmo, mas clima tava
péssimo, você e a Edna....
(...cont.)
Mas o que tem a Edna a ver com
isso? O que tem a minha vida
pessoal a ver com esse mistério
de voces dois? Olha, eu não vou
aceitar nenhum tipo de invasão na
minha vida, os meus problemas...
JULIO
Não é invasão nenhuma, Albiere.
Não nesse sentido. O que nós
temos pra te falar é assunto do
laboratório.
ALBIERE
Assunto do laboratório? Desde
ontem? E vocês dois so vêm falar
comigo agora? O que tá
acontencendo?
ESCOBAR
É o sobre o exame de DNA,
Albiere. Você errou no exame, é
isso.
11.
ALBIERE
O que?!!
E na incredulidade de Albiere, corta para:
CENA 25. CASA DE ALBIERE. COZINHA. INT. DIA
Edna acabrunhada à mesa do café da manhã. Alicinha prepara
algo para comer.
ALICINHA
Tem certeza que a a senhora não
vai mesmo pra clínica, tia Edna?
EDNA
Não, não vou. Albiere foi muito
grosseiro comigo, ontem.
ALICINHA
Olha que ele vai sentir falta da
senhora lá, organizando o
corre-corre que é a vida dele,
hein...
EDNA
É, só mesmo assim pra ele saber
que eu existo.
ALICINHA
Ai, tia, eu não quis dizer isso.
Eu tava só tentando animar a
senhora.
EDNA
Eu sei, Alicinha. Você é um anjo
pra mim, mas a verdade é uma só:
Albiere só me enxerga atrás
daquela mesa, naquele maldito
escritório. Quem sabe hoje ele dê
por falta da secretária e se
lembre que é casado comigo.
ALICINHA
Ah, tia, não fala assim, eu sei
que o tio Albiere adora a
senhora.
EDNA
Não, Alicinha, ela adora a
secretária que eu sou pra ele,
sempre eficaz, sempre pronta pra
resolver tudo. Aqui dentro de
casa, ele quase não me enxerga...
Aliás, só enxerga quando precisa
de alguma coisa, de algum
documento, fotografia... Não viu
ontem?
12.
ALICINHA
Fica calma, tia. Daqui a pouco
essa mágoa passa.
EDNA
Essa mágoa só vai passar quando o
Albiere me enxergar.
CORTA RÁPIDO PARA:
CENA 26. CLÍNICA DE ALBIERE. ANTE SALA. INT. DIA
Albiere diante a mesa de Edna. Julio e Escobar com ele.
ALBIERE
Cadê a Edna?
JULIO
Ela não veio trabalhar, Albiere.
Você não tinha percebido?
E no espanro de Albiere diante a ausência de Edna, CORTA
PARA:
CENA 27. CASA DE LEONIDAS. COZINHA. DIA
Dalva prepara uma bandeja. Maysa ao lado.
DALVA
Pronto, a dieta do seu Leônidas
agora é essa. Ordem do médico.
MAYSA
E o Lucas nem pra me avisar.
DALVA
Nao deu tempo de nada, Maysa.
MAYSA
Tempo a gente arruma, Maysa. O
Lucas não me quis por perto. Isso
é culpa, muita culpa.
Lucas entra.
LUCAS
Culpa do que, Maysa?
E no clima, CORTA PARA:
COMERCIAL 2
CENA 28. CASA DE LEONIDAS. SALA. INT. DIA
Dalva subindo as escadas com a bandeja para Leonidas.
Lucas no encalço de Maysa.
13.
LUCAS
Fala, Maysa, culpa de quê?
MAYSA
Você deve saber melhor do que eu.
LUCAS
Olha, Maysa, sem provocação, por
favor. Hoje não. Meu pai tá se
recuperando, essa casa precisa de
paz.
MAYSA
É mesmo, paz? Seu pai quase
infartou porque você resolveu
correr atrás da Jade, e você vem
me falar de paz, Lucas?
LUCAS
Melhor a gente parar por aqui. Eu
não quero discutir.
MAYSA
Se você tá esperando que eu vou
dar um minuto de paz pra você e
praquela marroquina, ah, Lucas
você que se prepare. Eu não vou
deixar barato.
LUCAS
Não tem nada que você possa
fazer, Maysa...
MAYSA
Tem certeza que não, Lucas? Eu
posso começar indo lá em cima
contar pro seu pai que a sua
promessa de não procurar a Jade,
é mentira! Depois, eu posso
procurar o Said e contar tudo pra
ele! Vai ser lindo aquela lá
morrendo apedrejada!
Lucas explode, toma Maysa pelos braços.
LUCAS
Cala essa boca, Maysa!
MAYSA
Vai fazer o que? Vai me bater?
Vai, bate!
Mel chegou, eles não perceberam.
MEL
Pai, o que é isso?!
Reação de Lucas ao ver Mel, CORTA PARA:
14.
CENA 29. CLÍNICA. SALA DE ALBIERE. INT. DIA
Albiere reagindo diante Júlio e Escobar.
ALBIERE
Mas isso, a catagolação dos
exames, é responsabilidade da
Edna, não minha!
ESCOBAR
Eu sei disso, Albiere. Mas quem
assinou o laudo foi você.
JULIO
E a família que requisitou o
exame, com certeza, não vai
deixar barato.
ALBIERE
(abalado)
A família já foi informada?
ESCOBAR
Nós não tivemos outra escolha.
ALBIERE
Foi por isso que a Edna não veio
trabalhar, é isso! Ela já sabia
que essa bomba iria explodir!
JULIO
Olha, Albiere, eu não sei se é
bem isso, não...
ALBIERE
Como não sabe, Júlio? A verdade
tá aí, na nossa cara. Ela nunca
foi de faltar! Saí de casa, ela
tava estranha, mal falou comigo,
mas não me disse que não viria
trabalhar...Na verdade, ela não
me disse nada!
ESCOBAR
Olha, Albiere, a gente tá
tentando te dizer isso de um
jeito delicado, mas quem errou
mesmo foi você.
ALBIERE
Eu?! Você enlouqueceu, Escobar?!
Eu nunca erro! Ainda mais com uma
falta primária dessas,
identificação de tubo de ensaio,
imagina!
15.
JULIO
Mas o exame de contraprova é você
quem identifica, não é, Albiere?
ALBIERE
Sim, na seguda amostra...
ESCOBAR
Foi aí que deu o erro, Albiere!
ALBIERE
Não! Nunca! Se eu errei, a culpa
é dela, é da Edna, que errou o
material desde o início! Eu quero
ela aqui e agora!
Albiere ao telefone, já discando. Troca de olhares entre
Júio e Escobar.
CORTA PARA:
CENA 30. CASA DE ALBIERE. SALA. INT. DIA
Telefone toca. Alicinha atende.
ALICINHA
Alô? Oi tio? Tudo bem? Nossa, o
senhor tá nervoso! Não, ela não
tá aqui não! É, saiu! Não, acho
que ela não foi pra clínica
não...
Sinal de ligação interrompida. Alicinha sorri.
EDNA
(OFF, do banheiro)
Quem era, Alicinha?
ALICINHA
Ninguém, tia. Deve ser engano.
Toma seu banho sossegada.
CORTA PARA:
CENA 31. CASA DE LEONIDAS. SALA. INT. DIA
Lucas, Maysa e Mel.
MAYSA
Vai, Lucas, responde! Conta pra
sua filha o que você tá pensando
em fazer?
MEL
Contar o que, mãe??
16.
LUCAS
Nada, Mel, eu não tenho nada pra
contar. Isso é invenção da sua
mãe.
MAYSA
Invenção? Você tem coragem de
jogar nas minhas costas uma culpa
que é sua, Lucas?
MEL
Pelo amor de Deus, vocês podem me
dizer o que tá acontecendo?
MAYSA
Vai, Lucas, fala!
LUCAS
Para e botar fogo, Maysa! Chega!
MAYSA
(também se exalta)
Botar fogo? O incendiário dessa
casa é você, Lucas! Melhor, quem
taca fogo nessa casa é aquela
infeliz...
Dalva desce as escadas, afobada.
DALVA
Mas o que é isso? Que gritaria é
essa, gente? O seu Leônidas tá lá
em cima num nervosismo só! Lucas,
meu filho, você sabe que seu pai
não pode passar por
contrariação...
LUCAS
(saindo)
Eu sei, Dalva. Eu tô indo pra
empresa.
MAYSA
(vai atrás)
Vai fugir, Lucas? Não foge não,
vem aqui! Vem aqui!
MEL
Dalva, o que tá acontecendo com
eles?
DALVA
(vai subindo, não quer se
comprometer)
Eu não sei, Melzinha, eu não sei.
CORTA PARA:
17.
CENA 32. CASA DE LEONIDAS. FRENTE. EXTERIOR. DIA
Lucas entrando em seu carro. Maysa o alcança. Impede de
dar partida.
MAYSA
Sai desse carro, Lucas! Até
quando você vai fugir? Quando
você vai ter coragem de assumir
as coisas que você faz?
LUCAS
Maysa, por favor, olha o
escândalo.
No PV de Lucas, Xande e o motorista da casa.
MAYSA
Que se dane o escândalo! Eu tô
cheia da sua covardia! Eu tô
cheia de você jogar os seus
problemas nas minhas costas! Vai
lá dentro agora e conta pra sua
filha que a gente vai se separar,
pra você correr atrás daquela
Jade!
LUCAS
Maysa, eu não quero envolver a
Mel nisso. Isso é assunto nosso.
A gente resolve.
MAYSA
Esse problema é da família toda!
É problema da Mel, do seu pai, e
até problema das empresas dele.
Sai desse carro! Eu não quero
saber mais de desculpas. Sai
desse carro e encara seus
problemas pelo menos uma vez na
vida!
LUCAS
(dando partida)
Maysa, eu tenho que ir pra
empresa...
MAYSA
Empresa? E você lá tá preocupado
com a empresa? Pensa que eu não
sei dos negócios que o seu pai
quer fechar com o Said? Pensei
que eu não sei o motivo do seu
Leonidas enfartar? Eu sei sim, a
Dalva me contou.
18.
LUCAS
(vai movimentando o carro)
Não dá pra conversar com você,
desse jeitio, Maysa, não dá pra
conversar com ninguém desse
jeito!
Carro de Lucas vai saindo, Maysa corre atrás.
MAYSA
Volta aqui, seu desgraçado,
covarde! Volta!
Maysa pragueja um pouco mais, até se dar conta de que é
observada por Xande. Tempo na vergonha dela até que se
recomponha e volte para a casa.
CORTA PARA:
CENA 33. CASA DE LEONIDAS. SALA. INTERIOR. DIA
Maysa passa por Mel.
MEL
Mãe, por favor, me diz o que tá
acontecendo?
MAYSA
(subido as escadas)
Me deixa, Mel! Me deixa!
CORTA PARA:
CENA 34. CASA DE LEONIDAS. QUARTO DE MAYSA. INT. DIA
Maysa tranca a porta e desconta sua raiva no que encontra
pela frente. Quebra vasos, arranca fotos dela e de Lucas
de porta-retratos, rasga roupas dele. Desaba aos prantos
sobre a cama. Tempo.
MAYSA
(deitada, olhando pro teto)
Isso não vai ficar assim, Lucas.
Não vai.
CORTA PARA:
CENA 35. CASA DE MOHAMED. SALA. INT. DIA
Mohamed e Said. Latiffa serve o chá.
MOHAMED
É isso, Said, Nazira tá
contaminada pela desobediência
das mulheres brasileiras. Eu não
sei mais o que fazer.
19.
SAID
(alheio ao que Mohamed diz)
Eu lá, naquela situação, com
aquela mulher do Lucas...
MOHAMED
(faz sinal, interrompe)
Said, Said, nós temos que decidir
o que fazer com a Nazira. Não dá
mais pra esperar. Eu não quero
levar problemas pro tio Abdul,
mas não tô vendo outro jeito.
SAID
Faça o que você achar melhor,
Mohamed.
MOHAMED
O que você acha, minha gazela?
LATIFFA
Ah, eu não sei marido. Vocês que
são irmãos é que decidem.
MOHAMED
Pois é, minha gazela, eu sei
disso, mas penso que vai ficar
muito peso nas suas costas tomar
conta dessa casa toda sozinha.
LATIFFA
Habib, Lala Nazira me ajuda
muito, mas eu posso dar conta,
habib...
Nazira entra.
NAZIRA
Olha só que bela naja você tem
dentro de casa, Mohamed.
MOHAMED
(se exalta)
La La La, deixe Latiffa fora
disso, Nazira. Quem decide alguma
coisa aqui sou eu! Eu e Said!
NAZIRA
(enfrenta)
Pois então decidam! Eu prefiro
ser escrava no Marrocos do que
continuar debaixo do mesmo teto
que essa najinha traiçoeira!
LATIFFA
(se dói)
Eu não tenho culpa de nada,
Nazira. A única culpada é a
(MAIS...)
20.
LATIFFA (...cont.)
senhora que desrespeita meu
marido e sapateia na palavra do
profeta
NAZIRA
(berra e sai pisando duro)
Naja! Eu vou fazer as minhas
malas agora!
LATIFFA
(aflita)
E agora, marido, o que eu faço?
MOHAMED
Deixa minha gazela, deixa. Seu
habib vai resolver. Deixa o chá
aí, vá descansar, minha gazela,
vá descansar.
LATIFFA
(sai choramingando)
Eu não quero ser culpada de nada,
marido, não quero.
MOHAMED
Viu, Said? Parece que o teto
dessa casa vai desabar na minha
cabeça, e a culpa é de Nazira.
SAID
Despacha pro Marrocos, Mohamed,
despacha.
MOHAMED
Eu tô percebendo que você também
não está bem, (olha ao redor, tom
de segredo), tem a ver com o
encontro com aquela mulher? O que
foi que ela te disse?
SAID
O problema é o que ela não disse,
Mohamed?
MOHAMED
Como assim o que ela não disse?
SAID
Essas mulheres brasileiras são
assim, Mohamed, ela dizem as
coisas não dizendo, (pensa alto),
a melhor coisa foi ter deixado a
Jade ir pro Marrocos.
21.
MOHAMED
(confuso)
O que?
SAID
(se dando conta)
Nada, Mohamed, nada.
CORTA PARA:
CENA 36. CASA DE ALI. SALA. INT. NOITE
Radija dança para tio Ali. A parte, Jade e Zoraide.
JADE
Eu não tô aguentado mais,
Zoraide.
ZORAIDE
Calma, Jade. Se alguma coisa
tivesse acontecido, a notícia já
tinha chegado.
JADE
Aí que tá, Zoraide: eu não
consigo ficar aqui, parada,
esperando qualquer notícia
chegar.
ZORAIDE
Jade, Jade, controla seu gênio.
Sid Ali pode perceber alguma
coisa. Ele é muito astuto. Se
perceber que você tá escondendo
alguma coisa, você não se safa do
inquérito dele.
JADE
Ele tá distraído com a dança da
Radija.
ZORAIDE
Até parece que você não conhece o
seu tio. Com um olho, ele vê a
dança, com o outro, enxerga tudo
o que acontece nessa casa.
E na dança de Radija, CORTA PARA:
CORTA PARA:
CENA 37. CASA DE ALBIERE. SALA. INT. DIA
Edna ajeita a estante. Toca a campainha. Vai atender.
22.
EDNA
Será que a Alicinha esqueceu as
chaves?
ALBIERE
(entrando, possesso)
Então você mandou a Alicinha
mentir pra mim? Tá tentando
ganhar tempo?
EDNA
(pasma)
Ganhar tempo? Do que você tá
falando, Albiere?
ALBIERE
Da sua incompentência, Edna! Da
sua incompetência!
E no clima, CORTA PARA:
COMERCIAL 3
CENA 38. CASA DE ALBIERE. SALA INTERIOR. DIA
Continuação da cena anterior. Albiere e Edna.
EDNA
Incompetência? Você tá louco,
Albiere?
ALBIERE
Louca tá você, Edna! Como você
foi capaz de cometer uma
barbaridade daquelas e deixar a
bomba explodir nas minhas mãos?
EDNA
Mas de que bomba você está
falando?
ALBIERE
Da troca do exame de DNA, Edna!
Para de se fazer de sonsa! Eu tô
sabendo de tudo! A culpa é sua!
Você vai pra clínia agora! Pega
suas coisas!
EDNA
Eu não vou pra lugar nenhum
enquanto você não me explicar o
que tá acontecendo?
(...cont.)
Será que além de burra você
também é surda?
23.
EDNA
(berra)
Chega! (estala um tapa na cara de
Albiere).
E na tensão entre os dois, CORTA PARA:
CENA 39. CASA DE DEUSA. QUARTO. INT. DIA
Deusa ajeita uma mala. Dona Mocinha e tia Filó com ela.
DONA MOCINHA
Mas pra onde você vai, Deusa?
DEUSA
Vou atrás do Léo! Tô cansada de
correr atrás desse menino e ele
escapar pelo vão dos meus dedos,
como se fosse areia.
TIA FILÓ
Mas vai atrás onde, minha filha?
DEUSA
A senhora não disse que ele
andava com plano de ir pra São
Paulo? Então, eu vou pra lá!
DONA MOCINHA
Mas procurar onde, minha filha?
Numa cidade daquele tamanho?
DEUSA
Eu não sei! Eu procuro polícia,
procuro programa de televisão, eu
faço qualquer coisa pra ter o Léo
comigo!
TIA FILÓ
Isso é loucura, Deusa. Não vai
dar certo e pode afastar o Léo
ainda mais de você. Me escuta.
DONA MOCINHA
A Filó tá com a razão, Deusa. E
você sabe como o Léo é. Melhor
esperar, minha filha!
DEUSA
(fecha a mala, decidida)
Eu não vou esperar mais nada!
Toca o telefone. CORTE BRUSCO PARA:
CENA 40. CASA DE DEUSA. SALA. INT. DIA
Deusa ao telefone.
24.
DEUSA
(atende)
Alô?
LEO
(OFF)
Alô, mãe? Sou eu, o Léo.
DEUSA
(perdendo o chão,
emocionada)
Léo, meu filho. Onde é que você
está?
CORTA PARA:
CENA 41 . ESCRITÓRIO. SALA DE SAID. INT DIA
Said analisa algumas panilhas. Secretária entra.
SECRETÁRIA
Doutor Said, desculpe, eu sei que
o senhor pediu pra não ser
incomodado, mas é que tem uma
moça lá na recepção. Ela disse
que é urgente.
SAID
E que moça é essa?
SECRETÁRIA
Ela não disse o nome, mas...
Maysa, vestida para matar, entra.
MAYSA
Sou eu, Said. Será que você teria
uns minutinhos pra mim?
CORTA PARA:
CENA 42. CASA DE ALI. QUARTO DE JADE. INT. NOITE
Jade desperta, asfixiada por um presságio.
JADE
Aquela naja, aquela naja veio no
meu sonho.
CORTA PARA:
CENA 43. BAR DE JURA. EXTERIOR. DIA
Basílio na limpeza das mesas. Jura serve um lance para
Xande. Raposão passa na rua.
25.
JURA
E aí, Raposão, alguma notícia dos
dentes?
RAPOSÃO
(arrasado)
Nada, Dona Jura. Nem sinal,
(segue cabisbaixo), nem sinal.
XANDE
Dentes, mãe? Que história de
dentes é essa?
JURA
E você não tá sabendo que
roubaram os dentes de ouro do
Raposão, não? Foi num baile,
voltou quase banguela. Oxe,
menino, eu já te contei esse
caso, tá com a cabeça onde?
XANDE
(engraçadinho)
No lugar de sempre: em cima do
pescoço.
JURA
(puxa uma cadeira)
Sei. E veio pra casa mais cedo
hoje por que?
XANDE
A Mel me dispensou. Disse que não
ia pro curso, que não ia pra
lugar nenhum. Ela tá arrasada.
JURA
Sei. E tá arrasada por quê?
XANDE
Sei lá. Deve ser problema de
família. Hoje a mãe dela se pegou
numa discussão com o doutor
Lucas.
JURA
Sei...
XANDE
Que tanto "sei" é esse, mãe, eu
hein!
JURA
"Eu hein!" digo eu, Xande. Tô bem
de olho nessa sua cara?
26.
XANDE
Ué, cara? O que tem a minha cara?
JURA
Cara de bobo, toda vez que fala
nessa tal de Mel.
XANDE
Ih, mãe, nada a ver.
JURA
Nada a ver? Sei...
XANDE
Ih, mãe, já perdi até a fome,
(vai se levantando), vou entrar e
tomar um banho...
JURA
(segura pelo braço)
Senta aí, menino. Você saiu daqui
ó, te conheço do avesso. Pode
desembuchar o que você tá me
escondendo aí!
XANDE
Mãe, pelo amor de Deus, que papo
chato, eu não tô escondendo nada.
Me deixa.
Xande sai. Basílio olha para Jura, dá uma piscadinha.
JURA
Tá se psicando todo aí por que,
Basílio? Eu hein!
BASÍLIO
O Xande tá gostando da tal de
Mel, né não, Dona Jura?
JURA
E desde quando eu ou Xande
devemos satisfação pra você,
hein, Basílio? Coisa feia ficar
ouvindo conversa dos outros. Não
é brinquedo, não!
Jura entra. Basílio com cara de tacho.
CORTA PARA:
CENA 44. CLÍNICA DE ALBIERE. RECEPÇÃO. INT. DIA
Alicinha acabou de chegar. Júlio se aproxima.
27.
JULIO
Alicinha?
ALICINHA
Oi Júlio, tudo bem?
JULIO
Tudo. É, mais ou menos.
ALICINHA
Ué, mais ou menos por quê? Algum
problema com o tio Albiere?
JULIO
Como é que voce sabe?
ALICINHA
Eu não sei. Mas do jeito que você
falou. Eu saí do meu curso,
passei perto de uma confeitaria,
vi um bolo que o tio adora e
resolvi comprar. Trouxe pro
lanche.
JULIO
Pelo jeito, o lanche vai ter que
esperar. O Albiere saiu louco
atrás da Edna? Ela tá em casa?
ALICINHA
(pensa rápido)
Não sei. Quando eu saí, ela tava
lá.
JULIO
Ué, mas ele ligou e você disse
que ela não tava.
ALICINHA
(finge constrangimento)
Ai, Júlio...
JULIO
O que que tá acontecendo,
Alicinha?
ALICINHA
(segreda)
Julio, por favor, não diz nada
pra ele, mas ela me pediu pra
falar que não tava. Você sabe,
eles brigaram. Eu comprei o bolo
até pra dizer que foi ela quem
fez. Quem sabe assim eles se
harmonizem de novo, né? Um docê
sempre cai bem...
28.
JULIO
Sei não. Com o problema que tá
aqui, nada vai ser capaz de
adoçar o Albiere.
CORTA PARA:
CENA 45. CASA DE ALBIERE. SALA. INT. DIA
Edna e Albiere. Tensão ainda maior entre eles.
ALBIERE
(alisa a face ofendida)
Agora é isso, Edna, violência?
EDNA
Violência é o que você acabou de
fazer comigo. Me acusando de uma
coisa que eu não fiz!
ALBIERE
Como que não fez, Edna? A
responsável pela catagolação dos
examens é você!
EDNA
Chega! (vai indo para o quarto),
eu não preciso aguentar isso!
ALBIERE
(segue)
Pra onde você vai?
EDNA
Eu vou embora!
ALBIERE
(segura)
Não, você não vai pra lugar
nenhum. Você vai para a clínica e
vai esclarecer a burrada que você
fez!
EDNA
(empurra, se solta)
Me larga!
Albiere perde o equílibrio. Cai, bate a cabeça na quina da
mesa de centro. Desmaia. Edna se desespera. Vai até ele, o
chacoalha. Nenhuma resposta. Ela tenta erguê-lo. Em vão.
Corre para o telefone. Quando vai discar, percebe suas
mãos sujas de sangue. Grita.
CORTA PARA:
FIM DO CAPÍTULO 78.
`).then(e => console.log(`Código finalizado, ${e} mensagens enviadas`)).catch(console.error)