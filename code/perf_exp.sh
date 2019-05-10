#!/usr/bin/bash

echo "RSS,elapsed,cpu.sys,.user,k,n_words,approach,execution" | tee --append result.csv

for k in {1..10} ; do
   for nw in {1..15} ; do
           for i in {1..30} ; do
	   /usr/bin/time -f "%M,%E,%S,%U,$k,$nw,by_document,$i" python ./retrieve_by_doc.py $k $nw 

   	   done
   done

   for nw in {1..15} ; do
          for j in {1..30} ; do
	   /usr/bin/time -f "%M,%E,%S,%U,$k,$nw,by_term,$j" python ./retrieve_by_term.py $k $nw
   	  done 
   done
done 2>&1 | tee --append result.csv
