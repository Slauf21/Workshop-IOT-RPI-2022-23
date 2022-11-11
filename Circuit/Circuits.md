## RPI GPIO to Relais Circuit

The relais needs a voltage of 5V across it and a current of 106mA running trough it to power on. The RPI GPIO pins output 3.3V and can deliver a maximum of 16mA.
This means the RPI cant power the coil of the relais with its GPIO pins. A transistor needs to be used as a switch so that the GPIO can control the transistor, enabling a
higher current circuit. The 5V pin of the RPI is directly connected to the supply and can deliver 1-2A of current. This is more then needed.

The circuit is as follows:
![image](https://user-images.githubusercontent.com/79916416/201322184-61c4039c-487b-450e-9a2a-63061ff01687.png)

R3 is the coil. It has a resistance of 47 ohm. The Ic is simple to determine. Use ohms law to devide the voltage across the coil by the resistance of the coil. 
The voltage over the coil needs to be 5V. This will result in a current of 106mA. It is assumed the voltage drop across the transistor is 0. In reality this isnt the case.
But the voltage across the collector and emitter is small enough that it can be ignored.

There needs to 0.7V across the base to the emitter of the transistor. For this a resistor is needed to hold 2.6V. The BJT is a current driven transistor.
