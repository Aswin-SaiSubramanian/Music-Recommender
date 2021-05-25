This directory is a record of the data collection for our initial approach to genre classification: feeding into a pretrained image classification model, song features collected from the Million Song Dataset (reshaped and resized to fit through torchvision's VGG-19).

This approach was pursued until Milestone 3, when we realized that using spectrograms instead might be more natural for our image classification model and may yield better results. 

While switching to spectrograms by itself did not improve the accuracy of our model significantly, it did give us freedom to look ouside the Million Song Dataset for samples. Indeed, we were able to more than double the number of samples we could use for training, and the genre classification accuracy improved from 35% to %60 by Milestone 4.