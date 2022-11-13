## RPI GPIO to Relais Circuit

The relais needs a voltage of 5V across it and a current of 106mA running trough it to power on. The RPI GPIO pins output 3.3V and can deliver a maximum of 16mA.
This means the RPI cant power the coil of the relais with its GPIO pins. A transistor needs to be used as a switch so that the GPIO can control the transistor, enabling a
higher current circuit. The 5V pin of the RPI is directly connected to the supply and can deliver 1-2A of current. This is more then needed.

The circuit is as follows:
![image](https://user-images.githubusercontent.com/79916416/201524161-f12ba5d8-3de5-474e-a622-263a7e5baf0c.png)

R3 is the coil. It has a resistance of 47 ohm. The Ic is simple to determine. Use ohms law to devide the voltage across the coil by the resistance of the coil. 
The voltage over the coil needs to be 5V. This will result in a current of 106mA. It is assumed the voltage drop across the transistor is 0. In reality this isnt the case.
But the voltage across the collector and emitter is small enough that it can be ignored.

There needs to 0.7V across the base to the emitter of the transistor. For this a resistor is needed to hold 2.6V. The BJT is a current driven transistor. Meaning that the total Ic will be proportional to the Ib. The DC current gain is the factor that determines the relationship. This can be found in the datasheet and show by which factor Ic is bigger then Ib.

The correct Hfe or current gain is found by calculating the power dissipated by the BJT which is P = Uce * Ic. Then do the same for the conditions of the Hfe values in the datasheet. Pick the Hfe of the P value that is closest to the calculated P in the circuit. This will be used as the current gain.That way the voltage across the resistor and current through it are known. Using ohms law it is calculated that a resistor of 1250 ohm is needed. The closes real value is a 1.2kohm resistor.

The current is also less then the max current of a rpi GPIO pin
![image](https://user-images.githubusercontent.com/79916416/201524343-dc2d5419-977f-4067-81e7-6140ed56d6ea.png)
