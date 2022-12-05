# PCB 

Add a PCB document to the project like you added a schematic. The first step will be to define the boards shape. It will go over the RPI and allign with the screwholes on the RPI. These measurements of the rpi can be found its [datasheet](https://static.raspberrypi.org/files/product-briefs/Raspberry-Pi-Model-Bplus-Product-Brief.pdf).

The PCB will come on the RPI like this:

![Screenshot 2022-12-05 111956](https://user-images.githubusercontent.com/79916416/205613234-8d5d4146-bf41-4407-98a1-fa89ffdc8a95.png)

Define the PCB Shape by first adding the holes. These are regular holes with diameter that alligns to the screwholes. The distances need to be placed correct too like in the measurements. The command jump to location can be used for precise movements. This is done by clicking J on the keyboard and then new location. 

For the shape itself switch to the mechanical layer and then use the same jump to location position to trace wires across the board:

![image](https://user-images.githubusercontent.com/79916416/205616071-e8a8f38a-a271-4a02-ab5e-ddcfd71ba498.png)<br>
*Wires Board Shape*

Round edges will make the PCB cleaner. The RPI has 3.0mm radius on its edges. This will be copied on the PCB. The radius is 3mm, meaning that from the edges the lines need to be reduced by 3mm.

![image](https://user-images.githubusercontent.com/79916416/205617767-6ebe359e-4ce4-4b04-9ab9-4906f45fbd49.png)<br>
*Round Edges*

Now to actually define the boardshape hold shift and click on all the edge pieces to select them all. Then go to Design tab on the toolbar -> "Board Shape" -> "Redefine Boardshape From Selected Objects".

The edge pieces can now be deleted.

![image](https://user-images.githubusercontent.com/79916416/205618480-ff649944-9186-43a7-8e81-eb0ed2d022f5.png)<br>
*Final Board Shape*

Now its a matter of placing all the components in the most efficient way. The RPI header will go all the way on the right. A little space needs to be left because two tracks will come from the right side.

![image](https://user-images.githubusercontent.com/79916416/205624575-04836ca0-0093-44b9-9d64-f7265280ecff.png)<br>
*Components Placed*
