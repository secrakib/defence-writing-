import os
from PIL import Image

graphics_dir = "e:/Writing Defence/graphics"
png_files = [
    'overview.png', 
    'source_contributions_advanced.png', 
    'coverage_matrix_advanced.png', 
    'model_comparison.png', 
    'bleu_heatmap.png', 
    'directionality.png', 
    'dataset_scaling.png', 
    'comparative_sota.png'
]

for png_file in png_files:
    png_path = os.path.join(graphics_dir, png_file)
    pdf_path = os.path.join(graphics_dir, png_file.replace('.png', '.pdf'))
    
    if os.path.exists(png_path):
        print(f"Converting {png_file} to PDF...")
        image = Image.open(png_path)
        
        # Convert RGBA to RGB if necessary because PDF doesn't support alpha channel properly in this way sometimes
        if image.mode == 'RGBA':
            image = image.convert('RGB')
            
        # Save as PDF with high resolution
        image.save(pdf_path, "PDF", resolution=300.0)
        print(f"Saved {pdf_path}")
    else:
        print(f"File not found: {png_path}")
