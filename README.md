# An-evaluation-of-Art-Synthesis-on-modern-GAN-models

## Abstract
Artificial Intelligence (AI) image synthesis is one of the most influential topics in recent years,
and Generative Adversarial Network (GAN) is undoubtedly one of the influential contributors
to the progression of image synthesis. While there are many different variations of the GAN
model that can synthesize high-quality images with very different components, the overall
architecture still stays true to the GAN model of having a Generator (G) and a Discriminator
(D). However, existing GAN image synthesis models that produces images from a noise image
have neglected Art synthesis as the amount of literature about GAN models that step into
the field of art generation is very limited in terms of quantity. This paper will delve into the
differences between real life such as pictures of humans, birds, and cars, and art images and
utilize a modern image synthesis model, StyleGAN2-ADA PyTorch version, to evaluate the
generated art images.






For downsize.py:

The purpose of this code is to downsize the images and convert the colour mode of the images to RGB.

1) Training set: This folder should include the dataset images you wish to train and make sure that the non of the images have alpha channel.
2) Output Folder: This folder should be empty, this is where all the processed images will go.

Remark: Make sure to run this code first to ensure all the images is the same size.


For L2.py:

1) Training set: This folder should include the dataset images you wish to train and make sure that the non of the images have alpha channel. Note that at this stage, the training set is the processed images that share the same size.

2) Generate image output: This should contain the generated image that the model has produced. A sample image can be found within the .Zip folder.


For stylegan2-ada-pytorch-main:
This code belongs to: https://github.com/NVlabs/stylegan2-ada-pytorch



# Ukiyo-e Face results

![Alt Text](Ukei.png)


# Nearest Neighbour Results results

![Alt Text](Nearest Neighbour.png)







@inproceedings{Karras2020ada,
  title     = {Training Generative Adversarial Networks with Limited Data},
  author    = {Tero Karras and Miika Aittala and Janne Hellsten and Samuli Laine and Jaakko Lehtinen and Timo Aila},
  booktitle = {Proc. NeurIPS},
  year      = {2020}
}
