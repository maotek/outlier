import os
import numpy as np
import torch
import torchvision.transforms as transforms
from albumentations import HorizontalFlip, VerticalFlip, RandomRotate90, Transpose, Normalize
from albumentations.pytorch import ToTensorV2
from torch.utils.data import Dataset, DataLoader

# Define the augmentation transform
transform = transforms.Compose([
    HorizontalFlip(p=0.5),
    VerticalFlip(p=0.5),
    RandomRotate90(p=0.5),
    Transpose(p=0.5),
    Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2()
])

# Define the custom dataset class
class CustomImageDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_files = [f for f in os.listdir(root_dir) if f.endswith('.jpeg')]

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        # Load the image and extract the label
        image_file = self.image_files[idx]
        label_part = image_file.split('_')[0]  # Assuming labels are before '_' in the filename
        label = int(label_part)  # Convert label to an integer

        # Load the image
        image = np.array(PIL.Image.open(os.path.join(self.root_dir, image_file)).convert('RGB'))

        # Apply the augmentation transform
        if self.transform:
            augmented = self.transform(image=image)
            image = augmented['image']

        return image, label

# Specify the root directory of the images
root_dir = 'images'


# Create the dataset and dataloader
dataset = CustomImageDataset(root_dir, transform=transform)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=4)

# Example of iterating over the dataloader
for images, labels in dataloader:
    print(images.shape)
    print(labels)
    break