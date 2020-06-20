# Decreased Anomaly Score by Repeated Sequence (DASRS)

![alt text](doc/img/dasrs.png "Decreased Anomaly Score by Repeated Sequence")

The DASRS algorithm identifies and counts the sequences of normalized values that appear in a time series and generates an anomaly score as a function of the number of times it identifies each sequence. The first time DASRS identifies a given sequence, the returned score is as high as possible because the algorithm interprets it as a new behavior. 
Otherwise, the returned score decreases as the number of times a given sequence is found.
