# -*- coding: utf-8 -*-
# """VoteNet.ipynb

# Automatically generated by Colab.

# Original file is located at
#     https://colab.research.google.com/drive/1nMeA-OWgtkELVrrdSEfoXf14Peq8hcuZ

# MMDetection3D is an open source object detection toolbox based on PyTorch, towards the next-generation platform for general 3D detection. It is a part of the OpenMMLab project. @misc{mmdet3d2020,
#     title={{MMDetection3D: OpenMMLab} next-generation platform for general {3D} object detection},
#     author={MMDetection3D Contributors},
#     howpublished = {\url{https://github.com/open-mmlab/mmdetection3d}},
#     year={2020}
# }
# """

# Commented out IPython magic to ensure Python compatibility.
#!pip install -U openmim
#!pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
#!mim install "mmcv>=2.0.0rc4,<2.2.0"
#!mim install "mmengine>=0.7.1,<1.0.0"
#!mim install "mmdet>=3.0.0,<3.3.0"

# # Instalação MMDetection3D
#!git clone https://github.com/open-mmlab/mmdetection3d.git -b dev-1.x
# %cd mmdetection3d
#!pip install -e .
# %cd ..


# !git clone https://github.com/open-mmlab/mmdetection3d.git -b dev-1.x
# # "-b dev-1.x" means checkout to the `dev-1.x` branch.
# %cd mmdetection3d
# !pip install -v -e .
# # "-v" means verbose, or more output
# # "-e" means installing a project in edtiable mode,
# # thus any local modifications made to the code will take effect without reinstallation.

#!pip install "matplotlib>=3.7.1"

# Checkpoints para Detecção
#!mkdir ./checkpoints
#!mim download mmdet3d --config votenet_8xb16_sunrgbd-3d.py --dest ./checkpoints

# Redução e limpeza da nuvem.
import open3d as o3d
#import trimesh

#from google.colab import drive
#drive.mount('/content/drive')

# point_cloud = o3d.io.read_point_cloud("./test.ply")
# pcd_filtered = point_cloud.voxel_down_sample(voxel_size=0.005)
# pcd_filter, ind = pcd_filtered.remove_statistical_outlier(nb_neighbors=20, std_ratio=1)

# o3d.io.write_point_cloud("copy.ply", pcd_filter)

#Visualização da Nuvem
#import trimesh
import numpy as np

# cloud = trimesh.load("example_kmeans.ply")
# pcd = trimesh.PointCloud(cloud.vertices, [255, 0, 0])
# scene = trimesh.Scene([pcd])
# scene.show()

#Preparação da nuvem para treinamento e inferência
import numpy as np
import pandas as pd
from plyfile import PlyData

# def inspect_ply(input_path):
#     plydata = PlyData.read(input_path)
#     data = plydata.elements[0].data
#     property_names = data[0].dtype.names
#     print(f"Number of points: {len(data)}")
#     print(f"Properties per point: {property_names}")

# inspect_ply('copy.ply')

# def convert_ply(input_path, output_path):
#     plydata = PlyData.read(input_path)  # read file
#     data = plydata.elements[0].data  # read data
#     data_pd = pd.DataFrame(data)  # convert to DataFrame
    
#     # Especificar as propriedades a serem utilizadas
#     properties_to_use = ['x', 'y', 'z', 'nx', 'ny', 'nz']
#     num_points = data_pd.shape[0]
#     num_properties = len(properties_to_use)
    
#     data_np = np.zeros((num_points, num_properties), dtype=np.float64)  # initialize array to store data
    
#     for i, name in enumerate(properties_to_use):  # read data by property
#         data_np[:, i] = data_pd[name]
    
#     # Save the array to a binary file
#     data_np.astype(np.float32).tofile(output_path)

# convert_ply('copy.ply', 'test.bin')

# Executando inferência de Detecção
#!python /content/mmdetection3d/demo/pcd_demo.py /content/test.bin /content/checkpoints/votenet_8xb16_sunrgbd-3d.py /content/checkpoints/votenet_16x8_sunrgbd-3d-10class_20210820_162823-bf11f014.pth --pred-score-thr 0.99

# Executando inferência de Segmentação
#!python /content/mmdetection3d/demo/pcd_seg_demo.py /content/test2.bin /content/checkpoints/pointnet2_ssg_2xb16-cosine-200e_scannet-seg.py /content/checkpoints/pointnet2_ssg_16x2_cosine_200e_scannet_seg-3d-20class_20210514_143644-ee73704a.pth

######################################################################################

# import json
# import numpy as np
# from open3d import geometry
# import trimesh

# point_cloud = o3d.io.read_point_cloud("test.ply")
# geometries = [point_cloud]

# with open("./outputs/preds/test.json", "r") as f:
#   data = json.load(f)

# labels_3d = np.array(data["labels_3d"])
# scores_3d = np.array(data["scores_3d"])
# bboxes_3d = np.array(data["bboxes_3d"])

# unique_labels = np.unique(labels_3d)
# best_bbox_indices = []

