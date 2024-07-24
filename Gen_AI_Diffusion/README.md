# Diffusion Models from Scratch to generate numbers from MNIST

**First we will try to train and create a model which can generate MNIST dataset numbers**
Basic Image Diffusion model has the same philosophy as `UNet`.

In UNet we scale down to a lower latent space and again scale up to high dimensions.
This lower latent space contains enough information to exterpolate the correct distribution of the underlying data.

In Diffusion, we do this lower lattent space breakdown and again scalling up very slowly in controlled manner. Concretely, we add noise of desired amount in each step sequentially, but the number of such steps are in down/up scalling is so much that we literally touch down to a random sample and then again construct the image starting from the random sample.
A single model is repetetively used to do this.

In the `Diffusion_from_scratch_MNIST_Basic.ipynb` we do the training using basic UNet and random addition of noise (corruption). This is to show the initial performance if we do not add noise step by step.
Next in `Diffusion_from_scratch_MNIST_UNet2DModel.ipynb` we improve the update the basic model of UNet.
The `UNet2DModel` model has a number of improvements over our basic UNet above:

*   GroupNorm applies group normalization to the inputs of each block
*   Dropout layers for smoother training
*   Multiple resnet layers per block (if layers_per_block isn't set to 1)
*   Attention (usually used only at lower resolution blocks)
*   Conditioning on the timestep. 
*   Downsampling and upsampling blocks with learnable parameters

## TODO:

Next in `Diffusion_from_scratch_MNIST_DDPM.ipynb` we do the training with step by step addition of noise as per the phenomenal paper [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) (DDPM).

Here, the gist is, although the noise is supposed to be added step by step in the following manner, we will be doing something clever to expedite the process.
The basic idea is:
1. add noise and predict the original image.
2. add more noise and predict the first noisy image
3. repeat the process till the entire image is noisy.

During generation time:
1. feed the noise into the model and get a little denoised image
2. take this and again feed into the model to get more denoised image.
3. repeat this process to the exact number of times by which you downscaled the image


We will not do the full training part, instead we will do finetunning.

----------------

Finetuning of Face generation model. `Diffusion_finetuning_face