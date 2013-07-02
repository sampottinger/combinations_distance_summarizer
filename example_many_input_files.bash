# Demonstrates how to run many input files with summarizer.py
# 
# Simple bash snippet that demonstrates how to run summarizer.py with many
# input files (many files each with a list of words to summarize) while using
# the same distance matrix CSV.
#
# Author: A. Samuel Pottinger (2013)
# License: MIT
#

while read target; do
  echo $target >> combined_values.txt;
  python summarizer.py $target HowellNounDistances.csv >> combined_values.txt;
  echo >> combined_values.txt;
done < word_list_files.txt