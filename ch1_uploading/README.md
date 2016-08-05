# Uploading Data

So, you have some data in a __file__ (e.g. `.csv`,`.xlsx`,`.dta`) and or in a __database__ somewhere.  This section will describe how you can __access the data__ based on where the data is stored.

Here are links to the specific parts of this section:
- <a href="#dfs">What is a Dataframe?</a>
- <a href="#files">Reading Files</a>
- <a href="#dbs">Querying Databases</a>

### <a name="dfs">What is a Dataframe?</a>

But first, let's briefly talk about how the data structures.  When analyzing data, both Python and R use a structure called a __dataframe__.  Sounds fancy, yes, but really a dataframe is __just a special kind of table__ stored in memory.  Dataframes have columns and rows like a spreadsheet does.  The benefit of a dataframe is that you can manipulate these "tables" using code rather than having to build mammoth spreadsheets.

*Key take away: Dataframe = Table*

### <a name="files">Reading Files</a>
How do you access data stored in a file on a computer?  Both Python and R have ways to import most file formats (e.g. `.csv`,`.xlsx`,`.dta`) directly into a dataframe.  So, in most cases, this should reduce your code to just a couple lines.

In the examples below, let's layout some basic assumptions. 
- We will call our dataframe `df` 
- `pandas` is a Python package required to mimic the dataframe structure native to R
- Our fake file is located in folder `C:/my_project/data`

#### Python

#### R

### <a name="dbs">Querying Databases</a>
