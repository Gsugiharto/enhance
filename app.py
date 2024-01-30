from PIL import Image, ImageEnhance
import streamlit as st

def enhance_image(image, enhancement_factor):
    # Membuka gambar menggunakan PIL
    img = Image.open(image)

    # Meningkatkan kecerahan gambar
    enhancer = ImageEnhance.Brightness(img)
    enhanced_image = enhancer.enhance(enhancement_factor)

    return enhanced_image

def main():
    st.title('Image Enhancement App')

    uploaded_image = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        enhancement_factor = st.slider('Enhancement Factor', 0.0, 2.0, 1.0)

        if st.button('Enhance Image'):
            enhanced_image = enhance_image(uploaded_image, enhancement_factor)
            st.image(enhanced_image, caption='Enhanced Image', use_column_width=True)

if __name__ == "__main__":
    main()
