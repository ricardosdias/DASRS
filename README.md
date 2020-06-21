# Decreased Anomaly Score by Repeated Sequence (DASRS)
###### An Anomaly Detection Algorithm for Time Series

![alt text](doc/img/dasrs.png "Decreased Anomaly Score by Repeated Sequence")

The DASRS algorithm identifies and counts the sequences of normalized values that appear in a time series and generates an anomaly score as a function of the number of times it identifies each sequence. We normalize observed values to limit the number of distinct sequences without changing the main characteristics of a time series. As the normalization reduces the number of distinct sequences, we can increase the performance of the anomaly detection algorithm. The first time DASRS identifies a given sequence, the returned score is as high as possible because the algorithm interprets it as a new behavior. Otherwise, the returned score decreases as the number of times a given sequence is found.

### Sequence

Let <img src="https://render.githubusercontent.com/render/math?math=X_t "> be a time series with the observations <img src="https://render.githubusercontent.com/render/math?math=x_1, x_2, \dots ">. A sequence of <img src="https://render.githubusercontent.com/render/math?math=X_t "> is a subset of <img src="https://render.githubusercontent.com/render/math?math=X_t "> consisting of consecutive elements, for example, <img src="https://render.githubusercontent.com/render/math?math=x_i, \dots, x_j ">, with <img src="https://render.githubusercontent.com/render/math?math=i < j ">.

Let X<sub>t</sub> be a time series with the observations x<sub>1</sub>, x<sub>2</sub>, ... . A sequence of X<sub>t</sub> is a subset of X<sub>t</sub> consisting of consecutive elements, for example, x<sub>i</sub>, ..., x<sub>j</sub>, with i < j.

### Normalization
The normalization applied by DASRS consists of transforming the observation value into an integer between <img src="https://render.githubusercontent.com/render/math?math=0 "> and a normalization factor that we call <img src="https://render.githubusercontent.com/render/math?math=\theta ">. The equation below represents the operations performed on <img src="https://render.githubusercontent.com/render/math?math=x_i "> to get its normalized value (<img src="https://render.githubusercontent.com/render/math?math=x_i'">):

The normalization applied by DASRS consists of transforming the observation value into an integer between 0 and a normalization factor that we call θ. The equation below represents the operations performed on x<sub>i</sub> to get its normalized value (x<sub>i</sub>'):


<img src="https://render.githubusercontent.com/render/math?math=x_i' = \Big\lfloor \frac{x_i - min_X}{max_X - min_X} \times \theta \Big\rfloor ">

Where <img src="https://render.githubusercontent.com/render/math?math=x_i"> is the input observation (<img src="https://render.githubusercontent.com/render/math?math=x_i \in \mathbb{R} ">), <img src="https://render.githubusercontent.com/render/math?math=min_X "> and <img src="https://render.githubusercontent.com/render/math?math=max_X "> are respectively the smallest and highest possible observation values of <img src="https://render.githubusercontent.com/render/math?math=X_t ">. <img src="https://render.githubusercontent.com/render/math?math=\theta ">  represents the normalization factor, <img src="https://render.githubusercontent.com/render/math?math=x_i' "> is the normalized value of <img src="https://render.githubusercontent.com/render/math?math=x_i "> observation, <img src="https://render.githubusercontent.com/render/math?math=x_i' \in \mathbb {N} "> and <img src="https://render.githubusercontent.com/render/math?math=0 \leq x_i' \leq \theta ">.


