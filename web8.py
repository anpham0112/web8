import streamlit as st
import os
def get_pass(filename):
     # Lấy đường dẫn tuyệt đối đến thư mục chứa script hiện tại
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Xây dựng đường dẫn đến thư mục 'assets' và tệp cụ thể
    asset_dir = os.path.join(script_dir, 'assets')
    
    # Tạo đường dẫn đầy đủ đến tệp
    file_path = os.path.join(asset_dir, filename)

    
    # Kiểm tra xem tệp có tồn tại không
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Tệp {filename} không tồn tại trong thư mục 'assets'.")
   
    return file_path


with st.sidebar: #tạo thanh bên
##    Lấy ảnh và đưa ảnh lên trang web 
    image = get_pass("python4_8.png")
    st.image(image,caption= "Đen Vâu")
    st.write("Họ và tên: Nguyễn Đức Cường")
    st.write("Nghệ danh: Đen Vâu")
    st.write("Nguyễn Đức Cường thường được biết đến với nghệ danh Đen Vâu hay Đen, là một nam rapper và nhạc sĩ người Việt Nam. Đen Vâu từng giành được giải cống hiến và lầ 'một trong số ít nghệ sĩ thành công từ làn  sóng underground và âm nhạc indie' của Việt Nam")
##tạo tiêu đề 
st.title ("Bài hát yêu thích")
##tên bài hát
st.write("Mưa trên những mái tôn")
##Lấy audio theo đường dẫn và đưa audio lên trang web
audio = open(get_pass("python4_8.mp3"),"rb")
st.audio(audio,format ='audio/mp3')
st.title ("MV yêu thích")
st.write("Đưa nhau đi trốn")
##lấy video theo đường dẫn, đưa video lên trang web
video = "https://www.youtube.com/watch?v=5e7e_KZINA4"
st.video(video,format ='video/mp4')
