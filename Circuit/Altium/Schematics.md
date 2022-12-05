# Schematic

[RPI pins header detailed](https://user-images.githubusercontent.com/79916416/205603582-8edb5c64-c594-4c13-aa63-774d3fb8d8f8.png)

The PCB will be designed in Altium designer. In Altium create a new project and add a schematic to the project. The components will be put on this schematic. 
A lot of the sensors we read are external, meaning they are their own circuit boards and need to be connected with headers. The PCB will sit on the RPI headers. 
Here are the measurements of the pin headers:

![image](https://user-images.githubusercontent.com/79916416/202998758-d3084e8b-d7c6-4c54-bdb8-5ecac14820c2.png)
*Measurements in millimeters*

[Library Loader](https://www.samacsys.com/altium-designer-library-instructions/) is a software that allows you to import libraries for components. These include pre made footprints and schematic icons. This will be used for the SGP40 sensor

## Pin Header
These pin headers are not basic components in Altium and need to be created with a footprint wizard. Before starting create a libs folder in the Altium project.

![image](https://user-images.githubusercontent.com/79916416/203011348-39ad64b4-d7a6-49b4-8055-d19d05f3969c.png) <br>
*Libs Folder*

### PCB Footprint
To add a custom component right click the project (.PrjPcb file) 
then **Add New To Project** -> **PCB Library**. The new file will be openned and will be blank. On the left panel a footprint is visible. This one wont be used. Press **CTRL+S** and save the file in the **Libs** folder.

![image](https://user-images.githubusercontent.com/79916416/203002904-d9896105-0451-43e5-a2c0-8b8fc58ac5e1.png)<br>
*Default Footprint*

<br>

First the header for the RPI GPIO will be created. To create a new footprint press the **Tools** tab on the toolbar and select **Footprint Wizard**. A new Footprint Wizard window will open. Press next and select the type of footprint needed. A header is a **Dual In Line Package (DIP)**. Change the unit of measurement to **millimeters**

Next you will be asked for the hole dimensions. The dimensions from the measurements above need to be used. The pin diameters of the header is 1.02mm. A slightly wider diameter of 1.2mm will be used so the header can fit into the holes easily. Dimensions of the pad can be 2mm by 2mm. 

![image](https://user-images.githubusercontent.com/79916416/203004519-79197a7c-7328-4fd7-88fb-83ae4afd7dea.png)<br>
*Hole Dimensions*

<br>

Press next and now the distance between the pins need to be determined. The measurements say thet header pins are 2.54mm from each other. Since the hole and pad size was set to 2mm by 2mm there will be 1mm from the hole center to the edge of the pad. This will result in 0.54mm of free space between the pads.

![image](https://user-images.githubusercontent.com/79916416/203005567-be6d6c0e-9fd1-41f0-a70d-dfce81c54a9a.png)<br>
*Hole Distance*

<br>

The width of the outline can be left as it is. This outline will be deleted later.
Next the total number of pins need to be selected. The rpi 3b has 40 GPIO pins in a 2x20 structure.

![image](https://user-images.githubusercontent.com/79916416/203006647-39148ce0-5d94-446c-ab24-4f9a7425cf27.png)<br>
*Pin Amounts*

<br>

Call it RPI-Header and then click finish.

The design will appear on screen and the first this that needs to be done is to delete the yellow outline by selecting it and pressing delete. Then delete the original footprint. Result:

![image](https://user-images.githubusercontent.com/79916416/203009007-dee7c6fc-b8a5-4c7e-95c8-b6f7dbe375cb.png)<br>
*New Footprint*


### Schematic Icon

A new component also needs a schematic icon to put on the schematic design. This is done by adding a schematic library to the project like a PCB library was added. 
Name it the same as the PCB library and save it under the same directory (Libs). Select the icon item and press edit. Under the new tab call the icon **RPI-Header*. The custom footprint needs to be linked to this icon. This is done by pressing the add footprint button at the bottom.

A window will appear to select a library. Press browse, then select the correct library called RPI-Header.

![image](https://user-images.githubusercontent.com/79916416/203012484-e9745785-24ee-41a2-b47b-2d1a3ec10b99.png)<br>
*Add Footprint*

![image](https://user-images.githubusercontent.com/79916416/203012608-88bfb36e-c8a9-40d7-85ad-568a3ff39835.png)<br>
*Select Library*

Press OK, then OK again. The footprint is succesfully linked to the icon. Now an actually schematic icon needs to be created.

To do this press **Tools** -> **Symbol Wizard** in the toolbar. A new window will apear asking the layout. RPI gpio has 40 pins in a zig zag style. Seelct zig zag in the layout style. Now all the pins are set as inputs. Select them all by first selecting the first, then holding shift and pressing the last one. Change the electrical type from Inputs to I/O by clicking the drop down menu of the last item.

![image](https://user-images.githubusercontent.com/79916416/203013946-f334472f-2497-433b-b3b7-cb5844734830.png)<br>
*Icon Design*

Then **Place** -> **Place New Symbol**

In the SCH LIB window select the icon and press place. Place it somewhere on the schematic. Double click it and give it the name J1

## Sensors

The same process needs to be repeated for the sensor headers. This is a 5x1, 3x1 and 2 times 1x4 headers. When creating a one dimensional header like a 4x1. Select 8 pins for the DIP and remove one of the sides.

![image](https://user-images.githubusercontent.com/79916416/203021777-bb5b9310-5cbb-4a27-8611-6c42e9a493c4.png)

## Screw Terminals

The screw terminals dont have the same measurments as pin headers. 

![image](https://user-images.githubusercontent.com/79916416/203022143-64acddcc-53fc-4086-95aa-b112e071dcbb.png)<br>
*Screw Terminal Header*

![image](https://user-images.githubusercontent.com/79916416/203023751-d26eb459-ec07-4451-94cb-20c3781e8cfc.png)<br>
*Hole Measurements*

![image](https://user-images.githubusercontent.com/79916416/203024502-cf9d76ab-16a7-4916-b683-28a7f4d2c2f5.png)<br>
*On Schematic*

## Relais

The relais has a much different pin design the a header or terminal. 

![image](https://user-images.githubusercontent.com/79916416/203024929-793bfb97-0f3d-41aa-8f30-005dc7d58e82.png)<br>
*Relais Measurements*

![image](https://user-images.githubusercontent.com/79916416/204232282-617cd91c-9d5e-4081-aa7a-9bcf55d1ad8f.png)<br>
*Footprint*

The distance is the distance that was written in mm in the datasheet converted to mils.

![image](https://user-images.githubusercontent.com/79916416/203032510-4f5602a5-f81a-467d-876f-e5073b929eda.png)<br>
*Schematic Icon*

The schematic icon pin numbering is the same as the pins on the datasheet of the relais.

## Resistors and Capacitors

Throught hole resistors are used. These are already included in the standard library of Altium. In the components search, select miscellanious devices from the drop down menu and search for Res1. The same method is used for importing capactitors.

![image](https://user-images.githubusercontent.com/79916416/203328175-2cfcdf56-2bdc-4358-8549-ca882f684c01.png)<br>
*Miscellanious Devices*

## Wiring the Schematic

After adding all the components, the schematic should look like this:

![image](https://user-images.githubusercontent.com/79916416/205596907-9b91dbb2-e162-416f-884a-932de654a84c.png)<br>
*Schematic Not-Wired*

Now all the components need to be wired to the RPI header. For this, a [rpi gpio pinout](https://www.raspberrypi.com/documentation/computers/images/GPIO-Pinout-Diagram-2.png) picture is usefull. The right side of the gpio pins should be used as much as possible because the pcb is going to sit on the right side of the RPI.

Pin 16 is a free GPIO pin that will be used to drive the transistor base. Connect it to the pin number 2 of transistor Q1 with the 1.2k ohm resistor in between. The collector of the transsitor needs to be connected to the 5V power supply of the RPi which is pins 2 or 4. This will then power the coil, which needs to be connected to the emitter of the transtor (pin 3). Wires can be placed using CTRL+W command. Looking at [the data sheet of the relais](https://www.mouser.be/datasheet/2/307/Omron_(ENG)G5PZ_E-1843616.pdf), the coil is between pins 1 and 4 and the contact is between 2 and 3. Connect the Emitter of the BJT to pin 1 of the relais, then connect pin 4 to ground of the RPI.

Then the screw terminals need to be connected through the contact of the relais. Pins 2 and 3 can be connected since they are neutral and earth, but pins one will be live and need to go to the contact of the coil. The fly back diode 1n4007G needs to be connected reverse and in parallel with the coil. This means the anode will be connected to pin 4 and the kathode to pin 1 of the relais. 

The [DHT11](https://www.google.com/search?q=dht11+pinout+resistor&sxsrf=ALiCzsY3LPts4QoQ96bUZEVuVdWRRar4pg:1669126484691&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiPuNHZ_MH7AhUJi_0HHUXWBlgQ_AUoAXoECAEQAw&biw=1536&bih=754&dpr=1.25#imgrc=dNX5LVLrUIyOnM) has 3 connected pins. Vcc, Data and fround. It also needs a resistor between the data and the 5V. Pin 1 will be connected to the same 5V pin. Pin 2 will be connected to pin7 which is the gpio pin that support 1 wire protocol. 3 is not connected and 4 is ground which is pin 6. Also connect the 10k resistor between dht pins 1 and 2.

The mic uses and SPI ADC to convert the analog data to digital. Here are its pinouts:

![image](https://user-images.githubusercontent.com/79916416/203338400-d0879bc2-c969-43c2-bf77-2496ff0f610c.png)<br>
*LTC1864 Pinouts*

Align the headers in the schematic to match the pinouts. This will create less confusion.

![image](https://user-images.githubusercontent.com/79916416/203341361-08ffe19f-a1e7-46d8-8e87-2b90161a3799.png)<br>
*Schematic Pinout LTC1864*

This component is devided into tho headers, one 4x1 header for each side. Vcc (Pin8) and Vref (pin1) need to be connected with 5V. [Here](https://www.cuidevices.com/product/resource/cma-4544pf-w.pdf) is the mic basic operation circuit. The output will go to the SPI adc converter.

Pins 5 (CONV),6 (SDO) and 7 (SCK) are the SPI pins. The SDO and SCK need to be connected to the MISO and SCLK pins on the RPI respectivly. WHich are pins 21 and 23. The CONV pin is the slave select and needs to be connected to SPI0 CE1 pin.

The [PIR motion sensor](https://www.mouser.be/datasheet/2/737/pir_passive_infrared_proximity_motion_sensor-932858.pdf) has 3 simple connectors. Pin 1 is the vcc, Pin2 is the data and pin 3 is the GND. Pin 22 will be used for the data of the PIR motion sensor.

The [gas sensor](https://www.mouser.be/datasheet/2/682/Sensirion_Gas_Sensors_Datasheet_SGP40-2001008.pdf) also has a reading circuit. This will be recreated in altium.

## Result

The schematic will look like this:

![image](https://user-images.githubusercontent.com/79916416/204230306-3accb1fc-8c68-4c18-8d1c-3f2381f4258d.png)<br>
*Resulting Schematic*

Then the next step is to design the PCB. This can be read [here](https://github.com/Slauf21/Workshop-IOT-RPI-2022-23/blob/main/Circuit/Altium/PCB.md).
