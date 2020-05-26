# AU-Rich-Elements

This repo contains materials relevant to our upcoming paper, preprint DOI: https://doi.org/10.1101/2020.02.12.945063.

The python script "EffectiveLengthCalculator.py" prints the length, registration, and "effective length" of the largest AU-rich element in an input sequence.  To run it, download the code and run it with a command like:

python EffectiveLengthCalculator.py -seqstring CGAUUUAUUUACG

The sequence of interest should come after the "seqstring" flag.

Flag "maxlength" tells the program where to start looking.  If maxlength is small then the code will run faster, but the upper limit for effective lengths will be restricted.

Flag "mismatch" tells the program whether to allow zero or one mismatch (as of now).  Zero is default.

Flag "startreg" tells the program whether to use the starting registration (1) or ending registration (0).  Starting registration is default.

Let me (David S) know if you have any problems.
