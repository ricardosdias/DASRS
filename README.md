# Decreased Anomaly Score by Repeated Sequence (DASRS)

![alt text](doc/img/dasrs.png "Decreased Anomaly Score by Repeated Sequence")

The DASRS algorithm identifies and counts the sequences of normalized values that appear in a time series and generates an anomaly score as a function of the number of times it identifies each sequence. The first time DASRS identifies a given sequence, the returned score is as high as possible because the algorithm interprets it as a new behavior. 
Otherwise, the returned score decreases as the number of times a given sequence is found.

Let <img src="https://render.githubusercontent.com/render/math?math=X_t "> be a time series with the observations <img src="https://render.githubusercontent.com/render/math?math=x_1, x_2, \dots ">. A sequence of <img src="https://render.githubusercontent.com/render/math?math=X_t "> is a subset of <img src="https://render.githubusercontent.com/render/math?math=X_t "> consisting of consecutive elements, for example, <img src="https://render.githubusercontent.com/render/math?math=x_i, \dots, x_j ">, with <img src="https://render.githubusercontent.com/render/math?math=i < j ">.
The normalization applied by DASRS consists of transforming the observation value into an integer between <img src="https://render.githubusercontent.com/render/math?math=0 "> and a normalization factor that we call <img src="https://render.githubusercontent.com/render/math?math=\theta ">. The equation below represents the operations performed on <img src="https://render.githubusercontent.com/render/math?math=x_i "> to get its normalized value (<img src="https://render.githubusercontent.com/render/math?math=x_i' ">):

<img src="https://render.githubusercontent.com/render/math?math=x_i' = \Big\lfloor \frac{x_i - min_X}{max_X - min_X} \times \theta \Big\rfloor ">
