import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('breast_cancer_classification.sav','rb'))
def cancer_prediction(input1):
    input_to_array = np.asarray(input1)
    reshaped = input_to_array.reshape(1, -1)
    predict = loaded_model.predict(reshaped)
    if predict[0] == 'B':
        return "This is B type cancer"
    else:
        return "This is M type cancer"
def main():
    st.title("Breast Cancer Prediction")
    c1,c2,c3,c4=st.columns(4)
    with c1:
        radius_mean=(st.text_input(" Radius Mean",value="0"))
    with c2:
        texture_mean = (st.text_input(" Texture Mean",value="0"))
    with c3:
        perimeter_mean = (st.text_input(" Perimeter Mean",value="0"))
    with c4:
        area_mean = (st.text_input(" Area Mean",value="0"))
    with c1:
        smoothness_mean = (st.text_input(" Smoothness Mean",value="0"))
    with c2:
        compactness_mean = (st.text_input(" Compactness Mean",value="0"))
    with c3:
        concavity_mean = (st.text_input(" Concavity Mean",value="0"))
    with c4:
        concave_pos_mean = (st.text_input(" Concavity Pos Mean",value="0"))
    with c1:
        symmetry_mean= (st.text_input(" Symmetry Mean",value="0"))
    with c2:
        fractal_dimension_mean= (st.text_input(" Fractal Dimension Mean",value="0"))
    with c3:
        radius_se = (st.text_input(" Radius SE",value="0"))
    with c4:
        texture_se = (st.text_input(" Texture SE",value="0"))
    with c1:
        perimeter_se = (st.text_input(" Perimeter SE",value="0"))
    with c2:
        area_se = (st.text_input(" Area SE",value="0"))
    with c3:
        smoothness_se = (st.text_input(" Smoothness SE",value="0"))
    with c4:
        compactness_se = (st.text_input(" Compactness SE",value="0"))
    with c1:
        concavity_se = (st.text_input(" Concavity SE",value="0"))
    with c2:
        concave_pos_se = (st.text_input(" Concave Pos SE",value="0"))
    with c3:
        symmetry_se = (st.text_input(" Symmetry SE",value="0"))
    with c4:
        fractal_dimension_se = (st.text_input(" Fractal Dimension SE",value="0"))
    with c1:
        radius_worst = (st.text_input(" Radius Worst",value="0"))
    with c2:
        texture_worst = (st.text_input(" Texture Worst",value="0"))
    with c3:
        perimeter_worst = (st.text_input(" Perimeter Worst",value="0"))
    with c4:
        area_worst = (st.text_input(" Area Worst",value="0"))
    with c1:
        smoothness_worst = (st.text_input(" Smoothness Worst",value="0"))
    with c2:
        compactness_worst = (st.text_input(" Compactness Worst",value="0"))
    with c3:
        concavity_worst = (st.text_input(" Concavity Worst",value="0"))
    with c4:
        concave_pos_worst = (st.text_input(" Concave Pos Worst",value="0"))
    with c1:
        symmetry_worst = (st.text_input(" Symmetry Worst",value="0"))
    with c2:
        fractal_dimension_worst = (st.text_input(" Fractal Dimension Worst",value="0"))
    diagnosis=""
    if st.button("Predict"):
        diagnosis=cancer_prediction([float(radius_mean), float(texture_mean), float(perimeter_mean), float(area_mean), float(smoothness_mean),
                                     float(compactness_mean), float(concavity_mean), float(concave_pos_mean), float(symmetry_mean),
                                     float(fractal_dimension_mean), float(radius_se), float(texture_se), float(perimeter_se), float(area_se),
                                     float(smoothness_se), float(compactness_se), float(concavity_se), float(concave_pos_se), float(symmetry_se),
                                     float(fractal_dimension_se), float(radius_worst), float(texture_worst), float(perimeter_worst), float(area_worst),
                                     float(smoothness_worst), float(compactness_worst), float(concavity_worst), float(concave_pos_worst),
                                     float(symmetry_worst), float(fractal_dimension_worst)])
    st.success(diagnosis)
if __name__ == '__main__':
    main()

