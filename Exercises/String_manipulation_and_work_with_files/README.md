# Tasks
## Weather
Write a read_line(filename) function that reads and returns a list of lines in the file_name.

Example for the file data.txt:
```
>>> read_lines ('data.txt')
['Ljubljana; cloudy; 12.1', 'Maribor; sunny; 9', 'Koper; sunny; 14.7']
```
Write a read_csv(filename) function that opens and reads the file filename, which contains semicolon-separated weather data (location, weather, and temperature) in each line, and returns them as a list of files.
```
>>> data = read_csv ('data.txt')
>>> data
[('Ljubljana', 'cloudy', 12.1), ('Maribor', 'sunny', 9.0), ('Koper', 'sunny', 14.7)]
```
Write a format (data) function that accepts a list of tuple data with weather data and returns a list of strings that are formatted as shown below:
```
>>> format (data)
['City: Ljubljana, Weather: cloudy, Temperature: 12.1 ° C',
 'Location: Maribor, Weather: sunny, Temperature: 9.0 ° C',
 'City: Koper, Weather: sunny, Temperature: 14.7 ° C']
```
The output from the previous task was not formatted, so we decide to write the data in the table. To do this, write a form_table (data) function that returns a list of arrays that are formatted as shown.
```
>>> format_table (data)
['End Time Temperature (° C)',
 '------------------------------------------------' ,,
 'Ljubljana cloudy 12.1',
 'Maribor sunny 9.0',
 'Koper sunny 14.7']
```
Write the function form_table_f(data) so that the temperature will be displayed in the Fahrenheit scale. Round the result to one decimal place.
```
>>> format_table_f (data)
['End Time Temperature (° F)',
 '------------------------------------------------' ,,
 'Ljubljana cloudy 53.8',
 'Maribor sunny 48.2',
 'Koper sunny 58.5']
```
The printout could be even more transparent if the table were formatted as shown below (documentation). To do this, write a dot_form(data) function.
```
>>> form_pike (data)
['End Time Temperature (° F)',
 '------------------------------------------------' ,,
 'Ljubljana ....... cloudy ..................... 53.8',
 'Maribor ......... sunny ...................... 48.2',
 'Koper ........... sunny ...................... 58.5']
```
In the last column, display the temperature in Fahrenheit and Celsius with function the form_fc(data)
```
>>> form_fc (data)
['End Time Temperature ° F (° C)',
 '------------------------------------------------' ,,
 'Ljubljana ....... cloudy .............. 53.8 (12.1)',
 'Maribor ......... sunny ................ 48.2 (9.0)',
 'Koper ........... sunny ............... 58.5 (14.7)']
```
Write a function save(lines, file_name) that saves a list of line strings each in its own line in file filename.
```
>>> save (['first line', 'second line', 'third line'], 'file.txt')
```
## The longest words
Write the longest_word(s) function, which finds all the longest words in the string s and returns them separated by commas.
```
>>> the longest_words ('it will be ten and five minutes at the sign')
'sign, ten, minute'
```
## .py
List all files in the current directory that have a .py extension.

If you find the task too easy, try writing a program that lists all .py files in the current directory and all subdirectories of the current directory. So, if you are in the /home/glenda directory, your program must find both the /home/glenda/p9.py file and the /home/glenda/plan9/from/outer/space.py file.

## ID3v1
Write a function that reads all files with the .mp3 extension in the specified directory and composes the displayed output:
```
 Title: Tonight
Artist: Slon in Sadez
 Album: Sponsorska plata - NeCenzurira
  Year: 2010
  File: 10 Slon in Sadez - Nocoj.mp3

 Title: Warning
Artist: Slon in Sadez
 Album: Sponsorska plata - NeCenzurira
  Year: 2010
  File: 17 Slon in Sadez - Opozorilo.mp3
  ```
You may not read the song information from the file name but from its contents. To do this, read the last 128 characters of the file. If the first three characters of this string are not the same as "TAG" then the artist data file does not contain and should be skipped. Otherwise, the next 30 characters contain the title of the song, the next 30 the name of the artist, the next 30 the name of the album and the next 4 the year of release. If the title of the song, artist or album name is less than 30 characters, the appropriate number of "\ x00" characters will be added at the end of the string, which you will need to remove.

You can use selected Elephant and Fruit songs from the freely available Sponsorship Board for testing.

## Plagiarist
Unzip the directory with ten files and find the plagiarist! Write a program that determines in which two files at least 1000 characters are repeated.
