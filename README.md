# HENI tech test

## Installation

tested with Python 3.7.3+
- create a virtual environment
- clone repo `git clone https://github.com/ahmadRazaa/HENItest.git`
- move to project directory `cd HENItest`
- install dependencies by `pip install -r requirements.txt`


## Task 1

code for parsing `candidateEvalData > webpage.html`HTML can be found in dir `task1`.
to execute follow:

- `cd task1`
- `python3 parsing_html.py`

## Task 2

Following regex can be used to extract height, width and depth from rawDim strings

19×52cm   
```
r'(\d+)×(\d+)cm'
```

50 x 66,4 cm   
```
r'(\d+(?:,\d+)?)\s*x\s*(\d+(?:,\d+)?)\s*cm'
```

168.9 x 274.3 x 3.8 cm (66 1/2 x 108 x 1 1/2 in.)   
```
r'(\d+(?:.\d+)?)\s*x\s*(\d+(?:.\d+)?)\s*x\s*(\d+(?:.\d+)?)\s*cm'
```

Sheet: 16 1/4 × 12 1/4 in. (41.3 × 31.1 cm) Image: 14 × 9 7/8 in. (35.6 × 25.1 cm)   
```
r'Image.*\((\d+(?:.\d+)?)\s*×\s*(\d+(?:.\d+)?)\s*cm'
```

5 by 5in   
```
r'(\d+)\s*by\s*(\d+)\s*in'
```

## Task 3

web crawler to crawl gallery's listing can be found under dir `task3 > bearspacescraper > bearspacescraper > spiders > bearspace_spider.py`

project contains two spiders:
- bearspace-parse
- bearspace-crawl

**bearspace-parse** can be used to parse a single artwork/page by following command  
```
scrapy parse
--spider=bearspace-parse
"https://www.bearspace.co.uk/product-page/ore-by-vic-wright" 
```



**bearspace-crawl** can be used to crawl all gallery's listing of works available for sale by following command    
```
scrapy crawl bearspace-crawl -o data.csv
```

## Task 4

Following are the SQL queries and joins asked, can also be found under dir `task4` 

#### Task 4.1:

**Inner join:**  
Inner join is a type of join that returns all rows from both the tables where the key record of one table is equal to the key records of another table.

**Left join:**  
Left join is a type of join that returns all rows from the left table, and the matching rows from the right table.

**Right join:**  
Right join is a type of join that returns all rows from the right table, and the matching rows from the left table.

**Full join:**  
Full join combines the results of both left and right outer joins. The joined table will contain all records from both the tables and fill in NULLs for missing matches on either side.


#### Task 4.2:

**1**  
  
```
SELECT flights.arr_time, flights.origin, flights.dest, airlines.name  
FROM flights  
INNER JOIN airlines ON flights.carrier = airlines.carrier  
```

**2**  

```
SELECT flights.arr_time, flights.origin, flights.dest, airlines.name  
FROM flights  
INNER JOIN airlines ON flights.carrier = airlines.carrier  
WHERE airlines.name LIKE '%JetBlue%'  
```

**3**  

```
SELECT origin, count(origin)  
FROM flights  
GROUP BY origin  
```

**4**  

```
SELECT origin, count(origin)  
FROM flights  
GROUP BY origin  
HAVING COUNT(origin) > 10000  
```