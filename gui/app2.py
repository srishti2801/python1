import streamlit as st
from PIL import Image, ImageFilter

st.header("Image Processing")

st.sidebar.subheader("options")

image = st.sidebar.file_uploader("upload an image", type=['jpg','png','gif'])

if image:
    st.image(image, use_column_width=True)
    filters = ['grayscale','outline','outline reverse','emboss']
    fil = st.sidebar.selectbox("select a filter", filters)

    im = Image.open(image)
    if fil == filters[0]:
        out = im.convert('L')
        st.image(out)
        if st.sidebar.button("save the image"):
            out.save(image.name)
    if fil == filters[1]:
        out = im.filter(ImageFilter.CONTOUR)
        st.image(out)
    if fil == filters[2]:
        out = im.filter(ImageFilter.FIND_EDGES)
        st.image(out)
    if fil == filters[3]:
        out = im.filter(ImageFilter.EMBOSS)
        st.image(out)