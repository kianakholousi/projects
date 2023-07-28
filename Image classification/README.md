# Image Classification using Graph-Based Features
This project focuses on image classification using graph-based features extracted from images. The process involves extracting nodes(keypoints/superpixel centroids) from images, building graphs based on Euclidean distance/intensity/color dominance of these nodes, extracting features, and applying various machine learning algorithms for classification.

## Installation

To use this project, you need to have the following dependencies installed:

- pandas
- numpy
- OpenCV
- networkx
- scikit-image
- scikit-learn
- category_encoders
- matplotlib

You can install these dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage

The project provides several functions for image processing and graph analysis. Here's an overview of the main functionalities:

### Superpixel Segmentation

The `slic_segmentation` function performs superpixel segmentation on an input image. It uses the SLIC algorithm to divide the image into compact and visually meaningful segments.

```python
segments = slic_segmentation(image, n_segments=250, compactness=10, sigma=1, start_label=1)
```

### Keypoint Extraction

The `keypoint_extraction` function extracts keypoints from an input image using the SIFT algorithm. It returns a list of keypoints detected in the image.

```python
keypoints = sift.detect(gray, None)
```

### Graph Construction

The project provides three different methods for graph construction based on different image features:

- **Euclidean distance**: constructing a graph based on the Euclidean distance of nodes.

```python
graph1 = graph_euclidean(superpixels_centroids)
graph2 = graph_euclidean(keypoints)
```

- **Intensity**: constructing a graph based on the similarity of intensities between nodes.

```python
graph3 = graph_intensityK(keypoints,K_intensities,threshold)
graph5 = graph_intensityS(superpixels_centroids,S_intensities,threshold)
```

- **Dominant Color**: constructing a graph based on the similarity of dominant color between nodes.

```python
graph4 = graph_dominant_colorK(keypoints,K_dominant_colors,threshold)
graph6 = graph_dominant_colorS(superpixels_centroids,S_dominant_colorss,threshold)
```

### Visualization

You can visualize the constructed graph using the `nx.draw` function from the `networkx` library.

```python
nx.draw(graph)
plt.show()
```
## Data set
The project is tested on the "wangdataset.zip" data set, which can be downloaded from the following link: https://www.kaggle.com/datasets/ambarish/wangdataset.

## Example Output

To view the outcome of a trial sample containing 100 images, simply execute the `justML.py` code on with the existing csv files.
![image](https://github.com/kianakholousi/projects/assets/44377174/3cdda121-13eb-4477-8d56-e682aeca4020)

sample image 

![superpixel](https://github.com/kianakholousi/projects/assets/44377174/54bea6fc-61b8-43e2-aabf-2015c42b106e)

superpixels 

![keypoints](https://github.com/kianakholousi/projects/assets/44377174/826f0be2-224e-4dfd-9e67-0f13dc03aaed)

keypoints


graphs of the first image of a sample test (100 images):

![graph1](https://github.com/kianakholousi/projects/assets/44377174/d5da25e5-e87b-4538-91e6-bb8fc1e72fd1)

graph 1 (nodes: superpixels centroids, edges: euclidean distance)
![graph2](https://github.com/kianakholousi/projects/assets/44377174/2f495ffa-5d7c-4517-8a3c-826a706fddd7)

graph 2 (nodes: keypoints, edges: euclidean distance)
![graph3](https://github.com/kianakholousi/projects/assets/44377174/8355a5e4-8794-4bfb-9dbc-23b2d5385948)

graph 3 (nodes: keypoints, edges: intensities)
![graph4](https://github.com/kianakholousi/projects/assets/44377174/e4e355ab-2a16-45c6-84bc-404939559edf)

graph 4 (nodes: keypoints, edges: dominant color)
![graph5](https://github.com/kianakholousi/projects/assets/44377174/fe228175-7f69-405c-8a39-c77ca1fc35b2)

graph 5 (nodes: superpixels centroids, edges: intensities)
![graph6](https://github.com/kianakholousi/projects/assets/44377174/0f718499-68b8-4619-9cc5-a240095804e0)

graph 6 (nodes: superpixels centroids, edges: dominant color)

results:

![Graph1MLacc](https://github.com/kianakholousi/projects/assets/44377174/c33a8707-daf2-4e68-9050-098d84c3c09a)
![Graph2MLacc](https://github.com/kianakholousi/projects/assets/44377174/326f14c2-c69e-4436-868f-c3cad3c2bab9)
![Graph3MLacc](https://github.com/kianakholousi/projects/assets/44377174/f69ec46a-ba53-459f-944a-f17cb81db9c7)
![Graph4MLacc](https://github.com/kianakholousi/projects/assets/44377174/fc8614ef-ce95-4843-9bd4-6498f55643b0)
![Graph5MLacc](https://github.com/kianakholousi/projects/assets/44377174/bcc36b4f-1a8f-45ff-b4cd-f5ae65cf8a91)
![Graph6MLacc](https://github.com/kianakholousi/projects/assets/44377174/2565a8ed-0181-4130-9e4e-154126b6dae4)

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
