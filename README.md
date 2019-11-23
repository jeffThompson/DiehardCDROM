# THE MARSAGLIA RANDOM NUMBER CDROM
## Including the Diehard Battery of Tests of Randomness

In 1995, [George Marsaglia](https://en.wikipedia.org/wiki/George_Marsaglia), a professor in the Department of Statistics at Florida State University created [`Diehard`](https://en.wikipedia.org/wiki/Diehard_tests), a set of statistical tests to determine the quality of a sequence of random values. Marsaglia originally released the software on a CD-ROM, pressed in an edition of "several hundred copies" and given away for free, along with 60 files containing a total of 4.8-billion random bits, an "unassailable source for those who absolutely positively have to have a large, reliable set of random numbers of serious simulation studies."

This re-creation of the 1995 CD-ROM comes mainly from the [Wayback Machine archive of Marsaglia's FTP site](https://web.archive.org/web/20160119150146/http://stat.fsu.edu/pub/diehard/cdrom/) at FSU. But since that archive is difficult to download in bulk, I've provided it here for historical research and general random number digging.

Included in this repo:  
* **`CD-ROM`:** the full contents of the original CD-ROM  
* **`CDInCase.png`:** a photo (the only one I could find) of the original CD in its case  
* **`ConvertRandomNumberFiles.py`: a Python script for converting the CD's binary random number files into a more easily-used format  
* **`Downloader.py`:** the Python script used to download the FTP archive  
* **`Label.gif`:** label design used in the original release  

The `Diehard` has since been updated and renamed [`Dieharder`](https://webhome.phy.duke.edu/~rgb/General/dieharder.php) by Robert G. Brown of the Duke University Physics Department.

One final note: `Diehard` and it's subsequent iterations have been highly influential in statistics, cryptography, and related research. That said, software is made by humans, who often have flaws. In some of the included papers (which were part of the original CD-ROM), Marsaglia repeatedly refers to his using images of "naked ladies" as inputs to his generators as well as rap music, which he calls "black noise." This sexist and racist language should not have been acceptable to his fellow researchers in 1995 and certainly isn't today... and people wonder there aren't enough women and people of color in tech.


## ORIGINAL README  
*The CD-ROM included the file `cdrom.doc` which includes this README information (with some typographical improvements from me). The original file is in the `CD-ROM` folder in this repo.*

This CDROM contains 4.8 billion random bits in sixty 10-megabyte files, `bit.01`, `bit.02`, ..., `bit.60`. They are a combination of some of the best deterministic random number generators with three commercial devices that claim to produce true randomness. There are three approx. 10 meg files of typical output from those devices: `canada.bit`, `germany.bit`, `calif.bit`. They fail to meet the stringent requirements of `DIEHARD`: a battery of tests of randomness, files for which are also included on this CDROM. But the sixty 10-meg files `bit.01`, ..., `bit.60` seem to pass all tests of randomness and independence, and they are offered here as a source for those doing serious Monte Carlo work, who absolutely positively have to have a reliable source of random bits. 

Details of the method for producing the bits are in the postscript file `cdmake.ps`. There are three other postscript files that give further information.

The file structure of this CDROM is simple: the root directory with
the sixty files of what I claim to be virtually unassailable sources
of random bits, and the three files of output from physical devices
for which claims of perfect randomness have been made, but `DIEHARD` refutes.

In addition, the root directory has four subdirectories:

**`pscript:`** Four postscript files, `cdmake.ps`, `keynote.ps`, `monkey.ps`, `mwc1.ps`, describing the making of this disk and background theory for tests and RNG's.

**`dos:`** Files for describing and running `DIEHARD` on 386/486+ PC's under dos.

**`sun:`** Files for describing and running `DIEHARD` on Sun platforms under unix.

**`linux:`** Files for describing and running `DIEHARD` on i486+ sytems under linux.               

**`source:`** Source files for `DIEHARD`, in C, translated from Fortran files by f2c. The `DIEHARD` battery of tests can be constructed from them, for other platforms.


## COPYRIGHT NOTICE  
From the CD-ROM:

    Research sponsored by the National Science Foundation (Grants DMS-8807976 and DMS-9206972),
    copyright 1995 George Marsaglia

