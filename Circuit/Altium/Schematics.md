# Schematic

The PCB will be designed in Altium designer. In Altium create a new project and add a schematic to the project. The components will be put on this schematic. 
A lot of the sensors we read are external, meaning they are their own circuit boards and need to be connected with headers. The PCB will sit on the RPI headers. 
Here are the measurements of the pin headers:

![image](https://user-images.githubusercontent.com/79916416/202998758-d3084e8b-d7c6-4c54-bdb8-5ecac14820c2.png)
*Measurements in millimeters*

## Pin Header
These pin headers are not basic components in Altium and need to be created with a footprint wizard. 

### PCB Footprint
To add a custom component right click the project (.PrjPcb file) 
then **Add New To Project** -> **PCB Library**. The new file will be openned and will be blank. On the left panel a footprint is visible. This one wont be used.

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

<br>

### Schematic Icon

A new component also needs a schematic icon to put on the schematic design. This is done by adding a schematic library to the project like a PCB library was added. 
Name it the same as the PCB library and save it under the same directory. Select the icon item and press edit. Under the new tab call the icon **RPI-Header*. The custom footprint needs to be linked to this icon. This is done by pressing the add footprint button at the bottom.
