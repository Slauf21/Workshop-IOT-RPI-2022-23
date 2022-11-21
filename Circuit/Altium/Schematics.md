# Schematic

The PCB will be designed in Altium designer. In Altium create a new project and add a schematic to the project. The components will be put on this schematic. 
A lot of the sensors we read are external, meaning they are their own circuit boards and need to be connected with headers. The PCB will sit on the RPI headers. 
Here are the measurements of the pin headers:

![image](https://user-images.githubusercontent.com/79916416/202998758-d3084e8b-d7c6-4c54-bdb8-5ecac14820c2.png)
*Measurements in millimeters*

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

![image](https://user-images.githubusercontent.com/79916416/203020430-e598ac47-6891-48d0-930e-a5f1950e097c.png)

