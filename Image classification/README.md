
Image classification
Converting images to graphs(nodes: keypoints/superpixel centroids, edges based on Euclidean distance/intensity/color dominance of nodes), extracting features,
then using ten machine learning algorithms to classify images to compare and find the best ML algorithm and graph construction method for image classification.
libs: numpy, pandas, matplotlib, cv2(opencv), networkx(graph), sklearn, skimage.

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

