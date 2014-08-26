register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by subject column
subjects = group ntriples by (subject) PARALLEL 50;

-- flatten the objects out (because group by produces a tuple of each object
-- in the first column, and we want each object ot be a string, not a tuple),
-- and count the number of tuples associated with each object
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

--order the resulting tuples by their count in descending order
group_by_count = group count_by_subject by (count) PARALLEL 50;
frequency = foreach group_by_count generate flatten($0), COUNT($1) as freq PARALLEL 50;

frequency_ordered = order frequency by (freq)  PARALLEL 50;

freq_group = group frequency_ordered ALL;

freq_count = foreach freq_group generate COUNT(frequency_ordered); 

-- store the results in the folder /user/hadoop/example-results
--store freq_count into '/user/hadoop/histogram2B' using PigStorage();
dump freq_count;
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman/example-results';


-- START Question 6
register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-*' USING TextLoader as (line:chararray);
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);
subjects = group ntriples by (subject) PARALLEL 50;
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;
group_by_count = group count_by_subject by (count) PARALLEL 50;
frequency = foreach group_by_count generate flatten($0), COUNT($1) as freq PARALLEL 50;
frequency_ordered = order frequency by (freq)  PARALLEL 50;
freq_group = group frequency_ordered ALL;
freq_count = foreach freq_group generate COUNT(frequency_ordered); 
dump freq_count;

-- End Question 6
