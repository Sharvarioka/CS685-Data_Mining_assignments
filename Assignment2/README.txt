assign1.sh is the top-level scrip which generates results of all the scripts.

Following points describe the plugins and dependencies needed to run the assignment.It is mentioned question wise.
1. Run question1.sh
---> It generates two files after running question1.sh

articles-ids.json
---> This is the file used for internal processing consisting of article name and article id.

article-ids.csv
---> which contains the article name and corresponding article id assigned from A0001 to A4604.

2. Run question2.sh
It outputs a file: category-ids.csv
---> which contains category name and category id starting from C0001 to C0146.

3. Run question3.sh
It creates article-categories.csv. 
---> which contains article id and its corresponding category ids.

4. Run question4.sh
It outputs a file: edges.csv
---> which contains edges between articles.	

5. Run question5.sh
It creates a file: graph-components.csv
---> which contains nodes, edges and diameter of each connected component

This programs takes approximately 18-20 minutes to run on my system.

I have used networkx library which gives connected components having more than two nodes and hence I have added the rest 12 isolated articles manually with nodes=1,edges=0 and diameter=0

6. Run question6.sh
It creates 2 files: 
	finished-paths-no-back.csv  
	finished-paths-back.csv.
---> which calculate human path length,shortest path length and their ratio not considering the backlinks and considering the backlinks respectively.	 
	 

7. Run question7.sh
It creates 2 files:
	 percentage-paths-no-back.csv  
	 percentage-paths-back.csv
---> which show percentage of human paths that have equal path length as the shortest path,path length is 1 to 10 more than the shortest path (each separately) and path length is 11 or more than the shortest path in separate column.

8. Run question8.sh
It creates a file: category-paths.csv
---> which shows number of human paths traversed, number of times human path traversed, number of shortest paths traversed, number of times shortest path traversed by particular category.

I have not considered the paths which have only one entry(article) in the paths_finished.tsv.

I have not considered the path 'Bird;Wikipedia_Text_of_the_GNU_Free_Documentation_License' from paths_finished.tsv since there is no shortest path available for 'Bird' as  source and 'Wikipedia_Text_of_the_GNU_Free_Documentation_License' as destination.


9. Run question9.sh
It creates a file: category-subtree-paths.csv
---> which shows number of human paths traversed, number of times human path traversed, number of shortest paths traversed, number of times shortest path traversed by particular category considering all its subcategories as well.

I have not considered the paths which have only one entry(article) in the paths_finished.tsv.

I have not considered the path 'Bird;Wikipedia_Text_of_the_GNU_Free_Documentation_License' from paths_finished.tsv since there is no shortest path available for 'Bird' as  source and 'Wikipedia_Text_of_the_GNU_Free_Documentation_License' as destination.


10. Run question10.sh

It creates a file: category-pairs.csv
---> which shows percentage for the occurrence of particular category pair in unfinished and finished path.

I have not considered the paths which have only one entry(article) in the paths_finished.tsv.

The articles which where present in paths_unfinished.tsv but not in articles.tsv are assigned the category C0001.

Some spelling corrections are made in the article names of the paths_unfinished.tsv.


11.Run question11.sh
It creates a file: category-ratios.csv
---> which shows the ratio between human path and shortest path for every source and destination pair.




