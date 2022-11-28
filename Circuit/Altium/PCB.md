# PCB 

First a PCB file needs to be added to the project. Rightclick tje PrjPcb file, then add new to project followed by PCB. Save ths file and name it. 
Now the schematic needs to be imported into the PCB. This is done by opening the design tab on the toolbar and pressing import changes from "projectName". Validate changes
and solve errors that might occure. Then execute changes.

![image](https://user-images.githubusercontent.com/79916416/204139344-a47263ed-14de-4cc3-b0bd-f50559d54af4.png)<br>
*Imported Schematic*

With the schematic imported, the components need to be placed on the circuit board in an effecient way. Then they need to be connected.

![image](https://user-images.githubusercontent.com/79916416/204234691-3a5d6aff-c24e-4c19-b7d9-e5e2a55bf880.png)<br>
*Components Placed*

The size of the board can be changed by clicking on board planning mode under the view tab. Then edit board shape under the design tab.

There will also be holes in the PCB that align with the ones on the RPi. This way the PCB can sit on the RPi using standoffs and it wont bend under its own weight. [Here](https://static.raspberrypi.org/files/product-briefs/Raspberry-Pi-Model-Bplus-Product-Brief.pdf) is an image with the measurements of the rpi.

These are made by first placing a pad:

![image](https://user-images.githubusercontent.com/79916416/204238642-f936fa26-1da1-41f7-b17d-7aae80a33330.png)<br>
*Place Pad*

And then under properties changing its hole size to the needed diameter, 2.75mm.

![image](https://user-images.githubusercontent.com/79916416/204249687-a9066ca6-6bd8-4124-aadd-d5e6b8f74acb.png)<br>
*PCB with screw holes*
