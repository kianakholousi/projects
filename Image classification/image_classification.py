import pandas as pd
import networkx as nx
import numpy as np
import cv2
import os
from skimage.segmentation import slic
from skimage.measure import regionprops
from category_encoders import OrdinalEncoder
import matplotlib.pyplot as plt
import math
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from skimage.segmentation import mark_boundaries
from scipy.spatial import distance
from sklearn.metrics import accuracy_score

T1 = 40 
T2 = 10
T3 = 20

def superpixels_segmentation(img):
    superpixels = []
    nodes = []
    intensities = []
    dominant_colors = []
    # Perform superpixel segmentation on the image
    segments = slic(img, n_segments=250, compactness=10, sigma=1, start_label=1)
    labels = segments.reshape(-1)
    superpixels.append(np.unique(labels))
    
    # image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(mark_boundaries(image_rgb, segments))
    # plt.tight_layout()
    # plt.show()
    
    # Compute the region centroid for each superpixel
    regions = regionprops(segments, intensity_image=img)
    for props in regions:
        y, x = props.centroid
        # compute mean intensity for each superpixel 
        intensities.append(props.mean_intensity)
        # Extract the dominant color for each superpixel
        dominant_color = img[props.coords[:, 0], props.coords[:, 1]]
        dominant_colors.append(dominant_color.mean(axis=0))
        nodes.append((x,y))
        
    print("Number of superpixel centroids for image", idx ,"is:", len(np.unique(labels)))
    return nodes, intensities, dominant_colors

def keypoint_extraction(img):
    # Perform keypoint extraction on the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    keypoints = sift.detect(gray, None)
    print("Number of keypoints for image", idx ,"is:", len(keypoints))
    keypoints = np.array([(kp.pt[0], kp.pt[1]) for kp in keypoints])
    
    # plt.imshow(img)
    # plt.scatter(keypoints[:, 0], keypoints[:, 1], color='red', marker='x')
    # plt.title("Image with Keypoints")
    # plt.axis('off')
    # plt.show()
    
    intensities = []
    dominant_color_intensities = []
    for kp in keypoints:
        x, y = kp
        x, y = int(x), int(y)
        # Extract intensity at the keypoint location
        intensity = gray[y, x]
        intensities.append(intensity)
        # Extract dominant color intensity at the keypoint location
        dominant_color = img[y, x]
        dominant_color_intensity = dominant_color.mean()
        dominant_color_intensities.append(dominant_color_intensity)
                
    # print("intensity",len(intensities)) 
    # print("dominant_color_intensities",len(dominant_color_intensities)) 
    return keypoints, intensities, dominant_color_intensities

def graph_euclidean(nodes):
    graph = nx.Graph()
    # adding keypoints/centroid of superpixels as nodes 
    for i in range (len(nodes)):
        graph.add_node(i)
            
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            node1 = nodes[i]
            node2 = nodes[j]
            x1, y1 = node1
            x2, y2 = node2
            distance = math.dist((x1, y1), (x2, y2))
            if distance < T1:
                graph.add_edge(i, j)
                
    # print("Graph - Euclidean distance done")            
    # nx.draw(graph, with_labels=True)
    # plt.title("Graph - Euclidean distance")
    # plt.show()
    print("numeber of nodes, edgs ",len(nodes),nx.number_of_edges(graph))
    return graph

def graph_intensityK(keypoints, intensities, threshold):
    G = nx.Graph()    
    # Add nodes to the graph
    for i, kp in enumerate(keypoints):
        G.add_node(i, keypoint=kp, intensity=intensities[i])
    
    # Add edges based on intensity similarity
    for i in range(len(keypoints)):
        for j in range(i+1, len(keypoints)):
            if abs(int(intensities[i]) - int(intensities[j])) < threshold:
                G.add_edge(i, j)
                
    # print("Graph - Intensity K done")     
    # nx.draw(G, with_labels=True)
    # plt.title("Graph - Intensity K")
    # plt.show()
    print("Number of nodes, edges:", len(keypoints), nx.number_of_edges(G))
    return G

