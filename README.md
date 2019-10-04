# pybuka
Darbuka rythm player from a string

Don't forget to install pygame `pip install pygame` for playing sounds.

You can edit in pybuka.py RYTHM and BPM variables. 

RYTHM rules:

* `D` - loud doum sound
* `T` - loud tek sound
* `t` and `k` - weak tek and ka sound
* `-` pause

Example:
~~~~
RYTHM = 'D-T---T-D---T-tkD-T---T-D--kS---'  # Maqsum
BPM = 120
~~~~

Also you can pass the rhythm as a command line argument. The second argument is BPM (optional). 
~~~
python pybuka.py "D-k-D-S-tktkD-tkT-tk" 100
~~~

