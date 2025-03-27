import os
import numpy as np
import torch
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
import albumentations as A
import PIL


# Transformaties definiëren met albumentations
def get_transforms():
    return A.Compose([
        A.Resize(224, 224),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.5),
        A.RandomRotate90(p=0.5),
        A.Transpose(p=0.5),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),  # VGG normalisatie waarden
        A.ToTensorV2()
    ])


# Afbeeldingslabels afleiden van de bestandsnaam
def extract_label(filename):
    label = filename.split('_')[0]
    return len(label)


# Aangepaste PyTorch Dataset klasse
class ImagesDataset(Dataset):
    def __init__(self, root_dir, transforms=None):
        self.root_dir = root_dir
        self.transforms = transforms
        self.img_files = os.listdir(root_dir)
        # Verwijder alle niet-afbeeldingsbestanden uit de lijst
        self.img_files = [file for file in self.img_files if file.endswith(('.jpeg'))]

    def __len__(self):
        return len(self.img_files)

    def __getitem__(self, idx):
        img_name = self.img_files[idx]
        img_path = os.path.join(self.root_dir, img_name)
        image = np.asarray(PIL.Image.open(img_path))  # Inladen met PIL

        label = extract_label(img_name)
        # Label coderen naar een getal als je dat nodig hebt (bijvoorbeeld voor classificatie)
        # label = self.label_to_idx[label]

        if self.transforms:
            augmented = self.transforms(image=image)
            image = augmented['image']

        return image, label


# Root directory met de afbeeldingen
root_dir = 'images'

# Transformaties instellen
transforms = get_transforms()

if __name__ == "__main__":
    # Dataset en DataLoader aanmaken
    dataset = ImagesDataset(root_dir, transforms=transforms)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=4)

    # Een voorbeeldbatch weergeven
    for inputs, labels in dataloader:
        print("Inputs Shape:", inputs.shape)
        print("Labels:", labels)
        break