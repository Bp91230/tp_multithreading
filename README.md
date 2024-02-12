# TP Multithreading
This repository is a school project for the multiprocessing class. 


To access to the code of the project you may clone the repository by doing :

`git clone https://github.com/Bp91230/tp_multithreading.git`

Once the repository is clone in your terminal open the created directory tp_multithreading :

`cd tp_multithreading`
Dependencies
First check the version of python by doing `python -V` or `python3 -V`
It should be python 3... if not then upgraded it !
Also check if you have pip : `python -m pip -V` if you don't make sure to install it: `sudo apt install python3-pip`
Also install the multiprocessing python library : `pip install multiprocessing` or `pip3 install multiprocessing`






To run the project first execute the QueueManager.py file by doing 



`python3 QueueManager.py`    which will start the local server.

Then execute the Boss.py file by doing 


`python3 Boss.py`

And then the Minion.py file by doing :


`python3 Minion.py`

The Boss program sends tasks to the Minion program precisely the size of the task and the number of time it should be computed. 
The task to compute in the Minion program is a resolution of a linear system which size is sent by the Boss

The Boss sends the task in a queue handled by the QueueManager, the Minion read the task queue and execute the tasks and send back to the Boss 
results like the execution time of the computed task. 

The second part of the project is to compare the performance of minions in python and minions in cpp.


In order to do that, we have a python made proxy in the file `proxy.py`
The proxy file allows us to create an HTTP server on which the boss can publish tasks using a json format others can connect to it and read the tasks sent
The proxy enables communication between the Boss in python and the minions (task solver) in cpp. Communication will be done by sending data in json format to the server.

And to use the cpp task solver, you need first to build the environment by executing these 
Cmake instructions :


`cmake -B build -S .`


`cmake --build build`


In order to run the cpp task solver, run first in different terminals the QueueManager.py and the Boss.py files as shown earlier, then in another terminal the python proxy by doing : 


`python3 proxy.py`. And finally, you may run the cpp solver :


`./build/low_level`

Also make sure that the minion.py program is not running as the same time to avoid consuming data 




