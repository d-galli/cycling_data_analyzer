# Cycling Data Analyzer
This is a personal project aimed to retrieve useful information about athletic performances by analysing data from sensors, sepcifically Garmin Edge.

## Converting Garmin FIT to CSV (and GPX to CSV)
Requirements:

* Python 3.5+
* BeautifulSoup
* fitparse

    sudo pip3 install fitparse
* tzwhere (to localize timezones)

    sudo pip3 install tzwhere
* pytz (to localize timezones)

    sudo pip3 install timezones
* numpy (to calculate workout variables)
    sudo pip3 install numpy

To process FIT files, copy them into *FIT_source* folder, then run:

    python3 process_all.py --subject-name = mysubjectname --fit-source-dir=~/cycling_data_analyzer/FIT_source/

This will create a bunch of CSVs for all of your workouts in the directory *CSV_generated* directory. The files will be stored in a subject_data directory's subdirectory (check the defaults for the specific folders), which is generated based off the subject name. Up to 3 files are made per FIT file:

A CSV of all of the track data

A CSV of the lap data

A CSV of the start (and stop) data

Each of the CSVs is in the format '{activity_type}YY-MM-DD_HH-MM-SS[{laps,starts}].csv.

You can also provide a csv to censor certain geographic regions by latitude, lo.ngitude, and radius. Simply create a CSV with longitude, latitude, and radius column headers, and add as many circular regions as you want. Note that radius is assumed to be in meters.

    python3 process_all.py --subject-name=mysubjectname --fit-source-dir=~/cycling_data_analyzer/FIT_source/ --censorfile=~/cycling_data_analyzer/CENSOR_source/censor.csv --censor

This will be stored in a folder called "censored" that is in the subject's directory. You can use the --censor-string= to change what censored fields are replaced with (default is [CENSORED]).

You can also archive the data after it's been processed:

    python3 process_all.py --subject-name=mysubjectname --fit-source-dir=~/cycling_data_analyzer/FIT_source/ --censorfile=/cycling_data_analyzer/CENSOR_source/censor.csv --censor --archive-results

By default, this stores data in a directory called archives in the main subject_data folder. You can add the --archive-censored-only, which will only archive the censored folder.

 ### GPX data
You can also process GPX data (and censor it the same way as FIT data)

For the initial processing, you can do

    python3 process_all.py --subject-name=mysubjectname --skip-fit-conversion gpx-source-dir=/home/mydir/gpx_files
By default, the program will always try to copy/process FIT files unless you add the --skip-fit-conversion flag, but you can always tweak the code to your needs.

### Additional Help
You can use python3 process_all.py --help to see more information.