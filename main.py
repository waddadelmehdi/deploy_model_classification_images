import streamlit as st
import tensorflow as tf
import numpy as np
import PIL as pl
from PIL import ImageOps

st.title('Classification image')

data_load_state = st.text('Loading data...')



image=st.file_uploader(label='Upload',type=None)



model=tf.keras.models.load_model(
filepath='model.h5', custom_objects=None, compile=True, safe_mode=True
)


