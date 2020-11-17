# Toolbox for GSuite admin

This toolkit was created for adding a lot of 
Russian students into GSuite.

It doesn't use any api, sou should add users manually,
using **mass update** in GSuite admin panel.

## Features:
- csv users creation
- csv groups creation

## How to use
1. install requirements `pip install -r requirements.txt`

1. insert input data in **input** folder, according to
example files format.
> We recommend to use csv, the first column 
> must contain fullname (ФИО)
>
> You can create txt file with 

1. change **config.py** as you need 

1. run **main.py** 

1. get yours csv in **output** folder