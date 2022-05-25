# Beosztástervezés Hopfield-háló/Boltzmann-gép segítségével
2021 ősz - Témalabor \
Budapesti Műszaki és Gazdaságtudományi Egyetem, Villamosmérnöki és Informatikai Kar (VIK)

**Készítette:** Seben Domonkos (*dseben AT edu.bme.hu*), Szeredi Péter (*szeredipeter AT edu.bme.hu*) \
**Konzulens:** Erdős Szilvia

## A projektről
Az alábbi projekt a BME-VIK záróvizsgabeosztásának automatizálása céljából készült. Egy saját Hopfield-hálózat implementáció hivatott az ún. *bővített problémakörrel*  megbirkózni, melyben nem csak alapszakos, de a  mesterszakos hallgatók vizsgáit is beosztjuk. Ez több problémát felvet, pl. nem kezelhetjük a vizsgák hosszát egységesen. Mi 5 perces időegységekre bontottuk fel az egyes napokat, ez természesen azt az újabb problémát tárta elénk, hogy ne robbanjon lehetőleg a neuronok állapottere.  

## Az implementáció
A projekt az előre kiadott .xlsx fájlokat képes beolvasni, értelmezni. (az elnökök előzetes beosztását nem használva) Ez alapján létrehozza az egyes modellentitások példányait és inicializálja a súlymátrixokat. Ezután következik az algoritmus, mely egy optimum felé viszi a kezdetleges beosztást. Fejlesztettünk egy energiafüggvényt is, mely egy beosztásnak az energiaértékét képes meghatározni. (Ez kerül minimalizálásra.) 

## Jövőbeli fejlesztések
 - Sajnos a legtöbb, követelményeknek megfelelő súlymátrix csak a kidolgozás szintjéig jutott, nincsen még implementálva. 
 - A program még nem képes exportálni a kész beosztásokat. 
 - A projektet nem tudtuk még futtatni egy beosztáson, mert csak egy súlymátrixunk állt rendelkezésre. Így a teljes algoritmus kiértékelése, hatékonyságának vizsgálata is hátravan.
 - További optimalizációs iterációk lehetnek szükségesek a kiértékelések függvényében. 

## Elérhetőségek
A projektről bővebben az általunk készített [diasorból](prezi/temalab_beszamolo.pptx) lehet többet megtudni (ennek végén az általunk használt irodalom is fel van tüntetve.) 
Kérdések esetén bátran forduljatok hozzánk a feltüntetett e-mail címeken! 
