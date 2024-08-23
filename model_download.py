from diffusers import StableDiffusionPipeline
import torch

# Download and save the model locally
model_name = "CompVis/stable-diffusion-v1-4"
generator = torch.Generator().manual_seed(1024)
pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=True)
#pipeline = StableDiffusionPipeline.from_pretrained(model_name, use_auth_token=True)
pipeline.save_pretrained("./local_stable_diffusion")