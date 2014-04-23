sudoku
======
A top down generator

Use mapreduce.py if running on local system.
mapper.py and reducer.py are suitable for running on a Hadoop cluster in streaming mode.
Keep in mind that the numpy library is used which may cause an issue in clusters where it is not installed.

The mincemeatpy implementation used here is from this repo by Paul Talaga: https://github.com/fuzzpault/mincemeatpy which is in turn forked from https://github.com/michaelfairley/mincemeatpy