# for label in unique_labels:
#   mask = (labels_3d == label)
#   indices = np.where(mask)[0]
#   best_index = np.argmax(scores_3d[indices])
#   best_bbox_indices.append(indices[best_index])

# best_bboxes = bboxes_3d[best_bbox_indices]

# point_clouds = []

# # Loop sobre as melhores bounding boxes
# for label, bbox in zip(unique_labels, best_bboxes):
#     # Extrair as coordenadas mínimas e máximas da bounding box
#     min_bound = bbox[:3]
#     max_bound = bbox[3:]

#     # Calcula o centro, dimensões e orientação da bounding box
#     center = bbox[0:3]
#     dim = bbox[3:6]
#     yaw = np.zeros(3)
#     yaw[2] = bbox[6]

#     # Obtém a matriz de rotação a partir das orientações
#     rot_mat = geometry.get_rotation_matrix_from_xyz(yaw)
#     center[2] += dim[2] / 2  # Ajusta a altura do centro

#     # Cria uma caixa delimitadora orientada (OBB)
#     box3d = geometry.OrientedBoundingBox(center, rot_mat, dim)

#     # Cria uma cópia da nuvem de pontos
#     point_cloud_copy = o3d.geometry.PointCloud()
#     point_cloud_copy.points = o3d.utility.Vector3dVector(np.asarray(point_cloud.points))

#     # Usa o método crop para extrair a subnuvem de pontos dentro da bounding box
#     cropped_point_cloud = point_cloud_copy.crop(box3d)

#     # Salva a subnuvem de pontos em um arquivo PLY
#     filename = f"nova_nuvem_classe_{label}.ply"
#     o3d.io.write_point_cloud(filename, cropped_point_cloud)

#     print(f"Nova nuvem de pontos para a classe {label} salva em {filename}")

#     # Adiciona a nuvem de pontos à lista
#     point_clouds.append(cropped_point_cloud)

# Agora, a lista 'point_clouds' contém as nuvens de pontos para cada objeto encontrado.

# import json
# import numpy as np
# from open3d import geometry

# #cloud = trimesh.load("example_kmeans.ply")
# #pcd = trimesh.PointCloud(cloud.vertices, [255, 0, 0])
# #scene = trimesh.Scene([pcd])

# point_cloud = o3d.io.read_point_cloud("test.ply")
# geometries = [point_cloud]

# with open("./outputs/preds/test.json", "r") as f:
#   data = json.load(f)

# scores_array = np.array(data["scores_3d"])
# indice_best_score = np.argmax(scores_array)
# bbox = data["bboxes_3d"][indice_best_score]

# center = bbox[0:3]
# dim = bbox[3:6]
# yaw = np.zeros(3)
# yaw[2] = bbox[6]

# print(center, dim, yaw)

# rot_mat = geometry.get_rotation_matrix_from_xyz(yaw)
# center[2] += dim[2] / 2

# box3d = geometry.OrientedBoundingBox(center, rot_mat, dim)
# print(box3d)

# line_set = geometry.LineSet.create_from_oriented_bounding_box(box3d)
# print(line_set)

# geometries.append(line_set)

# print(geometries)
# o3d.visualization.draw_plotly(geometries)

# #cloud = trimesh.load("example_kmeans.ply")
# #line_set = trimesh.load("line_set.ply")
# #pcd = trimesh.PointCloud(cloud.vertices, [245, 245, 220])
# #line = trimesh.PointCloud(line_set.vertices, [255, 0, 0])
# #scene = trimesh.Scene([pcd, line])
# #scene.show()

# point_cloud_copy = o3d.geometry.PointCloud()
# point_cloud_copy.points = o3d.utility.Vector3dVector(np.asarray(point_cloud.points))

# min_bound = np.min(np.asarray(line_set.points), axis=0)
# max_bound = np.max(np.asarray(line_set.points), axis=0)

# mask = np.all((point_cloud_copy.points >= min_bound) & (point_cloud_copy.points <= max_bound), axis=1)
# filtered_points = np.asarray(point_cloud_copy.points)[mask]

# new_point_cloud = o3d.geometry.PointCloud()
# new_point_cloud.points = o3d.utility.Vector3dVector(filtered_points)

# o3d.io.write_point_cloud("nova_nuvem.ply", new_point_cloud)

###########################################################################################################3
# cloud = trimesh.load("nova_nuvem.ply")
# pcd = trimesh.PointCloud(cloud.vertices, [255, 0, 0])
# scene = trimesh.Scene([pcd])
# scene.show()



# # Visualização da Segmentação
# import json
# import open3d as od3
# import numpy as np

# point_cloud = o3d.io.read_point_cloud("test.ply")

# with open("/content/outputs/preds/test.json", "r") as f:
#   data = json.load(f)

# pts_mask = data['pts_semantic_mask']
# pts_mask_unique = np.unique(pts_mask)

# colors = {classe: np.random.rand(3,) for classe in pts_mask_unique}

