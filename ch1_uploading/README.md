# Uploading Data

So, you have some data in a __file__ (e.g. `.csv`,`.xlsx`,`.dta`) and or in a __database__ somewhere.  This section will describe how you can __access the data__ based on where the data is stored.

Here are links to the specific parts of this section:
- <a href="#dfs">What is a Dataframe?</a>
- <a href="#files">Reading Files</a>
- <a href="#dbs">Querying Databases</a>

### <a name="dfs"><u>What is a Dataframe?</u></a>

But first, let's briefly talk about how the data structures.  When analyzing data, both Python and R use a structure called a __dataframe__.  Sounds fancy, yes, but really a dataframe is __just a special kind of table__ stored in memory.  Dataframes have columns and rows like a spreadsheet does.  The benefit of a dataframe is that you can manipulate these "tables" using code rather than having to build mammoth spreadsheets.

*Key take away: Dataframe = Table*

<hr>

### <a name="files"><u>Reading Files</u></a>
How do you access data stored in a file on a computer?  Both Python and R have ways to import most file formats (e.g. `.csv`,`.xlsx`,`.dta`) directly into a dataframe.  So, in most cases, this should reduce your code to just a couple lines.

In the examples below, let's layout some basic assumptions. 
- We will assume to be working with client-level data, thus will call our dataframe `clients` 
- `pandas` is a Python package required to mimic the dataframe structure native to R
- Our fake file is located in folder `C:/my_project/data`

#### Python
```python
import pandas as pd

data = pd.read_csv("C:/Users/jsmith/my_data.csv")
```
#### R
In R, you should use one of the `read` functions to import your data.  For example, if importing a `.csv` file, then you should use the `read.csv` function.
```r
clients <- read.csv("C:/my_project/data/clients.csv", header=TRUE, stringsAsFactors=FALSE)
```

For `.xlsx` files, use the `read...` function.


For `.dta` files (via Stata), use the `read...` function.

<hr>

### <a name="dbs"><u>Querying Databases</u></a>

