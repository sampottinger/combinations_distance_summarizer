while read target; do
  echo $target >> combined_values.txt;
  python summarizer.py $target HowellNounDistances.csv >> combined_values.txt;
  echo >> combined_values.txt;
done < word_list_files.txt