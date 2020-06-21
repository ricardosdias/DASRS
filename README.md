# Decreased Anomaly Score by Repeated Sequence (DASRS)
###### An Anomaly Detection Algorithm for Time Series

![alt text](doc/img/dasrs.png "Decreased Anomaly Score by Repeated Sequence")

The DASRS algorithm identifies and counts the sequences of normalized values that appear in a time series and generates an anomaly score as a function of the number of times it identifies each sequence. We normalize observed values to limit the number of distinct sequences without changing the main characteristics of a time series. As the normalization reduces the number of distinct sequences, we can increase the performance of the anomaly detection algorithm. The first time DASRS identifies a given sequence, the returned score is as high as possible because the algorithm interprets it as a new behavior. Otherwise, the returned score decreases as the number of times a given sequence is found.

### Sequence

Let X<sub>t</sub> be a time series with the observations x<sub>1</sub>, x<sub>2</sub>, ... . A sequence of X<sub>t</sub> is a subset of X<sub>t</sub> consisting of consecutive elements, for example, x<sub>i</sub>, ..., x<sub>j</sub>, with i < j.

### Normalization

The normalization applied by DASRS consists of transforming the observation value into an integer between 0 and a normalization factor that we call θ. The equation below represents the operations performed on x<sub>i</sub> to get its normalized value (x<sub>i</sub>'):

<img src="https://render.githubusercontent.com/render/math?math=x_i' = \Big\lfloor \frac{x_i - min_X}{max_X - min_X} \times \theta \Big\rfloor ">

Where x<sub>i</sub> is the input observation (x<sub>i</sub> ∈ R, min<sub>X</sub> and max<sub>X</sub> are respectively the smallest and highest possible observation values of X<sub>t</sub>. θ  represents the normalization factor, x<sub>i</sub>' is the normalized value of x<sub>i</sub> observation, x<sub>i</sub>' ∈  N and 0 ≤ x<sub>i</sub>' ≤ θ.