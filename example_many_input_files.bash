# Demonstrates how to run many input files with summarizer.py
# 
# Simple bash snippet that demonstrates how to run summarizer.py with many
# input files (many files each with a list of words to summarize) while using
# the same distance matrix CSV. See README.texttile first.
#
# Usage: bash example_many_input_files.bash input_file_list dist_csv out_file
# 
#   input_file_list: The TXT file with one file per line that should be used
#     as the list of words to summarize for summarizer.py. Should be file name
#     or path.
#
#   dist_csv: The CSV file with the word distances. Should be file name or path.
#
#   out_file: The file to which the results (averages) should be written.
#
# Example: bash example_many_input_files.bash word_list_files.txt
#   HowellNounDistances.csv combined_results.txt
#
# Author: A. Samuel Pottinger (2013)
# License: MIT
#

while read target; do
  echo $target >> $3;
  python summarizer.py $target $2 >> $3;
  echo >> $3;
done < $1