# Hadoop MapReduce on Docker — Cloud Computing HW3 (Phase 1)
**Amirkabir University of Technology | Fall 2024**  
**Course: Fundamentals of Cloud Computing**

## Overview
A local Hadoop cluster running on Docker, with two MapReduce jobs implemented in Python using Hadoop Streaming.

## Cluster Setup
The cluster runs via Docker Compose with two containers:
- **NameNode** — manages the HDFS filesystem and metadata
- **DataNode** — stores actual data blocks

```bash
git clone https://github.com/sadegh-msm/hind.git
cd hind
sh start-hadoop.sh      # bring cluster up
sh stop-hadoop.sh       # bring cluster down
```

- NameNode UI: `http://localhost:50070`
- DataNode UI: `http://localhost:50075`

## MapReduce Jobs

### Task 1 — Inverted Index (`mapper.py` / `reducer.py`)
For each word in a document corpus, outputs the set of document IDs containing that word.

**Input format:** `docID,text content`  
**Output format:** `word doc1 doc2 ...`

### Task 2 — Top-K Words per Document (`mapper2.py` / `reducer2.py`)
Finds the top K most frequent words in each document (K=3).

**Input format:** `docID,text content`  
**Output format:** `docID,word,count`

## Running a Job
```bash
# Copy scripts into NameNode
docker cp mapper.py namenode:/mapper.py
docker cp reducer.py namenode:/reducer.py

# Upload input to HDFS
docker exec namenode hdfs dfs -mkdir /input
docker exec namenode hdfs dfs -put input1.txt /input/

# Run Hadoop Streaming job
docker exec namenode hadoop jar \
  /opt/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar \
  -files mapper.py,reducer.py \
  -mapper mapper.py -reducer reducer.py \
  -input /input/input1.txt -output /output
```

## Files
| File | Description |
|------|-------------|
| `docker-compose.yml` | Hadoop cluster definition |
| `hadoop.env` | Hadoop environment config |
| `init.sh` / `start-hadoop.sh` | Cluster startup scripts |
| `data/namenode/mapper.py` | Inverted index mapper |
| `data/namenode/reducer.py` | Inverted index reducer |
| `data/namenode/mapper2.py` | Top-K words mapper |
| `data/namenode/reducer2.py` | Top-K words reducer |
| `data/namenode/input1.txt` | Input for Task 1 |
| `data/namenode/input2.txt` | Input for Task 2 |