# colors = [colors[classe] for classe in pts_mask]
# point_cloud.colors = o3d.utility.Vector3dVector(colors)

# o3d.io.write_point_cloud("nuvem_de_pontos_colorida.ply", point_cloud)

# cloud = trimesh.load("example_kmeans.ply")
# pcd = trimesh.PointCloud(
#     vertices=np.array(cloud.vertices),
#     colors=np.array(colors)
# )
# scene = trimesh.Scene([pcd])
# scene.show()

# # cloud = trimesh.load("./test.ply")
# # pcd = trimesh.PointCloud(cloud.vertices, [255, 0, 0])
# # scene = trimesh.Scene([pcd])
# # scene.show()

#######################################################################

# import json
# import numpy as np
# import open3d as o3d

# # Carregar nuvem de pontos e bounding box a partir dos dados salvos
# point_cloud = o3d.io.read_point_cloud("test.ply")

# # Carregar dados da predição da bounding box a partir do arquivo JSON
# with open("./outputs/preds/test.json", "r") as f:
#     data = json.load(f)

# # Extrair a bounding box com o maior score
# scores_array = np.array(data["scores_3d"])
# indice_best_score = np.argmax(scores_array)
# bbox = data["bboxes_3d"][indice_best_score]

# # Extrair parâmetros da bounding box (centro, dimensões e orientação)
# center = bbox[0:3]
# dim = bbox[3:6]
# yaw = np.zeros(3)
# yaw[2] = bbox[6]

# # Calcular matriz de rotação a partir da orientação da bounding box
# rot_mat = o3d.geometry.get_rotation_matrix_from_xyz(yaw)
# center[2] += dim[2] / 2

# # Criar a bounding box orientada
# box3d = o3d.geometry.OrientedBoundingBox(center, rot_mat, dim)

# # Função para verificar se um ponto está dentro da bounding box orientada
# def is_point_inside_bbox(point, bbox):
#     # Transformar o ponto para o sistema de coordenadas da bounding box alinhada
#     point_local = np.dot(np.linalg.inv(bbox.R), point - bbox.center)
#     return np.all(np.abs(point_local) <= bbox.extent / 2)

# # Filtrar os pontos da nuvem de pontos que estão fora da bounding box
# filtered_points = []
# for point in np.asarray(point_cloud.points):
#     if not is_point_inside_bbox(point, box3d):
#         filtered_points.append(point)

# # Criar uma nova nuvem de pontos com os pontos filtrados
# new_point_cloud = o3d.geometry.PointCloud()
# new_point_cloud.points = o3d.utility.Vector3dVector(np.asarray(filtered_points))

# # Salvar a nova nuvem de pontos em um novo arquivo
# o3d.io.write_point_cloud("nova_nuvem.ply", new_point_cloud)


#####################################3

import json
import numpy as np
import open3d as o3d

# Carregar nuvem de pontos e bounding box a partir dos dados salvos
point_cloud = o3d.io.read_point_cloud("test.ply")

# Carregar dados da predição da bounding box a partir do arquivo JSON
with open("./outputs/preds/test.json", "r") as f:
    data = json.load(f)

# Extrair a bounding box com o maior score
scores_array = np.array(data["scores_3d"])
indice_best_score = np.argmax(scores_array)
bbox = data["bboxes_3d"][indice_best_score]

# Extrair parâmetros da bounding box (centro, dimensões e orientação)
center = bbox[0:3]
dim = bbox[3:6]
yaw = np.zeros(3)
yaw[2] = bbox[6]

# Calcular matriz de rotação a partir da orientação da bounding box
rot_mat = o3d.geometry.get_rotation_matrix_from_xyz(yaw)
center[2] += dim[2] / 2

# Criar a bounding box orientada
box3d = o3d.geometry.OrientedBoundingBox(center, rot_mat, dim)

# Função para verificar se um ponto está dentro da bounding box orientada
def is_point_inside_bbox(point, bbox):
    # Transformar o ponto para o sistema de coordenadas da bounding box alinhada
    point_local = np.dot(np.linalg.inv(bbox.R), point - bbox.center)
    return np.all(np.abs(point_local) <= bbox.extent / 2)

# Filtrar os pontos da nuvem de pontos que estão fora da bounding box
filtered_points = []
filtered_colors = []
for i, point in enumerate(np.asarray(point_cloud.points)):
    if not is_point_inside_bbox(point, box3d):
        filtered_points.append(point)
        filtered_colors.append(point_cloud.colors[i])

# Criar uma nova nuvem de pontos com os pontos filtrados e suas cores correspondentes
new_point_cloud = o3d.geometry.PointCloud()
new_point_cloud.points = o3d.utility.Vector3dVector(np.asarray(filtered_points))
new_point_cloud.colors = o3d.utility.Vector3dVector(np.asarray(filtered_colors))

# Salvar a nova nuvem de pontos em um novo arquivo
o3d.io.write_point_cloud("nova_nuvem_com_cores.ply", new_point_cloud)
