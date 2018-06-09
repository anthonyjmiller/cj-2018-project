# Adding Census tract ID info to crime data


First, install the **geopandas** library:


```sh
$ conda install geopandas
```

Assuming that `static/data/crimes.csv` contains the data as downloaded from Chicago. Running `bootstrap.py`:


```sh
$ python helpers/bootstrap.py
```

Will create a file named: `static/data/tractcrimes.csv`, which is just `crimes.csv` but with a `tract_id` column.

