from PIL import Image, ImageFilter

def apply_filter(input_file, output_file, filter_name):
    # Open input image file
    counter=0
    while counter < 1:
        counter+=1
        with Image.open(input_file) as img:
            # Apply filter
            if filter_name == 'blur':
                img = img.filter(ImageFilter.BLUR)
            elif filter_name == 'contour':
                img = img.filter(ImageFilter.CONTOUR)
            elif filter_name == 'emboss':
                img = img.filter(ImageFilter.EMBOSS)
            elif filter_name == 'edge_enhance':
                img = img.filter(ImageFilter.EDGE_ENHANCE)
            elif filter_name == 'sharpen':
                img = img.filter(ImageFilter.SHARPEN)
            else:
                raise ValueError('Invalid filter name')
    
            # Save output image file
    img.save(output_file)

# Example usage:
apply_filter('input.jpeg', 'output.jpg', 'edge_enhance')