def graph_dominant_colorK(keypoints, dominant_color_intensities, threshold):
    G = nx.Graph()
    # Check if the lengths of keypoints and dominant_color_intensities match
    if len(keypoints) != len(list(np.atleast_1d(dominant_color_intensities))):
        raise ValueError("Lengths of keypoints and dominant_color_intensities do not match.")
    
    # Add nodes to the graph
    for i, kp in enumerate(keypoints):
        G.add_node(i, keypoint=kp, dominant_color_intensity=int(dominant_color_intensities[i]))
    
    # Add edges based on dominant color intensity similarity
    for i in range(len(keypoints)):
        for j in range(i+1, len(keypoints)):
            if abs(dominant_color_intensities[i] - dominant_color_intensities[j]) < threshold:
                G.add_edge(i, j)
    
    # print("Graph - Dominant Color K done") 
    # nx.draw(G, with_labels=True)
    # plt.title("Graph - Dominant Color K")
    # plt.show()
    print("Number of nodes, edges:", len(keypoints), nx.number_of_edges(G))
    return G     


def graph_intensityS(nodes, intensities, threshold):
    G = nx.Graph()
    # Add nodes to the graph
    for i, node in enumerate(nodes):
        G.add_node(i, centroid=node, intensity=intensities[i])
    
    # Add edges based on intensity similarity
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if np.all(np.abs(intensities[i] - intensities[j]) < threshold):
                G.add_edge(i, j)
                
    # print("Graph - Intensity S done")             
    # nx.draw(G, with_labels=True)
    # plt.title("Graph - Intensity S")
    # plt.show()
    print("Number of nodes, edges:", len(nodes), nx.number_of_edges(G))   
    return G         

def graph_dominant_colorS(nodes, dominant_colors, threshold):
    G = nx.Graph()
    # Add nodes to the graph
    for i, node in enumerate(nodes):
        G.add_node(i, centroid=node, dominant_color=dominant_colors[i])
    
    # Add edges based on dominant color similarity
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            color_distance = distance.euclidean(dominant_colors[i], dominant_colors[j])
            if color_distance < threshold:
                G.add_edge(i, j)  
                
    # print("Graph - Dominant Color K done") 
    # nx.draw(G, with_labels=True)
    # plt.title("Graph - Dominant Color K")
    # plt.show()
    print("Number of nodes, edges:", len(nodes), nx.number_of_edges(G))    
    return G                      


def extract_features(graph):
    # check if graph is connected 
    if nx.number_of_edges(graph)>0:
    # Extract features from the obtained graph
        degree_centrality = list(nx.degree_centrality(graph).values())
        betweenness_centrality = list(nx.betweenness_centrality(graph).values())
        closeness_centrality = list(nx.closeness_centrality(graph).values())
        eigenvector_centrality = list(nx.eigenvector_centrality(graph, max_iter=10000).values())
        pagerank = list(nx.pagerank(graph).values())
        katz_centrality = list(nx.katz_centrality_numpy(graph).values())
        clustering_coefficient = list(nx.clustering(graph).values())
        features = [
        degree_centrality,
        betweenness_centrality,
        closeness_centrality,
        eigenvector_centrality,
        pagerank,
        katz_centrality,
        clustering_coefficient]
    # print(len(degree_centrality.values()),len(betweenness_centrality.values()),len(closeness_centrality.values()),len(eigenvector_centrality.values()),len(pagerank.values()),len(katz_centrality.values()),len(clustering_coefficient.values()),len(features))           
    print("feature extraction done")           
    return features


# Step 1: Read a dataset containing 100 images one by one
images = []
folder_path = os.getcwd() + "\\img100"
superpixels_centroids , keypoints = [], []
features_G1 ,features_G2 ,features_G3 ,features_G4,features_G5 ,features_G6= [] , [] , [] , [] , [] , []
categories = [f"category{i}" for i in range(0, 10)] 

