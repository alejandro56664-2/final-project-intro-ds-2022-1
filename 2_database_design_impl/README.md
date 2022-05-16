# EXERCISE – DATABASE DESIGN/IMPLEMENTATION.

## DESCRIPTION

The goal of this exercise is to reinforce concepts and processes about database design and implementation. In this exercise, for the data used in their particular term project, each project team will need to perform i) some relational database modeling and implementation, and ii) some NoSQL database modeling and implementation. This homework must be done by the particular teams assigned to develop the term projects.
Deliverables:

I. A document with a detailed description of the modeling and implementation of the two database approaches which should include at least:

- A description of the domain and the problem tackled in the term project.
- A detailed description of the data to manage in the problem.
- A relational database model and implementation for your data.
- A NoSQL database model and implementation for your data.
- A comparison of the relational and NoSQL databases implemented needs to be includes, stating which of the two models is more suitable to handle your data.
- In both cases, the rationale for the selection of the software tools used must be included.

II. The software implementations need to be added/uploaded in the corresponding repository of your project.

The public repository for this project is:

https://github.com/alejandro56664-2/final-project-intro-ds-2022-1

## 1. Introduction

One of the main considerations to take into account when creating a project that uses data is its computational representation and future storage. Databases currently focus on managing massive amounts of data in a quick, consistent, stable and repeatable manner.

The relational model is based on mathematical theory (set theory, relational theory) whereas the nonrelational databases may or may not have a single
groundwork. Relational databases are beneficial when it comes to robustness, flexibility, reliability and scalability requirements but in order to cater to the needs of modern applications where the data is huge and generally unstructured; Non-relational databases show true signs of usability aiming at being "developer-friendly".

SQL databases are most often implemented in a scale-up architecture, which is based on using ever larger computers with more CPUs and more memory to improve performance. NoSQL databases were created in Internet and cloud computing eras that made it possible to more easily implement a scale-out architecture, where scalability is achieved by spreading the storage of data and the work to process the data over a large cluster of computers. To increase capacity, more computers are added to the cluster.

Still, many Non-relational databases are disk-based which implement buffer pool and multithreading hence require buffer management and locking features which add on to performance overhead. Also, many provide BASE properties and sacrifice conventional ACID properties as a step to increase performance. That's why the degree of reliability provided by non-relational databases is lower than what is provided by the relational databases. Developers have to rope in programming to apply ACID restraints which could have been provided easily in relational databases.

We will compare two implementations of our database model (one Relational in PostgreSQL and one Non-relational in MongoDB) and pick the best given the implementation requirements based on our domain and the intrinsic characteristics of our data, its ease of access, performance and scalability.

## 2. Domain description

TODO

## 3. Data description

For this PoC (Proof of Concept) only a small portion of the data (~10 samples) will be used to perform the Transform and Load tests on the data from the original file structure and formats. This data can be found in `./data/`.

Document example in the 'Bad' code dataset:

```json
{
  "3f75c5788ea80f1ea8de77ed565a3281": {
    "code_string": "def test_delitem_keyerror(self):\n    e = EntryBase(req_()\n    del e['missing_key']\n",
    "code_toks_joined": "def test_delitem_keyerror ( self ) : <NEWLINE> <INDENT> e = EntryBase ( req_ ( ) <NEWLINE> del e [ <STRING> ] <NEWLINE> <DEDENT>",
    "anonymize_dict": {
      "<STRING>": ["'missing_key'"]
    },
    "err_obj": {
      "msg": "unbalanced (){}[]"
    }
  }
}
```

Document example in the 'Good' code dataset:

```json
{
  "1bdd18d071e2bd423a7f43edaf2bede6": {
    "code_string": "\"\"\"Helper functions\"\"\"\nimport datetime\nimport math\nimport pytz\nimport random\nimport re\n",
    "code_toks_joined": "<STRING> <NEWLINE> import datetime <NEWLINE> import math <NEWLINE> import pytz <NEWLINE> import random <NEWLINE> import re <NEWLINE>",
    "anonymize_dict": {
      "<STRING>": ["\"\"\"Helper functions\"\"\""]
    }
  }
}
```

## 4. First Approach: Relational Database Model

TODO

### 4.1 Data Modeling

TODO

**Figure with the proposed data model**

![sql model](./assets/exercise_db_design_impl-sql_data_model.drawio.png)

### 4.2 Rational for SQL Engine selection

TODO

**Selection criteria**

The selection criteria proposed to help choose the right database engine to carry out this exercise are described below.

- C1 Preference over open source database engines.
  - We specify the license that covers the engine.
- C2 Database engines in which the team has previous knowledge or experience, in order to reduce risks when implementing the exercise.
  - The group or individual that built or is maintaining the software.
- C3 Database engines that can be executed locally using a container tool.
  - If there's a docker supported container on https://hub.docker.com.
- C4 Preference will be given to database engines fully adopted in the industry.
  - Popularity ranking taken from https://db-engines.com/en/ranking for the month of May of 2022. It is based on:
    - Number of mentions on websites (using Google and Bing).
    - General interest (Google Trends).
    - Frequency of technical discussions about the system (Stack Overflow and DBA Stack Exchange).
    - Number of job offers (Indeed and Simply Hired).
    - Profiles in professional networks (LinkedIn).
    - Relevance in social networks (number of Tweets).

