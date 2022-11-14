## RPI GPIO to Relais Circuit

De spoel heeft een spanning van 5V nodig en een stroom van 106mA die er doorheen loopt om bekrachtigt te worden. De RPI GPIO-pinnen hebben een output van 3,3V en kunnen maximaal 16mA leveren. Dit betekent dat de RPI de spoel van het relais niet kan voeden met zijn GPIO-pinnen. 

Een transistor moet als schakelaar worden gebruikt. Zo kan de GPIO pin de transistor aansturen waardoor de RPI controle heeft over een hogere stroomkring. De 5V-pin van de RPI is direct aangesloten op de voeding en kan 1-2A stroom leveren. Dit is meer dan nodig en zal dus gebruikt worden voor de spoel aan te sturen.

De schakeling is als volgt:

![image](https://user-images.githubusercontent.com/79916416/201616980-9ea22a41-7f6a-4d6f-9d85-ef45ceddfed6.png)

R3 is de spoel. Volgens de datasheet heeft hij een weerstand van 47 ohm. De collector stroom Ic is eenvoudig te bepalen. Gebruik de wet van Ohm om de spanning over de spoel te delen door de weerstand van de spoel.
De spanning over de spoel moet 5V zijn. Dit resulteert in een stroom van 106mA. Er wordt veronderstelt dat de spanningsval over de transistor 0V is. In werkelijkheid is dit niet het geval.
Maar de spanning over de collector en de emitter is klein genoeg om te negeren.

Er moet 0,7V over de basis en emitter van de transistor te staan voor geleiding. Hiervoor is een weerstand nodig om de 2.6V van de 3.3V op te nemen. De BJT is een stroomgestuurde transistor. Dit betekent dat de totale Ic evenredig zal zijn met de Ib. De DC-stroomversterking is de factor die de relatie bepaalt. Dit is te vinden in de datasheet en laat zien met welke factor Ic groter is dan Ib.

De juiste Hfe of stroomversterkingsfactor wordt gevonden door het gedissipeerde vermogen van de BJT te berekenen, namelijk P = Uce * Ic. Doe vervolgens hetzelfde voor de voorwaarden van de Hfe-waarden in de datasheet. Kies de Hfe waarvan de P-waarde het dichtst bij de berekende P in het circuit ligt. Dit wordt gebruikt als de stroomversterking. Op die manier zijn de spanning over de weerstand en de stroom erdoor bekend. Met behulp van de wet van Ohm wordt berekend dat een weerstand van 1250 ohm nodig is. De werkelijke waarde van het sluiten is een weerstand van 1,2 kohm.

De basis stroom is minder dan de maximum stroom van de RPI GPIO pinnen, namelijk 16mA
