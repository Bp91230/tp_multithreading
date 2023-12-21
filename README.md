#TP Multithreading
This repository is a school project for the multiprocessing class. 


To access to the code of thee project you may clone the repository by doing :

'git clone https://github.com/Bp91230/tp_multithreading.git'

Once the repository is clone in your terminal open the created directory tp_multithreading :

'cd tp_multithreading'
dependencies .... (TODO) 
Cmake instructions ... (TODO)

To run the project first execute the QueueManager.py file by doing

'python3 QueueManager.py'

Then execute the Boss.py file by doing 
'python3 Boss.py'

And then the Minion.py file by doing :

'python3 Minion.py'

The Boss program sends tasks to the Minion program precisely the size of the task and the number of time it should be computed. 
The task to compute in the Minion program is a resolution of a linear system which size is sent by the Boss

The Boss sends the task in a queue handled by the QueueManager, the Minion read the task queue and execute the tasks and send back to the Boss 
results like the execution time of the computed task. 

