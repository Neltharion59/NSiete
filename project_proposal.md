# maCaPeLa - návrh projektu

Cieľom tohto projektu je vytvoriť a natrénovať hlbokú neurónovú sieť, ktorá bude schopná separovať vokály (hlas) od hudby v hudobnom súbore, obsahujúcom oboje.
## Motivácia

Jedným z dôvodov, prečo je separovanie hlasu zaujímavou témou, je tvorba _karaoke_ (hudba bez vokálov), resp. _a cappella_ (iba vokály) verzií hudobných skladieb. Množstvo hudobných skladieb nemá verejne dostupnú karaoke / a cappella verziu a z toho dôvodu vzniká dopyt po nástrojoch, ktoré by takúto verziu dokázali vytvoriť priamo z originálneho hudobného súboru.

Do triedy príbuzných problémov môže pritom patriť tiež problematika "čistenia" zvukových nahrávok od šumu, príp. oddelenie inej zložky zvukového signálu od pôvodnej nahrávky (napr. bicie nástroje). Tieto problémy ponechávame v kontexte realizácie nášho projektu ako otvorené možnosti, pričom sa plánujeme zamerať na už spomínanú problematiku automatizovanej tvorby _karaoke_, resp. _a cappella_ verzií existujúcich nahrávok.


## Existujúce práce

Neurónové siete predstavujú vhodný a zaujímavý nástroj pre účely tvorby modelu, schopného realizovať separáciu vokálov a hudby v rámci hudobnej nahrávky, o čom svedčí tiež existencia viacerých odborných prác tohto zamerania. Príkladom je [DeepConvSep](https://github.com/MTG/DeepConvSep), kde autori z Univerzity Pompeu Fabra pomocou konvolučných neurónových sietí dokázali separovať hudobné nástroje z nahrávok klasickej hudby, ako aj hlas a nástroje z modernejšej hudby. Prácou s rovnakým účelom je [Wavenet for Music Source Separation](https://github.com/francesclluis/source-separation-wavenet), kde autori natrénovali neurónovú sieť na separáciu hlasu od hudby, ako aj jednotlivých hudobných 

## Datasety

Jedným z datasetov, ktoré by sme mohli využiť, je [!!!!TODO!!!!](), ktorý príhodne poskytuje hudobné súbory, ktoré majú hlas a pozadie uložené v oddelených kanáloch, ktoré pri trénovaní vieme zlúčiť do jedného.

Alternatívou je pracovať so separátnymi nahrávkami hlasu a hudby, ktoré zlúčime, aj ak by šlo o inak nesúvisiace nahrávky. V tomto prípade by bolo zaujímavé zistiť, či model natrénovaný na takýchto dátach dokáže separovať hlas aj z reálnych hudobných skladieb.
## Vysokoúrovňový návrh
Postupovať budeme takzvanou slepou separáciu zdrojov [1], teda sa budeme snažiť separovať jeden signál z viacerých zmiešaných signálov bez dodatočných informácií.


## Zdroje

[1] "Biomedical Signal and Image Processing", Spring 2008.

[Source](http://www.mit.edu/~gari/teaching/6.555/LECTURE_NOTES/ch15_bss.pdf)

[2] P. T. Selvan and V. Vaishnavi, "Singing pitch extraction and voice separation from music accompaniment using trend estimation and tandem algorithm," 2013 IEEE International Conference ON Emerging Trends in Computing, Communication and Nanotechnology (ICECCN), Tirunelveli, 2013, pp. 232-235. doi: 10.1109/ICE-CCN.2013.6528499

[Source](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6528499&isnumber=6528464)

[3] G. -. Jang, Te-Won Lee and Yung-Hwan Oh, "Single-channel signal separation using time-domain basis functions," in IEEE Signal Processing Letters, vol. 10, no. 6, pp. 168-171, June 2003.
doi: 10.1109/LSP.2003.811630

[Source](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1198666&isnumber=26980)