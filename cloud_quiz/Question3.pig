-- This is pig for Problem 3
register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar 


-- Start Question 4
-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- Filter the n-triples by subject column
filtered_subjects = filter ntriples by (subject matches '.*business.*');
set2 = foreach filtered_subjects generate $0 as subject2, $1 as predicate2, $2 as object2;
joined_record = join ntriples by subject, set2 by subject2;
distincted_record = distinct joined_record;
store distincted_record into '/user/hadoop/Problem4' using PigStorage();

-- End Question 4

-- Start Question 5
register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar
-- load the test file into Pig
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- Filter the n-triples by subject column
filtered_subjects = filter ntriples by (subject matches '.*rdfabout\\.com.*');
set2 = foreach filtered_subjects generate $0 as subject2, $1 as predicate2, $2 as object2;
joined_record = join filtered_subjects by object, set2 by subject2;
distincted_record = distinct joined_record;
store distincted_record into '/user/hadoop/Question5' using PigStorage();

-- End Question 5

