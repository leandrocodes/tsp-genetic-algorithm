# Traveling Salesman Problem - A Genetic Algorithm implementation
This is my first implementation of a Genetic Algorithms using Python.
## The problem

### A salesman intends to elaborate a script to visit a total of 6 cities in the state of Mato Grosso do Sul.
  
Giving the following table, extract the minimum shortest distance, going through all the points, starting and ending through Campo Grande without leaving any city outside, or passing twice or more through the same city point.
|  | Campo Grande | Bonito | Corumbá | Dourados | Camapuã | Água Clara
|--|--|--|--|--|--|--
| Campo Grande
| Bonito | 325km
| Corumbá | 420km | 335km
| Dourados | 230km | 270km | 588km
| Camapuã | 143km | 285km | 563km | 373km
| Água Clara | 189km | 474km | 609km | 413km | 213km

And its got converted to a JSON file:

    graph.json

To run this project, make sure that you have python installed. Then simply run this command line:

    python tsp.py