for idx, filename in enumerate(os.listdir(folder_path)):
    img = cv2.imread(os.path.join(folder_path, filename))
    if img is not None:
        images.append(img)
        image_number=int(filename.split(".")[0])
        print("image number",image_number)
        # Step 2:  Convert each image into a set of nodes (keypoints/superpixel centroids)
        superpixels_centroids, S_intensities, S_dominant_colors = superpixels_segmentation(img)
        keypoints,K_intensities, K_dominant_colors = keypoint_extraction(img)
        # Step 3:  Create a link between the nodes (graph construction)
        graph1 = graph_euclidean(superpixels_centroids)
        graph2 = graph_euclidean(keypoints)
        graph3 = graph_intensityK(keypoints,K_intensities,T2)
        graph4 = graph_dominant_colorK(keypoints,K_dominant_colors,T3)
        graph5 = graph_intensityS(superpixels_centroids,S_intensities,T2)
        graph6 = graph_dominant_colorS(superpixels_centroids,S_dominant_colors,T3)
        # step 4: Extract features from graphs
        features_G1.append(extract_features(graph1)+[categories[image_number//100]])
        features_G2.append(extract_features(graph2)+[categories[image_number//100]]) 
        features_G3.append(extract_features(graph3)+[categories[image_number//100]]) 
        features_G4.append(extract_features(graph4)+[categories[image_number//100]]) 
        features_G5.append(extract_features(graph5)+[categories[image_number//100]]) 
        features_G6.append(extract_features(graph6)+[categories[image_number//100]]) 
print("importing images done")

# Step 5: write feature vector to csv file 
df_G1 = pd.DataFrame(features_G1)
df_G2 = pd.DataFrame(features_G2)
df_G3 = pd.DataFrame(features_G3)
df_G4 = pd.DataFrame(features_G4)
df_G5 = pd.DataFrame(features_G5)
df_G6 = pd.DataFrame(features_G6)
header = ["feature 1", "feature 2", "feature 3", "feature 4", "feature 5", "feature 6", "feature 7","category"]
df_G1.to_csv("features_G1.csv", index=False, header=header)
df_G2.to_csv("features_G2.csv", index=False, header=header)
df_G3.to_csv("features_G3.csv", index=False, header=header)
df_G4.to_csv("features_G4.csv", index=False, header=header)
df_G5.to_csv("features_G5.csv", index=False, header=header)
df_G6.to_csv("features_G6.csv", index=False, header=header)


# Step 6: Apply the learning algorithms and report the classification accuracy obtained from each in a comparison table
for k in range(1,7):
        data = pd.read_csv(f'features_G{k}.csv')

        X = data.drop("category", axis=1)
        y = data['category'].str.replace('category', '')

        # Encode categorical data 
        encoder = OrdinalEncoder()
        X = encoder.fit_transform(X)

        # Split data to train and test sets 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        Classifiers=[
            DecisionTreeClassifier(),
            RandomForestClassifier(),
            KNeighborsClassifier(n_neighbors=7),
            BaggingClassifier(),
            AdaBoostClassifier(),
            GaussianNB(),
            SVC(),
            LogisticRegression(),
            SGDClassifier(),
            VotingClassifier(estimators=[('lr', LogisticRegression()), ('rf', RandomForestClassifier()), ('gnb', GaussianNB())])
        ]

        results=[]
        for i in range(len(Classifiers)):
            classifier = Classifiers[i]
            classifier.fit(X_train, y_train)
            y_pred = classifier.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            results.append(accuracy)
        df = pd.DataFrame({"Algorithm": ["Decision Tree", "Random Forest", "K-Nearest Neighbor", "Bagging", "Boosting",
                                        "Naive Bayes", "SVM", "Logistic Regression", "SGD", "Voting"], "Accuracy": results})
        df = df.sort_values(by="Accuracy", ascending=False)
        print("graph ",str(k))
        print(df)