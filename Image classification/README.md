Image classification
Converting images to graphs(nodes: keypoints/superpixel centroids, edges based on Euclidean distance/intensity/color dominance of nodes), extracting features,
then using ten machine learning algorithms to classify images to compare and find the best ML algorithm and graph construction method for image classification.
libs: numpy, pandas, matplotlib, cv2(opencv), networkx(graph), sklearn, skimage.

![image](https://github.com/kianakholousi/projects/assets/44377174/3cdda121-13eb-4477-8d56-e682aeca4020)

sample image 

![superpixel](https://github.com/kianakholousi/projects/assets/44377174/391ad92e-7828-40cc-9fef-a25021dfa2bb)

superpixels 

![keypoints](https://github.com/kianakholousi/projects/assets/44377174/13987e90-a9f8-4011-a66f-3729c8158a65)

keypoints

graphs of the first image of a sample test (100 images):
![graph1](https://github.com/kianakholousi/projects/assets/44377174/d3e8b8dc-f88c-4b23-a0eb-d63a822f4122)
graph 1 (nodes: superpixels centroids, edges: euclidean distance)
![graph2](https://github.com/kianakholousi/projects/assets/44377174/ac7c7fd8-35e0-4011-9b57-3314f713c568)
graph 2 (nodes: keypoints, edges: euclidean distance)
![graph3](https://github.com/kianakholousi/projects/assets/44377174/22951550-ead9-4b4e-8b4a-b3a828233482)
graph 3 (nodes: keypoints, edges: intensities)
![graph4](https://github.com/kianakholousi/projects/assets/44377174/7db1220b-219d-4af8-8060-a9df1fe83aac)
graph 4 (nodes: keypoints, edges: dominant color)
![graph5](https://github.com/kianakholousi/projects/assets/44377174/1ce613cc-8341-4caf-a029-8d5b1ee4e453)
graph 5 (nodes: superpixels centroids, edges: intensities)
![graph6](https://github.com/kianakholousi/projects/assets/44377174/e8a3285f-582c-4554-add2-c909f845d0d8)
graph 6 (nodes: superpixels centroids, edges: dominant color)

results:

![Graph1MLacc](https://github.com/kianakholousi/projects/assets/44377174/c33a8707-daf2-4e68-9050-098d84c3c09a)
![Graph2MLacc](https://github.com/kianakholousi/projects/assets/44377174/326f14c2-c69e-4436-868f-c3cad3c2bab9)
![Graph3MLacc](https://github.com/kianakholousi/projects/assets/44377174/f69ec46a-ba53-459f-944a-f17cb81db9c7)
![Graph4MLacc](https://github.com/kianakholousi/projects/assets/44377174/fc8614ef-ce95-4843-9bd4-6498f55643b0)
![Graph5MLacc](https://github.com/kianakholousi/projects/assets/44377174/bcc36b4f-1a8f-45ff-b4cd-f5ae65cf8a91)
![Graph6MLacc](https://github.com/kianakholousi/projects/assets/44377174/2565a8ed-0181-4130-9e4e-154126b6dae4)

