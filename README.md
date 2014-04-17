sudoku
======
A top down generator

Use mapreduce.py if running on local system.
mapper.py and reducer.py are suitable for running on a Hadoop cluster in streaming mode.
Keep in mind that the numpy library is used which may cause an issue in clusters where it is not installed.