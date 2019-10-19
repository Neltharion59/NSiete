# SiMaOke - návrh projektu

Cieľom tohto projektu je vytvoriť a natrénovať hlbokú neurónovú sieť, ktorá by bola schopná separovať hlas od hudby v hudobnom súbore obsahujúcom oboje.
## Motivácia

Jedným z dôvodov, prečo je separovanie hlasu zaujímavou témou, je tvorba karaoke verzií hudobných skladieb. Mnoho hudobných skladieb nemá verejne dostupnú karaoke verziu, preto je záujem o nástroje, ktoré by automatizovane vytvorili karaoke verziu z hudobného súboru, bez dodatočných informácií. V tomto prípade je cieľom _odstrániť hlas_.

Serióznejším problémom je odstránenie šumu zo zvukovej nahrávky, napríklad pri menej kvalitných bezpečnostných kamerách so zvukovým záznamom. V hlučných oblastiach, napríklad pri hustej premávke, môže byť náročné na týchto nahrávkach rozpoznať, čo inkriminované osoby hovoria. Vtedy je potrebné odfiltrovať šum pozadia, aby bolo možné zreteľne počuť reč. V týchto prípadoch je cieľom _odstrániť šum_.

Tieto problémy majú svoje algoritmické riešenia [2][3], avšak typicky majú jednotlivé algoritmy svoje špecializácie a obmedzenia. Preto je zaujímavé využiť na tento problém neurónovú sieť, ktorá síce v našej práci bude pravdepodobne obmedzená na základe trénovacieho datasetu, avšak má potenciál stať sa všeobecným riešením.

Našu prácu plánujeme zamerať na _odstránenie hlasu_ z nahrávky. Postupovať budeme takzvanou slepou separáciu zdrojov [1], teda sa budeme snažiť separovať jeden signál z viacerých zmiešaných signálov bez dodatočných informácií.

## Existujúce práce

Separácia hlasu je zaujímavou témou v oblasti neurónových sietí, keďže existuje viacero prác využívajúcich neurónov= siete na separáciu hlasu. Príkladom je [DeepConvSep](https://github.com/MTG/DeepConvSep), kde autori z Univerzity Pompeu Fabra pomocou konvolučných neurónových sietí dokázali separovať hudobné nástroje z nahrávok klasickej hudby, ako aj hlas a nástroje z modernejšej hudby. Prácou s rovnakým účelom je [Wavenet for Music Source Separation](https://github.com/francesclluis/source-separation-wavenet), kde autori natrénovali neurónovú sieť na separáciu hlasu od hudby, ako aj jednotlivých hudobných 

## Datasety

Jedným z datasetov, ktoré by sme mohli využiť, je [!!!!TODO!!!!](), ktorý príhodne poskytuje hudobné súbory, ktoré majú hlas a pozadie uložené v oddelených kanáloch, ktoré pri trénovaní vieme zlúčiť do jedného.

Alternatívou je pracovať so separátnymi nahrávkami hlasu a hudby, ktoré zlúčime, aj ak by šlo o inak nesúvisiace nahrávky. V tomto prípade by bolo zaujímavé zistiť, či model natrénovaný na takýchto dátach dokáže separovať hlas aj z reálnych hudobných skladieb.
## Vysokoúrovňový návrh


## Zdroje

[1] "Biomedical Signal and Image Processing", Spring 2008.

[Source](http://www.mit.edu/~gari/teaching/6.555/LECTURE_NOTES/ch15_bss.pdf)

[2] P. T. Selvan and V. Vaishnavi, "Singing pitch extraction and voice separation from music accompaniment using trend estimation and tandem algorithm," 2013 IEEE International Conference ON Emerging Trends in Computing, Communication and Nanotechnology (ICECCN), Tirunelveli, 2013, pp. 232-235. doi: 10.1109/ICE-CCN.2013.6528499

[Source](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6528499&isnumber=6528464)

[3] G. -. Jang, Te-Won Lee and Yung-Hwan Oh, "Single-channel signal separation using time-domain basis functions," in IEEE Signal Processing Letters, vol. 10, no. 6, pp. 168-171, June 2003.
doi: 10.1109/LSP.2003.811630

[Source](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1198666&isnumber=26980)