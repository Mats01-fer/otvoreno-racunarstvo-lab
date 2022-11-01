
Licence:
[CC0 1.0 Universal (CC0 1.0)
Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)

**Autor:** Matej Butković

**Version:** 1.0


# Dataset
Jezik podataka: english

## Tablice i atributi
![databse schema](orf1%20-%20public.png)

### Driver
- id
- name
- surname
- code
- dob
- nationality

<!-- turn driver into markdown table -->
Primjer:
| id | name | surname | code | dob |
| --- | --- | --- | --- | --- |
| 1 | Lewis | Hamilton | HAM | 1985-01-07 |


### Season
- year

Primjer:
| year |
| --- | 
| 2022 |

### Constructor
- id
- name
- nationality

Primjer:
| id | name |
| --- | --- |
| 1 | Mercedes |

### Circuit
- id
- name
- location
- country
- alt 
- lon
- lat 

Primjer:
| id | name | location | country | alt | lon | lat |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Albert Park | Melbourne | Australia | 10 | 144.968 | -37

### Grandprix
- id
- name
- year
- round
- circuitid
- date

Primjer:
| id | name | year | round | circuitid | date |
| --- | --- | --- | --- | --- | --- |
| 1 | Australian Grand Prix | 2022 | 1 | 1 | 2022-03-26 |

### Driver in season 
- driverid
- year
- constructorid
- number

Primjer:
| driverid | year | constructorid | number |
| --- | --- | --- | --- |
| 1 | 2022 | 1 | 44 |

### Raceresult
- fastestLapTime 
- grid 
- position 
- laps 
- time 
- fastestLap 
- points 
- status 
- driverID INT 
- Year 
- constructorID INT 
- GPID INT 

Primjer:
| fastestLapTime | grid | position | laps | time | fastestLap | points | status | driverID | Year | constructorID | GPID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1:30.000 | 1 | 1 | 58 | 1:30.000 | 1 | 25 | Finished | 1 | 2022 | 1 | 1 |





## More info
Dataset kojim sam punio ovu bazu podataka nalazi se na https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020