# Components
All components are listed in the bill of materials which you can find [here](https://github.com/Slauf21/Workshop-IOT-RPI-2022-23/tree/main/Circuit/Bill%20Of%20Materials)

## LDR
LDR: https://www.gotron.be/ldr-photoresistor-100mw-50-160kohm.html

The LDR will assume a resistance value depending on the incidence of light. The voltage across this will therefore vary and be an analog value. For this we need an ADC.

![image](https://user-images.githubusercontent.com/79916416/197495382-c62f6ac9-0afe-435c-8baf-716bd85ffba2.png)

## ADC
ADC TLC549: https://www.gotron.be/8-bit-adc-converter-with-serial-control.html?gclid=CjwKCAjw79iaBhAJEiwAPYwoCLWCTqcdT3dClwdzuin4MIdrPvn4DQg3hyETrE1SUpddLzwZSJvRzRoCZ3gQAvD_BwE

Datasheet: https://pdf1.alldatasheet.com/datasheet-pdf/view/28912/TI/TLC549.html

![image](https://user-images.githubusercontent.com/79916416/197496335-5483d1d2-a319-4482-ad6b-eb48fd0b88e4.png)

## Relais
G5PZ-1A-E 5VDC: https://www.mouser.be/ProductDetail/653-G5PZ-1A-EDC5

This relais has a coil which powers at 5V and 106mA. It has a coil resistance of 47 ohm. The relais will be used to control an external, higher voltage circuit that the Rpi cant controll with its GPIOs.

![image](https://user-images.githubusercontent.com/79916416/201310495-3af5b13c-349c-4b45-966b-4f8a19eecf09.png)

## Transistor

2n2222a: https://www.mouser.be/ProductDetail/Diotec-Semiconductor/2N2222A?qs=OlC7AqGiEDmNlRSTGL2dYg%3D%3D&gclid=Cj0KCQiAgribBhDkARIsAASA5btApKR5Wi0awd6l1xYTlflaXAFN-934qWyK9pfrrR_6dCfe9-h9G84aAgFrEALw_wcB

A transistor is needed because the GPIO pins of the RPI cant drive the coil of the relais. The 5V pin can. So a BJT npn transistor is used as a switch, controlled by the RPI gpio.

![image](https://user-images.githubusercontent.com/79916416/201316302-7d30c3cb-90a4-4755-af86-603813e2542b.png)
