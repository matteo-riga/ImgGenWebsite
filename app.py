from flask import Flask, render_template, request, send_file
import io
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline

app = Flask(__name__)

pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=True)

def generate_image(prompt):
    # image generation code
    generator = torch.Generator().manual_seed(1024)
    global pipeline
    image = pipeline(prompt, num_inference_steps=2, generator=generator).images[0]
    #image = Image.new('RGB', (512, 512), color='white')
    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')

        generated_image = generate_image(prompt)
        
        # Save the image to a BytesIO object
        img_io = io.BytesIO()
        generated_image.save(img_io, 'PNG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2345, debug=True)
