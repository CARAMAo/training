import os, random, shutil

os.mkdir('dataset/train')
os.mkdir('dataset/train/images')
os.mkdir('dataset/train/Annotations')

os.mkdir('dataset/validation')
os.mkdir('dataset/validation/images')
os.mkdir('dataset/validation/Annotations')

os.mkdir('dataset/test')
os.mkdir('dataset/test/images')
os.mkdir('dataset/test/Annotations')


image_paths = os.listdir('dataset/images')
random.shuffle(image_paths)

print(f'found {len(image_paths)} images, shuf')

for i, image_path in enumerate(image_paths):
  if image_path.split(".")[-1] != "jpeg" and image_path.split(".")[-1] != "jpg":
    print(image_path,image_path.split(".")[-1])

  if i < int(len(image_paths) * 0.8):
    shutil.copy(f'dataset/images/{image_path}', 'dataset/train/images')
    ext = image_path.split(".")[-1]
    shutil.copy(f'dataset/Annotations/{image_path.replace(ext, "xml")}', 'dataset/train/Annotations')
  elif i < int(len(image_paths)*0.9):
    shutil.copy(f'dataset/images/{image_path}', 'dataset/validation/images')
    ext = image_path.split(".")[-1]
    shutil.copy(f'dataset/Annotations/{image_path.replace(ext, "xml")}', 'dataset/validation/Annotations')
  else:
    shutil.copy(f'dataset/images/{image_path}', 'dataset/test/images')
    ext = image_path.split(".")[-1]
    shutil.copy(f'dataset/Annotations/{image_path.replace(ext, "xml")}', 'dataset/test/Annotations')