**Comparative Table**

|                              | C1          | C2                                  | C3                                   | C4      |
|------------------------------|-------------|-------------------------------------|--------------------------------------|---------|
| Oracle                       | Commercial  | Oracle                              | https://hub.docker.com/_/oraclelinux | 1262.82 |
| MySQL                        | Open Source | Oracle                              | https://hub.docker.com/_/mysql       | 1202.10 |
| Microsoft SQL Server         | Commercial  | Microsoft                           | No                                   | 941.20  |
| PostgreSQL                   | Open Source | PostgreSQL Global Development Group | https://hub.docker.com/_/postgres    | 615.29  |
| IBM Db2                      | Commercial  | IBM                                 | https://hub.docker.com/r/ibmcom/db2  | 160.32  |
| Microsoft Access             | Commercial  | Microsoft                           | No                                   | 143.44  |
| SQLite                       | Open Source | Dwayne Richard Hipp                 | No                                   | 134.73  |
| MariaDB                      | Open Source | MariaDB Corporation                 | https://hub.docker.com/_/mariadb     | 111.13  |
| Snowflake                    | Commercial  | Snowflake Computing Inc.            | No                                   | 93.51   |
| Microsoft Azure SQL Database | Commercial  | Microsoft                           | No                                   | 85.33   |

## 5. Second Approach: NoSQL Database Model

TODO

### 5.1 Data Modeling

TODO

**Figure with the proposed data model**

![nosql model](./assets/exercise_db_design_impl-nosql_data_model.drawio.png)

TODO

### 5.2 Rational for NoSQL Engine selection

For simplicity, the same criteria used to select software tools (relational database engines) are used here.

**Comparative Table**

|                 | C1          | C2                                                        | C3                                             | C4     |
|-----------------|-------------|-----------------------------------------------------------|------------------------------------------------|--------|
| MongoDB         | Open Source | MongoDB, Inc                                              | https://hub.docker.com/_/mongo                 | 478.24 |
| Redis           | Open Source | Redis project core team, inspired by Salvatore Sanfilippo | https://hub.docker.com/_/redis                 | 179.00 |
| Elasticsearch   | Open Source | Elastic                                                   | https://hub.docker.com/_/elasticsearch         | 157.69 |
| Cassandra       | Open Source | Apache Software Foundation                                | https://hub.docker.com/_/cassandra             | 118.01 |
| Splunk          | Commercial  | Splunk Inc.                                               | No                                             | 96.35  |
| Amazon DynamoDB | Commercial  | Amazon                                                    | https://hub.docker.com/r/amazon/dynamodb-local | 84.46  |
| Neo4j           | Open Source | Neo4j, Inc.                                               | https://hub.docker.com/_/neo4j                 | 60.14  |
| Solr            | Open Source | Apache Software Foundation                                | https://hub.docker.com/_/solr                  | 57.26  |
| Databricks      | Open Source | Databricks                                                | No                                             | 47.85  |
| HBase           | Open Source | Apache Software Foundation                                | No                                             | 43.19  |

## 6. Implementation

This section describes the steps to replicate the data models deployed to the selected database engines.

Important:
In this proof of concept, containerized database engines using docker compose do not have persistence configured.

![exercise schema](./assets/exercise_db_design_impl-exercise_scheme.drawio.png)

### 6.1 Software requeriments

To replicate this work we recommend having the following software installed on your computer:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/products/docker-desktop/)

### 6.2 Steps to execute

Clone the repository:

```sh
git clone git@github.com:alejandro56664-2/final-project-intro-ds-2022-1.git
```

Move to the folder:

```sh
cd final-project-intro-ds-2022-1/2_database_design_impl
```

Create the Transform & Load Container:

```sh
cd src
docker build -t tltask .
```

Start the containers using docker compose:

```sh
cd ..
docker compose up
```

Wait until de docker compose pull the images and load the containers.

Now you can enter the path `localhost:8080` in your browser to enter Adminer, which will allow you to query the db database that contains the relational model of the data.

![login adminer](./assets/login_adminer.png)

> Remember to select 'PostgreSQL' and the server 'db'.
> The credentials can be found in the `docker-compose.yml` file.

> Remember to select 'bifi' schema.

You can query bad code using the next SQL code:

```sql
SELECT *
FROM code_snipped
WHERE not id in (SELECT code_id FROM bug)
```

Result:

![query bad code](./assets/query_bad_code.png)

The query for good code:

```sql
SELECT *
FROM code_snipped
INNER JOIN bug
ON code_snipped.id= bug.code_id
```

Result:

![query good code](./assets/query_good_code.png)

On the other hand, to query the NoSQL model, you must enter the path `localhost:8081` in your browser to access Mongo Express, which will allow you to query the data.

![login mongo express](./assets/login_mongo_express.png)

You can see the items in the bad code collection:

![mongo bad code](./assets/mongo_bad_code.png)

The items for good are shown in the image below:

![mong good code](./assets/mongo_good_code.png)

## 7. Conclusions

TODO

## 8. References

- https://docs.docker.com/compose/
- https://hub.docker.com/_/postgres
- https://hub.docker.com/_/mongo
- https://wiki.postgresql.org/wiki/Psycopg
- https://www.mongodb.com/languages/python
